import logging
import os

import allure
import pytest

from framework.config import get_config
from framework.auth import logout
from framework.test_data import load_json_test_data
from framework import selectors as app_selectors


def pytest_addoption(parser):
    parser.addoption(
        "--account",
        action="store",
        default=os.getenv("TEST_ACCOUNT", "booking"),
        help="Provider account to use: booking, order, ip",
    )


@pytest.fixture(scope="session", autouse=True)
def configure_playwright_test_id(playwright):
    """
    Configure Playwright test id attribute.

    Playwright default is already data-testid, but keeping this explicit
    makes it easy to change later.
    """

    playwright.selectors.set_test_id_attribute(app_selectors.TEST_ID_ATTRIBUTE)


@pytest.fixture(scope="session")
def config(request):
    """
    Loads .env configuration once for all tests.

    Account can be selected from command line:
        --account booking
        --account order
        --account ip
    """

    account_name = request.config.getoption("--account")

    return get_config(account_name)



@pytest.fixture(scope="session")
def appointment_data():
    """
    Loads appointment test data once for all appointment tests.
    """

    return load_json_test_data("appointment_test_data.json")


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


@pytest.fixture(autouse=True)
def test_logger(request):
    """
    Clean per-test logging.

    Use inside tests or framework functions:
        logging.info("message")
    """

    logger = logging.getLogger(request.node.nodeid)
    logger.info("START TEST: %s", request.node.nodeid)

    yield logger

    logger.info("END TEST: %s", request.node.nodeid)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Adds screenshots to Allure for failed test cases.
    """

    outcome = yield
    report = outcome.get_result()

    if report.passed:
        return

    page = item.funcargs.get("page", None)

    if page is None:
        return

    try:
        screenshot_bytes = page.screenshot(full_page=True)

        allure.attach(
            screenshot_bytes,
            name=f"Failure Screenshot - {report.when}",
            attachment_type=allure.attachment_type.PNG,
        )

    except Exception as error:
        logging.getLogger(__name__).warning(
            "Could not attach screenshot to Allure: %s",
            error,
        )