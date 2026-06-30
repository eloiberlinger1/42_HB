from typing import Optional, Any
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)

    def __str__(self) -> str:
        status = "Operational" if self.is_operational else "Not Operational"
        return (
            f"Valid station created:\n"
            f"ID: {self.station_id}\n"
            f"Name: {self.name}\n"
            f"Crew: {self.crew_size} people\n"
            f"Power: {self.power_level}%\n"
            f"Oxygen: {self.oxygen_level}%\n"
            f"Status: {status}"
        )


def main() -> None:

    valid_demo_data: dict[str, Any] = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 90,
        "last_maintenance": "2026-06-30T12:00:00",
        "is_operational": True,
    }

    invalid_demo_data: dict[str, Any] = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 60,
        "power_level": 85.5,
        "oxygen_level": 90,
        "last_maintenance": "2026-06-30T12:00:00",
        "is_operational": True,
        "notes": "ASLkdajslkdnjsalkdjaklsdnaskljdnqwkjndkjn",
    }

    print("\n\nSpace Station Data Validation")
    print("=" * 40)
    print("")

    valid_station = SpaceStation(**valid_demo_data)
    print(valid_station)

    print("")
    print("=" * 40)
    print("Expected validation error:")

    try:
        SpaceStation(**invalid_demo_data)
    except ValidationError as e:
        error_msg = e.errors()[0]["msg"]

        if "Value error, " in error_msg:
            error_msg = error_msg.replace("Value error, ", "")

        print(error_msg)


if __name__ == "__main__":
    main()
