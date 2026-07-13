from playwright.sync_api import expect


DEFAULT_EXPECT_TIMEOUT = 15000


def wait_for_page_ready(page):
    """
    Wait until the page HTML is loaded.
    """

    page.wait_for_load_state("domcontentloaded")


def wait_for_network_idle(page, timeout: int = 15000) -> None:
    """
    Waits for page readiness without failing only because networkidle is not reached.

    Angular/PrimeNG dashboard pages may keep polling APIs or background requests active.
    In those cases, networkidle is not reliable even though the page is usable.

    This helper:
    - waits for DOM content if possible
    - tries networkidle
    - falls back to a short wait if networkidle times out
    """

    try:
        page.wait_for_load_state("domcontentloaded", timeout=timeout)
    except Exception:
        pass

    try:
        page.wait_for_load_state("networkidle", timeout=timeout)
    except Exception:
        page.wait_for_timeout(1000)

        


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