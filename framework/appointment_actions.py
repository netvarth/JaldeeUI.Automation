import re
from playwright.sync_api import expect

from framework import selectors
from framework.common import click_when_visible, wait_for_network_idle


def select_first_business_card(page):
    """
    Selects the first visible business/profile card after login.

    We removed BUSINESS_CARD_INDEX from .env to keep the framework simpler.
    """

    first_business_card = page.locator(selectors.BUSINESS_CARD_SELECTOR).first
    click_when_visible(first_business_card)

    wait_for_network_idle(page)


def open_appointment_by_patient_name(page, patient_name):
    """
    Opens appointment tab/card by patient name.

    This avoids depending on full generated text like:
    John Miller 12:05 PM 02/06/

    Time and date can change, so we match only the patient name.
    """

    appointment_tab = page.get_by_role(
        "tab",
        name=re.compile(patient_name, re.I)
    )

    click_when_visible(appointment_tab)


def click_view_details_or_assign_myself(page):
    """
    Clicks appointment details button.

    Handles both possible button texts:
    - Assign Myself View Details
    - View Details
    """

    button = page.get_by_role(
        "button",
        name=re.compile(r"(Assign Myself|View Details)", re.I)
    )

    click_when_visible(button)


def assert_appointment_details_opened(page):
    """
    Checks whether appointment details page is opened.
    """

    expect(page.locator(selectors.APPOINTMENT_DETAILS_BACK_BUTTON)).to_be_visible()


def go_back_from_appointment_details(page):
    """
    Clicks back button from appointment details page.
    """

    back_button = page.locator(selectors.APPOINTMENT_DETAILS_BACK_BUTTON)
    click_when_visible(back_button)


def assert_appointment_not_visible(page, patient_name):
    """
    Confirms that a patient appointment is not present.
    """

    appointment_tab = page.get_by_role(
        "tab",
        name=re.compile(patient_name, re.I)
    )

    expect(appointment_tab).to_have_count(0)