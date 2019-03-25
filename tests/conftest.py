"""Tests fixtures for Google Fire examples."""
from os.path import (
    abspath,
    dirname,
    join
)

import pytest


@pytest.fixture(scope='session')
def path_builder():

    PROJECT_ROOT = dirname(dirname(abspath(__file__)))

    def build_path(directory, filename):
        return join(PROJECT_ROOT, directory, filename)

    return build_path
