import random
import re
import uuid
from datetime import date, timedelta
from pathlib import Path

from playwright.sync_api import expect, TimeoutError as PlaywrightTimeoutError

from framework import selectors
from framework.common import (
    click_when_visible,
    fill_when_visible,
    wait_for_network_idle,
    is_text_visible,
)


# ----------------------------------------------------------------------
# Dashboard appointment actions
# ----------------------------------------------------------------------

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
        open_booking_by_patient_name_from_dashboard(page, "Jisha Rajan")
    """

    patient_pattern = build_flexible_text_pattern(patient_name)

    view_button_pattern = re.compile(r"^View$", re.I)

    booking_container = (
        page.locator("div")
        .filter(has_text=patient_pattern)
        .filter(has=page.get_by_role("button", name=view_button_pattern))
        .last
    )

    expect(booking_container).to_be_visible(timeout=15000)

    view_button = booking_container.get_by_role(
        "button",
        name=view_button_pattern
    ).first

    click_when_visible(view_button)

    wait_for_network_idle(page)


def assert_patient_not_visible_on_dashboard(page, patient_name):
    """
    Confirms that a patient name is not visible on the dashboard.
    """

    patient_pattern = build_flexible_text_pattern(patient_name)

    patient_text = page.get_by_text(patient_pattern)

    expect(patient_text).to_have_count(0)


# ----------------------------------------------------------------------
# Appointment details actions
# ----------------------------------------------------------------------

def click_view_details_or_assign_myself(page):
    """
    Clicks appointment details button if a popup appears.

    Handles possible button texts:
    - Assign Myself View Details
    - View Details
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

    expect(page.locator(selectors.APPOINTMENT_DETAILS_BACK_BUTTON)).to_be_visible(
        timeout=15000
    )


def go_back_from_appointment_details(page):
    """
    Clicks back button from appointment details page.
    """

    back_button = page.locator(selectors.APPOINTMENT_DETAILS_BACK_BUTTON)

    click_when_visible(back_button)

    wait_for_network_idle(page)


# ----------------------------------------------------------------------
# Take appointment / create appointment actions
# ----------------------------------------------------------------------

def wait_for_appointment_options_form(page):
    """
    Waits until the appointment options form is visible after new patient creation.

    Do not wait for role=combobox visibility because PrimeNG keeps the real
    combobox input hidden. Instead, wait for visible form labels/text.
    """

    try:
        expect(
            page.get_by_role("heading", name=re.compile(r"Create Appointment", re.I))
        ).to_be_visible(timeout=20000)

        expect(page.get_by_text("Select Location", exact=True)).to_be_visible(
            timeout=20000
        )

        expect(page.get_by_text("Select Department", exact=True)).to_be_visible(
            timeout=20000
        )

        expect(page.get_by_text("Select doctor", exact=True)).to_be_visible(
            timeout=20000
        )

        expect(page.get_by_text("Select Service", exact=True)).to_be_visible(
            timeout=20000
        )

        return

    except Exception as error:
        raise AssertionError(
            "Appointment options form did not open after saving new patient. "
            f"Current URL: {page.url}"
        ) from error
    

def open_take_appointment_from_dashboard_button(page):
    """
    Opens take appointment flow from dashboard using Create Appointment button.
    """

    create_appointment_button = page.get_by_role(
        "button",
        name=re.compile(r"^Create Appointment$", re.I),
    ).first

    click_when_visible(create_appointment_button, timeout=10000)

    wait_for_network_idle(page)

    assert_take_appointment_form_opened(page)


def open_take_appointment_from_sidebar(page):
    """
    Opens take appointment flow from the sidebar Appointment link.

    Flow:
    1. Click sidebar Appointment link
    2. Click Appointment card or Create Appointment button if shown
    """

    appointment_sidebar_link = page.locator(
        "a[href*='/business/appointments']"
    ).first

    click_when_visible(appointment_sidebar_link, timeout=10000)

    wait_for_network_idle(page)

    appointment_card = page.locator("p-card").filter(
        has_text=re.compile(r"\bAppointment\b", re.I)
    ).first

    if click_if_visible(appointment_card, timeout=5000):
        wait_for_network_idle(page)
        return

    create_appointment_button = page.get_by_role(
        "button",
        name=re.compile(r"^Create Appointment$", re.I),
    ).first

    if click_if_visible(create_appointment_button, timeout=5000):
        wait_for_network_idle(page)
        return

    raise AssertionError(
        "Could not open take appointment flow from sidebar. "
        "Tried sidebar Appointment link, Appointment card, and Create Appointment button."
    )


def click_create_new_patient(page):
    """
    Clicks Create New Patient.
    """

    create_new_patient = page.get_by_text("Create New Patient", exact=True)

    click_when_visible(create_new_patient)


def fill_new_patient_basic_details(page, consumer_profile):
    """
    Fills new patient details.

    Consumer profile values are generated randomly:
    - first name
    - last name
    - email
    - phone
    - gender
    - DOB
    - address

    After saving, waits until the appointment options form is visible.
    """

    fill_when_visible(
        page.get_by_role("textbox", name=re.compile(r"First Name", re.I)),
        consumer_profile["first_name"],
    )

    fill_when_visible(
        page.get_by_role("textbox", name=re.compile(r"Last Name", re.I)),
        consumer_profile["last_name"],
    )

    fill_when_visible(
        page.get_by_role("textbox", name=re.compile(r"Email", re.I)),
        consumer_profile["email"],
    )

    fill_patient_phone_fields(page, consumer_profile["phone"])

    page.get_by_role(
        "radio",
        name=re.compile(rf"^{re.escape(consumer_profile['gender'])}$", re.I),
    ).check()

    fill_patient_dob(page, consumer_profile["dob"])

    click_when_visible(page.get_by_role("button", name=re.compile(r"^Save$", re.I)))

    wait_for_network_idle(page)

    # Some flows ask a confirmation question after saving patient details.
    if click_if_visible(
        page.get_by_role("button", name=re.compile(r"^No$", re.I)),
        timeout=5000,
    ):
        wait_for_network_idle(page)

    fill_patient_address(page, consumer_profile["address"])

    click_when_visible(page.get_by_role("button", name=re.compile(r"^Save$", re.I)))

    wait_for_network_idle(page)

    # Some flows ask confirmation after address save.
    if click_if_visible(
        page.get_by_role("button", name=re.compile(r"^Yes$", re.I)),
        timeout=5000,
    ):
        wait_for_network_idle(page)

    wait_for_appointment_options_form(page)



def fill_patient_phone_fields(page, phone_number):
    """
    Fills phone/mobile fields.

    The recorded old UI had multiple textboxes with accessible name '10123'.
    Codegen filled:
    - first textbox
    - third textbox

    This keeps that behavior but avoids failing if only one phone field exists.
    """

    phone_fields = page.get_by_role("textbox", name=re.compile(r"10123"))

    fill_when_visible(phone_fields.first, phone_number)

    for index in [2, 1]:
        try:
            extra_phone_field = phone_fields.nth(index)
            expect(extra_phone_field).to_be_visible(timeout=1000)
            extra_phone_field.fill(phone_number)
            return

        except Exception:
            continue


def fill_patient_dob(page, dob):
    """
    Fills date of birth.

    Expected format:
        DD/MM/YYYY

    Uses placeholder/CSS fallback instead of role regex because DD/MM/YYYY
    contains slashes and can break Playwright's role selector parser.
    """

    dob_input_candidates = [
        page.get_by_placeholder("DD/MM/YYYY").first,
        page.locator("input[placeholder='DD/MM/YYYY']").first,
        page.locator("input[placeholder*='DD']").first,
    ]

    last_error = None

    for dob_input in dob_input_candidates:
        try:
            expect(dob_input).to_be_visible(timeout=3000)

            dob_input.click()
            dob_input.press("Control+A")
            dob_input.fill(dob)
            dob_input.press("Tab")

            return

        except Exception as error:
            last_error = error

    raise AssertionError("Could not find or fill DOB field.") from last_error

def fill_patient_address(page, address):
    """
    Fills patient address.
    """

    address_box = page.get_by_role(
        "textbox",
        name=re.compile(r"Enter Patient Address", re.I),
    )

    fill_when_visible(address_box, address)


def select_random_appointment_options(page, appointment_config):
    """
    Selects appointment options.

    Fixed from test data:
    - location
    - department
    - provider
    - service

    Random:
    - available appointment slot
    """

    selected_options = {}

    selected_options["location"] = select_dropdown_option_by_index(
        page,
        dropdown_index=0,
        option_text=appointment_config["location"],
        field_name="Location",
    )

    selected_options["department"] = select_dropdown_option_by_index(
        page,
        dropdown_index=1,
        option_text=appointment_config["department_name"],
        field_name="Department",
    )

    selected_options["provider"] = select_dropdown_option_by_index(
        page,
        dropdown_index=2,
        option_text=appointment_config["provider_name"],
        field_name="Provider",
    )

    selected_options["service"] = select_dropdown_option_by_index(
        page,
        dropdown_index=3,
        option_text=appointment_config["service_name"],
        field_name="Service",
    )

    selected_options["slot"] = select_random_available_appointment_slot(page)

    click_when_visible(page.locator(".pro-action").first)

    return selected_options


def select_random_department_with_fixed_provider_and_service(
    page,
    appointment_config,
    max_attempts=5,
):
    """
    Randomly selects a department, then tries fixed provider and fixed service.

    This is safer than blindly selecting any department because the fixed
    provider/service may not be available for every department.
    """

    tried_departments = set()
    last_error = None

    for _ in range(max_attempts):
        try:
            department = select_random_dropdown_option_by_index(
                page,
                dropdown_index=1,
                field_name="Department",
                exclude_texts=tried_departments,
            )

            tried_departments.add(department)

            provider = select_dropdown_option_by_index(
                page,
                dropdown_index=2,
                option_text=appointment_config["provider_name"],
                field_name="Provider",
                timeout=5000,
            )

            service = select_dropdown_option_by_index(
                page,
                dropdown_index=3,
                option_text=appointment_config["service_name"],
                field_name="Service",
                timeout=5000,
            )

            return {
                "department": department,
                "provider": provider,
                "service": service,
            }

        except Exception as error:
            last_error = error
            page.keyboard.press("Escape")
            continue

    raise AssertionError(
        "Could not select a department where fixed provider and service are available. "
        f"Provider: {appointment_config['provider_name']}, "
        f"Service: {appointment_config['service_name']}, "
        f"Tried departments: {sorted(tried_departments)}"
    ) from last_error


def select_dropdown_option_by_index(
    page,
    dropdown_index,
    option_text,
    field_name,
    timeout=10000,
):
    """
    Opens a dropdown by index and selects the required option text.

    If the required value is already visible/selected, it returns without
    reopening the dropdown.
    """

    if is_text_visible(page, option_text, timeout=1000):
        return option_text

    close_open_dropdowns(page)

    open_dropdown_by_index(page, dropdown_index, field_name)

    role_option = page.get_by_role(
        "option",
        name=re.compile(rf"^{re.escape(option_text)}$", re.I),
    ).first

    fallback_option = page.locator(
        "[role='option'], .p-dropdown-item, mat-option"
    ).filter(
        has_text=re.compile(rf"^{re.escape(option_text)}$", re.I)
    ).first

    try:
        if click_if_visible(role_option, timeout=timeout):
            close_open_dropdowns(page)
            return option_text

        click_when_visible(fallback_option, timeout=timeout)

        close_open_dropdowns(page)

        return option_text

    except Exception:
        close_open_dropdowns(page)
        raise
    
    
def close_open_dropdowns(page):
    """
    Closes any currently open dropdown/listbox.

    This is useful because PrimeNG dropdowns can remain expanded and block
    the next dropdown selection.
    """

    page.keyboard.press("Escape")


def open_dropdown_by_index(page, dropdown_index, field_name):
    """
    Opens a dropdown by visible dropdown index.

    Current create appointment form order:
    0. Location
    1. Department
    2. Doctor / Provider
    3. Service
    4. Schedule

    Supports PrimeNG dropdown structures where the actual combobox input
    may be hidden.
    """

    candidate_selectors = [
        "[aria-label='dropdown trigger']",
        ".p-dropdown-trigger",
        "[role='button'][aria-haspopup='listbox']",
        ".p-dropdown",
    ]

    last_error = None

    for selector in candidate_selectors:
        try:
            locator_group = page.locator(selector)
            visible_locators = get_visible_locators(locator_group)

            if len(visible_locators) <= dropdown_index:
                continue

            dropdown = visible_locators[dropdown_index]

            click_when_visible(dropdown, timeout=5000)

            if wait_for_dropdown_options_to_open(page, timeout=3000):
                return

            close_open_dropdowns(page)

        except Exception as error:
            last_error = error
            close_open_dropdowns(page)
            continue

    raise AssertionError(
        f"Could not open {field_name} dropdown at index {dropdown_index}. "
        f"Tried: {candidate_selectors}. "
        f"Current URL: {page.url}"
    ) from last_error


def select_random_dropdown_option_by_index(
    page,
    dropdown_index,
    field_name,
    exclude_texts=None,
):
    """
    Opens a visible dropdown by index and selects a random available option.
    """

    if exclude_texts is None:
        exclude_texts = set()

    close_open_dropdowns(page)

    open_dropdown_by_index(page, dropdown_index, field_name)

    option = get_random_visible_dropdown_option(
        page,
        field_name,
        exclude_texts=exclude_texts,
    )

    selected_text = clean_visible_text(option.inner_text())

    click_when_visible(option)

    close_open_dropdowns(page)

    return selected_text


def get_random_visible_dropdown_option(page, field_name, exclude_texts=None):
    """
    Returns a random visible and enabled dropdown option.
    """

    if exclude_texts is None:
        exclude_texts = set()

    normalized_exclude_texts = {
        clean_visible_text(text).lower() for text in exclude_texts
    }

    options = page.locator("[role='option']:visible, .p-dropdown-item:visible")

    expect(options.first).to_be_visible(timeout=10000)

    valid_options = []

    option_count = options.count()

    for index in range(option_count):
        option = options.nth(index)

        try:
            text = clean_visible_text(option.inner_text(timeout=1000))

            if not text:
                continue

            if text.lower() in normalized_exclude_texts:
                continue

            if is_placeholder_option(text):
                continue

            aria_disabled = option.get_attribute("aria-disabled")
            class_name = option.get_attribute("class") or ""

            if aria_disabled == "true" or "disabled" in class_name.lower():
                continue

            valid_options.append(option)

        except Exception:
            continue

    if not valid_options:
        raise AssertionError(f"No valid options found for {field_name} dropdown.")

    return random.choice(valid_options)


def select_random_available_appointment_slot(page):
    """
    Randomly selects one available appointment time slot.

    Uses visible role='option' elements with AM/PM time text.
    """

    time_pattern = re.compile(r"\b\d{1,2}:\d{2}\s*(AM|PM)\b", re.I)

    time_options = page.locator("[role='option']:visible").filter(
        has_text=time_pattern
    )

    expect(time_options.first).to_be_visible(timeout=15000)

    valid_time_options = []

    time_option_count = time_options.count()

    for index in range(time_option_count):
        option = time_options.nth(index)

        try:
            text = clean_visible_text(option.inner_text(timeout=1000))

            if not text:
                continue

            aria_disabled = option.get_attribute("aria-disabled")
            class_name = option.get_attribute("class") or ""

            if aria_disabled == "true" or "disabled" in class_name.lower():
                continue

            valid_time_options.append(option)

        except Exception:
            continue

    if not valid_time_options:
        raise AssertionError("No available appointment time slots were found.")

    selected_time_option = random.choice(valid_time_options)
    selected_time = clean_visible_text(selected_time_option.inner_text())

    click_when_visible(selected_time_option)

    return selected_time


def add_appointment_note(page, note):
    """
    Adds appointment note.
    """

    note_box = page.get_by_role("textbox", name=re.compile(r"Add Note", re.I))

    fill_when_visible(note_box, note)

    click_when_visible(page.get_by_role("button", name=re.compile(r"^Save$", re.I)))


def upload_appointment_attachment(page, attachment_path):
    """
    Uploads appointment attachment.

    Handles file chooser correctly when clicking the attachment icon opens
    the system/browser file picker.
    """

    file_path = Path(attachment_path).resolve()

    if not file_path.exists():
        raise FileNotFoundError(f"Attachment file not found: {file_path}")

    attachment_button = page.locator("#actnImg_BUS_notAttch")

    try:
        with page.expect_file_chooser(timeout=5000) as file_chooser_info:
            click_when_visible(attachment_button, timeout=10000)

        file_chooser = file_chooser_info.value
        file_chooser.set_files(str(file_path))

        return

    except PlaywrightTimeoutError:
        # Fallback for UI versions where the file input exists directly
        # and no file chooser event is emitted.
        file_input = page.locator("input[type='file']").last

        expect(file_input).to_be_attached(timeout=5000)
        file_input.set_input_files(str(file_path))

        return
    
def wait_for_created_appointment_to_appear(page, consumer_profile):
    """
    Waits until the created appointment/consumer is visible after confirmation.

    After confirming an appointment, the app may return to:
    - dashboard booking list
    - appointments listing page

    This wait prevents trying to click View before the page has finished loading.
    """

    consumer_pattern = build_flexible_text_pattern(consumer_profile["full_name"])

    created_consumer_text = page.get_by_text(consumer_pattern).first

    expect(created_consumer_text).to_be_visible(timeout=30000)


def confirm_appointment(page, consumer_profile=None):
    """
    Confirms appointment creation.

    If consumer_profile is provided, waits until the created appointment appears
    on the returned dashboard/listing page.
    """

    confirm_button = page.get_by_role("button", name=re.compile(r"^Confirm$", re.I))

    click_when_visible(confirm_button)

    wait_for_network_idle(page)

    if consumer_profile is not None:
        wait_for_created_appointment_to_appear(page, consumer_profile)


def open_created_appointment_details(page, consumer_profile):
    """
    Opens the newly created appointment details.

    Supports both UI results after appointment confirmation:
    1. Appointments listing page with patient appointment tab
    2. Dashboard page with booking row and View button
    """

    wait_for_created_appointment_to_appear(page, consumer_profile)

    consumer_pattern = build_flexible_text_pattern(consumer_profile["full_name"])

    # Scenario 1:
    # Appointments listing page has appointment rows/tabs.
    # Use locator("[role='tab']").filter(has_text=...) instead of get_by_role(..., name=...)
    # because the accessible name can include checkbox/status/provider text.
    appointment_tab = page.locator("[role='tab']").filter(
        has_text=consumer_pattern
    ).first

    if click_if_visible(appointment_tab, timeout=10000):
        wait_for_network_idle(page)

        details_button = page.get_by_role(
            "button",
            name=re.compile(r"(Assign Myself\s*)?View Details", re.I),
        ).first

        if click_if_visible(details_button, timeout=10000):
            wait_for_network_idle(page)
            return

        # Some UI versions may open the details directly after tab click.
        if page.locator(selectors.APPOINTMENT_DETAILS_BACK_BUTTON).is_visible():
            return

        raise AssertionError(
            "Clicked created appointment tab, but View Details button did not appear. "
            f"Consumer: {consumer_profile['full_name']}. "
            f"Current URL: {page.url}"
        )

    # Scenario 2:
    # Dashboard booking card/row has patient name and View button.
    view_button_pattern = re.compile(r"^View$", re.I)

    booking_container = (
        page.locator("div")
        .filter(has_text=consumer_pattern)
        .filter(has=page.get_by_role("button", name=view_button_pattern))
        .last
    )

    try:
        expect(booking_container).to_be_visible(timeout=20000)

        view_button = booking_container.get_by_role(
            "button",
            name=view_button_pattern,
        ).first

        click_when_visible(view_button, timeout=10000)

        wait_for_network_idle(page)

        details_button = page.get_by_role(
            "button",
            name=re.compile(r"(Assign Myself\s*)?View Details", re.I),
        ).first

        if click_if_visible(details_button, timeout=5000):
            wait_for_network_idle(page)

        return

    except Exception as error:
        raise AssertionError(
            "Could not open created appointment details. "
            f"Consumer: {consumer_profile['full_name']}. "
            f"Current URL: {page.url}"
        ) from error


def assert_created_patient_visible(page, consumer_profile):
    """
    Verifies created consumer/patient name is visible somewhere on the page.
    """

    consumer_pattern = build_flexible_text_pattern(consumer_profile["full_name"])

    expect(page.get_by_text(consumer_pattern).first).to_be_visible(timeout=15000)

def is_take_appointment_form_opened(page, timeout=3000):
    """
    Returns True if the take appointment/create appointment form is open.
    """

    create_new_patient = page.get_by_text("Create New Patient", exact=True)

    try:
        expect(create_new_patient).to_be_visible(timeout=timeout)
        return True

    except Exception:
        return False


def assert_take_appointment_form_opened(page):
    """
    Verifies that the take appointment/create appointment form is open.
    """

    create_new_patient = page.get_by_text("Create New Patient", exact=True)

    expect(create_new_patient).to_be_visible(timeout=15000)


def open_take_appointment_from_dashboard_button(page):
    """
    Opens take appointment flow from dashboard using Create Appointment button.
    """

    create_appointment_button = page.get_by_role(
        "button",
        name=re.compile(r"^Create Appointment$", re.I),
    ).first

    click_when_visible(create_appointment_button, timeout=10000)

    wait_for_network_idle(page)

    assert_take_appointment_form_opened(page)


def open_take_appointment_from_sidebar(page):
    """
    Opens take appointment flow from the sidebar Appointment link.

    Flow:
    1. Click sidebar Appointment link
    2. Try possible Appointment entry points
    3. Verify Create New Patient is visible
    """

    appointment_sidebar_link = page.locator(
        "a[href*='/business/appointments']"
    ).first

    click_when_visible(appointment_sidebar_link, timeout=10000)

    wait_for_network_idle(page)

    if is_take_appointment_form_opened(page):
        return

    possible_appointment_entry_points = [
        page.locator("p-card").filter(
            has_text=re.compile(r"^\s*Appointment\s*$", re.I)
        ).first,

        page.get_by_text("Appointment", exact=True).last,

        page.locator("text=Appointment").last,
    ]

    for entry_point in possible_appointment_entry_points:
        if click_if_visible(entry_point, timeout=5000):
            wait_for_network_idle(page)

            if is_take_appointment_form_opened(page, timeout=5000):
                return

    create_appointment_button = page.get_by_role(
        "button",
        name=re.compile(r"^Create Appointment$", re.I),
    ).first

    if click_if_visible(create_appointment_button, timeout=5000):
        wait_for_network_idle(page)

        if is_take_appointment_form_opened(page, timeout=5000):
            return

    raise AssertionError(
        "Could not open take appointment flow from sidebar. "
        "Tried sidebar Appointment link, Appointment card/text, and Create Appointment button."
    )




# ----------------------------------------------------------------------
# Shared appointment helper actions
# ----------------------------------------------------------------------

def build_flexible_text_pattern(text):
    """
    Converts normal text into a flexible regex.

    Example:
        Jisha Rajan

    Becomes:
        Jisha\\s+Rajan

    This helps when the UI has hidden spaces, new lines, or non-breaking spaces.
    """

    words = text.strip().split()

    flexible_text = r"\s+".join(
        re.escape(word) for word in words
    )

    return re.compile(flexible_text, re.I)


def click_if_visible(locator, timeout=3000):
    """
    Clicks locator only if it is visible within the given timeout.
    """

    try:
        expect(locator).to_be_visible(timeout=timeout)
        locator.click()
        return True

    except Exception:
        return False


def clean_visible_text(value):
    """
    Normalizes visible text from UI elements.
    """

    return " ".join(value.split())


def is_placeholder_option(text):
    """
    Returns True for placeholder options that should not be selected.
    """

    placeholder_words = [
        "select",
        "choose",
        "please choose",
        "service",
    ]

    lowered_text = text.strip().lower()

    return lowered_text in placeholder_words


def get_visible_locators(locator_group):
    """
    Returns visible locators from a locator group.
    """

    visible_locators = []

    count = locator_group.count()

    for index in range(count):
        locator = locator_group.nth(index)

        try:
            expect(locator).to_be_visible(timeout=300)
            visible_locators.append(locator)

        except Exception:
            continue

    return visible_locators


def wait_for_dropdown_options_to_open(page, timeout=3000):
    """
    Returns True when dropdown options are visible.
    """

    options = page.locator(
        "[role='option']:visible, "
        ".p-dropdown-item:visible, "
        "mat-option:visible"
    )

    try:
        expect(options.first).to_be_visible(timeout=timeout)
        return True

    except Exception:
        return False
    

def open_appointments_dashboard_from_sidebar(page):
    """
    Opens the appointment dashboard from the side panel appointment icon/link.
    """

    appointment_sidebar_link = page.locator("a[href*='/business/appointments']").first

    click_when_visible(appointment_sidebar_link, timeout=15000)

    expect(page).to_have_url(re.compile(r".*/business/appointments.*"), timeout=20000)

    expect(
        page.get_by_text(re.compile(r"Welcome to your Appointments", re.I)).first
    ).to_be_visible(timeout=20000)

    wait_for_network_idle(page)


def open_random_appointment_details_from_dashboard(page):
    """
    Randomly selects one visible appointment accordion/tab from the
    appointment dashboard and opens its details page.
    """

    appointment_tabs = page.locator("[role='tab']").filter(
        has_text=re.compile(r"\d{1,2}:\d{2}\s*(AM|PM)", re.I)
    )

    expect(appointment_tabs.first).to_be_visible(timeout=20000)

    visible_appointment_tabs = []

    tab_count = appointment_tabs.count()

    for index in range(tab_count):
        appointment_tab = appointment_tabs.nth(index)

        try:
            if appointment_tab.is_visible():
                visible_appointment_tabs.append(appointment_tab)

        except Exception:
            continue

    if not visible_appointment_tabs:
        raise AssertionError(
            f"No visible appointment accordion/tab found. Current URL: {page.url}"
        )

    random_appointment_tab = random.choice(visible_appointment_tabs)

    selected_appointment_text = clean_visible_text(
        random_appointment_tab.inner_text()
    )

    click_when_visible(random_appointment_tab, timeout=10000)

    details_button = page.get_by_role(
        "button",
        name=re.compile(r"(Assign Myself\s*)?View Details|View Details", re.I),
    ).first

    click_when_visible(details_button, timeout=15000)

    wait_for_network_idle(page)

    assert_appointment_details_opened(page)

    return selected_appointment_text


def open_last_appointment_details_from_dashboard(page):
    """
    Opens the last appointment accordion/tab from the appointment dashboard,
    then clicks View Details / Assign Myself View Details.
    """

    appointment_tabs = page.locator("[role='tab']").filter(
        has_text=re.compile(r"\d{1,2}:\d{2}\s*(AM|PM)", re.I)
    )

    expect(appointment_tabs.first).to_be_visible(timeout=20000)

    tab_count = appointment_tabs.count()

    if tab_count == 0:
        raise AssertionError(
            f"No appointment accordion/tab found. Current URL: {page.url}"
        )

    last_appointment_tab = appointment_tabs.nth(tab_count - 1)

    click_when_visible(last_appointment_tab, timeout=10000)

    details_button = page.get_by_role(
        "button",
        name=re.compile(r"(Assign Myself\s*)?View Details", re.I),
    ).first

    click_when_visible(details_button, timeout=15000)

    wait_for_network_idle(page)

    assert_appointment_details_opened(page)

def open_more_actions_menu(page):
    """
    Opens More Actions only when still on appointment details page.

    If Less Actions or expanded action buttons are already visible,
    it does nothing.
    """

    if is_followup_create_page(page):
        return

    less_actions_button = page.get_by_role(
        "button",
        name=re.compile(r"Less Actions", re.I),
    ).first

    if less_actions_button.is_visible():
        return

    send_message_button = page.get_by_role(
        "button",
        name=re.compile(r"Send Message", re.I),
    ).first

    if send_message_button.is_visible():
        return

    more_actions_button = page.get_by_role(
        "button",
        name=re.compile(r"More Actions", re.I),
    ).first

    click_when_visible(more_actions_button, timeout=15000)

    page.wait_for_timeout(500)


def get_appointment_action_button(page, action_text):
    """
    Returns an appointment action button by exact visible action text.

    This avoids clicking Share Info when we need Send Message.
    """

    return page.locator("button").filter(
        has_text=re.compile(rf"^\s*{re.escape(action_text)}\s*$", re.I)
    ).first


def generate_random_automation_note(prefix="Automation note"):
    """
    Generates a random note/message for appointment actions.
    """

    return f"{prefix} {uuid.uuid4().hex[:8]}"


def wait_for_success_message_to_disappear(page):
    """
    Waits for success/toast message to appear and disappear.

    Different UI versions may use different toast/snackbar containers,
    so this function checks common success message containers.
    """

    success_message = page.locator(
        ".p-toast-message-success, "
        ".p-toast-message, "
        ".toast-success, "
        ".mat-mdc-snack-bar-container, "
        "[role='alert']"
    ).first

    try:
        expect(success_message).to_be_visible(timeout=8000)
        expect(success_message).to_be_hidden(timeout=20000)

    except Exception:
        # Do not fail only because toast timing was too fast or UI changed.
        page.wait_for_timeout(2000)


def send_random_message_from_appointment_details(page):
    """
    Opens More Actions if needed, clicks Send Message, enters a random message,
    and sends it.
    """

    random_message = generate_random_automation_note("Automation message")

    open_more_actions_menu(page)

    send_message_button = get_appointment_action_button(page, "Send Message")

    click_when_visible(send_message_button, timeout=15000)

    message_box = page.get_by_role(
        "textbox",
        name=re.compile(r"Message", re.I),
    ).first

    fill_when_visible(message_box, random_message, timeout=10000)

    send_button = page.get_by_role(
        "button",
        name=re.compile(r"^send$", re.I),
    ).last

    click_when_visible(send_button, timeout=10000)

    wait_for_success_message_to_disappear(page)

    return random_message


def upload_file_using_file_chooser(page, upload_button_locator, attachment_path):
    """
    Uploads a file using Playwright file chooser handling.

    This prevents the file picker from opening and staying there.
    """

    file_path = Path(attachment_path).resolve()

    if not file_path.exists():
        raise FileNotFoundError(f"Attachment file not found: {file_path}")

    try:
        with page.expect_file_chooser(timeout=5000) as file_chooser_info:
            click_when_visible(upload_button_locator, timeout=10000)

        file_chooser = file_chooser_info.value
        file_chooser.set_files(str(file_path))

        return

    except PlaywrightTimeoutError:
        file_input = page.locator("input[type='file']").last

        expect(file_input).to_be_attached(timeout=5000)
        file_input.set_input_files(str(file_path))


def send_attachment_from_appointment_details(page, attachment_path):
    """
    Opens More Actions if needed, clicks Send Attachments, uploads the sample
    attachment, and sends it.
    """

    open_more_actions_menu(page)

    send_attachment_button = get_appointment_action_button(page, "Send Attachments")

    click_when_visible(send_attachment_button, timeout=15000)

    upload_area = page.locator(".select-wrapper").last

    upload_file_using_file_chooser(
        page,
        upload_button_locator=upload_area,
        attachment_path=attachment_path,
    )

    send_button = page.get_by_role(
        "button",
        name=re.compile(r"^send$", re.I),
    ).last

    click_when_visible(send_button, timeout=10000)

    wait_for_success_message_to_disappear(page)


def select_random_future_followup_date(page):
    """
    Selects a random future date from the follow-up calendar.
    """

    days_to_add = random.randint(2, 14)
    target_date = date.today() + timedelta(days=days_to_add)

    target_pattern = re.compile(
        rf"\b{target_date.day}\s+{target_date.strftime('%B')}\b",
        re.I,
    )

    target_date_button = page.get_by_role(
        "button",
        name=target_pattern,
    ).first

    if click_if_visible(target_date_button, timeout=5000):
        return target_date

    # If the target date is in the next visible month, move calendar forward once.
    next_month_button = page.get_by_role(
        "button",
        name=re.compile(r"Next month", re.I),
    ).first

    if click_if_visible(next_month_button, timeout=5000):
        click_when_visible(target_date_button, timeout=10000)
        return target_date

    raise AssertionError(
        f"Could not select future follow-up date: {target_date}. "
        f"Current URL: {page.url}"
    )


def select_random_followup_slot(page):
    """
    Selects a random visible follow-up slot.
    """

    slot_options = page.locator("[role='option']").filter(
        has_text=re.compile(r"\d{1,2}:\d{2}\s*(AM|PM)", re.I)
    )

    expect(slot_options.first).to_be_visible(timeout=15000)

    visible_slots = []

    slot_count = slot_options.count()

    for index in range(slot_count):
        slot = slot_options.nth(index)

        try:
            if slot.is_visible():
                visible_slots.append(slot)

        except Exception:
            continue

    if not visible_slots:
        raise AssertionError(f"No visible follow-up slots found. Current URL: {page.url}")

    selected_slot = random.choice(visible_slots)
    selected_slot_text = clean_visible_text(selected_slot.inner_text())

    click_when_visible(selected_slot, timeout=10000)

    return selected_slot_text


def add_followup_note(page, note):
    """
    Adds note in follow-up popup.
    """

    notes_tab = page.get_by_text("Notes", exact=True).first

    if click_if_visible(notes_tab, timeout=5000):
        page.wait_for_timeout(500)

    note_box = page.get_by_role(
        "textbox",
        name=re.compile(r"Add Note", re.I),
    ).first

    fill_when_visible(note_box, note, timeout=10000)

    save_button = page.get_by_role(
        "button",
        name=re.compile(r"^Save$", re.I),
    ).first

    click_when_visible(save_button, timeout=10000)

    page.wait_for_timeout(1000)


def add_followup_attachment(page, attachment_path):
    """
    Adds attachment in follow-up popup.
    """

    attachment_button = page.locator("#actnImg_BUS_notAttch").first

    upload_file_using_file_chooser(
        page,
        upload_button_locator=attachment_button,
        attachment_path=attachment_path,
    )

    page.wait_for_timeout(1000)


def create_followup_from_appointment_details(page, attachment_path):
    """
    Creates a follow-up appointment from appointment details.

    Steps:
    - Click Follow Up from appointment details page
    - Wait for follow-up Create Appointment page
    - Select random future date
    - Select random slot
    - Add note
    - Add attachment
    - Confirm
    """

    followup_note = generate_random_automation_note("Automation follow-up note")

    if not is_followup_create_page(page):
        open_more_actions_menu(page)

        followup_button = page.get_by_role(
            "button",
            name=re.compile(r"Follow Up", re.I),
        ).first

        click_when_visible(followup_button, timeout=15000)

        wait_for_network_idle(page)

    wait_for_followup_create_form(page)

    selected_date = select_random_future_followup_date(page)

    page.wait_for_timeout(1000)

    selected_slot = select_random_followup_slot(page)

    add_followup_note(page, followup_note)

    add_followup_attachment(page, attachment_path)

    confirm_button = page.get_by_role(
        "button",
        name=re.compile(r"^Confirm$", re.I),
    ).first

    click_when_visible(confirm_button, timeout=15000)

    wait_for_success_message_to_disappear(page)

    return {
        "followup_date": str(selected_date),
        "followup_slot": selected_slot,
        "followup_note": followup_note,
    }


def wait_for_reschedule_form(page):
    """
    Waits until the reschedule dialog is visible.
    """

    dialog = page.get_by_role("dialog").filter(
        has_text=re.compile(r"Reschedule Booking", re.I)
    ).first

    expect(dialog).to_be_visible(timeout=20000)

    expect(dialog.get_by_text("Appointment Date", exact=True)).to_be_visible(
        timeout=20000
    )

    expect(dialog.get_by_text("Choose Slot", exact=True)).to_be_visible(
        timeout=20000
    )

    expect(
        dialog.get_by_role("button", name=re.compile(r"^Reschedule$", re.I)).first
    ).to_be_visible(timeout=20000)


def open_reschedule_calendar(page):
    """
    Opens the calendar inside the reschedule dialog by clicking the calendar icon.
    """

    dialog = page.get_by_role("dialog").filter(
        has_text=re.compile(r"Reschedule Booking", re.I)
    ).first

    expect(dialog).to_be_visible(timeout=10000)

    calendar_button = dialog.locator(
        "button.p-datepicker-trigger, "
        ".p-datepicker-trigger, "
        "button.p-button-icon-only"
    ).first

    click_when_visible(calendar_button, timeout=10000)

    datepicker = page.locator(".p-datepicker").last
    expect(datepicker).to_be_visible(timeout=10000)


def select_random_future_reschedule_date(page):
    """
    Opens the reschedule calendar icon and selects a random future date.

    It first tries future enabled dates in the visible month.
    If no future date is available, it moves to next month and selects a random date.
    """

    open_reschedule_calendar(page)

    datepicker = page.locator(".p-datepicker").last

    today = date.today()

    header_text = ""

    try:
        header_text = clean_visible_text(
            datepicker.locator(".p-datepicker-title").inner_text()
        )
    except Exception:
        header_text = ""

    day_candidates = datepicker.locator(
        "td:not(.p-disabled):not(.p-datepicker-other-month) "
        "span:not(.p-disabled), "
        "td:not(.p-disabled):not(.p-datepicker-other-month) "
        "button:not([disabled])"
    ).filter(
        has_text=re.compile(r"^\d{1,2}$")
    )

    visible_future_days = []

    day_count = day_candidates.count()

    for index in range(day_count):
        day_locator = day_candidates.nth(index)

        try:
            if not day_locator.is_visible():
                continue

            day_text = clean_visible_text(day_locator.inner_text())

            if not day_text.isdigit():
                continue

            day_number = int(day_text)

            # If current visible calendar is the current month/year,
            # choose only dates after today.
            if (
                today.strftime("%B").lower() in header_text.lower()
                and str(today.year) in header_text
                and day_number <= today.day
            ):
                continue

            visible_future_days.append(day_locator)

        except Exception:
            continue

    if not visible_future_days:
        next_month_button = page.get_by_role(
            "button",
            name=re.compile(r"Next month", re.I),
        ).first

        click_when_visible(next_month_button, timeout=10000)

        page.wait_for_timeout(500)

        day_candidates = datepicker.locator(
            "td:not(.p-disabled):not(.p-datepicker-other-month) "
            "span:not(.p-disabled), "
            "td:not(.p-disabled):not(.p-datepicker-other-month) "
            "button:not([disabled])"
        ).filter(
            has_text=re.compile(r"^\d{1,2}$")
        )

        visible_future_days = []

        day_count = day_candidates.count()

        for index in range(day_count):
            day_locator = day_candidates.nth(index)

            try:
                if day_locator.is_visible():
                    visible_future_days.append(day_locator)
            except Exception:
                continue

    if not visible_future_days:
        raise AssertionError(
            f"No enabled future date found in reschedule calendar. Current URL: {page.url}"
        )

    selected_day = random.choice(visible_future_days)
    selected_day_text = clean_visible_text(selected_day.inner_text())

    click_when_visible(selected_day, timeout=10000)

    page.wait_for_timeout(1000)

    return selected_day_text



def select_random_reschedule_slot(page):
    """
    Randomly selects one visible reschedule time slot.
    """

    slot_options = page.locator("[role='option']").filter(
        has_text=re.compile(r"\d{1,2}:\d{2}\s*(AM|PM)", re.I)
    )

    expect(slot_options.first).to_be_visible(timeout=20000)

    visible_slots = []

    slot_count = slot_options.count()

    for index in range(slot_count):
        slot = slot_options.nth(index)

        try:
            if slot.is_visible():
                visible_slots.append(slot)

        except Exception:
            continue

    if not visible_slots:
        raise AssertionError(
            f"No visible reschedule slots found. Current URL: {page.url}"
        )

    selected_slot = random.choice(visible_slots)
    selected_slot_text = clean_visible_text(selected_slot.inner_text())

    click_when_visible(selected_slot, timeout=10000)

    return selected_slot_text


def assert_reschedule_success_message(page):
    """
    Asserts that a success message appears after rescheduling.
    """

    success_message = page.locator(
        ".p-toast-message-success, "
        ".p-toast-message, "
        ".toast-success, "
        ".mat-mdc-snack-bar-container, "
        "[role='alert']"
    ).filter(
        has_text=re.compile(r"success|reschedule|updated", re.I)
    ).first

    expect(success_message).to_be_visible(timeout=15000)

    try:
        expect(success_message).to_be_hidden(timeout=20000)
    except Exception:
        page.wait_for_timeout(2000)


def reschedule_random_appointment_from_details(page):
    """
    Reschedules one random appointment.

    Steps:
    - Open More Actions if needed
    - Click Reschedule
    - Click calendar icon
    - Select random future date
    - Select random slot
    - Click Reschedule
    - Assert success message
    """

    open_more_actions_menu(page)

    reschedule_button = get_appointment_action_button(page, "Reschedule")

    click_when_visible(reschedule_button, timeout=15000)

    wait_for_reschedule_form(page)

    selected_date = select_random_future_reschedule_date(page)

    selected_slot = select_random_reschedule_slot(page)

    dialog = page.get_by_role("dialog").filter(
        has_text=re.compile(r"Reschedule Booking", re.I)
    ).first

    confirm_reschedule_button = dialog.get_by_role(
        "button",
        name=re.compile(r"^Reschedule$", re.I),
    ).first

    click_when_visible(confirm_reschedule_button, timeout=15000)

    assert_reschedule_success_message(page)

    return {
        "reschedule_date": selected_date,
        "reschedule_slot": selected_slot,
    }


def perform_random_appointment_reschedule(page):
    """
    Complete reschedule flow:
    - Open appointment dashboard from sidebar
    - Randomly select one visible appointment
    - Open appointment details
    - Reschedule with random future date and random slot
    """

    open_appointments_dashboard_from_sidebar(page)

    selected_appointment = open_random_appointment_details_from_dashboard(page)

    reschedule_result = reschedule_random_appointment_from_details(page)

    return {
        "selected_appointment": selected_appointment,
        "reschedule_result": reschedule_result,
    }

def perform_random_appointment_detail_actions(page, attachment_path):
    """
    Complete flow:
    - Open appointment dashboard from sidebar
    - Randomly select one visible appointment
    - Open appointment details
    - Send random message
    - Send attachment
    - Create follow-up with random future date, random slot, note, and attachment

    Function name kept same to avoid changing existing test imports.
    """

    open_appointments_dashboard_from_sidebar(page)

    selected_appointment = open_random_appointment_details_from_dashboard(page)

    sent_message = send_random_message_from_appointment_details(page)

    send_attachment_from_appointment_details(page, attachment_path)

    followup_details = create_followup_from_appointment_details(page, attachment_path)

    return {
        "selected_appointment": selected_appointment,
        "sent_message": sent_message,
        "followup_details": followup_details,
    }

def is_followup_create_page(page):
    """
    Returns True if the current page is the follow-up appointment creation page.
    """

    return "type=followup" in page.url


def wait_for_followup_create_form(page):
    """
    Waits until the follow-up Create Appointment form is visible.
    """

    expect(
        page.get_by_role("heading", name=re.compile(r"Create Appointment", re.I))
    ).to_be_visible(timeout=20000)

    expect(page.get_by_text("Select Service", exact=True)).to_be_visible(
        timeout=20000
    )

    expect(page.get_by_text("Select Slots", exact=True)).to_be_visible(
        timeout=20000
    )

    expect(
        page.get_by_role("button", name=re.compile(r"^Confirm$", re.I)).first
    ).to_be_visible(timeout=20000)


def open_random_appointment_details_from_dashboard(page):
    """
    Randomly selects one visible appointment accordion/tab from the
    appointment dashboard and opens its details page.
    """

    appointment_tabs = page.locator("[role='tab']").filter(
        has_text=re.compile(r"\d{1,2}:\d{2}\s*(AM|PM)", re.I)
    )

    expect(appointment_tabs.first).to_be_visible(timeout=20000)

    visible_appointment_tabs = []

    tab_count = appointment_tabs.count()

    for index in range(tab_count):
        appointment_tab = appointment_tabs.nth(index)

        try:
            if appointment_tab.is_visible():
                visible_appointment_tabs.append(appointment_tab)

        except Exception:
            continue

    if not visible_appointment_tabs:
        raise AssertionError(
            f"No visible appointment accordion/tab found. Current URL: {page.url}"
        )

    random_appointment_tab = random.choice(visible_appointment_tabs)

    selected_appointment_text = clean_visible_text(
        random_appointment_tab.inner_text()
    )

    click_when_visible(random_appointment_tab, timeout=10000)

    details_button = page.get_by_role(
        "button",
        name=re.compile(r"(Assign Myself\s*)?View Details|View Details", re.I),
    ).first

    click_when_visible(details_button, timeout=15000)

    wait_for_network_idle(page)

    assert_appointment_details_opened(page)

    return selected_appointment_text
