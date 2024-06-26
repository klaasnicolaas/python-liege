"""Models for Open Data Platform of Liège."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any


@dataclass
class Garage:
    """Object representing a garage."""

    name: str
    capacity: int
    charging_stations: int
    address: str
    municipality: str
    city: str
    provider: str
    schedule: str
    url: str

    longitude: float
    latitude: float

    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls: type[Garage], data: dict[str, Any]) -> Garage:
        """Return a Garage object from a dictionary.

        Args:
        ----
            data: The data from the API.

        Returns:
        -------
            A Garage object.

        """
        attr = data["fields"]
        geo = data["geometry"]["coordinates"]
        return cls(
            name=attr.get("title"),
            capacity=attr.get("available_spaces"),
            charging_stations=attr.get("charging_stations"),
            address=set_address(
                attr.get("street_name"),
                attr.get("house_number"),
                attr.get("postal_code"),
            ),
            municipality=attr.get("municipality"),
            city=attr.get("city"),
            provider=attr.get("provider"),
            schedule=attr.get("schedule"),
            url=attr.get("website"),
            longitude=geo[0],
            latitude=geo[1],
            created_at=datetime.strptime(attr.get("created"), "%Y-%m-%d").replace(
                tzinfo=UTC
            ),
            updated_at=datetime.strptime(attr.get("last_modified"), "%Y-%m-%d").replace(
                tzinfo=UTC
            ),
        )


@dataclass
class DisabledParking:
    """Object representing a disabled parking."""

    spot_id: str
    number: int
    address: str
    municipality: str
    city: str
    status: str

    longitude: float
    latitude: float

    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_dict(cls: type[DisabledParking], data: dict[str, Any]) -> DisabledParking:
        """Return a DisabledParking object from a dictionary.

        Args:
        ----
            data: The data from the API.

        Returns:
        -------
            A DisabledParking object.

        """
        attr = data["fields"]
        geo = data["geometry"]["coordinates"]
        return cls(
            spot_id=str(data.get("recordid")),
            number=attr.get("available_spaces"),
            address=set_address(
                attr.get("street_name"),
                attr.get("house_number"),
                attr.get("postal_code"),
            ),
            municipality=attr.get("municipality"),
            city=attr.get("city"),
            status=attr.get("status"),
            longitude=geo[0],
            latitude=geo[1],
            created_at=datetime.strptime(attr.get("created"), "%Y-%m-%d").replace(
                tzinfo=UTC
            ),
            updated_at=datetime.strptime(attr.get("last_modified"), "%Y-%m-%d").replace(
                tzinfo=UTC
            ),
        )


def set_address(street: str, number: str, postal_code: str) -> str:
    """Set the address.

    Args:
    ----
        street: The street name.
        number: The house number.
        postal_code: The postal code.


    Returns:
    -------
        The address.

    """
    return f"{street} {number}, {postal_code}"
