import re
from playwright.sync_api import expect

from framework import selectors
from framework.common import click_when_visible, wait_for_network_idle


def select_first_business_card(page):
    """
    Selects the first visible business/profile card after login.
    """

    first_business_card = page.locator(selectors.BUSINESS_CARD_SELECTOR).first
    click_when_visible(first_business_card)

    wait_for_network_idle(page)


def open_first_booking_from_dashboard(page):
    """
    Opens the first visible appointment/booking from the dashboard.

    Use this when you do not want to select by patient name.
    It clicks the first visible View button.
    """

    first_view_button = page.get_by_role(
        "button",
        name=re.compile(r"^View$", re.I)
    ).first

    click_when_visible(first_view_button)

    wait_for_network_idle(page)


def open_booking_by_patient_name_from_dashboard(page, patient_name):
    """
    Opens a visible dashboard booking by patient name.

    Example:
        open_booking_by_patient_name_from_dashboard(page, "Mary Nelson")

    This version is more flexible because the dashboard text can contain
    hidden spaces or combined text like:
        Mary Nelson +91 5557231469 11:10 AM Jun 3, 2026 Naveen Consultation
    """

    patient_pattern = build_flexible_text_pattern(patient_name)

    view_button_pattern = re.compile(r"^View$", re.I)

    booking_container = (
        page.locator("div")
        .filter(has_text=patient_pattern)
        .filter(has=page.get_by_role("button", name=view_button_pattern))
        .last
    )

    expect(booking_container).to_be_visible()

    view_button = booking_container.get_by_role(
        "button",
        name=view_button_pattern
    ).first

    click_when_visible(view_button)

    wait_for_network_idle(page)


def build_flexible_text_pattern(text):
    """
    Converts normal text into a flexible regex.

    Example:
        Mary Nelson

    Becomes:
        Mary\\s+Nelson

    This helps when the UI has hidden spaces, new lines, or non-breaking spaces.
    """

    words = text.strip().split()

    flexible_text = r"\s+".join(
        re.escape(word) for word in words
    )

    return re.compile(flexible_text, re.I)


def click_view_details_or_assign_myself(page):
    """
    Clicks appointment details button if a popup appears.

    Handles possible button texts:
    - Assign Myself View Details
    - View Details

    Use this only if clicking the dashboard View button opens a popup
    instead of directly opening the appointment details page.
    """

    button = page.get_by_role(
        "button",
        name=re.compile(r"(Assign Myself|View Details)", re.I)
    ).first

    click_when_visible(button)

    wait_for_network_idle(page)


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

    wait_for_network_idle(page)


def assert_patient_not_visible_on_dashboard(page, patient_name):
    """
    Confirms that a patient name is not visible on the dashboard.
    """

    patient_pattern = build_flexible_text_pattern(patient_name)

    patient_text = page.get_by_text(patient_pattern)

    expect(patient_text).to_have_count(0)