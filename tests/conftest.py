"""Fixtures for the Liege ODP tests."""

from collections.abc import AsyncGenerator

import pytest
from aiohttp import ClientSession

from liege import ODPLiege


@pytest.fixture(name="odp_liege_client")
async def client() -> AsyncGenerator[ODPLiege, None]:
    """Fixture to create an ODPLiege client."""
    async with (
        ClientSession() as session,
        ODPLiege(session=session) as odp_liege_client,
    ):
        yield odp_liege_client
