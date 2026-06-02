from playwright.sync_api import expect


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


def click_when_visible(locator):
    """
    Waits until an element is visible, then clicks it.
    """

    expect(locator).to_be_visible()
    locator.click()


def fill_when_visible(locator, value):
    """
    Waits until an input is visible, then fills it.
    """

    expect(locator).to_be_visible()
    locator.fill(value)


def assert_text_visible(page, text):
    """
    Checks whether given text is visible on the page.
    """

    expect(page.get_by_text(text)).to_be_visible()


def assert_locator_visible(locator):
    """
    Checks whether a locator is visible.
    """

    expect(locator).to_be_visible()