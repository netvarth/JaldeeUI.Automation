from playwright.sync_api import expect

from framework import selectors
from framework.common import (
    wait_for_page_ready,
    wait_for_network_idle,
    fill_when_visible,
    click_when_visible,
)


def open_login_page(page, config):
    """
    Opens the Jaldee business login page.
    """

    page.goto(config["login_url"])
    wait_for_page_ready(page)


def login(page, config):
    """
    Reusable login function.

    All tests should call this function instead of writing login steps again.
    """

    if not config["login_id"] or not config["password"]:
        raise ValueError(
            "Missing TEST_LOGIN_ID or TEST_PASSWORD. "
            "Please add them in your .env file."
        )

    open_login_page(page, config)

    fill_when_visible(
        page.get_by_role("textbox", name=selectors.LOGIN_ID_TEXTBOX_NAME),
        config["login_id"]
    )

    fill_when_visible(
        page.get_by_role("textbox", name=selectors.PASSWORD_TEXTBOX_NAME),
        config["password"]
    )

    click_when_visible(
        page.get_by_role("button", name=selectors.SIGN_IN_BUTTON_NAME)
    )

    wait_for_network_idle(page)


def logout(page):
    """
    Reusable logout function.

    Used directly in logout tests and also during test cleanup.
    """

    try:
        page.get_by_text(selectors.PROFILE_INITIAL_TEXT, exact=True).click()
        page.get_by_text(selectors.SIGN_OUT_TEXT).click()
    except Exception:
        # Do not fail cleanup if user is already logged out.
        pass


def assert_login_page_visible(page):
    """
    Verifies login page is visible.
    """

    expect(page.get_by_text(selectors.WELCOME_TEXT)).to_be_visible()


def login_with_invalid_credentials(page, config, login_id, password):
    """
    Used for negative login test cases.
    """

    open_login_page(page, config)

    fill_when_visible(
        page.get_by_role("textbox", name=selectors.LOGIN_ID_TEXTBOX_NAME),
        login_id
    )

    fill_when_visible(
        page.get_by_role("textbox", name=selectors.PASSWORD_TEXTBOX_NAME),
        password
    )

    click_when_visible(
        page.get_by_role("button", name=selectors.SIGN_IN_BUTTON_NAME)
    )