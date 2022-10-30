"""pytest Local Config File

> 💡 This is a special `pytest` file, so even if this is empty, please don't
> remove this, otherwise the local tests might not work.

Common fixtures and definitions for tests should go here, as this file will be
automatically imported and parsed by `pytest`.
"""
# pylint: disable=missing-function-docstring
import json
import pathlib

import pytest


@pytest.fixture(scope="session")
def plotly_example_sankey_energy_json() -> dict:
    """Read JSON Data File into a pytest Fixture for Sankey Diagrams

    Source for data captured on 2022-10-30 around 6pm ET with command:

    ```bash
    curl -X GET https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json -o ./_data/plotly_sankey_energy.json
    ```

    Returns:
        dict: plotly Example `sankey_energy.json` Data read-in as a JSON Object
    """
    data = None
    data_path = pathlib.Path("_data/plotly_sankey_energy.json")
    with open(data_path, "r") as json_file:
        data = json.load(json_file)
    return data
