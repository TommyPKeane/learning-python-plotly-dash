"""pytest `dash-geographical` Config File

Common fixtures and definitions for the `dash-geographical` demo go here, to
avoid cluttering the `run.py` module.
"""
# pylint: disable=missing-function-docstring
import pytest


@pytest.fixture(scope="session")
def run_host() -> str:
    return "localhost"


@pytest.fixture(scope="session")
def run_port() -> str:
    return "8080"
