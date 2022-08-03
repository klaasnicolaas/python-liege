# pylint: disable=W0621
"""Asynchronous Python client providing Open Data information of Liege."""

import asyncio

from liege import ODPLiege


async def main() -> None:
    """Show example on using the Liege API client."""
    async with ODPLiege() as client:
        garages = await client.garages(limit=12)
        disabled_parkings = await client.disabled_parkings(limit=5)
        print(garages)

        count: int
        for index, item in enumerate(disabled_parkings, 1):
            count = index
            print(item)

        # Count unique id's in disabled_parkings
        unique_values: list[str] = []
        for item in disabled_parkings:
            unique_values.append(item.spot_id)
        num_values = len(set(unique_values))

        print("__________________________")
        print(f"Total locations found: {count}")
        print(f"Unique ID values: {num_values}")


if __name__ == "__main__":
    asyncio.run(main())
