import re
import argparse
from pathlib import Path
from typing import Dict, Any


class CLIParser:

    def parse_input(self) -> Path:
        """
        For now input parsing only focuses on letting the user pick a map
        """
        parser = argparse.ArgumentParser(description="Fly-in drone simulation")
        parser.add_argument("map_file", type=Path, help="Path to map file")
        args = parser.parse_args()

        return args.map_file


class MapParser:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.nb_drones = 0
        self.zones: Dict[str, Dict[str, Any]] = {}
        self.connections = []

    def _parse_metadata(self, metadata_str: str) -> Dict[str, str]:
        """Extract all the [key=value] format in the input file"""
        metadata = {}
        if not metadata_str:
            return metadata
        matches = re.findall(r"([a-zA-Z0-9_]+)=([a-zA-Z0-9_-]+)", metadata_str)
        for key, value in matches:
            metadata[key] = value
        return metadata

    def parse(self) -> None | Dict:
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
                        self._parse_zone_line(line)

                    elif line.startswith("connection:"):
                        self._parse_connection_line(line)

                    else:
                        raise ValueError(f"Line {line_num}: Error -> {line}")

                except Exception as e:
                    raise ValueError(f"Parsing error at line {line_num}: {e}")

        return {
            "nb_drones": self.nb_drones,
            "zones": self.zones,
            "connections": self.connections,
        }

    def _parse_zone_line(self, line: str) -> None:
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

        self.zones[name] = {
            "type_def": zone_type_str,
            "x": int(x_str),
            "y": int(y_str),
            "metadata": metadata,
        }

    def _parse_connection_line(self, line: str) -> None:
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
        self.connections.append(
            {"from": zone1.strip(), "to": zone2.strip(), "metadata": metadata}
        )
