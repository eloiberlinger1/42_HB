from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from typing import Optional, Any
from typing_extensions import Self


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)

    contact_type: ContactType

    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_alien_rules(self) -> Self:

        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (>7.0) should include received messages"
            )

        return self

    def __str__(self) -> str:
        msg = f"'{self.message_received}'" if self.message_received else "None"

        return (
            f"ID: {self.contact_id}\n"
            f"Type: {self.contact_type.value}\n"
            f"Location: {self.location}\n"
            f"Signal: {self.signal_strength}/10\n"
            f"Duration: {self.duration_minutes} minutes\n"
            f"Witnesses: {self.witness_count}\n"
            f"Message: {msg}"
        )


def main() -> None:

    valid_data: dict[str, Any] = {
        "contact_id": "AC_2024_001",
        "timestamp": "2024-01-20T00:00:00",
        "location": "Atacama Desert, Chile",
        "contact_type": "visual",
        "signal_strength": 9.6,
        "duration_minutes": 99,
        "witness_count": 11,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False,
    }

    invalid_data: dict[str, Any] = {
        "contact_id": "AC_2024_002",
        "timestamp": "2024-08-20T00:00:00",
        "location": "Mauna Kea Observatory, Hawaii",
        "contact_type": "thelepatic",
        "signal_strength": 5.6,
        "duration_minutes": 152,
        "witness_count": 1,
        "is_verified": False,
    }

    print("\n\nAlien Contact Log Validation")
    print("=" * 40)

    print("Valid contact report:")

    valid_contact = AlienContact(**valid_data)
    print(valid_contact)

    print()
    print("=" * 40)
    print()

    try:
        AlienContact(**invalid_data)
    except ValidationError as e:
        error_msg = e.errors()[0]["msg"]

        if "Value error, " in error_msg:
            error_msg = error_msg.replace("Value error, ", "")

        print(error_msg)


if __name__ == "__main__":
    main()
