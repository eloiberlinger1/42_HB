from datetime import datetime
from enum import Enum
from typing import List, Any
from typing_extensions import Self
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    """Enum of the possible ranks."""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Represents an individual crew member."""

    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)

    def __str__(self) -> str:
        rank_str = (
            self.rank.value if hasattr(self.rank, "value") else self.rank
        )
        return f"  {self.name} ({rank_str})".ljust(40) + self.specialization


class SpaceMission(BaseModel):
    """REpresents a spatial station with it's crew"""

    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_safety(self) -> Self:
        """Global validation to check the mission values"""

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        for member in self.crew:
            if not member.is_active:
                raise ValueError(f"Crew member {member.name} must be active")

        has_leader = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            if experienced_count / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need "
                    "50% experienced crew (5+ years)"
                )

        return self

    def __str__(self) -> str:
        lines = [
            "Space Mission Crew Validation",
            f"Mission: {self.mission_name}",
            f"ID: {self.mission_id}",
            f"Destination: {self.destination}",
            f"Duration: {self.duration_days} days",
            f"Budget: ${self.budget_millions:.1f}M",
            f"Crew size: {len(self.crew)}",
            "Crew members:",
        ]

        for member in self.crew:
            lines.append(str(member))

        return "\n".join(lines)


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    valid_mission_data: dict[str, Any] = {
        "mission_id": "M2024_TITAN",
        "mission_name": "Solar Observatory Research Mission",
        "destination": "Solar Observatory",
        "launch_date": "2024-03-30T00:00:00",
        "duration_days": 451,
        "crew": [
            {
                "member_id": "CM001",
                "name": "Sarah Williams",
                "rank": "captain",
                "age": 43,
                "specialization": "Mission Command",
                "years_experience": 19,
                "is_active": True,
            },
            {
                "member_id": "CM002",
                "name": "James Hernandez",
                "rank": "captain",
                "age": 43,
                "specialization": "Pilot",
                "years_experience": 30,
                "is_active": True,
            },
            {
                "member_id": "CM003",
                "name": "Anna Jones",
                "rank": "cadet",
                "age": 35,
                "specialization": "Communications",
                "years_experience": 15,
                "is_active": True,
            },
            {
                "member_id": "CM004",
                "name": "David Smith",
                "rank": "commander",
                "age": 27,
                "specialization": "Security",
                "years_experience": 15,
                "is_active": True,
            },
            {
                "member_id": "CM005",
                "name": "Maria Jones",
                "rank": "cadet",
                "age": 55,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True,
            },
        ],
        "mission_status": "planned",
        "budget_millions": 2208.1,
    }

    invalid_mission_data: dict[str, Any] = {
        "mission_id": "M2024_MARS",
        "mission_name": "Jupiter Orbit Colony Mission",
        "destination": "Jupiter Orbit",
        "launch_date": "2024-10-01T00:00:00",
        "duration_days": 1065,
        "crew": [
            {
                "member_id": "CM012",
                "name": "John Hernandez",
                "rank": "lieutenant",
                "age": 36,
                "specialization": "Science Officer",
                "years_experience": 22,
                "is_active": True,
            }
        ],
        "mission_status": "planned",
        "budget_millions": 4626.0,
    }

    valid_crew: list[CrewMember] = []
    for member in valid_mission_data["crew"]:
        valid_crew.append(CrewMember(**member))

    mission = SpaceMission(
        mission_id=valid_mission_data["mission_id"],
        mission_name=valid_mission_data["mission_name"],
        destination=valid_mission_data["destination"],
        launch_date=valid_mission_data["launch_date"],
        duration_days=valid_mission_data["duration_days"],
        crew=valid_crew,
        mission_status=valid_mission_data["mission_status"],
        budget_millions=valid_mission_data["budget_millions"],
    )

    print("Valid mission created:")
    print(mission)
    print()

    print("-" * 40)
    print("Expected validation error:")

    invalid_crew: list[CrewMember] = []
    for member in invalid_mission_data["crew"]:
        invalid_crew.append(CrewMember(**member))

    try:
        mission = SpaceMission(
            mission_id=invalid_mission_data["mission_id"],
            mission_name=invalid_mission_data["mission_name"],
            destination=invalid_mission_data["destination"],
            launch_date=invalid_mission_data["launch_date"],
            duration_days=invalid_mission_data["duration_days"],
            crew=invalid_crew,
            mission_status=invalid_mission_data["mission_status"],
            budget_millions=invalid_mission_data["budget_millions"],
        )
    except ValidationError as e:
        error_msg = e.errors()[0]["msg"]

        if "Value error, " in error_msg:
            error_msg = error_msg.replace("Value error, ", "")

        print(error_msg)


if __name__ == "__main__":
    main()
