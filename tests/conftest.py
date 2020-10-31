import pytest
from quotes import create_app


@pytest.yield_fixture(scope="function")
def app():
    return create_app()
