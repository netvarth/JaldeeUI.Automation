import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://scale.jaldee.com/business/login?v=2.4.566")
    page.get_by_role("textbox", name="Enter Login ID").click()
    page.get_by_role("textbox", name="Enter Login ID").fill("5555556030")
    page.get_by_role("textbox", name="Enter Login ID").press("Tab")
    page.get_by_role("textbox", name="Enter password").fill("Jaldee01")
    page.get_by_role("button", name="Sign In").click()
    page.locator("div:nth-child(3) > div > .p-element > .p-card > .p-card-body > .p-card-content > div > div").click()
    page.get_by_role("tab", name="John Miller 12:05 PM 02/06/").click()
    page.get_by_role("button", name="Assign Myself View Details").click()
    page.locator("#btnBack_BUS_provApptDeatail").click()
    page.get_by_text("V", exact=True).click()
    page.get_by_text("Sign Out").click()
    page.locator("div").filter(has_text="Sign In Hi, Welcome to Jaldee").nth(2).click()
