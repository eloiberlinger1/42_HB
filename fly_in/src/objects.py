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
