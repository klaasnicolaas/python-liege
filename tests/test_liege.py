"""Basic tests for the Open Data Platform API of Liège."""

# pylint: disable=protected-access
import asyncio
from unittest.mock import patch

import aiohttp
import pytest
from aresponses import Response, ResponsesMockServer

from liege import ODPLiege
from liege.exceptions import ODPLiegeConnectionError, ODPLiegeError

from . import load_fixtures


@pytest.mark.asyncio
async def test_json_request(aresponses: ResponsesMockServer) -> None:
    """Test JSON response is handled correctly."""
    aresponses.add(
        "opendata.liege.be",
        "/api/records/1.0/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("garages.json"),
        ),
    )
    async with aiohttp.ClientSession() as session:
        client = ODPLiege(session=session)
        response = await client._request("test")
        assert response is not None
        await client.close()


@pytest.mark.asyncio
async def test_internal_session(aresponses: ResponsesMockServer) -> None:
    """Test internal session is handled correctly."""
    aresponses.add(
        "opendata.liege.be",
        "/api/records/1.0/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "application/json"},
            text=load_fixtures("garages.json"),
        ),
    )
    async with ODPLiege() as client:
        await client._request("test")


@pytest.mark.asyncio
async def test_timeout(aresponses: ResponsesMockServer) -> None:
    """Test request timeout from the Open Data Platform API of Liège."""

    # Faking a timeout by sleeping
    async def response_handler(_: aiohttp.ClientResponse) -> Response:
        await asyncio.sleep(0.2)
        return aresponses.Response(
            body="Goodmorning!",
            text=load_fixtures("garages.json"),
        )

    aresponses.add(
        "opendata.liege.be",
        "/api/records/1.0/test",
        "GET",
        response_handler,
    )

    async with aiohttp.ClientSession() as session:
        client = ODPLiege(
            session=session,
            request_timeout=0.1,
        )
        with pytest.raises(ODPLiegeConnectionError):
            assert await client._request("test")


@pytest.mark.asyncio
async def test_content_type(aresponses: ResponsesMockServer) -> None:
    """Test request content type error from Open Data Platform API of Liège."""
    aresponses.add(
        "opendata.liege.be",
        "/api/records/1.0/test",
        "GET",
        aresponses.Response(
            status=200,
            headers={"Content-Type": "blabla/blabla"},
        ),
    )

    async with aiohttp.ClientSession() as session:
        client = ODPLiege(session=session)
        with pytest.raises(ODPLiegeError):
            assert await client._request("test")


@pytest.mark.asyncio
async def test_client_error() -> None:
    """Test request client error from the Open Data Platform API of Liège."""
    async with aiohttp.ClientSession() as session:
        client = ODPLiege(session=session)
        with (
            patch.object(
                session,
                "request",
                side_effect=aiohttp.ClientError,
            ),
            pytest.raises(ODPLiegeConnectionError),
        ):
            assert await client._request("test")
