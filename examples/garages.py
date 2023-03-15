# pylint: disable=W0621
"""Asynchronous Python client providing Open Data information of Liège."""

import asyncio

from liege import ODPLiege


async def main() -> None:
    """Get the garages data from Liège API."""
    async with ODPLiege() as client:
        garages = await client.garages(limit=12)
        print(garages)

        count: int
        for index, item in enumerate(garages, 1):
            count = index
            print(item)

        print("__________________________")
        print(f"Total locations found: {count}")


if __name__ == "__main__":
    asyncio.run(main())
