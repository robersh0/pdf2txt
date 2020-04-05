import pytest


from app.main import create_app
from app.settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)
