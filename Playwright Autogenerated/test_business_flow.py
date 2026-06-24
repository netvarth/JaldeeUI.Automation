import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://scale.jaldee.com/business/login?v=2.4.588")
    page.get_by_role("textbox", name="Enter Login ID").click()
    page.get_by_role("textbox", name="Enter Login ID").fill("40251")
    page.get_by_role("textbox", name="Enter Login ID").press("Tab")
    page.get_by_role("textbox", name="Enter password").fill("Jaldee01")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("link").nth(3).click()
    page.goto("https://scale.jaldee.com/business/ip/dashboard?v=2.4.588&p_source=p_sidebar")
    page.locator("div:nth-child(2) > div > div > #actionNav_IP_DBoard > .dashboard-card-image > img").click()
    page.get_by_role("row", name="RE000774 D Dhruv Patel #Id :").locator("#btnViewIp_IP_IpGrd").click()
    page.get_by_role("button", name="   Service").click()
    page.get_by_role("searchbox", name="Search Service").click()
    page.get_by_role("searchbox", name="Search Service").fill("do")
    page.get_by_role("option", name="Doc Visit").click()
    page.locator("app-time-picker").get_by_role("button", name="dropdown trigger").click()
    page.get_by_role("option", name="02:30 AM").click()
    page.get_by_role("button", name="Add Service").click()
    page.get_by_text("V", exact=True).click()
    page.get_by_text("Sign Out").click()
