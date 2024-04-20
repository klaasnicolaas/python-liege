<!-- Banner -->
![alt Banner of the ODP Liege package](https://raw.githubusercontent.com/klaasnicolaas/python-liege/main/assets/header_liege-min.png)

<!-- PROJECT SHIELDS -->
[![GitHub Release][releases-shield]][releases]
[![Python Versions][python-versions-shield]][pypi]
![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE)

[![GitHub Activity][commits-shield]][commits-url]
[![PyPi Downloads][downloads-shield]][downloads-url]
[![GitHub Last Commit][last-commit-shield]][commits-url]
[![Open in Dev Containers][devcontainer-shield]][devcontainer]

[![Code Quality][code-quality-shield]][code-quality]
[![Build Status][build-shield]][build-url]
[![Typing Status][typing-shield]][typing-url]

[![Maintainability][maintainability-shield]][maintainability-url]
[![Code Coverage][codecov-shield]][codecov-url]

Asynchronous Python client for the open datasets of Liège (Belgium).

## About

A python package with which you can retrieve data from the Open Data Platform of Liège via [their API][api]. This package was initially created to only retrieve parking data from the API, but the code base is made in such a way that it is easy to extend for other datasets from the same platform.

## Installation

```bash
pip install liege
```

## Datasets

You can read the following datasets with this package:

- [Disabled parking spaces / Stationnement PMR][disabled_parking] (1062 locations)
- [Garages / Les parkings voitures hors voirie][garages] (32 locations)

<details>
    <summary>Click here to get more details</summary>

### Disabled parkings

Parameters:

- **limit** (default: 10) - How many results you want to retrieve.

| Variable | Type | Description |
| :------- | :--- | :---------- |
| `spot_id` | int | The ID of the parking spot |
| `number` | int | How many parking spots there are on this location |
| `address` | str | The address of the parking spot |
| `municipality` | str | The municipality of the parking spot |
| `city` | str | The city of the parking spot |
| `status` | str | The status of the parking spot |
| `longitude` | float | The longitude of the parking spot |
| `latitude` | float | The latitude of the parking spot |
| `created_at` | datetime | When the parking spot was added to the dataset |
| `updated_at` | datetime | The last time the data was updated |

### Garages

Parameters:

- **limit** (default: 10) - How many results you want to retrieve.

| Variable | Type | Description |
| :------- | :--- | :---------- |
| `name` | string | The name of the garage |
| `capacity` | int | The capacity of the garage |
| `charging_stations` | int | The number of charging stations |
| `address` | string | The address of the garage |
| `municipality` | string | The municipality of the garage |
| `city` | string | The city of the garage |
| `provider` | string | The provider of the garage |
| `schedule` | string | The schedule of the garage |
| `longitude` | float | The longitude of the garage |
| `latitude` | float | The latitude of the garage |
| `created_at` | datetime | When the garage was added to the dataset |
| `updated_at` | datetime | The last time the data was updated |
</details>

## Example

```python
import asyncio

from liege import ODPLiege


async def main() -> None:
    """Show example on using the Open Data API client."""
    async with ODPLiege() as client:
        garages = await client.garages(limit=10)
        disabled_parkings = await client.disabled_parkings(limit=10)
        print(garages)
        print(disabled_parkings)


if __name__ == "__main__":
    asyncio.run(main())
```

## Use cases

[NIPKaart.nl][nipkaart]

A website that provides insight into where disabled parking spaces are, based
on data from users and municipalities. Operates mainly in the Netherlands, but
also has plans to process data from abroad.

## Contributing

This is an active open-source project. We are always open to people who want to
use the code or contribute to it.

We've set up a separate document for our
[contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Setting up development environment

The simplest way to begin is by utilizing the [Dev Container][devcontainer]
feature of Visual Studio Code or by opening a CodeSpace directly on GitHub.
By clicking the button below you immediately start a Dev Container in Visual Studio Code.

[![Open in Dev Containers][devcontainer-shield]][devcontainer]

This Python project relies on [Poetry][poetry] as its dependency manager,
providing comprehensive management and control over project dependencies.

You need at least:

- Python 3.11+
- [Poetry][poetry-install]

Install all packages, including all development requirements:

```bash
poetry install
```

Poetry creates by default an virtual environment where it installs all
necessary pip packages, to enter or exit the venv run the following commands:

```bash
poetry shell
exit
```

Setup the pre-commit check, you must run this inside the virtual environment:

```bash
pre-commit install
```

*Now you're all set to get started!*

As this repository uses the [pre-commit][pre-commit] framework, all changes
are linted and tested with each commit. You can run all checks and tests
manually, using the following command:

```bash
poetry run pre-commit run --all-files
```

To run just the Python tests:

```bash
poetry run pytest
```

To update the [syrupy](https://github.com/tophat/syrupy) snapshot tests:

```bash
poetry run pytest --snapshot-update
```

## License

MIT License

Copyright (c) 2022-2024 Klaas Schoute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[api]: https://opendata.liege.be/explore
[disabled_parking]: https://opendata.liege.be/explore/dataset/stationnement-pmr
[garages]: https://opendata.liege.be/explore/dataset/parkings-voitures-hors-voirie
[nipkaart]: https://www.nipkaart.nl

<!-- MARKDOWN LINKS & IMAGES -->
[build-shield]: https://github.com/klaasnicolaas/python-liege/actions/workflows/tests.yaml/badge.svg
[build-url]: https://github.com/klaasnicolaas/python-liege/actions/workflows/tests.yaml
[code-quality-shield]: https://github.com/klaasnicolaas/python-liege/actions/workflows/codeql.yaml/badge.svg
[code-quality]: https://github.com/klaasnicolaas/python-liege/actions/workflows/codeql.yaml
[commits-shield]: https://img.shields.io/github/commit-activity/y/klaasnicolaas/python-liege.svg
[commits-url]: https://github.com/klaasnicolaas/python-liege/commits/main
[codecov-shield]: https://codecov.io/gh/klaasnicolaas/python-liege/branch/main/graph/badge.svg?token=jTIsaqV5x0
[codecov-url]: https://codecov.io/gh/klaasnicolaas/python-liege
[devcontainer-shield]: https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode
[devcontainer]: https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/klaasnicolaas/python-liege
[downloads-shield]: https://img.shields.io/pypi/dm/liege
[downloads-url]: https://pypistats.org/packages/liege
[license-shield]: https://img.shields.io/github/license/klaasnicolaas/python-liege.svg
[last-commit-shield]: https://img.shields.io/github/last-commit/klaasnicolaas/python-liege.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2024.svg
[maintainability-shield]: https://api.codeclimate.com/v1/badges/1b4ebe208e72d8f467f9/maintainability
[maintainability-url]: https://codeclimate.com/github/klaasnicolaas/python-liege/maintainability
[project-stage-shield]: https://img.shields.io/badge/project%20stage-experimental-yellow.svg
[pypi]: https://pypi.org/project/liege/
[python-versions-shield]: https://img.shields.io/pypi/pyversions/liege
[typing-shield]: https://github.com/klaasnicolaas/python-liege/actions/workflows/typing.yaml/badge.svg
[typing-url]: https://github.com/klaasnicolaas/python-liege/actions/workflows/typing.yaml
[releases-shield]: https://img.shields.io/github/release/klaasnicolaas/python-liege.svg
[releases]: https://github.com/klaasnicolaas/python-liege/releases

[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
