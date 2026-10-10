import pytest
from configuration import config
from fixtures import driver

@pytest.fixture(scope= "session")
def app_config():
    return config