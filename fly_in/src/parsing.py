import argparse
import re
from pathlib import Path
from typing import Any, Dict


class CLIParser:

    def parse_input(self) -> Path:
        """
        For now input parsing only focuses on letting the user pick a map
        """
        parser = argparse.ArgumentParser(description="Fly-in drone simulation")
        parser.add_argument("map_file", type=Path, help="Path to map file")
        args, unknown = parser.parse_known_args()

        return Path(args.map_file)


class MapParser:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        self.nb_drones = 0
        self.zones: Dict[str, Dict[str, Any]] = {}
        self.connections: list[dict[Any, Any]] = []

    def _parse_metadata(self, metadata_str: str) -> Dict[str, str]:
        """Extract all the [key=value] format in the input file"""
        metadata: dict[Any, Any] = {}
        if not metadata_str:
            return metadata
        matches = re.findall(r"([a-zA-Z0-9_]+)=([a-zA-Z0-9_-]+)", metadata_str)
        for key, value in matches:
            metadata[key] = value
        return metadata

    def parse(self) -> Dict[Any, Any] | None:
        """Read file, validate syntax and extract data"""
        if not self.file_path.exists():
            raise FileNotFoundError(f"File {self.file_path} not found.")

        with open(self.file_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                try:
                    if line.startswith("nb_drones:"):
                        self.nb_drones = int(line.split(":")[1].strip())

                    elif any(
                        line.startswith(prefix)
                        for prefix in ["start_hub:", "end_hub:", "hub:"]
                    ):
                        self._parse_zone_line(line, line_num)

                    elif line.startswith("connection:"):
                        self._parse_connection_line(line, line_num)

                    else:
                        raise ValueError(f"Line {line_num}: Error -> {line}")

                except Exception as e:
                    raise ValueError(f"Parsing error at line {line_num}: {e}")

        return {
            "nb_drones": self.nb_drones,
            "zones": self.zones,
            "connections": self.connections,
        }

    def _parse_zone_line(self, line: str, line_num: int) -> None:
        parts = line.split(":", 1)
        zone_type_str = parts[0].strip()  # start_hub, end_hub ou hub
        rest = parts[1].strip()

        # Removing []
        metadata = {}
        if "[" in rest and rest.endswith("]"):
            main_part, meta_part = rest.split("[", 1)
            meta_part = meta_part[:-1]
            metadata = self._parse_metadata(meta_part)
            rest = main_part.strip()

        # <name> <x> <y>
        tokens = rest.split()
        if len(tokens) != 3:
            raise ValueError(f"Invalid zone format : {rest}")

        name, x_str, y_str = tokens[0], tokens[1], tokens[2]

        if name in self.zones:
            raise ValueError(f"Duplicate zone found: {name}")

        self.zones[name] = {
            "type_def": zone_type_str,
            "x": int(x_str),
            "y": int(y_str),
            "metadata": metadata,
            "line": line_num,
        }

    def _parse_connection_line(self, line: str, line_num: int) -> None:
        parts = line.split(":", 1)
        rest = parts[1].strip()

        metadata = {}
        if "[" in rest and rest.endswith("]"):
            main_part, meta_part = rest.split("[", 1)
            meta_part = meta_part[:-1]
            metadata = self._parse_metadata(meta_part)
            rest = main_part.strip()

        # Expected format : zone1-zone2
        if "-" not in rest:
            raise ValueError(f"Invalid connexion format : {rest}")

        zone1, zone2 = rest.split("-", 1)
        z1 = zone1.strip()
        z2 = zone2.strip()

        for conn in self.connections:
            if (conn["from"] == z1 and conn["to"] == z2) or (
                conn["from"] == z2 and conn["to"] == z1
            ):
                raise ValueError(f"Duplicate connection found: {z1}-{z2}")

        self.connections.append(
            {
                "from": z1,
                "to": z2,
                "metadata": metadata,
                "line": line_num,
            }
        )
