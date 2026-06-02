import pytest

from framework.config import get_config
from framework.auth import logout


@pytest.fixture(scope="session")
def config():
    """
    Loads .env configuration once for all tests.
    """

    return get_config()


@pytest.fixture(autouse=True)
def setup_and_cleanup(page, config):
    """
    Runs automatically before and after every test.

    Before each test:
    - Set default timeout

    After each test:
    - Try to logout
    """

    page.set_default_timeout(config["default_timeout_ms"])

    yield

    logout(page)