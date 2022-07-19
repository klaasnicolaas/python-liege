# pylint: disable=W0621
"""Asynchronous Python client providing Open Data information of Liege."""

import asyncio

from liege import ODPLiege


async def main() -> None:
    """Show example on using the Liege API client."""
    async with ODPLiege() as client:
        garages = await client.garages(limit=12)
        disabled_parkings = await client.disabled_parkings(limit=5)
        print(disabled_parkings)

        count: int
        for index, item in enumerate(garages, 1):
            count = index
            print(item)
        print(f"{count} locations found")


if __name__ == "__main__":
    asyncio.run(main())
