"""

Use pydantic for values verification


- DroneGroup
    - Drone
        - ID

- Zone
    - 2DCoordinates: (x: int, y: int)
    - id: str
    -


- Connection

"""

from pydantic import BaseModel, Field
from typing import Literal, Optional, Dict


class Zone(BaseModel):
    """
    Represents defined coordinates in the graph
    """

    name: str
    x: int
    y: int
    zone_type: Literal["normal", "blocked", "restricted", "priority"] = "normal"
    max_drones: int = Field(default=1, gt=0)
    color: Optional[str] = None
    is_start: bool = False
    is_end: bool = False


class Connection(BaseModel):
    """
    Connect 2 zones together
    """

    zone1: Zone
    zone2: Zone
    max_link_capacity: int = Field(default=1, gt=0)


class Drone(BaseModel):
    """
    Represent one drone that has to move on the graph
    """

    drone_id: str
    current_position: str


class Graph(BaseModel):
    """
    Represents the global map for the execution of the app
    """

    nb_drones: int
    zones: Dict[str, Zone] = {}
    connections: list[Connection] = []
    drones: list[Drone] = []

    def __str__(self) -> str:
        """
        Briefly vibe coded nice display of the final data.
        """
        lines = [
            "\n" + "=" * 45,
            f" 📊 GRAPH SUMMARY — {self.nb_drones} Drones",
            "=" * 45,
            f" Zones ({len(self.zones)}):",
        ]

        for name, zone in self.zones.items():
            tags = []
            if zone.is_start:
                tags.append("START")
            if zone.is_end:
                tags.append("END")
            tag_str = f" [{', '.join(tags)}]" if tags else ""
            lines.append(
                f"   • {name:<15} | type: {zone.zone_type:<8} | max_drones: {zone.max_drones}{tag_str}"
            )

        lines.append(f"\n Connections ({len(self.connections)}):")
        for conn in self.connections:
            lines.append(
                f"   • {conn.zone1.name} ──( cap: {conn.max_link_capacity} )──> {conn.zone2.name}"
            )

        lines.append(f"\n Drones ({len(self.drones)}):")
        start_zone = next(
            (name for name, z in self.zones.items() if z.is_start), "unknown"
        )
        lines.append(f"   • {len(self.drones)} initialized at start hub ({start_zone})")
        lines.append("=" * 45 + "\n")

        return "\n".join(lines)
