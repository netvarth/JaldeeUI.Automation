from playwright.sync_api import expect


DEFAULT_EXPECT_TIMEOUT = 15000


def wait_for_page_ready(page):
    """
    Wait until the page HTML is loaded.
    """

    page.wait_for_load_state("domcontentloaded")


def wait_for_network_idle(page):
    """
    Wait until network calls are mostly completed.

    Useful after login, dashboard load, and page changes.
    """

    page.wait_for_load_state("networkidle")


def click_when_visible(locator, timeout=DEFAULT_EXPECT_TIMEOUT):
    """
    Waits until an element is visible, then clicks it.
    """

    expect(locator).to_be_visible(timeout=timeout)
    locator.click()


def fill_when_visible(locator, value, timeout=DEFAULT_EXPECT_TIMEOUT):
    """
    Waits until an input is visible, then fills it.
    """

    expect(locator).to_be_visible(timeout=timeout)
    locator.fill(value)


def assert_text_visible(page, text, timeout=DEFAULT_EXPECT_TIMEOUT):
    """
    Checks whether given text is visible on the page.
    """

    expect(page.get_by_text(text)).to_be_visible(timeout=timeout)


def assert_locator_visible(locator, timeout=DEFAULT_EXPECT_TIMEOUT):
    """
    Checks whether a locator is visible.
    """

    expect(locator).to_be_visible(timeout=timeout)


def is_text_visible(page, text, timeout=1000):
    """
    Returns True if exact text is visible.
    """

    try:
        expect(page.get_by_text(text, exact=True).first).to_be_visible(timeout=timeout)
        return True

    except Exception:
        return False