"""Test the models."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from aresponses import ResponsesMockServer
from syrupy.assertion import SnapshotAssertion

from . import load_fixtures

if TYPE_CHECKING:
    from liege import DisabledParking, Garage, ODPLiege


@pytest.mark.asyncio
async def test_all_garages(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    odp_liege_client: ODPLiege,
) -> None:
    """Test all garages function."""
    aresponses.add(
        "opendata.liege.be",
        "/api/records/1.0/search/",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("garages.json"),
        ),
    )
    spaces: list[Garage] = await odp_liege_client.garages()
    assert spaces == snapshot


@pytest.mark.asyncio
async def test_disabled_parkings(
    aresponses: ResponsesMockServer,
    snapshot: SnapshotAssertion,
    odp_liege_client: ODPLiege,
) -> None:
    """Test disabled parking spaces function."""
    aresponses.add(
        "opendata.liege.be",
        "/api/records/1.0/search/",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("disabled_parkings.json"),
        ),
    )
    spaces: list[DisabledParking] = await odp_liege_client.disabled_parkings()
    assert spaces == snapshot
