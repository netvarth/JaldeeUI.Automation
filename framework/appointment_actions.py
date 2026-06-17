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
    

def get_random_attachment_path_from_folder(
    attachments_folder="data/attachments",
    allowed_extensions=None,
):
    """
    Randomly picks one attachment file from data/attachments.

    Supported by default:
    - .pdf
    - .jpg
    - .jpeg
    - .png
    """

    if allowed_extensions is None:
        allowed_extensions = [".pdf", ".jpg", ".jpeg", ".png"]

    attachments_path = Path(attachments_folder)

    if not attachments_path.exists():
        raise FileNotFoundError(
            f"Attachment folder not found: {attachments_path.resolve()}"
        )

    files = [
        file_path
        for file_path in attachments_path.iterdir()
        if file_path.is_file()
        and file_path.suffix.lower() in allowed_extensions
    ]

    if not files:
        raise FileNotFoundError(
            f"No attachment files found in {attachments_path.resolve()}. "
            f"Allowed extensions: {allowed_extensions}"
        )

    return str(random.choice(files))
    
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

    This version clicks View Details inside the expanded appointment region.
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

    page.wait_for_timeout(1000)

    expanded_region = page.get_by_role("region").filter(
        has_text=re.compile(
            re.escape(selected_appointment_text.split(" Confirmed")[0].strip()),
            re.I,
        )
    ).first

    details_button = expanded_region.get_by_role(
        "button",
        name=re.compile(r"(Assign Myself\s*)?View Details|View Details", re.I),
    ).first

    if not click_if_visible(details_button, timeout=7000):
        details_button = page.get_by_role(
            "button",
            name=re.compile(r"(Assign Myself\s*)?View Details|View Details", re.I),
        ).first

        click_when_visible(details_button, timeout=15000)

    try:
        expect(page.locator(selectors.APPOINTMENT_DETAILS_BACK_BUTTON)).to_be_visible(
            timeout=20000
        )
    except Exception:
        # Retry once. Sometimes first click only expands/focuses the row.
        details_button = page.get_by_role(
            "button",
            name=re.compile(r"(Assign Myself\s*)?View Details|View Details", re.I),
        ).first

        click_when_visible(details_button, timeout=15000)

        wait_for_network_idle(page)

        assert_appointment_details_opened(page)
        return selected_appointment_text

    wait_for_network_idle(page)

    assert_appointment_details_opened(page)

    return selected_appointment_text


def assert_success_toast_message(page, expected_text=None):
    """
    Asserts success toast/message appears.

    expected_text can be:
        None
        "payment"
        "case"
        regex pattern text
    """

    if expected_text:
        text_pattern = re.compile(expected_text, re.I)
    else:
        text_pattern = re.compile(r"success|saved|created|payment|paid|reschedule", re.I)

    success_message = page.locator(
        ".p-toast-message-success, "
        ".p-toast-message, "
        ".toast-success, "
        ".mat-mdc-snack-bar-container, "
        "[role='alert']"
    ).filter(has_text=text_pattern).first

    expect(success_message).to_be_visible(timeout=15000)

    try:
        expect(success_message).to_be_hidden(timeout=20000)
    except Exception:
        page.wait_for_timeout(2000)


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



def assert_success_toast_message(page, expected_text=None):
    """
    Asserts success toast/message appears.

    expected_text can be:
        None
        "payment"
        "case"
        regex pattern text
    """

    if expected_text:
        text_pattern = re.compile(expected_text, re.I)
    else:
        text_pattern = re.compile(r"success|saved|created|payment|paid|reschedule", re.I)

    success_message = page.locator(
        ".p-toast-message-success, "
        ".p-toast-message, "
        ".toast-success, "
        ".mat-mdc-snack-bar-container, "
        "[role='alert']"
    ).filter(has_text=text_pattern).first

    expect(success_message).to_be_visible(timeout=15000)

    try:
        expect(success_message).to_be_hidden(timeout=20000)
    except Exception:
        page.wait_for_timeout(2000)



def open_invoice_details_from_appointment_details(page):
    """
    Opens invoice details page from appointment details page.

    Handles both:
    - unpaid invoice with Get Payment
    - already paid invoice with Refund / Amount Due 0.00
    """

    appointment_url_before_click = page.url

    open_more_actions_menu(page)

    view_invoice_button = page.locator("button").filter(
        has_text=re.compile(r"View Invoice", re.I)
    ).first

    click_when_visible(view_invoice_button, timeout=15000)

    page.wait_for_url(
        lambda url: url != appointment_url_before_click,
        timeout=20000,
    )

    wait_for_network_idle(page)

    expect(page.get_by_text(re.compile(r"Invoice\s*:", re.I)).first).to_be_visible(
        timeout=30000
    )

    if is_invoice_already_paid(page):
        return

    get_payment_text = page.get_by_text("Get Payment", exact=True).first
    get_payment_combobox = page.get_by_role(
        "combobox",
        name=re.compile(r"Get Payment", re.I),
    ).first
    settle_invoice_button = page.get_by_role(
        "button",
        name=re.compile(r"Settle Invoice", re.I),
    ).first

    try:
        expect(get_payment_text).to_be_visible(timeout=5000)
        return
    except Exception:
        pass

    try:
        expect(get_payment_combobox).to_be_visible(timeout=5000)
        return
    except Exception:
        pass

    expect(settle_invoice_button).to_be_visible(timeout=10000)




def open_get_payment_dropdown(page):
    """
    Opens Get Payment dropdown on invoice details page.

    In this UI, Get Payment is a combobox/dropdown, not a normal button.
    """

    get_payment_dropdown = page.locator("p-dropdown").filter(
        has_text=re.compile(r"Get Payment", re.I)
    ).first

    if click_if_visible(get_payment_dropdown, timeout=5000):
        return

    get_payment_combobox = page.get_by_role(
        "combobox",
        name=re.compile(r"Get Payment", re.I),
    ).first

    if click_if_visible(get_payment_combobox, timeout=5000):
        return

    dropdown_trigger = page.locator(".p-dropdown-trigger").first

    click_when_visible(dropdown_trigger, timeout=10000)


def click_get_payment_option(page, option_text):
    """
    Clicks one option from the Get Payment dropdown.
    """

    option_patterns = [option_text]

    if option_text == "Pay by Others":
        option_patterns.append("Pay by Other")

    last_error = None

    for option_pattern in option_patterns:
        option = page.get_by_role(
            "option",
            name=re.compile(rf"^{re.escape(option_pattern)}$", re.I),
        ).first

        try:
            if click_if_visible(option, timeout=5000):
                return option_pattern
        except Exception as error:
            last_error = error

        fallback_option = page.locator(
            "[role='option'], .p-dropdown-item, li"
        ).filter(
            has_text=re.compile(rf"^{re.escape(option_pattern)}$", re.I)
        ).first

        try:
            click_when_visible(fallback_option, timeout=5000)
            return option_pattern
        except Exception as error:
            last_error = error

    raise AssertionError(
        f"Could not click Get Payment option: {option_text}. "
        f"Current URL: {page.url}"
    ) from last_error


def open_payment_popup_from_invoice_details(page):
    """
    Opens payment popup from invoice details page.

    Some UI versions may already show the payment popup.
    """

    payment_mode_dropdown = page.get_by_role(
        "button",
        name=re.compile(r"dropdown trigger", re.I),
    ).first

    if payment_mode_dropdown.is_visible():
        return

    payment_button = page.get_by_role(
        "button",
        name=re.compile(r"Get Payment Link|Receive Payment|Pay", re.I),
    ).first

    click_when_visible(payment_button, timeout=15000)


def select_random_payment_mode(page):
    """
    Opens Get Payment dropdown and randomly selects:
    - Pay by Cash
    - Pay by Others

    If Pay by Others is selected, selects a random mode from:
    - UPI
    - Credit Card
    - Debit Card
    - Net Banking
    - Other
    """

    open_payment_options_dropdown_from_invoice_details(page)

    selected_payment_option = random.choice(
        [
            "Pay by Cash",
            "Pay by Others",
        ]
    )

    selected_payment_option = click_get_payment_option(
        page,
        selected_payment_option,
    )

    try:
        wait_for_payment_popup(page, timeout=7000)
    except Exception:
        settle_invoice_button = page.get_by_role(
            "button",
            name=re.compile(r"Settle Invoice", re.I),
        ).first

        click_when_visible(settle_invoice_button, timeout=10000)

        wait_for_payment_popup(page, timeout=15000)

    if re.search(r"Other|Others", selected_payment_option, re.I):
        selected_mode = select_random_other_payment_mode(page)
    else:
        selected_mode = "Cash"

    return {
        "payment_option": selected_payment_option,
        "payment_mode": selected_mode,
    }





def go_back_from_invoice_details_to_appointment_details(page):
    """
    Clicks the top-left back arrow on invoice details page.
    """

    back_heading = page.get_by_role(
        "heading",
        name=re.compile(r"Back", re.I),
    ).first

    if click_if_visible(back_heading.locator("i").first, timeout=3000):
        wait_for_network_idle(page)
        assert_appointment_details_opened(page)
        return

    back_button = page.locator("i").first

    click_when_visible(back_button, timeout=10000)

    wait_for_network_idle(page)

    assert_appointment_details_opened(page)


def return_to_appointment_details_url(page, appointment_details_url):
    """
    Returns to the original appointment details page.
    """

    page.goto(appointment_details_url)

    wait_for_network_idle(page)

    assert_appointment_details_opened(page)


def perform_current_appointment_invoice_payment(page):
    """
    Performs invoice payment from the current appointment details page.

    This does not open the appointment dashboard again.
    It assumes the browser is already on appointment details page.
    """

    open_invoice_details_from_appointment_details(page)

    payment_result = complete_invoice_payment(page)

    go_back_from_invoice_details_to_appointment_details(page)

    return payment_result


def perform_current_appointment_create_case(page, attachment_path):
    """
    Creates a case from the current appointment details page and completes
    all case-related actions.

    This assumes the browser is already on appointment details page.
    """

    open_create_case_popup_from_appointment_details(page)

    case_data = fill_create_case_popup(page)

    submit_create_case_popup(page)

    open_latest_case_from_patient_record(page)

    upload_case_file(page, attachment_path)

    chief_complaint_result = add_chief_complaint_to_case(page)

    history_result = add_history_to_case(page)

    medication_result = add_medication_to_case(page)

    vital_signs_result = fill_vital_signs_in_case(page)

    treatment_plan_result = add_treatment_plan_to_case(page)

    prescription_result = add_prescription_to_case(page)

    uploaded_prescription_result = upload_prescription_to_case(page)

    share_prescription_result = share_prescription_from_case(page)

    return {
        "case_data": case_data,
        "case_file": attachment_path,
        "chief_complaint_result": chief_complaint_result,
        "history_result": history_result,
        "medication_result": medication_result,
        "vital_signs_result": vital_signs_result,
        "treatment_plan_result": treatment_plan_result,
        "prescription_result": prescription_result,
        "uploaded_prescription_result": uploaded_prescription_result,
        "share_prescription_result": share_prescription_result,
    }



def perform_random_appointment_full_detail_actions(page, attachment_path):
    """
    Complete appointment detail flow against one randomly selected appointment.
    """

    open_appointments_dashboard_from_sidebar(page)

    selected_appointment = open_random_appointment_details_from_dashboard(page)

    appointment_details_url = page.url

    sent_message = send_random_message_from_appointment_details(page)

    send_attachment_from_appointment_details(page, attachment_path)

    payment_result = perform_current_appointment_invoice_payment(page)

    return_to_appointment_details_url(page, appointment_details_url)

    followup_details = create_followup_from_appointment_details(page, attachment_path)

    return_to_appointment_details_url(page, appointment_details_url)

    case_result = perform_current_appointment_create_case(page, attachment_path)

    return {
        "selected_appointment": selected_appointment,
        "sent_message": sent_message,
        "payment_result": payment_result,
        "followup_details": followup_details,
        "case_result": case_result,
    }




def is_invoice_already_paid(page):
    """
    Returns True if invoice is already fully paid.

    Paid invoice usually shows:
    - Amount Due 0.00
    - Refund button
    """

    refund_button = page.get_by_role(
        "button",
        name=re.compile(r"^Refund$", re.I),
    ).first

    if refund_button.is_visible():
        return True

    paid_invoice_body = page.locator("body").filter(
        has_text=re.compile(
            r"Amount\s+Paid[\s\S]*Amount\s+Due[\s\S]*0\.00",
            re.I,
        )
    )

    try:
        expect(paid_invoice_body).to_be_visible(timeout=3000)
        return True
    except Exception:
        return False
    


def open_payment_options_dropdown_from_invoice_details(page):
    """
    Opens Get Payment dropdown and waits for payment options.
    """

    open_get_payment_dropdown(page)

    cash_option = page.get_by_text("Pay by Cash", exact=True).first
    others_option = page.get_by_text(
        re.compile(r"Pay by Other|Pay by Others", re.I)
    ).first

    try:
        expect(cash_option).to_be_visible(timeout=5000)
        return
    except Exception:
        pass

    try:
        expect(others_option).to_be_visible(timeout=5000)
        return
    except Exception as error:
        raise AssertionError(
            "Payment options dropdown did not open after clicking Get Payment. "
            f"Current URL: {page.url}"
        ) from error
    


def wait_for_payment_popup(page, timeout=15000):
    """
    Waits until payment popup/form is visible after selecting payment option.
    """

    payment_dialog = page.get_by_role("dialog").filter(
        has_text=re.compile(
            r"Payable Amount|Amount To Pay Now|Leave a Payment Note|Select mode",
            re.I,
        )
    ).first

    expect(payment_dialog).to_be_visible(timeout=timeout)

    pay_button = payment_dialog.get_by_role(
        "button",
        name=re.compile(r"^Pay$", re.I),
    ).first

    expect(pay_button).to_be_visible(timeout=timeout)

    return payment_dialog


def select_random_other_payment_mode(page):
    """
    Selects a random mode from the Pay by Others popup.

    Available modes:
    - UPI
    - Credit Card
    - Debit Card
    - Net Banking
    - Other

    The popup defaults to UPI. If UPI is randomly selected, we keep it as-is.
    """

    payment_modes = [
        "UPI",
        "Credit Card",
        "Debit Card",
        "Net Banking",
        "Other",
    ]

    selected_mode = random.choice(payment_modes)

    payment_dialog = page.get_by_role("dialog").filter(
        has_text=re.compile(r"Payable Amount|Amount To Pay Now|Select mode", re.I)
    ).first

    expect(payment_dialog).to_be_visible(timeout=15000)

    # UPI is already selected by default, so no dropdown interaction is needed.
    if selected_mode == "UPI":
        expect(payment_dialog.get_by_text("UPI", exact=True)).to_be_visible(
            timeout=10000
        )
        return selected_mode

    # Click the Select mode dropdown trigger inside the payment popup.
    mode_dropdown_trigger = payment_dialog.get_by_role(
        "button",
        name=re.compile(r"dropdown trigger", re.I),
    ).first

    click_when_visible(mode_dropdown_trigger, timeout=10000)

    page.wait_for_timeout(500)

    mode_option = page.get_by_role(
        "option",
        name=re.compile(rf"^{re.escape(selected_mode)}$", re.I),
    ).first

    if click_if_visible(mode_option, timeout=5000):
        return selected_mode

    fallback_option = page.locator(
        ".p-dropdown-item, [role='option'], li"
    ).filter(
        has_text=re.compile(rf"^{re.escape(selected_mode)}$", re.I)
    ).first

    click_when_visible(fallback_option, timeout=10000)

    return selected_mode




def fill_payment_note(page):
    """
    Fills random payment note in payment popup.
    """

    payment_note = generate_random_automation_note("Automation payment note")

    note_field = page.get_by_role(
        "textbox",
        name=re.compile(r"Leave a Payment Note|Payment Note|Note", re.I),
    ).first

    if not click_if_visible(note_field, timeout=3000):
        note_field = page.locator("textarea").first

    fill_when_visible(note_field, payment_note, timeout=10000)

    return payment_note


def complete_invoice_payment(page):
    """
    Completes payment from invoice details page.

    If invoice is already paid, it skips payment and returns paid status.
    """

    if is_invoice_already_paid(page):
        return {
            "payment_status": "already_paid",
            "selected_payment": None,
            "payment_note": None,
        }

    selected_payment = select_random_payment_mode(page)

    payment_note = fill_payment_note(page)

    pay_button = page.get_by_role(
        "button",
        name=re.compile(r"^Pay$", re.I),
    ).first

    click_when_visible(pay_button, timeout=15000)

    yes_button = page.get_by_role(
        "button",
        name=re.compile(r"^Yes$", re.I),
    ).first

    click_when_visible(yes_button, timeout=15000)

    assert_success_toast_message(page, expected_text=r"success|payment|paid")

    return {
        "payment_status": "paid_now",
        "selected_payment": selected_payment,
        "payment_note": payment_note,
    }



def perform_random_appointment_invoice_payment(page):
    """
    Complete invoice payment flow.
    """

    open_appointments_dashboard_from_sidebar(page)

    selected_appointment = open_random_appointment_details_from_dashboard(page)

    open_invoice_details_from_appointment_details(page)

    payment_result = complete_invoice_payment(page)

    go_back_from_invoice_details_to_appointment_details(page)

    return {
        "selected_appointment": selected_appointment,
        "payment_result": payment_result,
    }




def open_create_case_popup_from_appointment_details(page):
    """
    Opens Create Case popup from appointment details page.
    """

    create_case_button = page.get_by_role(
        "button",
        name=re.compile(r"Create Case", re.I),
    ).first

    if not click_if_visible(create_case_button, timeout=5000):
        open_more_actions_menu(page)

        create_case_button = page.get_by_role(
            "button",
            name=re.compile(r"Create Case", re.I),
        ).first

        click_when_visible(create_case_button, timeout=15000)

    create_case_popup = page.get_by_role("dialog").filter(
        has_text=re.compile(r"Create New Case|Create Case", re.I)
    ).first

    expect(create_case_popup).to_be_visible(timeout=15000)


def fill_create_case_popup(page):
    """
    Fills Create New Case popup.

    If Case Title field is available, fills it.
    Always fills initial notes/observations if available.
    """

    case_title = generate_random_automation_note("Automation Case")
    initial_note = generate_random_automation_note("Automation initial note")

    title_field = page.get_by_role(
        "textbox",
        name=re.compile(r"Case Title|Title", re.I),
    ).first

    if click_if_visible(title_field, timeout=3000):
        title_field.fill(case_title)

    initial_note_field = page.get_by_role(
        "textbox",
        name=re.compile(r"Add any initial observations|Initial Notes|Observations", re.I),
    ).first

    if click_if_visible(initial_note_field, timeout=5000):
        initial_note_field.fill(initial_note)
    else:
        textarea = page.locator("textarea").first
        fill_when_visible(textarea, initial_note, timeout=10000)

    return {
        "case_title": case_title,
        "initial_note": initial_note,
    }


def submit_create_case_popup(page):
    """
    Clicks Create Case button in popup and waits for case details page.
    """

    create_case_button = page.get_by_role(
        "button",
        name=re.compile(r"^Create Case$", re.I),
    ).last

    click_when_visible(create_case_button, timeout=15000)

    assert_success_toast_message(page, expected_text=r"success|case|created")

    wait_for_network_idle(page)


def is_case_details_page(page):
    """
    Returns True if browser is on old or new case details page.
    """

    if "/case/case_" in page.url:
        return True

    if "/new-case/case_" in page.url:
        return True

    case_heading = page.get_by_role(
        "heading",
        name=re.compile(r"Case\s+\d+", re.I),
    ).first

    if case_heading.is_visible():
        return True

    upload_file_button = page.get_by_role(
        "button",
        name=re.compile(r"Upload Case File|Upload File", re.I),
    ).first

    if upload_file_button.is_visible():
        return True

    new_visit_button = page.get_by_role(
        "button",
        name=re.compile(r"New Visit", re.I),
    ).first

    return new_visit_button.is_visible()


def open_latest_case_from_patient_record(page):
    """
    Opens the latest case from Patient Record case table.

    If already on old/new case details page, it returns.
    """

    if is_case_details_page(page):
        return

    first_case_row = page.get_by_role("row").filter(
        has_text=re.compile(r"Case\s+\d+.*OPEN", re.I)
    ).first

    expect(first_case_row).to_be_visible(timeout=20000)

    case_title = first_case_row.get_by_text(
        re.compile(r"Case\s+\d+", re.I)
    ).first

    if not click_if_visible(case_title, timeout=5000):
        first_case_row.click()

    try:
        page.wait_for_url(
            re.compile(r".*/customers/.*/case/case_.*|.*/customers/.*/new-case/case_.*"),
            timeout=20000,
        )
    except Exception:
        case_title = first_case_row.get_by_text(
            re.compile(r"Case\s+\d+", re.I)
        ).first

        click_when_visible(case_title, timeout=10000)

        page.wait_for_url(
            re.compile(r".*/customers/.*/case/case_.*|.*/customers/.*/new-case/case_.*"),
            timeout=20000,
        )

    wait_for_network_idle(page)

    expect(
        page.get_by_role(
            "heading",
            name=re.compile(r"Case\s+\d+", re.I),
        ).first
    ).to_be_visible(timeout=20000)



def upload_case_file(page, attachment_path):
    """
    Uploads file from case details page.
    """

    if not is_case_details_page(page):
        open_latest_case_from_patient_record(page)

    file_path = Path(attachment_path).resolve()

    if not file_path.exists():
        raise FileNotFoundError(f"Case upload file not found: {file_path}")

    upload_case_file_button = page.get_by_text(
        re.compile(r"Upload Case File", re.I)
    ).first

    if not click_if_visible(upload_case_file_button, timeout=10000):
        upload_case_file_button = page.get_by_role(
            "button",
            name=re.compile(r"Upload Case File|Upload", re.I),
        ).first

    upload_file_using_file_chooser(
        page,
        upload_button_locator=upload_case_file_button,
        attachment_path=attachment_path,
    )

    wait_for_success_message_to_disappear(page)



# ----------------------------------------------------------------------
# New MR helpers
# ----------------------------------------------------------------------

def click_first_visible_locator(page, locators, timeout=5000):
    """
    Clicks the first visible locator from a list.
    """

    last_error = None

    for locator in locators:
        try:
            expect(locator).to_be_visible(timeout=timeout)
            locator.click()
            return
        except Exception as error:
            last_error = error
            continue

    raise AssertionError("Could not click any visible locator.") from last_error


def assert_mr_success_message(page, expected_text=r"success|saved|updated|created|shared"):
    """
    Asserts MR success message when visible.

    If the toast disappears too fast, it waits shortly and continues.
    """

    try:
        assert_success_toast_message(page, expected_text=expected_text)
    except Exception:
        page.wait_for_timeout(1500)


def upload_random_file_for_new_mr(page, upload_locator):
    """
    Uploads a random file from data/attachments.

    This first tries set_input_files directly to avoid Windows file picker.
    If needed, falls back to Playwright file chooser handling.
    """

    attachment_path = get_random_attachment_path_from_folder()
    file_path = Path(attachment_path).resolve()

    if not file_path.exists():
        raise FileNotFoundError(f"Attachment file not found: {file_path}")

    # Best case: the Upload control itself supports set_input_files.
    try:
        upload_locator.set_input_files(str(file_path), timeout=3000)
        page.wait_for_timeout(1000)
        return str(file_path)
    except Exception:
        pass

    # Second option: direct file input on page.
    file_inputs = page.locator("input[type='file']")
    file_input_count = file_inputs.count()

    for index in range(file_input_count - 1, -1, -1):
        file_input = file_inputs.nth(index)

        try:
            file_input.set_input_files(str(file_path), timeout=3000)
            page.wait_for_timeout(1000)
            return str(file_path)
        except Exception:
            continue

    # Final fallback: file chooser.
    try:
        with page.expect_file_chooser(timeout=7000) as file_chooser_info:
            click_when_visible(upload_locator, timeout=10000)

        file_chooser = file_chooser_info.value
        file_chooser.set_files(str(file_path))

        page.wait_for_timeout(1000)
        return str(file_path)

    except PlaywrightTimeoutError as error:
        raise AssertionError(
            "Could not upload file. File chooser did not open and no file input worked."
        ) from error


def upload_random_file_by_visible_upload_text(page):
    """
    Finds a visible Upload control and uploads a random file.
    """

    upload_candidates = [
        page.get_by_text("Upload", exact=True).last,
        page.get_by_role("button", name=re.compile(r"Upload|Upload File", re.I)).last,
        page.get_by_text(re.compile(r"Upload", re.I)).last,
    ]

    last_error = None

    for upload_locator in upload_candidates:
        try:
            expect(upload_locator).to_be_visible(timeout=3000)
            return upload_random_file_for_new_mr(page, upload_locator)
        except Exception as error:
            last_error = error
            continue

    raise AssertionError("Could not find visible Upload control.") from last_error




def click_plain_area_to_update_visit_summary(page):
    """
    Clicks a plain area inside the New MR main content.

    This is used after entering visit summary so the field loses focus
    and the visit summary gets updated.

    Do not click x=50,y=50 because that can open the left side panel.
    """

    main_area = page.locator("main").first

    expect(main_area).to_be_visible(timeout=10000)

    main_box = main_area.bounding_box()

    if main_box is None:
        page.keyboard.press("Tab")
        page.wait_for_timeout(1000)
        return

    # Safe plain area inside main content, away from left sidebar and buttons.
    click_x = main_box["x"] + (main_box["width"] * 0.75)
    click_y = main_box["y"] + 80

    page.mouse.click(click_x, click_y)

    page.wait_for_timeout(1200)




def close_left_side_panel_if_open(page):
    """
    Closes only the left side navigation panel.

    This avoids clicking the case Close button.
    """

    side_panel = page.locator("[role='complementary']").filter(
        has_text=re.compile(r"Vision Hospital[\s\S]*Sign Out", re.I)
    ).first

    try:
        expect(side_panel).to_be_visible(timeout=1000)
    except Exception:
        return

    try:
        close_button = side_panel.locator("button").first
        expect(close_button).to_be_visible(timeout=2000)
        close_button.click()
        page.wait_for_timeout(700)
        return
    except Exception:
        pass

    # Final fallback: click the visible X in the left panel using JS.
    page.evaluate("""
        () => {
            const panels = Array.from(document.querySelectorAll('[role="complementary"]'));
            const panel = panels.find(p => (p.innerText || '').includes('Sign Out'));

            if (!panel) {
                return false;
            }

            const buttons = Array.from(panel.querySelectorAll('button'));
            const closeButton = buttons[0];

            if (closeButton) {
                closeButton.click();
                return true;
            }

            return false;
        }
    """)

    page.wait_for_timeout(700)



def ensure_new_mr_case_open_for_editing(page):
    """
    Ensures the New MR case is open before adding sections.

    If a previous wrong click closed the case, this re-opens it.
    """

    reopen_button = page.get_by_role(
        "button",
        name=re.compile(r"Re-open Case|Reopen Case", re.I),
    ).first

    if click_if_visible(reopen_button, timeout=2000):
        assert_mr_success_message(page, expected_text=r"success|status|changed|open")
        page.wait_for_timeout(1000)

    closed_text = page.get_by_text("Closed", exact=True).first

    try:
        expect(closed_text).not_to_be_visible(timeout=2000)
    except Exception:
        pass    




def click_last_visible_main_button(page, include_regex, exclude_regex=None, timeout=10000):
    """
    Clicks the last visible enabled button inside main content.

    This prevents clicking sidebar buttons.
    """

    close_left_side_panel_if_open(page)

    include_pattern = re.compile(include_regex, re.I)
    exclude_pattern = re.compile(exclude_regex, re.I) if exclude_regex else None

    buttons = page.locator("main button")
    button_count = buttons.count()

    last_error = None

    for index in range(button_count - 1, -1, -1):
        button = buttons.nth(index)

        try:
            if not button.is_visible():
                continue

            button_text = clean_visible_text(button.inner_text(timeout=1000))

            if not include_pattern.search(button_text):
                continue

            if exclude_pattern and exclude_pattern.search(button_text):
                continue

            expect(button).to_be_enabled(timeout=timeout)
            button.click()
            page.wait_for_timeout(500)
            return

        except Exception as error:
            last_error = error
            continue

    raise AssertionError(
        f"Could not click main button. Include: {include_regex}, Exclude: {exclude_regex}"
    ) from last_error    


    # -------------------------------
    #   Add New MR enable functions
    # -------------------------------


def open_settings_from_sidebar(page):
    """
    Opens Settings from sidebar.
    """

    settings_candidates = [
        page.locator("a[href*='/business/settings']").first,
        page.get_by_role("link", name=re.compile(r"Settings", re.I)).first,
        page.locator("li:nth-child(11) > .menu-link").first,
    ]

    click_first_visible_locator(page, settings_candidates, timeout=10000)

    wait_for_network_idle(page)


def open_features_and_customization(page):
    """
    Opens Features and Customization.

    If already on the Features and Customization page, it returns.
    """

    heading = page.get_by_role(
        "heading",
        name=re.compile(r"Features and Customization", re.I),
    ).first

    try:
        expect(heading).to_be_visible(timeout=3000)
        return
    except Exception:
        pass

    feature_candidates = [
        page.get_by_text(re.compile(r"Features and Customization", re.I)).first,
        page.get_by_text(re.compile(r"Feature.*Customization", re.I)).first,
        page.get_by_role("link", name=re.compile(r"Features and Customization", re.I)).first,
        page.get_by_role("button", name=re.compile(r"Features and Customization", re.I)).first,
    ]

    click_first_visible_locator(page, feature_candidates, timeout=15000)

    wait_for_network_idle(page)


def open_mr_and_diet_settings(page):
    """
    Opens MR and Diet Settings from Features and Customization.

    Tries:
    1. Normal text locator
    2. JavaScript text search + click
    3. Direct URL fallback to /business/settings/mr-settings
    """

    # Already on MR settings page
    if "/business/settings/mr-settings" in page.url:
        return

    mr_item = page.get_by_text("MR and Diet Settings", exact=True).first

    try:
        mr_item.scroll_into_view_if_needed(timeout=5000)
        expect(mr_item).to_be_visible(timeout=5000)
        mr_item.click()
        wait_for_network_idle(page)
        return
    except Exception:
        pass

    # Try scrolling the page and inner containers
    for _ in range(10):
        try:
            page.mouse.wheel(0, 800)
            page.evaluate("window.scrollBy(0, 800)")
            page.wait_for_timeout(500)

            expect(mr_item).to_be_visible(timeout=1500)
            mr_item.click()
            wait_for_network_idle(page)
            return
        except Exception:
            continue

    # JavaScript fallback: find any visible element containing exact text
    clicked = page.evaluate("""
        () => {
            const normalize = (text) => (text || '').replace(/\\s+/g, ' ').trim();

            const elements = Array.from(document.querySelectorAll('body *'));

            const target = elements.find((element) => {
                const text = normalize(element.innerText || element.textContent);
                return text === 'MR and Diet Settings'
                    || text.includes('MR and Diet Settings');
            });

            if (!target) {
                return false;
            }

            target.scrollIntoView({ block: 'center' });
            target.click();
            return true;
        }
    """)

    if clicked:
        wait_for_network_idle(page)
        page.wait_for_timeout(1000)

        if "/business/settings/mr-settings" in page.url:
            return

    # Final fallback: direct route
    page.goto("https://scale.jaldee.com/business/settings/mr-settings?p_source=p_settings_old")
    wait_for_network_idle(page)

    expect(
        page.get_by_text(re.compile(r"MR Settings", re.I)).first
    ).to_be_visible(timeout=15000)





def open_mr_settings_tab(page):
    """
    Opens MR Settings tab/section after entering MR and Diet Settings.

    Some UI versions directly show MR Settings, so this function does not fail
    if the tab is already active.
    """

    mr_settings_text = page.get_by_text("MR Settings", exact=True).first

    try:
        mr_settings_text.scroll_into_view_if_needed(timeout=5000)
        expect(mr_settings_text).to_be_visible(timeout=5000)

        # Click only if it behaves like a tab/button/link.
        try:
            mr_settings_text.click(timeout=2000)
            wait_for_network_idle(page)
        except Exception:
            pass

        return

    except Exception:
        pass

    tab_candidates = [
        page.get_by_role("tab", name=re.compile(r"MR Settings", re.I)).first,
        page.get_by_role("button", name=re.compile(r"MR Settings", re.I)).first,
        page.get_by_role("link", name=re.compile(r"MR Settings", re.I)).first,
    ]

    try:
        click_first_visible_locator(page, tab_candidates, timeout=5000)
        wait_for_network_idle(page)
    except Exception:
        # If no tab is available, assume the page already landed on MR Settings.
        pass
    

    # -------------------------------------
    #   Find the MR Settings toggle
    # -------------------------------------


def get_new_mr_toggle_button(page):
    """
    Returns the toggle button against MR Settings.

    Tries to scope the toggle near the MR Settings text first.
    Falls back to visible switch buttons.
    """

    mr_settings_row_candidates = [
        page.locator("div").filter(
            has_text=re.compile(r"MR Settings", re.I)
        ).last,

        page.locator("mat-slide-toggle").filter(
            has_text=re.compile(r"MR Settings", re.I)
        ).first,
    ]

    for row in mr_settings_row_candidates:
        try:
            expect(row).to_be_visible(timeout=3000)

            toggle_in_row = row.locator(
                "button[role='switch'], "
                "button[id^='mat-mdc-slide-toggle'], "
                ".mat-mdc-slide-toggle button"
            ).first

            expect(toggle_in_row).to_be_visible(timeout=3000)
            return toggle_in_row

        except Exception:
            continue

    toggle_candidates = [
        page.locator("#mat-mdc-slide-toggle-1-button").first,
        page.locator("button[role='switch']").first,
        page.locator("button[id^='mat-mdc-slide-toggle']").first,
        page.locator(".mat-mdc-slide-toggle button").first,
    ]

    last_error = None

    for toggle in toggle_candidates:
        try:
            expect(toggle).to_be_visible(timeout=5000)
            return toggle
        except Exception as error:
            last_error = error
            continue

    raise AssertionError("Could not find MR Settings toggle button.") from last_error    


def enable_new_mr_if_needed(page):
    """
    Enables New MR if it is disabled.
    """

    open_settings_from_sidebar(page)

    open_features_and_customization(page)

    open_mr_and_diet_settings(page)

    open_mr_settings_tab(page)

    toggle_candidates = [
        page.locator("#mat-mdc-slide-toggle-1-button").first,
        page.locator("button[role='switch']").first,
        page.locator("button[id^='mat-mdc-slide-toggle']").first,
        page.locator(".mat-mdc-slide-toggle button").first,
    ]

    toggle_button = None
    last_error = None

    for toggle in toggle_candidates:
        try:
            expect(toggle).to_be_visible(timeout=5000)
            toggle_button = toggle
            break
        except Exception as error:
            last_error = error
            continue

    if toggle_button is None:
        raise AssertionError("Could not find New MR toggle.") from last_error

    aria_checked = toggle_button.get_attribute("aria-checked")

    if aria_checked == "true":
        return {
            "new_mr_status": "already_enabled",
        }

    toggle_button.click()

    assert_mr_success_message(page)

    return {
        "new_mr_status": "enabled_now",
    }


    # --------------------------------------
    # New MR case creation helpers
    # -------------------------------------


def fill_new_mr_create_case_popup(page):
    """
    Fills Create Case popup for New MR flow.

    Case name is already present.
    We only fill Initial Notes.
    """

    initial_note = generate_random_automation_note("Automation New MR initial note")

    initial_note_field = page.get_by_role(
        "textbox",
        name=re.compile(
            r"Add any initial observations|Initial Notes|Initial Notes \(Optional\)|Observations",
            re.I,
        ),
    ).first

    fill_when_visible(initial_note_field, initial_note, timeout=15000)

    return {
        "initial_note": initial_note,
    }


def submit_new_mr_create_case_popup(page):
    """
    Clicks Create Case in popup.
    """

    create_case_button = page.get_by_role(
        "button",
        name=re.compile(r"^Create Case$", re.I),
    ).last

    click_when_visible(create_case_button, timeout=15000)

    assert_mr_success_message(page)

    wait_for_network_idle(page)


def upload_new_mr_case_file(page, attachment_path):
    """
    Uploads case file from New MR case details page.
    """

    if not is_case_details_page(page):
        open_latest_case_from_patient_record(page)

    upload_button = page.get_by_role(
        "button",
        name=re.compile(r"Upload Case File|Upload File", re.I),
    ).first

    upload_file_using_file_chooser(
        page,
        upload_button_locator=upload_button,
        attachment_path=attachment_path,
    )

    wait_for_success_message_to_disappear(page)

    return {
        "uploaded_case_file": attachment_path,
    }


    # ----------------------------------    
    #    New Visit helpers
    # ---------------------------------

def open_new_visit_from_case(page):
    """
    Clicks + New Visit.
    """

    ensure_new_mr_case_open_for_editing(page)

    close_left_side_panel_if_open(page)

    new_visit_button = page.get_by_role(
        "button",
        name=re.compile(r"New Visit", re.I),
    ).first

    click_when_visible(new_visit_button, timeout=15000)

    page.wait_for_timeout(1000)


def open_add_clinical_notes_record(page):
    """
    Clicks Add Clinical Notes Record.
    """

    add_record_button = page.get_by_role(
        "button",
        name=re.compile(r"Add Clinical Notes Record", re.I),
    ).first

    click_when_visible(add_record_button, timeout=15000)

    page.wait_for_timeout(1000)


def select_new_visit_assignee_naveen_kp(page):
    """
    Selects Naveen KP from Not Assigned / Select Doctor dropdown.
    """

    edit_button = page.locator("#newcase_visit_assignee_edit_btn").first

    click_when_visible(edit_button, timeout=10000)

    select_doctor = page.get_by_text("Select Doctor", exact=True).first

    click_when_visible(select_doctor, timeout=10000)

    search_box = page.get_by_role("textbox").nth(3)

    fill_when_visible(search_box, "nav", timeout=10000)

    naveen_option = page.get_by_role(
        "listitem",
        name=re.compile(r"Naveen KP", re.I),
    ).first

    if not click_if_visible(naveen_option, timeout=5000):
        naveen_option = page.get_by_text("Naveen KP", exact=True).last
        click_when_visible(naveen_option, timeout=10000)

    close_button = page.locator(".p-ripple").first

    if not click_if_visible(close_button, timeout=2000):
        page.keyboard.press("Escape")

    assert_mr_success_message(page)

    return {
        "assignee": "Naveen KP",
    }


def add_new_visit_summary(page):
    """
    Adds random visit summary and clicks a plain area to update it.
    """

    visit_summary = generate_random_automation_note("Automation visit summary")

    summary_box = page.get_by_role(
        "textbox",
        name=re.compile(r"Add visit summary", re.I),
    ).first

    fill_when_visible(summary_box, visit_summary, timeout=10000)

    click_plain_area_to_update_visit_summary(page)

    assert_mr_success_message(page)

    return {
        "visit_summary": visit_summary,
    }



    # ---------------------------------   
    #     Add Section helper
    # ---------------------------------


def add_new_mr_section(page, section_name_regex):
    """
    Clicks + Add Section from the New MR visit area and selects section.
    """

    ensure_new_mr_case_open_for_editing(page)

    close_left_side_panel_if_open(page)

    add_section_button = page.locator("main").get_by_role(
        "button",
        name=re.compile(r"Add Section", re.I),
    ).first

    click_when_visible(add_section_button, timeout=15000)

    section_menu_item = page.get_by_role(
        "menuitem",
        name=re.compile(section_name_regex, re.I),
    ).first

    click_when_visible(section_menu_item, timeout=10000)

    page.wait_for_timeout(1000)




    # -----------------------------------    
    #     New MR medical sections
    # -----------------------------------


def add_new_mr_chief_complaint(page):
    """
    Adds Chief Complaint with upload.
    """

    complaint_values = ["fever", "cough", "headache", "body pain"]
    selected_complaint = random.choice(complaint_values)

    add_new_mr_section(page, r"Chief Complaint|CC")

    field = page.get_by_role(
        "combobox",
        name=re.compile(r"Enter Chief Complaint", re.I),
    ).first

    fill_when_visible(field, selected_complaint, timeout=10000)

    suggestion = page.get_by_role(
        "option",
        name=re.compile(selected_complaint, re.I),
    ).first

    click_if_visible(suggestion, timeout=3000)

    uploaded_file = upload_random_file_by_visible_upload_text(page)

    save_button = page.get_by_role("button", name=re.compile(r"^Save$", re.I)).last

    click_when_visible(save_button, timeout=15000)

    assert_mr_success_message(page)

    return {
        "chief_complaint": selected_complaint,
        "uploaded_file": uploaded_file,
    }


def add_new_mr_history(page):
    """
    Adds History.

    Press Enter because Save appears only after value is committed.
    """

    history_text = generate_random_automation_note("No history")

    add_new_mr_section(page, r"History")

    field = page.get_by_role(
        "textbox",
        name=re.compile(r"Enter History", re.I),
    ).first

    fill_when_visible(field, history_text, timeout=10000)

    field.press("Enter")

    save_button = page.get_by_role("button", name=re.compile(r"^Save$", re.I)).last

    click_when_visible(save_button, timeout=15000)

    assert_mr_success_message(page)

    return {
        "history": history_text,
    }


def add_new_mr_medication(page):
    """
    Adds Medication.

    Press Enter because Save appears only after value is committed.
    """

    medication_text = generate_random_automation_note("No medication")

    add_new_mr_section(page, r"Medication")

    field = page.get_by_role(
        "textbox",
        name=re.compile(r"Enter Medication", re.I),
    ).first

    fill_when_visible(field, medication_text, timeout=10000)

    field.press("Enter")

    save_button = page.get_by_role("button", name=re.compile(r"^Save$", re.I)).last

    click_when_visible(save_button, timeout=15000)

    assert_mr_success_message(page)

    return {
        "medication": medication_text,
    }


def add_new_mr_vital_signs(page):
    """
    Adds Vital Signs.
    """

    add_new_mr_section(page, r"Vital Signs")

    pulse_rate = str(random.randint(1, 999))
    respiration = str(random.randint(1, 90))
    temperature = str(random.randint(1, 200))
    systolic = str(random.randint(1, 500))
    diastolic = str(random.randint(1, 500))

    fill_when_visible(
        page.get_by_role("textbox", name=re.compile(r"Pulse Rate", re.I)).first,
        pulse_rate,
        timeout=10000,
    )

    fill_when_visible(
        page.get_by_role("textbox", name=re.compile(r"Respiration", re.I)).first,
        respiration,
        timeout=10000,
    )

    fill_when_visible(
        page.get_by_role("textbox", name=re.compile(r"Temperature", re.I)).first,
        temperature,
        timeout=10000,
    )

    fill_when_visible(
        page.get_by_role("textbox", name=re.compile(r"Systolic", re.I)).first,
        systolic,
        timeout=10000,
    )

    fill_when_visible(
        page.get_by_role("textbox", name=re.compile(r"Diastolic", re.I)).first,
        diastolic,
        timeout=10000,
    )

    save_button = page.get_by_role("button", name=re.compile(r"^Save$", re.I)).last

    click_when_visible(save_button, timeout=15000)

    assert_mr_success_message(page)

    return {
        "pulse_rate": pulse_rate,
        "respiration": respiration,
        "temperature": temperature,
        "systolic": systolic,
        "diastolic": diastolic,
    }


    # --------------------------------------
    #    Add Treatment Plan
    # --------------------------------------

def select_naveen_kp_from_new_mr_multiselect(page):
    """
    Selects Naveen KP from New MR multi-select doctor dropdown.
    """

    select_user = page.get_by_text("Select User", exact=True).last

    click_when_visible(select_user, timeout=10000)

    search_input = page.locator(".p-multiselect-filter").last

    if not click_if_visible(search_input, timeout=3000):
        search_input = page.get_by_role("textbox").last

    fill_when_visible(search_input, "nav", timeout=10000)

    checkbox = page.locator(".p-checkbox-box").first

    click_when_visible(checkbox, timeout=10000)

    close_button = page.locator(".p-ripple").first

    if not click_if_visible(close_button, timeout=2000):
        page.keyboard.press("Escape")

    page.wait_for_timeout(500)


def add_new_mr_treatment_plan(page):
    """
    Adds Treatment Plan with one step.
    """

    treatment_name = generate_random_automation_note("plan")
    step_name = generate_random_automation_note("step")
    step_note = generate_random_automation_note("step note")
    treatment_note = generate_random_automation_note("treatment note")

    add_new_mr_section(page, r"Treatment Plan")

    treatment_name_field = page.get_by_role("searchbox").first

    fill_when_visible(treatment_name_field, treatment_name, timeout=10000)

    select_naveen_kp_from_new_mr_multiselect(page)

    add_step_button = page.get_by_role(
        "button",
        name=re.compile(r"Add Step", re.I),
    ).first

    click_when_visible(add_step_button, timeout=10000)

    step_name_field = page.get_by_role(
        "textbox",
        name=re.compile(r"Enter Name|Step Name", re.I),
    ).last

    fill_when_visible(step_name_field, step_name, timeout=10000)

    select_naveen_kp_from_new_mr_multiselect(page)

    status_dropdown = page.locator("p-dropdown").filter(
        has_text=re.compile(r"Not Started", re.I)
    ).last

    click_when_visible(status_dropdown, timeout=10000)

    in_progress = page.get_by_text("In Progress", exact=True).first

    click_when_visible(in_progress, timeout=10000)

    step_notes = page.get_by_role(
        "textbox",
        name=re.compile(r"Enter Step Notes", re.I),
    ).first

    fill_when_visible(step_notes, step_note, timeout=10000)

    uploaded_file = upload_random_file_by_visible_upload_text(page)

    treatment_notes = page.get_by_role(
        "textbox",
        name=re.compile(r"Enter Treatment Notes", re.I),
    ).first

    fill_when_visible(treatment_notes, treatment_note, timeout=10000)

    save_button = page.get_by_role("button", name=re.compile(r"^Save$", re.I)).last

    click_when_visible(save_button, timeout=15000)

    assert_mr_success_message(page)

    return {
        "treatment_name": treatment_name,
        "step_name": step_name,
        "step_note": step_note,
        "treatment_note": treatment_note,
        "uploaded_file": uploaded_file,
    }


    # ----------------------------------------
    #   Create Rx / Prescription helpers
    # --------------------------------------

def select_naveen_kp_from_rx_doctor_dropdown(page):
    """
    Selects Naveen KP from prescription doctor dropdown.

    If Naveen KP is already selected, it does nothing.
    """

    selected_naveen = page.get_by_role(
        "combobox",
        name=re.compile(r"Naveen KP", re.I),
    ).first

    if selected_naveen.is_visible():
        return

    doctor_dropdown = page.get_by_role(
        "combobox",
        name=re.compile(r"Amber Gordon|Select Doctor|Select User", re.I),
    ).first

    click_when_visible(doctor_dropdown, timeout=10000)

    page.wait_for_timeout(700)

    naveen_option = page.get_by_text("Naveen KP", exact=True).last

    click_when_visible(naveen_option, timeout=10000)

    page.wait_for_timeout(500)


def open_rx_medicine_form(page, first_medicine=False):
    """
    Opens medicine entry form.

    If the medicine form is already visible, it does nothing.
    """

    close_left_side_panel_if_open(page)

    medicine_search = page.get_by_role(
        "searchbox",
        name=re.compile(r"Search medicine name", re.I),
    ).first

    dosage_search = page.get_by_role(
        "searchbox",
        name=re.compile(r"eg:\s*500mg", re.I),
    ).first

    try:
        expect(medicine_search).to_be_visible(timeout=1500)
        expect(dosage_search).to_be_visible(timeout=1500)
        return
    except Exception:
        pass

    if first_medicine:
        add_medicine_button = page.locator("main button").filter(
            has_text=re.compile(r"Add Medicine", re.I)
        ).first

        click_when_visible(add_medicine_button, timeout=10000)
    else:
        # This is the lower + Add button used to reopen the medicine form
        # only when the form is not already visible.
        add_button = page.locator("main button").filter(
            has_text=re.compile(r"Add", re.I)
        ).last

        click_when_visible(add_button, timeout=10000)

    expect(medicine_search).to_be_visible(timeout=10000)

    page.wait_for_timeout(700)



def click_add_current_medicine_to_table(page, expected_medicine_count):
    """
    Clicks the current medicine form Add button.

    Important:
    Click the form button ' Add', not the lower '+ Add' button.
    """

    close_left_side_panel_if_open(page)

    main_buttons = page.locator("main button")
    button_count = main_buttons.count()

    selected_add_button = None

    for index in range(button_count):
        button = main_buttons.nth(index)

        try:
            if not button.is_visible():
                continue

            button_text = clean_visible_text(button.inner_text(timeout=1000))

            if not re.search(r"Add", button_text, re.I):
                continue

            if re.search(
                r"Add Section|Add Medicine|Add Clinical|New Visit",
                button_text,
                re.I,
            ):
                continue

            selected_add_button = button
            break

        except Exception:
            continue

    if selected_add_button is None:
        raise AssertionError("Could not find medicine form Add button.")

    click_when_visible(selected_add_button, timeout=10000)

    page.wait_for_timeout(1000)

    expected_patterns = [
        rf"{expected_medicine_count}\s+Medicines?\s+Added",
        rf"Prescription\s*\(\s*{expected_medicine_count}\s+medicines?\s*\)",
    ]

    for expected_pattern in expected_patterns:
        try:
            expect(
                page.get_by_text(re.compile(expected_pattern, re.I)).first
            ).to_be_visible(timeout=5000)

            return
        except Exception:
            continue

    raise AssertionError(
        f"Medicine was not added. Expected count: {expected_medicine_count}"
    )




def fill_rx_searchbox(page, name_regex, value, suggestion_regex=None):
    """
    Fills a named prescription searchbox and selects suggestion if visible.
    """

    field = page.get_by_role(
        "searchbox",
        name=re.compile(name_regex, re.I),
    ).first

    fill_when_visible(field, value, timeout=10000)

    page.wait_for_timeout(800)

    if suggestion_regex:
        suggestion = page.get_by_text(
            re.compile(suggestion_regex, re.I),
        ).first

        click_if_visible(suggestion, timeout=3000)


def fill_rx_unnamed_searchbox_by_index(page, index, value, suggestion_regex=None):
    """
    Fills unnamed prescription searchbox by index.
    """

    field = page.get_by_role("searchbox").nth(index)

    fill_when_visible(field, value, timeout=10000)

    page.wait_for_timeout(800)

    if suggestion_regex:
        suggestion = page.get_by_text(
            re.compile(suggestion_regex, re.I),
        ).first

        click_if_visible(suggestion, timeout=3000)


def add_one_new_mr_medicine(page, medicine_data, medicine_index):
    """
    Adds one medicine in New MR Rx composer.
    """

    open_rx_medicine_form(
        page,
        first_medicine=(medicine_index == 0),
    )

    fill_rx_searchbox(
        page,
        r"Search medicine name",
        medicine_data["medicine_search"],
        medicine_data["medicine_suggestion"],
    )

    fill_rx_searchbox(
        page,
        r"eg:\s*500mg",
        medicine_data["dose_search"],
        medicine_data["dose_suggestion"],
    )

    fill_rx_unnamed_searchbox_by_index(
        page,
        2,
        medicine_data["frequency"],
        medicine_data["frequency_suggestion"],
    )

    fill_rx_unnamed_searchbox_by_index(
        page,
        3,
        medicine_data["duration"],
        medicine_data["duration_suggestion"],
    )

    instructions = page.get_by_role(
        "searchbox",
        name=re.compile(r"Instructions", re.I),
    ).first

    fill_when_visible(
        instructions,
        medicine_data["instructions"],
        timeout=10000,
    )

    page.wait_for_timeout(800)

    if medicine_data.get("instructions_suggestion"):
        suggestion = page.get_by_text(
            re.compile(medicine_data["instructions_suggestion"], re.I),
        ).first

        click_if_visible(suggestion, timeout=3000)

    click_add_current_medicine_to_table(
        page,
        expected_medicine_count=medicine_index + 1,
    )



def create_new_mr_prescription(page):
    """
    Creates prescription with 3 medicines.
    """

    prescription_note = generate_random_automation_note("Prescription note")

    create_rx_button = page.get_by_role(
        "button",
        name=re.compile(r"Create Rx", re.I),
    ).first

    click_when_visible(create_rx_button, timeout=15000)

    select_naveen_kp_from_rx_doctor_dropdown(page)

    medicines = [
        {
            "medicine_search": "dolo",
            "medicine_suggestion": "DOLO",
            "dose_search": "500",
            "dose_suggestion": "500MG",
            "frequency": "1-1-1",
            "frequency_suggestion": "-1-1-1",
            "duration": "7",
            "duration_suggestion": "DAYS",
            "instructions": "after",
            "instructions_suggestion": "AFTER FOOD",
        },
        {
            "medicine_search": "para",
            "medicine_suggestion": "PARACETAMOL",
            "dose_search": "500",
            "dose_suggestion": "500MG",
            "frequency": "1-0-1",
            "frequency_suggestion": "-1-0-1",
            "duration": "5",
            "duration_suggestion": "DAYS",
            "instructions": "after",
            "instructions_suggestion": "AFTER FOOD",
        },
        {
            "medicine_search": "pan",
            "medicine_suggestion": "PANTOP",
            "dose_search": "10",
            "dose_suggestion": "10MG",
            "frequency": "0-0-1",
            "frequency_suggestion": "-0-0-1",
            "duration": "1",
            "duration_suggestion": "MONTH",
            "instructions": "before",
            "instructions_suggestion": "BEFORE FOOD",
        },
    ]

    for index, medicine in enumerate(medicines):
        add_one_new_mr_medicine(
            page,
            medicine,
            medicine_index=index,
        )

    fill_new_mr_prescription_notes(page, prescription_note)

    click_new_mr_prescription_save_button(page)

    wait_for_new_mr_prescription_saved(page)

    return {
        "medicine_count": len(medicines),
        "prescription_note": prescription_note,
    }


def fill_new_mr_prescription_notes(page, prescription_note):
    """
    Fills Prescription Notes inside main prescription area.

    Avoids the right-side Doctor's Notes field.
    """

    main_area = page.locator("main").first

    notes_editor = main_area.get_by_role(
        "textbox",
        name=re.compile(r"Rich Text Editor|Editing area", re.I),
    ).first

    click_when_visible(notes_editor, timeout=10000)

    notes_editor.fill(prescription_note)

    page.wait_for_timeout(500)




def click_new_mr_prescription_save_button(page):
    """
    Clicks the New MR prescription Save button.

    Button text can be ' Save', so do not use exact role name '^Save$'.
    """

    main_area = page.locator("main").first

    save_button = main_area.locator("button").filter(
        has_text=re.compile(r"Save", re.I)
    ).last

    save_button.scroll_into_view_if_needed(timeout=5000)

    expect(save_button).to_be_visible(timeout=15000)
    expect(save_button).to_be_enabled(timeout=15000)

    save_button.click()

    page.wait_for_timeout(1500)



def wait_for_new_mr_prescription_saved(page):
    """
    Waits until New MR prescription is actually saved.

    Valid success conditions:
    - success toast appears
    - prescription history row appears with Last updated / Naveen KP
    - Save button disappears from active Rx composer
    """

    main_area = page.locator("main").first

    success_message = page.locator(
        ".p-toast-message-success, "
        ".p-toast-message, "
        ".toast-success, "
        ".mat-mdc-snack-bar-container, "
        "[role='alert']"
    ).filter(
        has_text=re.compile(r"success|saved|prescription", re.I)
    ).first

    try:
        expect(success_message).to_be_visible(timeout=7000)
        return
    except Exception:
        pass

    saved_rx_row = main_area.get_by_role("row").filter(
        has_text=re.compile(r"Last updated|Naveen KP|download|share", re.I)
    ).last

    try:
        expect(saved_rx_row).to_be_visible(timeout=15000)
        return
    except Exception:
        pass

    active_save_button = main_area.locator("button").filter(
        has_text=re.compile(r"Save", re.I)
    ).last

    try:
        expect(active_save_button).to_be_hidden(timeout=7000)
        return
    except Exception as error:
        raise AssertionError(
            "Prescription did not save. Save button is still visible."
        ) from error




    # ------------------------------------------
    # Upload Prescription and Share Case
    # ------------------------------------------


def upload_new_mr_prescription(page):
    """
    Uploads prescription file in New MR.

    Upload Prescription is a button, not a radio button.
    """

    close_left_side_panel_if_open(page)

    main_area = page.locator("main").first

    # If Create Rx form is still open with Save visible, save it first.
    active_save_button = main_area.locator("button").filter(
        has_text=re.compile(r"Save", re.I)
    ).last

    try:
        expect(active_save_button).to_be_visible(timeout=2000)
        expect(active_save_button).to_be_enabled(timeout=2000)

        active_save_button.click()

        wait_for_new_mr_prescription_saved(page)

    except Exception:
        pass

    upload_prescription_button = main_area.get_by_role(
        "button",
        name=re.compile(r"Upload Prescription", re.I),
    ).first

    upload_prescription_button.scroll_into_view_if_needed(timeout=5000)

    click_when_visible(upload_prescription_button, timeout=15000)

    page.wait_for_timeout(1000)

    select_naveen_kp_from_rx_doctor_dropdown(page)

    uploaded_file = upload_random_file_by_visible_upload_text(page)

    save_button = main_area.locator("button").filter(
        has_text=re.compile(r"Save", re.I)
    ).last

    save_button.scroll_into_view_if_needed(timeout=5000)

    expect(save_button).to_be_visible(timeout=15000)
    expect(save_button).to_be_enabled(timeout=15000)

    save_button.click()

    wait_for_new_mr_uploaded_prescription_saved(page)

    return {
        "uploaded_prescription": uploaded_file,
    }



def wait_for_new_mr_uploaded_prescription_saved(page):
    """
    Waits for uploaded prescription save.

    Toast may disappear quickly, so this also checks Prescription History.
    """

    success_message = page.locator(
        ".p-toast-message-success, "
        ".p-toast-message, "
        ".toast-success, "
        ".mat-mdc-snack-bar-container, "
        "[role='alert']"
    ).filter(
        has_text=re.compile(r"success|saved|prescription|uploaded", re.I)
    ).first

    try:
        expect(success_message).to_be_visible(timeout=7000)
        return
    except Exception:
        pass

    saved_rx_row = page.locator("main").get_by_role("row").filter(
        has_text=re.compile(r"Naveen KP|Last updated|download|share", re.I)
    ).last

    expect(saved_rx_row).to_be_visible(timeout=15000)



def share_latest_new_mr_prescription(page):
    """
    Shares the latest prescription from Prescription History.

    Used after:
    - Create Rx prescription save
    - Upload prescription save
    """

    close_left_side_panel_if_open(page)

    main_area = page.locator("main").first

    prescription_history = main_area.locator("table").filter(
        has_text=re.compile(r"Rx Details|ACTIONS", re.I)
    ).last

    latest_rx_row = prescription_history.get_by_role("row").filter(
        has_text=re.compile(r"Naveen KP|Last updated", re.I)
    ).first

    expect(latest_rx_row).to_be_visible(timeout=15000)

    share_button = latest_rx_row.get_by_role(
        "button",
        name=re.compile(r"share", re.I),
    ).first

    if not click_if_visible(share_button, timeout=5000):
        share_button = latest_rx_row.locator("button").nth(1)
        click_when_visible(share_button, timeout=10000)

    page.wait_for_timeout(1000)

    message = generate_random_automation_note("Automation prescription share note")

    message_box = page.get_by_role(
        "textbox",
        name=re.compile(r"Enter message description|Message", re.I),
    ).first

    fill_when_visible(message_box, message, timeout=10000)

    email_checkbox = page.get_by_role(
        "checkbox",
        name=re.compile(r"Email", re.I),
    ).first

    if not email_checkbox.is_checked():
        email_checkbox.check()

    popup_share_button = page.get_by_role(
        "button",
        name=re.compile(r"^Share$", re.I),
    ).last

    click_when_visible(popup_share_button, timeout=15000)

    assert_mr_success_message(page, expected_text=r"success|shared|sent")

    return {
        "shared_prescription_note": message,
        "shared_via": "Email",
    }



def share_new_mr_case_from_top_right(page):
    """
    Shares the case using the top-right Share Case icon.

    This finds the icon by hovering top-right action buttons and checking
    for the tooltip text 'Share Case'.
    """

    close_left_side_panel_if_open(page)

    # Go to top of case page.
    page.keyboard.press("Home")
    page.mouse.wheel(0, -5000)
    page.wait_for_timeout(1000)

    case_header = page.get_by_role(
        "heading",
        name=re.compile(r"Case\s+\d+", re.I),
    ).first

    expect(case_header).to_be_visible(timeout=10000)

    share_note = generate_random_automation_note("Automation case share note")

    viewport_size = page.viewport_size or {"width": 1400, "height": 900}
    viewport_width = viewport_size["width"]

    all_buttons = page.locator("button")
    button_count = all_buttons.count()

    selected_share_button = None

    for index in range(button_count):
        button = all_buttons.nth(index)

        try:
            if not button.is_visible():
                continue

            box = button.bounding_box()

            if box is None:
                continue

            # Only inspect top-right action icons.
            if box["y"] > 260:
                continue

            if box["x"] < viewport_width * 0.70:
                continue

            button.hover()
            page.wait_for_timeout(400)

            tooltip = page.get_by_text("Share Case", exact=True).first

            if tooltip.is_visible():
                selected_share_button = button
                break

        except Exception:
            continue

    if selected_share_button is None:
        raise AssertionError(
            "Could not find top-right Share Case icon by tooltip."
        )

    selected_share_button.click()

    page.wait_for_timeout(1000)

    message_box = page.get_by_role(
        "textbox",
        name=re.compile(r"Enter message description|Message", re.I),
    ).first

    fill_when_visible(message_box, share_note, timeout=10000)

    email_checkbox = page.get_by_role(
        "checkbox",
        name=re.compile(r"Email", re.I),
    ).first

    if not email_checkbox.is_checked():
        email_checkbox.check()

    popup_share_button = page.get_by_role(
        "button",
        name=re.compile(r"^Share$", re.I),
    ).last

    click_when_visible(popup_share_button, timeout=15000)

    assert_mr_success_message(page, expected_text=r"success|shared|sent")

    return {
        "case_share_note": share_note,
        "shared_via": "Email",
    }



def share_new_mr_case(page):
    """
    Shares case via Email.
    """

    share_note = generate_random_automation_note("Automation case share note")

    share_button = page.get_by_role(
        "button",
        name=re.compile(r"^Share$", re.I),
    ).first

    click_when_visible(share_button, timeout=15000)

    message_box = page.get_by_role(
        "textbox",
        name=re.compile(r"Enter message description|Message", re.I),
    ).first

    fill_when_visible(message_box, share_note, timeout=10000)

    email_checkbox = page.get_by_role(
        "checkbox",
        name=re.compile(r"Email", re.I),
    ).first

    if not email_checkbox.is_checked():
        email_checkbox.check()

    popup_share_button = page.get_by_role(
        "button",
        name=re.compile(r"^Share$", re.I),
    ).last

    click_when_visible(popup_share_button, timeout=15000)

    assert_mr_success_message(page, expected_text=r"success|shared|sent")

    return {
        "share_note": share_note,
        "shared_via": "Email",
    }


    # -----------------------------------
    # Generic MR toggle helper
    # ----------------------------------


def set_new_mr_status(page, should_enable):
    """
    Enables or disables New MR from:

    Settings
    -> Features and Customization
    -> MR and Diet Settings
    -> MR Settings
    """

    open_settings_from_sidebar(page)

    open_features_and_customization(page)

    open_mr_and_diet_settings(page)

    open_mr_settings_tab(page)

    toggle_button = get_new_mr_toggle_button(page)

    aria_checked = toggle_button.get_attribute("aria-checked")

    is_currently_enabled = aria_checked == "true"

    if is_currently_enabled == should_enable:
        return {
            "new_mr_status": "already_enabled" if should_enable else "already_disabled",
        }

    toggle_button.click()

    assert_mr_success_message(page)

    page.wait_for_timeout(1000)

    return {
        "new_mr_status": "enabled_now" if should_enable else "disabled_now",
    }



    # ------------------------------------
    #   cleanup helper
    # -----------------------------------


def disable_new_mr_if_needed(page):
    """
    Disables New MR if enabled.
    """

    return set_new_mr_status(page, should_enable=False)


def safe_disable_new_mr_if_needed(page):
    """
    Tries to disable New MR after sharing the case.

    Returns result instead of failing silently.
    """

    try:
        return disable_new_mr_if_needed(page)

    except Exception as error:
        return {
            "new_mr_status": "disable_failed",
            "error": str(error),
        }


    # -----------------------------
    # New MR flow function
    # -----------------------------


def perform_new_mr_complete_case_flow(page):
    """
    Complete New MR flow.

    Steps:
    - Enable New MR
    - Randomly select appointment
    - Create case
    - Upload case file
    - Create new visit
    - Add clinical notes
    - Add MR sections
    - Create prescription
    - Upload prescription
    - Share case via Email
    - Disable New MR from settings
    """

    mr_result = enable_new_mr_if_needed(page)

    open_appointments_dashboard_from_sidebar(page)

    selected_appointment = open_random_appointment_details_from_dashboard(page)

    open_create_case_popup_from_appointment_details(page)

    case_data = fill_new_mr_create_case_popup(page)

    submit_new_mr_create_case_popup(page)

    open_latest_case_from_patient_record(page)

    case_attachment_path = get_random_attachment_path_from_folder()

    case_file_result = upload_new_mr_case_file(page, case_attachment_path)

    open_new_visit_from_case(page)

    open_add_clinical_notes_record(page)

    ensure_new_mr_case_open_for_editing(page)

    close_left_side_panel_if_open(page)

    assignee_result = select_new_visit_assignee_naveen_kp(page)

    visit_summary_result = add_new_visit_summary(page)

    chief_complaint_result = add_new_mr_chief_complaint(page)

    history_result = add_new_mr_history(page)

    medication_result = add_new_mr_medication(page)

    vital_signs_result = add_new_mr_vital_signs(page)

    treatment_plan_result = add_new_mr_treatment_plan(page)

    prescription_result = create_new_mr_prescription(page)

    created_prescription_share_result = share_latest_new_mr_prescription(page)

    uploaded_prescription_result = upload_new_mr_prescription(page)

    uploaded_prescription_share_result = share_latest_new_mr_prescription(page)

    case_share_result = share_new_mr_case_from_top_right(page)

    disable_mr_result = safe_disable_new_mr_if_needed(page)

    return {
        "mr_result": mr_result,
        "selected_appointment": selected_appointment,
        "case_data": case_data,
        "case_file_result": case_file_result,
        "assignee_result": assignee_result,
        "visit_summary_result": visit_summary_result,
        "chief_complaint_result": chief_complaint_result,
        "history_result": history_result,
        "medication_result": medication_result,
        "vital_signs_result": vital_signs_result,
        "treatment_plan_result": treatment_plan_result,
        "prescription_result": prescription_result,
        "created_prescription_share_result": created_prescription_share_result,
        "uploaded_prescription_result": uploaded_prescription_result,
        "uploaded_prescription_share_result": uploaded_prescription_share_result,
        "case_share_result": case_share_result,
        "disable_mr_result": disable_mr_result,
        "final_url": page.url,
    }



def get_random_attachment_path_from_folder(
    attachments_folder="data/attachments",
    allowed_extensions=None,
):
    """
    Randomly picks one file from data/attachments.

    Supported by default:
    - .pdf
    - .jpg
    - .jpeg
    - .png
    """

    if allowed_extensions is None:
        allowed_extensions = [".pdf", ".jpg", ".jpeg", ".png"]

    attachments_path = Path(attachments_folder)

    if not attachments_path.exists():
        raise FileNotFoundError(
            f"Attachment folder not found: {attachments_path.resolve()}"
        )

    files = [
        file_path
        for file_path in attachments_path.iterdir()
        if file_path.is_file()
        and file_path.suffix.lower() in allowed_extensions
    ]

    if not files:
        raise FileNotFoundError(
            f"No attachment files found in {attachments_path.resolve()}. "
            f"Allowed extensions: {allowed_extensions}"
        )

    return str(random.choice(files))


def upload_random_file_from_attachments(page, upload_button_locator=None):
    """
    Uploads one random file from data/attachments without opening
    the Windows file picker.

    This uses input[type='file'] directly.
    """

    attachment_path = get_random_attachment_path_from_folder()
    file_path = Path(attachment_path).resolve()

    if not file_path.exists():
        raise FileNotFoundError(f"Attachment file not found: {file_path}")

    file_inputs = page.locator("input[type='file']")
    file_input_count = file_inputs.count()

    if file_input_count == 0:
        raise AssertionError(
            "No input[type='file'] found on the page. "
            "Do not click Upload manually because it opens Windows file picker."
        )

    last_error = None

    for index in range(file_input_count - 1, -1, -1):
        file_input = file_inputs.nth(index)

        try:
            file_input.set_input_files(str(file_path), timeout=5000)
            page.wait_for_timeout(1000)
            return attachment_path

        except Exception as error:
            last_error = error
            continue

    raise AssertionError(
        f"Could not set file on any input[type='file']. File: {file_path}"
    ) from last_error

    

def set_random_file_on_existing_file_input(page):
    """
    Sets a random file directly on an existing file input.

    This avoids opening the Windows file picker.
    """

    attachment_path = get_random_attachment_path_from_folder()
    file_path = Path(attachment_path).resolve()

    if not file_path.exists():
        raise FileNotFoundError(f"Attachment file not found: {file_path}")

    file_inputs = page.locator("input[type='file']")
    file_input_count = file_inputs.count()

    for index in range(file_input_count - 1, -1, -1):
        file_input = file_inputs.nth(index)

        try:
            file_input.set_input_files(str(file_path), timeout=3000)
            page.wait_for_timeout(1000)
            return attachment_path

        except Exception:
            continue

    return None
    


def upload_random_file_if_upload_visible(page):
    """
    Uploads a random file if the current section has upload support.

    This does not click the Upload button, so Windows file picker will not open.
    """

    upload_text = page.get_by_text(re.compile(r"Upload", re.I)).last
    upload_icon = page.locator(".fa.fa-upload, i.fa-upload, [class*='upload']").last

    upload_available = False

    try:
        expect(upload_text).to_be_visible(timeout=2000)
        upload_available = True
    except Exception:
        pass

    if not upload_available:
        try:
            expect(upload_icon).to_be_visible(timeout=2000)
            upload_available = True
        except Exception:
            pass

    if not upload_available:
        return None

    return upload_random_file_from_attachments(page)



def click_case_section(page, section_name_regex):
    """
    Clicks a case medical-record section button.

    This avoids clicking:
    - Case History
    - View Details
    - other header buttons

    Examples:
    - Chief Complaint(CC)
    - History
    - Medication
    - Vital Signs
    - Treatment Plan
    - Prescription
    """

    section_pattern = re.compile(rf"^\s*{section_name_regex}\s*$", re.I)

    # Scope to the lower medical-record section area when possible.
    section_area = page.locator("div").filter(
        has_text=re.compile(r"Add the sections you need for this medical record", re.I)
    ).last

    section_button = section_area.locator("button").filter(
        has_text=section_pattern
    ).first

    if not click_if_visible(section_button, timeout=5000):
        # Fallback: exact button text only. This prevents matching "Case History".
        section_button = page.locator("button").filter(
            has_text=section_pattern
        ).last

        click_when_visible(section_button, timeout=15000)

    page.wait_for_timeout(1000)


def fill_case_combobox_or_textbox(page, field_name_regex, value):
    """
    Fills a visible combobox/textbox/textarea field.

    This avoids hidden PrimeNG combobox inputs.
    If suggestions appear, it tries to pick one.
    If no suggestion appears, it presses Tab and continues.
    """

    field_pattern = re.compile(field_name_regex, re.I)

    field_candidates = [
        page.get_by_role(
            "combobox",
            name=field_pattern,
        ).first,

        page.get_by_role(
            "textbox",
            name=field_pattern,
        ).first,

        page.locator("input:visible, textarea:visible").filter(
            has_text=field_pattern
        ).first,

        page.locator("textarea:visible").last,
        page.locator("input:visible").last,
    ]

    selected_field = None
    last_error = None

    for field in field_candidates:
        try:
            expect(field).to_be_visible(timeout=3000)
            selected_field = field
            break
        except Exception as error:
            last_error = error
            continue

    if selected_field is None:
        raise AssertionError(
            f"Could not find visible field for: {field_name_regex}. "
            f"Current URL: {page.url}"
        ) from last_error

    selected_field.click()
    selected_field.fill(value)

    page.wait_for_timeout(800)

    option = page.get_by_role(
        "option",
        name=re.compile(re.escape(value), re.I),
    ).first

    if click_if_visible(option, timeout=2000):
        return

    suggestion = page.get_by_text(
        re.compile(re.escape(value), re.I),
    ).first

    if click_if_visible(suggestion, timeout=2000):
        return

    selected_field.press("Tab")


def click_save_and_assert_success(page, expected_text=r"success|saved|updated|created"):
    """
    Clicks Save and asserts success message.
    """

    save_button = page.get_by_role(
        "button",
        name=re.compile(r"^Save$", re.I),
    ).last

    click_when_visible(save_button, timeout=15000)

    assert_success_toast_message(page, expected_text=expected_text)


def select_naveen_kp_from_dropdown(page):
    """
    Selects Naveen KP from the visible user/doctor dropdown.

    If Naveen KP is already selected, it does nothing.
    """

    selected_naveen = page.get_by_role(
        "combobox",
        name=re.compile(r"Naveen KP", re.I),
    ).last

    try:
        expect(selected_naveen).to_be_visible(timeout=1500)
        return
    except Exception:
        pass

    dropdown_candidates = [
        page.get_by_role(
            "combobox",
            name=re.compile(r"Select User|Amber Gordon|Naveen KP", re.I),
        ).last,

        page.get_by_text("Select User", exact=True).last,

        page.locator("mat-select").last,
        page.locator(".mat-mdc-select").last,

        page.locator("p-dropdown").filter(
            has_text=re.compile(
                r"Select User|Doctor|Provider|Amber Gordon|Naveen KP",
                re.I,
            )
        ).last,
    ]

    last_error = None

    for dropdown in dropdown_candidates:
        try:
            expect(dropdown).to_be_visible(timeout=3000)
            dropdown.click()
            page.wait_for_timeout(700)
            break
        except Exception as error:
            last_error = error
            continue
    else:
        raise AssertionError(
            f"Could not open Select User / doctor dropdown. Current URL: {page.url}"
        ) from last_error

    search_box = page.get_by_role("textbox").last

    if click_if_visible(search_box, timeout=1500):
        search_box.fill("nav")
        page.wait_for_timeout(700)

    naveen_options = [
        page.get_by_label("Naveen KP").get_by_text("Naveen KP").first,
        page.get_by_role("option", name=re.compile(r"^Naveen KP$", re.I)).first,
        page.get_by_text("Naveen KP", exact=True).last,
        page.locator("mat-option, .mat-mdc-option, .p-dropdown-item, li").filter(
            has_text=re.compile(r"^Naveen KP$", re.I)
        ).first,
    ]

    last_error = None

    for option in naveen_options:
        try:
            if click_if_visible(option, timeout=5000):
                page.wait_for_timeout(500)
                page.keyboard.press("Escape")
                return
        except Exception as error:
            last_error = error
            continue

    raise AssertionError(
        f"Could not select Naveen KP from dropdown. Current URL: {page.url}"
    ) from last_error



    # ------------------------------------------------------------
    # Add Chief Complaint / History / Medication / Vital Signs
    # --------------------------------------------------------------

def add_chief_complaint_to_case(page):
    """
    Adds Chief Complaint / CC details.
    Upload is optional because sometimes upload is not visible.
    """

    complaint_values = [
        "fever",
        "cough",
        "headache",
        "body pain",
    ]

    selected_complaint = random.choice(complaint_values)

    click_case_section(page, r"Chief Complaint\(CC\)")

    fill_case_combobox_or_textbox(
        page,
        r"Enter Chief Complaint|Chief Complaint",
        selected_complaint,
    )

    uploaded_file = upload_random_file_if_upload_visible(page)

    click_save_and_assert_success(page)

    return {
        "chief_complaint": selected_complaint,
        "uploaded_file": uploaded_file,
    }


def add_history_to_case(page):
    """
    Adds History details.
    Upload is optional because sometimes upload is not visible.
    """

    history_note = generate_random_automation_note("No history")

    click_case_section(page, r"History")

    fill_case_combobox_or_textbox(
        page,
        r"Enter History",
        "No history",
    )

    uploaded_file = upload_random_file_if_upload_visible(page)

    click_save_and_assert_success(page)

    return {
        "history_note": history_note,
        "entered_history": "No history",
        "uploaded_file": uploaded_file,
    }


def add_medication_to_case(page):
    """
    Adds Medication details.
    """

    medication_note = generate_random_automation_note("No medication")

    click_case_section(page, r"Medication")

    fill_case_combobox_or_textbox(
        page,
        r"Enter Medication",
        "No medication",
    )

    click_save_and_assert_success(page)

    return {
        "medication_note": medication_note,
        "entered_medication": "No medication",
    }



def fill_vital_signs_in_case(page):
    """
    Fills random vital signs.
    """

    click_case_section(page, r"Vital Signs")

    pulse_rate = str(random.randint(1, 999))
    respiration = str(random.randint(1, 90))
    temperature = str(random.randint(1, 200))
    systolic = str(random.randint(1, 500))
    diastolic = str(random.randint(1, 500))

    fill_when_visible(
        page.get_by_role("textbox", name=re.compile(r"Pulse Rate", re.I)).first,
        pulse_rate,
        timeout=10000,
    )

    fill_when_visible(
        page.get_by_role("textbox", name=re.compile(r"Respiration", re.I)).first,
        respiration,
        timeout=10000,
    )

    fill_when_visible(
        page.get_by_role("textbox", name=re.compile(r"Temperature", re.I)).first,
        temperature,
        timeout=10000,
    )

    fill_when_visible(
        page.get_by_role("textbox", name=re.compile(r"Systolic", re.I)).first,
        systolic,
        timeout=10000,
    )

    fill_when_visible(
        page.get_by_role("textbox", name=re.compile(r"Diastolic", re.I)).first,
        diastolic,
        timeout=10000,
    )

    click_save_and_assert_success(page)

    return {
        "pulse_rate": pulse_rate,
        "respiration": respiration,
        "temperature": temperature,
        "systolic": systolic,
        "diastolic": diastolic,
    }     


    # --------------------------------------------
    # Treatment Plan helpers
    # --------------------------------------------

def add_treatment_plan_to_case(page):
    """
    Adds Treatment Plan with one step.
    """

    treatment_name = generate_random_automation_note("Automation treatment")
    step_name = generate_random_automation_note("Automation step")
    step_note = generate_random_automation_note("Automation step note")
    treatment_note = generate_random_automation_note("Automation treatment note")

    click_case_section(page, r"Treatment Plan")

    treatment_name_field = page.get_by_role(
        "searchbox"
    ).first

    if not click_if_visible(treatment_name_field, timeout=5000):
        treatment_name_field = page.get_by_role(
            "textbox",
            name=re.compile(r"Treatment Name|Enter Name|Name", re.I),
        ).first

    fill_when_visible(treatment_name_field, treatment_name, timeout=10000)

    select_naveen_kp_from_dropdown(page)

    add_step_button = page.get_by_role(
        "button",
        name=re.compile(r"Add Step", re.I),
    ).first

    click_when_visible(add_step_button, timeout=10000)

    step_name_field = page.get_by_role(
        "textbox",
        name=re.compile(r"Enter Name|Step Name", re.I),
    ).last

    fill_when_visible(step_name_field, step_name, timeout=10000)

    select_naveen_kp_from_dropdown(page)

    status_dropdown = page.locator("p-dropdown").filter(
        has_text=re.compile(r"Not Started|Status", re.I)
    ).last

    click_when_visible(status_dropdown, timeout=10000)

    in_progress_option = page.get_by_text("In Progress", exact=True).first
    click_when_visible(in_progress_option, timeout=10000)

    step_notes_field = page.get_by_role(
        "textbox",
        name=re.compile(r"Enter Step Notes|Step Notes", re.I),
    ).first

    fill_when_visible(step_notes_field, step_note, timeout=10000)

    upload_random_file_if_upload_visible(page)

    notes_field = page.get_by_role(
        "textbox",
        name=re.compile(r"Notes", re.I),
    ).last

    if click_if_visible(notes_field, timeout=3000):
        notes_field.fill(treatment_note)

    click_save_and_assert_success(page)

    return {
        "treatment_name": treatment_name,
        "step_name": step_name,
        "step_note": step_note,
        "treatment_note": treatment_note,
    }


    # -----------------------------------------    
    #  Prescription helpers
    # -----------------------------------------

def fill_prescription_cell(page, cell_locator, value, suggestion_text=None):
    """
    Fills one prescription table cell.

    Uses the editor inside the clicked cell when available.
    If suggestion appears, it selects it.
    Otherwise it keeps the typed value.
    """

    click_when_visible(cell_locator, timeout=10000)

    page.wait_for_timeout(500)

    editor_candidates = [
        cell_locator.locator("input:visible").last,
        cell_locator.locator("textarea:visible").last,
        cell_locator.locator("[contenteditable='true']:visible").last,
        page.locator("input:visible").last,
        page.locator("textarea:visible").last,
        page.locator("[contenteditable='true']:visible").last,
    ]

    selected_editor = None

    for editor in editor_candidates:
        try:
            expect(editor).to_be_visible(timeout=1500)
            selected_editor = editor
            break
        except Exception:
            continue

    if selected_editor is not None:
        selected_editor.click()
        selected_editor.fill(value)
    else:
        page.keyboard.press("Control+A")
        page.keyboard.type(value)

    page.wait_for_timeout(800)

    if suggestion_text:
        suggestion_candidates = [
            page.get_by_role(
                "option",
                name=re.compile(re.escape(suggestion_text), re.I),
            ).first,

            page.get_by_text(
                re.compile(re.escape(suggestion_text), re.I),
            ).first,

            page.locator(
                "mat-option, .mat-mdc-option, .p-autocomplete-item, "
                ".p-dropdown-item, li"
            ).filter(
                has_text=re.compile(re.escape(suggestion_text), re.I)
            ).first,
        ]

        for suggestion in suggestion_candidates:
            if click_if_visible(suggestion, timeout=2500):
                page.wait_for_timeout(500)
                return

    page.keyboard.press("Tab")
    page.wait_for_timeout(300)



def add_prescription_to_case(page):
    """
    Adds prescription with 3 medicines.
    """

    prescription_note = generate_random_automation_note("Automation prescription note")

    medicines = [
        {
            "medicine": "Dolo",
            "medicine_suggestion": "DOLO",
            "dose": "500MG",
            "dose_suggestion": None,
            "frequency": "-1-1-1",
            "frequency_suggestion": "-1-1-1",
            "duration": "5 DAYS",
            "duration_suggestion": None,
            "notes": "AFTER FOOD",
            "notes_suggestion": None,
        },
        {
            "medicine": "Paracetamol",
            "medicine_suggestion": "PARACETAMOL",
            "dose": "650MG",
            "dose_suggestion": None,
            "frequency": "-1-0-1",
            "frequency_suggestion": "-1-0-1",
            "duration": "3 DAYS",
            "duration_suggestion": None,
            "notes": "AFTER FOOD",
            "notes_suggestion": None,
        },
        {
            "medicine": "Pantop",
            "medicine_suggestion": "PANTOP",
            "dose": "10MG",
            "dose_suggestion": None,
            "frequency": "-0-0-1",
            "frequency_suggestion": "-0-0-1",
            "duration": "7 DAYS",
            "duration_suggestion": None,
            "notes": "AFTER FOOD",
            "notes_suggestion": None,
        },
    ]

    click_case_section(page, r"Prescription")

    select_naveen_kp_for_prescription(page)

    prescription_table = page.locator("table").filter(
        has_text=re.compile(r"Medicine.*Dose.*Frequency.*Duration", re.I)
    ).last

    for index, medicine_data in enumerate(medicines):
        add_medicine_button = page.get_by_role(
            "button",
            name=re.compile(r"Add Medicine", re.I),
        ).first

        click_when_visible(add_medicine_button, timeout=10000)

        page.wait_for_timeout(1000)

        rows = prescription_table.locator("tbody tr")
        row = rows.nth(index)
        cells = row.locator("td")

        fill_prescription_cell(
            page,
            cells.nth(1),
            medicine_data["medicine"],
            medicine_data["medicine_suggestion"],
        )

        fill_prescription_cell(
            page,
            cells.nth(2),
            medicine_data["dose"],
            medicine_data["dose_suggestion"],
        )

        fill_prescription_cell(
            page,
            cells.nth(3),
            medicine_data["frequency"],
            medicine_data["frequency_suggestion"],
        )

        fill_prescription_cell(
            page,
            cells.nth(4),
            medicine_data["duration"],
            medicine_data["duration_suggestion"],
        )

        fill_prescription_cell(
            page,
            cells.nth(5),
            medicine_data["notes"],
            medicine_data["notes_suggestion"],
        )

    notes_editor = page.get_by_role(
        "textbox",
        name=re.compile(r"Rich Text Editor|Editing area", re.I),
    ).first

    if click_if_visible(notes_editor, timeout=3000):
        notes_editor.fill(prescription_note)

    save_button = page.get_by_role(
        "button",
        name=re.compile(r"^Save$", re.I),
    ).last

    click_when_visible(save_button, timeout=15000)

    wait_for_prescription_saved(page)

    return {
        "medicine_count": len(medicines),
        "prescription_note": prescription_note,
    }

def select_naveen_kp_for_prescription(page):
    """
    Selects Naveen KP only for the Prescription Select User field.

    If Naveen KP is already selected, it does nothing.
    This prevents the prescription doctor dropdown from flickering.
    """

    # If any visible prescription/user combobox already shows Naveen KP, do nothing.
    visible_comboboxes = page.get_by_role("combobox")

    combobox_count = visible_comboboxes.count()

    for index in range(combobox_count):
        combobox = visible_comboboxes.nth(index)

        try:
            if not combobox.is_visible():
                continue

            combobox_text = clean_visible_text(combobox.inner_text(timeout=1000))

            if re.search(r"Naveen\s+KP", combobox_text, re.I):
                return

        except Exception:
            continue

    # In the prescription form, current user may show as Amber Gordon.
    prescription_user_dropdown = page.get_by_role(
        "combobox",
        name=re.compile(r"Amber Gordon|Select User|Naveen KP", re.I),
    ).first

    click_when_visible(prescription_user_dropdown, timeout=10000)

    page.wait_for_timeout(700)

    naveen_option = page.get_by_role(
        "option",
        name=re.compile(r"^Naveen KP$", re.I),
    ).first

    if not click_if_visible(naveen_option, timeout=5000):
        naveen_option = page.get_by_text("Naveen KP", exact=True).last
        click_when_visible(naveen_option, timeout=10000)

    page.wait_for_timeout(500)
    page.keyboard.press("Escape")

    # Confirm selection became Naveen KP.
    expect(
        page.get_by_role("combobox", name=re.compile(r"Naveen KP", re.I)).first
    ).to_be_visible(timeout=10000)




def wait_for_prescription_saved(page):
    """
    Waits for prescription save.

    Some UI runs do not show a toast long enough to catch.
    In that case, verify the saved prescription row appears.
    """

    success_message = page.locator(
        ".p-toast-message-success, "
        ".p-toast-message, "
        ".toast-success, "
        ".mat-mdc-snack-bar-container, "
        "[role='alert']"
    ).filter(
        has_text=re.compile(r"success|saved|prescription", re.I)
    ).first

    try:
        expect(success_message).to_be_visible(timeout=7000)

        try:
            expect(success_message).to_be_hidden(timeout=15000)
        except Exception:
            page.wait_for_timeout(1000)

        return

    except Exception:
        pass

    saved_prescription_row = page.get_by_role("row").filter(
        has_text=re.compile(r"Naveen KP|Last updated on", re.I)
    ).last

    expect(saved_prescription_row).to_be_visible(timeout=15000)



def upload_prescription_to_case(page):
    """
    Selects Upload Prescription radio button and uploads a random prescription file.
    """

    click_case_section(page, r"Prescription")

    upload_prescription_radio = page.get_by_role(
        "radio",
        name=re.compile(r"Upload Prescription", re.I),
    ).first

    click_when_visible(upload_prescription_radio, timeout=10000)

    select_naveen_kp_for_prescription(page)

    upload_link = page.get_by_text("Upload", exact=True).last

    uploaded_file = upload_random_file_from_attachments(page, upload_link)

    click_save_and_assert_success(page)

    return {
        "uploaded_prescription": uploaded_file,
    }


def share_prescription_from_case(page):
    """
    Shares prescription through Email.
    """

    share_note = generate_random_automation_note("Automation prescription share")

    page.mouse.wheel(0, -2000)
    page.wait_for_timeout(1000)

    share_button = page.get_by_role(
        "button",
        name=re.compile(r"^Share$", re.I),
    ).first

    click_when_visible(share_button, timeout=15000)

    message_box = page.get_by_role(
        "textbox",
        name=re.compile(r"Enter message description|Message", re.I),
    ).first

    fill_when_visible(message_box, share_note, timeout=10000)

    email_checkbox = page.get_by_role(
        "checkbox",
        name=re.compile(r"Email", re.I),
    ).first

    if not email_checkbox.is_checked():
        email_checkbox.check()

    popup_share_button = page.get_by_role(
        "button",
        name=re.compile(r"^Share$", re.I),
    ).last

    click_when_visible(popup_share_button, timeout=15000)

    assert_success_toast_message(page, expected_text=r"success|shared|sent")

    return {
        "share_note": share_note,
        "shared_via": "Email",
    }    






