import re
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


def get_visible_locator_from_candidates(candidates):
    """
    Returns the first visible locator from a list of locator candidates.

    Each candidate is:
        (locator, timeout_in_ms)

    Important:
    - Use short timeout for optional data-testid locators.
    - Use longer timeout for old stable locators like id/formcontrolname.
    """

    last_error = None

    for locator, timeout in candidates:
        try:
            expect(locator).to_be_visible(timeout=timeout)
            return locator
        except Exception as error:
            last_error = error

    raise AssertionError("None of the expected locators were visible.") from last_error


def get_login_id_input(page):
    """
    Finds the login ID input.

    Optimized priority:
    1. data-testid with very short timeout
    2. old UI stable id with normal timeout
    3. old Angular formcontrolname
    4. placeholder fallback
    5. role fallback
    """

    return get_visible_locator_from_candidates(
        [
            # New UI - quick check only. Do not wait long if not present.
            (page.get_by_test_id(selectors.LOGIN_ID_TEST_ID), 500),

            # Old UI - current stable selectors.
            (page.locator(selectors.LOGIN_ID_SELECTOR), 15000),
            (page.locator(selectors.LOGIN_ID_FORM_CONTROL_SELECTOR), 3000),
            (page.get_by_placeholder(re.compile(r"Enter Login ID", re.I)), 3000),
            (page.get_by_role("textbox", name=re.compile(r"Enter Login ID|Login ID", re.I)), 3000),
        ]
    )


def get_password_input(page):
    """
    Finds the password input.

    Optimized priority:
    1. data-testid with very short timeout
    2. old UI stable id
    3. old Angular formcontrolname
    4. placeholder fallback
    5. password type fallback
    """

    return get_visible_locator_from_candidates(
        [
            # New UI - quick check only. Do not wait long if not present.
            (page.get_by_test_id(selectors.PASSWORD_TEST_ID), 500),

            # Old UI - current stable selectors.
            (page.locator(selectors.PASSWORD_SELECTOR), 15000),
            (page.locator(selectors.PASSWORD_FORM_CONTROL_SELECTOR), 3000),
            (page.get_by_placeholder(re.compile(r"Enter password", re.I)), 3000),
            (page.locator("input[type='password']").first, 3000),
        ]
    )


def get_sign_in_button(page):
    """
    Finds the Sign In button.

    Optimized priority:
    1. data-testid with very short timeout
    2. role button
    3. text fallback
    """

    return get_visible_locator_from_candidates(
        [
            # New UI - quick check only. Do not wait long if not present.
            (page.get_by_test_id(selectors.SIGN_IN_TEST_ID), 500),

            # Current UI fallbacks.
            (page.get_by_role("button", name=re.compile(r"Sign In", re.I)), 10000),
            (page.get_by_text(re.compile(r"Sign In", re.I)).last, 3000),
        ]
    )


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

    login_id_input = get_login_id_input(page)
    fill_when_visible(login_id_input, config["login_id"])

    password_input = get_password_input(page)
    fill_when_visible(password_input, config["password"])

    sign_in_button = get_sign_in_button(page)
    click_when_visible(sign_in_button)

    wait_for_network_idle(page)


def open_profile_menu(page):
    """
    Opens the profile/account menu.
    """

    possible_profile_locators = [
        page.get_by_text(re.compile(r"Vision Hospital", re.I)).first,
        page.get_by_text(selectors.PROFILE_INITIAL_TEXT, exact=True).last,
    ]

    for profile_locator in possible_profile_locators:
        try:
            expect(profile_locator).to_be_visible(timeout=3000)
            profile_locator.click()

            sign_out_button = page.get_by_text(selectors.SIGN_OUT_TEXT)
            expect(sign_out_button).to_be_visible(timeout=3000)
            return

        except Exception:
            continue

    raise AssertionError("Could not open profile menu. Sign Out option was not visible.")


def logout(page, fail_if_not_logged_out=False):
    """
    Reusable logout function.

    By default, this does not fail during cleanup.
    For logout test cases, pass fail_if_not_logged_out=True.
    """

    try:
        open_profile_menu(page)

        page.get_by_text(selectors.SIGN_OUT_TEXT).click()

        expect(page).to_have_url(re.compile(r".*/business/login.*"), timeout=10000)

    except Exception as error:
        if fail_if_not_logged_out:
            raise error

        # Do not fail cleanup if user is already logged out.
        pass


def assert_login_page_visible(page):
    """
    Verifies login page is visible.
    """

    expect(page).to_have_url(re.compile(r".*/business/login.*"), timeout=10000)
    expect(page.get_by_text(selectors.WELCOME_TEXT)).to_be_visible(timeout=15000)


def login_with_invalid_credentials(page, config, login_id, password):
    """
    Used for negative login test cases.
    """

    open_login_page(page, config)

    login_id_input = get_login_id_input(page)
    fill_when_visible(login_id_input, login_id)

    password_input = get_password_input(page)
    fill_when_visible(password_input, password)

    sign_in_button = get_sign_in_button(page)
    click_when_visible(sign_in_button)