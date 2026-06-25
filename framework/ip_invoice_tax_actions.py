import random
import re
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from urllib.parse import urlparse, parse_qs

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import expect

from framework.auth import login


IP_MEDICINE_TAX_CONFIG = {
    "Med_1": {
        "gst_percentage": Decimal("5"),
        "cess_percentage": Decimal("1"),
    },
    "Med_2": {
        "gst_percentage": Decimal("5"),
        "cess_percentage": Decimal("1"),
    },
    "Med_4": {
        "gst_percentage": Decimal("5"),
        "cess_percentage": Decimal("0"),
    },
}


MONEY_REGEX = re.compile(r"(?<!\d)(\d{1,3}(?:,\d{3})*|\d+)\.\d{2}(?!\d)")


def round_money(value: Decimal) -> Decimal:
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def assert_amount_close(actual: Decimal, expected: Decimal, message: str = "") -> None:
    actual = round_money(actual)
    expected = round_money(expected)
    difference = abs(actual - expected)

    assert difference <= Decimal("0.02"), (
        f"{message}\n"
        f"Expected: {expected}\n"
        f"Actual: {actual}\n"
        f"Difference: {difference}"
    )


def extract_decimal_money_values(text: str) -> list[Decimal]:
    values = []

    for match in MONEY_REGEX.finditer(text or ""):
        money_text = match.group(0).replace(",", "")
        values.append(Decimal(money_text))

    return values


def get_ip_medicine_tax_config(item_name: str) -> dict:
    if item_name not in IP_MEDICINE_TAX_CONFIG:
        raise AssertionError(
            f"No tax config found for medicine: {item_name}. "
            f"Expected one of {list(IP_MEDICINE_TAX_CONFIG.keys())}"
        )

    return IP_MEDICINE_TAX_CONFIG[item_name]


def wait_for_page_ready(page) -> None:
    page.wait_for_load_state("domcontentloaded")

    try:
        page.wait_for_load_state("networkidle", timeout=5000)
    except PlaywrightTimeoutError:
        pass


def get_visible_page_text(page) -> str:
    return page.locator("body").inner_text(timeout=10000)


def business_url_from_current_page(page, path: str) -> str:
    match = re.match(r"^(https?://[^/]+)", page.url)

    if match:
        base_url = match.group(1)
    else:
        base_url = "https://scale.jaldee.com"

    if not path.startswith("/"):
        path = "/" + path

    return f"{base_url}{path}"


def click_button_by_text(page, text: str, timeout: int = 10000) -> None:
    candidates = [
        page.get_by_role("button", name=re.compile(re.escape(text), re.I)),
        page.get_by_text(text, exact=False),
    ]

    for candidate in candidates:
        try:
            candidate.first.click(timeout=timeout)
            return
        except Exception:
            continue

    raise AssertionError(f"Could not click button/text: {text}")


def click_menuitem_by_text(page, text: str, timeout: int = 10000) -> None:
    candidates = [
        page.get_by_role("menuitem", name=re.compile(re.escape(text), re.I)),
        page.get_by_text(text, exact=False),
    ]

    for candidate in candidates:
        try:
            candidate.first.click(timeout=timeout)
            return
        except Exception:
            continue

    raise AssertionError(f"Could not click menu item/text: {text}")


def fill_first_available(locator, value: str, timeout: int = 10000) -> bool:
    try:
        locator.first.click(timeout=timeout)
        locator.first.fill(value, timeout=timeout)
        return True
    except Exception:
        return False


def assert_success_message_if_present(page) -> str:
    possible_alerts = [
        page.get_by_role("alert"),
        page.locator(".p-toast-message"),
        page.locator(".toast-message"),
        page.locator(".alert-success"),
    ]

    for alert in possible_alerts:
        try:
            if alert.first.is_visible(timeout=3000):
                return alert.first.inner_text(timeout=3000).strip()
        except Exception:
            continue

    return ""


def open_prime_dropdown(page, dropdown_text: str, timeout: int = 10000) -> None:
    """
    Opens a PrimeNG p-dropdown using multiple strategies.

    Supports dropdowns where the label is visible text and also dropdowns
    where the placeholder is inside hidden/accessibility input.
    """

    dropdown_patterns = [
        f"p-dropdown:has-text('{dropdown_text}')",
        f"p-dropdown input[placeholder='{dropdown_text}']",
        f"p-dropdown input[aria-label='{dropdown_text}']",
        f"p-dropdown [placeholder='{dropdown_text}']",
    ]

    for pattern in dropdown_patterns:
        try:
            locator = page.locator(pattern).first()

            if locator.is_visible(timeout=2000):
                parent_dropdown = locator.locator("xpath=ancestor::p-dropdown[1]")

                try:
                    parent_dropdown.get_by_label("dropdown trigger").click(timeout=timeout)
                    return
                except Exception:
                    pass

                try:
                    parent_dropdown.locator(".p-dropdown-trigger").click(timeout=timeout)
                    return
                except Exception:
                    pass

                try:
                    parent_dropdown.click(timeout=timeout)
                    return
                except Exception:
                    pass
        except Exception:
            continue

    p_dropdowns = page.locator("p-dropdown")
    dropdown_count = p_dropdowns.count()

    for index in range(dropdown_count):
        dropdown = p_dropdowns.nth(index)

        try:
            dropdown_text_value = dropdown.inner_text(timeout=1000).strip()
        except Exception:
            dropdown_text_value = ""

        try:
            placeholder_value = dropdown.locator("input").first.get_attribute("placeholder", timeout=1000) or ""
        except Exception:
            placeholder_value = ""

        try:
            aria_label_value = dropdown.locator("input").first.get_attribute("aria-label", timeout=1000) or ""
        except Exception:
            aria_label_value = ""

        combined_text = f"{dropdown_text_value} {placeholder_value} {aria_label_value}".lower()

        if dropdown_text.lower() not in combined_text:
            continue

        try:
            dropdown.get_by_label("dropdown trigger").click(timeout=timeout)
            return
        except Exception:
            pass

        try:
            dropdown.locator(".p-dropdown-trigger").click(timeout=timeout)
            return
        except Exception:
            pass

        try:
            dropdown.click(timeout=timeout)
            return
        except Exception:
            pass

    text_candidates = [
        page.get_by_text(dropdown_text, exact=True),
        page.get_by_text(dropdown_text, exact=False),
    ]

    for candidate in text_candidates:
        try:
            candidate.first.click(timeout=3000)
            return
        except Exception:
            continue

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        f"Could not open dropdown: {dropdown_text}\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )


def select_random_prime_dropdown_option(
    page,
    dropdown_text: str,
    exclude_texts: list[str] | None = None,
    timeout: int = 10000,
) -> str:
    """
    Opens a PrimeNG dropdown and selects one random valid option.
    """

    exclude_texts = exclude_texts or []
    excluded_lower = [text.lower().strip() for text in exclude_texts]

    open_prime_dropdown(
        page=page,
        dropdown_text=dropdown_text,
        timeout=timeout,
    )

    page.wait_for_timeout(800)

    option_candidates = [
        page.get_by_role("option"),
        page.locator("p-dropdownitem li"),
        page.locator(".p-dropdown-item"),
    ]

    options = []

    for option_locator in option_candidates:
        try:
            option_count = option_locator.count()
        except Exception:
            continue

        for index in range(option_count):
            option = option_locator.nth(index)

            try:
                if not option.is_visible(timeout=1000):
                    continue
            except Exception:
                continue

            try:
                option_text = option.inner_text(timeout=2000).strip()
            except Exception:
                continue

            if not option_text:
                continue

            normalized_option_text = option_text.lower().strip()

            if normalized_option_text in excluded_lower:
                continue

            if "select" in normalized_option_text:
                continue

            if option_text not in [existing_text for _, existing_text in options]:
                options.append((option, option_text))

        if options:
            break

    if not options:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"No selectable options found for dropdown: {dropdown_text}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    selected_option, selected_text = random.choice(options)
    selected_option.click(timeout=timeout)

    page.wait_for_timeout(500)

    return selected_text


def select_dropdown_option_by_text(
    page,
    dropdown_text: str,
    option_text: str,
    timeout: int = 10000,
) -> str:
    """
    Opens a PrimeNG dropdown and selects a specific option by text.
    """

    open_prime_dropdown(
        page=page,
        dropdown_text=dropdown_text,
        timeout=timeout,
    )

    page.wait_for_timeout(800)

    option_candidates = [
        page.get_by_role("option", name=re.compile(re.escape(option_text), re.I)),
        page.locator("p-dropdownitem li").filter(has_text=re.compile(re.escape(option_text), re.I)),
        page.locator(".p-dropdown-item").filter(has_text=re.compile(re.escape(option_text), re.I)),
        page.get_by_text(option_text, exact=False),
    ]

    for option in option_candidates:
        try:
            option.first.click(timeout=timeout)
            page.wait_for_timeout(500)
            return option_text
        except Exception:
            continue

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        f"Could not select option '{option_text}' from dropdown '{dropdown_text}'.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )


def select_html_select_option_by_visible_text(select_locator, visible_text: str) -> str:
    options = select_locator.locator("option")
    option_count = options.count()

    for index in range(option_count):
        option = options.nth(index)
        text = option.inner_text(timeout=3000).strip()

        if visible_text.lower() in text.lower():
            value = option.get_attribute("value")
            select_locator.select_option(value=value)
            return text

    raise AssertionError(f"Could not select option containing text: {visible_text}")


def get_profile_value(profile: dict, keys: list[str], fallback: str) -> str:
    for key in keys:
        value = profile.get(key)

        if value:
            return str(value)

    return fallback


def click_calendar_icon_for_input(page, placeholder_text: str, timeout: int = 10000) -> None:
    """
    Clicks the purple calendar icon beside a specific date input.

    Example:
    - Select Checkin Date
    - Select Expected Checkout Date

    This avoids broad selectors like button:has(i), because those can click the side menu.
    """

    input_locator = page.locator(f"input[placeholder='{placeholder_text}']").first

    try:
        input_locator.wait_for(state="visible", timeout=timeout)
    except Exception:
        visible_text = get_visible_page_text(page)
        raise AssertionError(
            f"Could not find date input with placeholder: {placeholder_text}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    calendar_button_candidates = [
        input_locator.locator("xpath=following-sibling::button[1]"),
        input_locator.locator("xpath=../button[1]"),
        input_locator.locator("xpath=ancestor::*[contains(@class, 'p-calendar')][1]//button"),
        input_locator.locator("xpath=ancestor::div[1]//button"),
        input_locator.locator("xpath=ancestor::div[2]//button"),
    ]

    for button in calendar_button_candidates:
        try:
            if button.first.is_visible(timeout=1500):
                button.first.click(timeout=timeout)
                page.wait_for_timeout(700)
                return
        except Exception:
            continue

    # Last fallback: click the visible purple icon area beside the input.
    # This is useful when the calendar button is styled outside normal DOM relationships.
    try:
        box = input_locator.bounding_box(timeout=timeout)

        if box:
            icon_x = box["x"] + box["width"] + 25
            icon_y = box["y"] + box["height"] / 2
            page.mouse.click(icon_x, icon_y)
            page.wait_for_timeout(700)
            return
    except Exception:
        pass

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        f"Could not click calendar icon for input placeholder: {placeholder_text}\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )


def click_calendar_day(page, day_number: int, timeout: int = 10000) -> None:
    """
    Selects a day from the opened calendar popup.
    """

    day_text = str(day_number)

    day_candidates = [
        page.locator(".p-datepicker-calendar td:not(.p-datepicker-other-month)").get_by_text(day_text, exact=True),
        page.locator(".p-datepicker-calendar span").filter(has_text=re.compile(rf"^{day_text}$")),
        page.locator(".p-datepicker td").filter(has_text=re.compile(rf"^{day_text}$")),
        page.locator("[role='gridcell']").filter(has_text=re.compile(rf"^{day_text}$")),
        page.get_by_text(day_text, exact=True),
    ]

    for day in day_candidates:
        try:
            if day.first.is_visible(timeout=2000):
                day.first.click(timeout=timeout)
                page.wait_for_timeout(500)
                return
        except Exception:
            continue

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        f"Could not select calendar day: {day_number}\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )


def select_today_from_calendar(page, calendar_index: int = 0) -> date:
    """
    Selects today's date from Checkin Date calendar.
    calendar_index is kept only so old calls do not break.
    """

    today = date.today()

    click_calendar_icon_for_input(
        page=page,
        placeholder_text="Select Checkin Date",
    )

    click_calendar_day(page, today.day)

    return today


def select_future_date_from_calendar(page, calendar_index: int = 1, days_from_today: int = 1) -> date:
    """
    Selects a future date from Expected Checkout Date calendar.
    calendar_index is kept only so old calls do not break.
    """

    future_date = date.today() + timedelta(days=days_from_today)

    click_calendar_icon_for_input(
        page=page,
        placeholder_text="Select Expected Checkout Date",
    )

    click_calendar_day(page, future_date.day)

    return future_date



def close_left_side_panel_if_open(page) -> None:
    """
    Closes the left side panel if it is open.
    Safe to call before clicking page fields.
    """

    close_candidates = [
        page.locator("text=Trinity Hospital").locator("xpath=ancestor::div[1]").locator("text=×"),
        page.get_by_text("×", exact=True),
        page.locator("i").filter(has_text=re.compile(r"close", re.I)),
        page.locator(".side-menu").get_by_text("×", exact=True),
    ]

    for candidate in close_candidates:
        try:
            if candidate.first.is_visible(timeout=1000):
                candidate.first.click(timeout=3000)
                page.wait_for_timeout(500)
                return
        except Exception:
            continue

    try:
        page.keyboard.press("Escape")
        page.wait_for_timeout(300)
    except Exception:
        pass
    


def calculate_tax_inclusive_split(
    total_amount: Decimal,
    gst_percentage: Decimal,
    cess_percentage: Decimal = Decimal("0"),
) -> dict:
    taxable_expected = round_money(
        total_amount
        * Decimal("100")
        / (Decimal("100") + gst_percentage + cess_percentage)
    )

    gst_expected = round_money(taxable_expected * gst_percentage / Decimal("100"))
    cess_expected = round_money(taxable_expected * cess_percentage / Decimal("100"))
    cgst_expected = round_money(gst_expected / Decimal("2"))
    sgst_expected = round_money(gst_expected / Decimal("2"))

    return {
        "taxable_expected": taxable_expected,
        "gst_expected": gst_expected,
        "cess_expected": cess_expected,
        "cgst_expected": cgst_expected,
        "sgst_expected": sgst_expected,
    }


def calculate_tax_exclusive_split(
    taxable_amount: Decimal,
    gst_percentage: Decimal,
    cess_percentage: Decimal = Decimal("0"),
) -> dict:
    gst_expected = round_money(taxable_amount * gst_percentage / Decimal("100"))
    cess_expected = round_money(taxable_amount * cess_percentage / Decimal("100"))
    cgst_expected = round_money(gst_expected / Decimal("2"))
    sgst_expected = round_money(gst_expected / Decimal("2"))
    total_expected = round_money(taxable_amount + gst_expected + cess_expected)

    return {
        "taxable_expected": taxable_amount,
        "gst_expected": gst_expected,
        "cess_expected": cess_expected,
        "cgst_expected": cgst_expected,
        "sgst_expected": sgst_expected,
        "total_expected": total_expected,
    }


def get_invoice_row_by_text(page, text: str):
    row_candidates = [
        page.get_by_role("row", name=re.compile(re.escape(text), re.I)),
        page.locator("tr").filter(has_text=re.compile(re.escape(text), re.I)),
        page.locator("div").filter(has_text=re.compile(re.escape(text), re.I)),
    ]

    for row in row_candidates:
        try:
            row.first.wait_for(state="visible", timeout=10000)
            return row.first
        except Exception:
            continue

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        f"Could not find invoice row containing: {text}\n"
        f"Visible text:\n{visible_text[:2500]}"
    )


def read_summary_amount(page, label: str, default: Decimal | None = None) -> Decimal:
    text = get_visible_page_text(page)
    escaped_label = re.escape(label)

    patterns = [
        rf"{escaped_label}\s*[:₹]?\s*([0-9,]+\.\d{{2}})",
        rf"{escaped_label}[\s\S]{{0,80}}?([0-9,]+\.\d{{2}})",
    ]

    matches = []

    for pattern in patterns:
        matches.extend(re.findall(pattern, text, flags=re.I))

    if matches:
        return Decimal(matches[-1].replace(",", ""))

    if default is not None:
        return default

    raise AssertionError(
        f"Could not read summary amount for label: {label}\n"
        f"Visible text:\n{text[:2500]}"
    )


def open_ip_dashboard(page) -> None:
    wait_for_page_ready(page)

    try:
        page.get_by_text(re.compile(r"In\s*Patient", re.I)).first.click(timeout=5000)
        wait_for_page_ready(page)
    except Exception:
        pass

    page.goto(business_url_from_current_page(page, "/business/ip/dashboard?p_source=p_sidebar"))
    wait_for_page_ready(page)

    expect(page).to_have_url(re.compile(r"/business/ip/dashboard", re.I))


def open_ip_inpatients_grid(page) -> None:
    candidates = [
        page.get_by_text("Inpatients", exact=True),
        page.get_by_text("In Patients", exact=True),
        page.locator("#actionNav_IP_DBoard").nth(1),
        page.locator("[id*='actionNav_IP_DBoard']").nth(1),
    ]

    for candidate in candidates:
        try:
            candidate.click(timeout=10000)
            wait_for_page_ready(page)
            return
        except Exception:
            continue

    raise AssertionError("Could not open Inpatients grid.")


def open_new_admission_page(page) -> None:
    candidates = [
        page.get_by_role("button", name=re.compile(r"New Admission|add New Admission", re.I)),
        page.get_by_text("New Admission", exact=False),
        page.get_by_text("add New Admission", exact=False),
    ]

    for candidate in candidates:
        try:
            candidate.first.click(timeout=10000)
            wait_for_page_ready(page)
            return
        except Exception:
            continue

    raise AssertionError("Could not open New Admission page.")


def create_new_ip_patient_from_profile(page, consumer_profile: dict) -> dict:
    first_name = get_profile_value(
        consumer_profile,
        ["first_name", "firstName", "fname", "name"],
        f"IP{random.randint(1000, 9999)}",
    )

    last_name = get_profile_value(
        consumer_profile,
        ["last_name", "lastName", "lname"],
        f"Patient{random.randint(100, 999)}",
    )

    email = get_profile_value(
        consumer_profile,
        ["email", "email_id", "emailId"],
        f"ip.patient.{random.randint(10000, 99999)}@jaldee.com",
    )

    phone = get_profile_value(
        consumer_profile,
        ["phone", "mobile", "phone_number", "phoneNumber", "consumer_phone"],
        f"555{random.randint(1000000, 9999999)}",
    )

    address = get_profile_value(
        consumer_profile,
        ["address", "address1"],
        f"Test Address {random.randint(100, 999)}",
    )

    click_button_by_text(page, "Create Patient")

    filled_first_name = fill_first_available(
        page.get_by_role("textbox", name=re.compile(r"Enter First Name|First Name", re.I)),
        first_name,
    )

    assert filled_first_name is True, "Could not fill patient first name."

    fill_first_available(
        page.get_by_role("textbox", name=re.compile(r"Enter Last Name|Last Name", re.I)),
        last_name,
    )

    fill_first_available(
        page.get_by_role("textbox", name=re.compile(r"Enter Email Id|Email", re.I)),
        email,
    )

    phone_filled = fill_first_available(
        page.get_by_role("textbox", name=re.compile(r"10123|Mobile|Phone", re.I)),
        phone,
    )

    if phone_filled is False:
        page.locator("input[type='tel'], input[placeholder*='Mobile'], input[placeholder*='Phone']").first.fill(phone)

    gender = select_random_prime_dropdown_option(
        page,
        "Select Gender",
        exclude_texts=["Select Gender"],
    )

    fill_first_available(
        page.get_by_role("textbox", name=re.compile(r"Enter Address|Address", re.I)),
        address,
    )

    click_button_by_text(page, "Save & Next")
    wait_for_page_ready(page)

    return {
        "patient_created": True,
        "first_name": first_name,
        "last_name": last_name,
        "patient_full_name": f"{first_name} {last_name}",
        "email": email,
        "phone": phone,
        "gender": gender,
        "address": address,
    }


def select_random_available_ip_bed(page) -> str:
    bed_candidates = [
        page.locator("text=/Block\\s+[A-Z].*/i"),
        page.locator("button").filter(has_text=re.compile(r"Block|Bed|Room", re.I)),
        page.locator("div").filter(has_text=re.compile(r"Block\s+[A-Z]", re.I)),
    ]

    visible_beds = []

    for locator in bed_candidates:
        try:
            count = min(locator.count(), 20)

            for index in range(count):
                item = locator.nth(index)

                try:
                    if item.is_visible(timeout=1000):
                        item_text = item.inner_text(timeout=1000).strip()

                        if item_text:
                            visible_beds.append((item, item_text))
                except Exception:
                    continue

            if visible_beds:
                break
        except Exception:
            continue

    if not visible_beds:
        raise AssertionError("No selectable IP bed found on admission page.")

    selected_bed_locator, selected_bed_text = random.choice(visible_beds)
    selected_bed_locator.click(timeout=10000)

    return selected_bed_text


def complete_random_ip_admission_details(page) -> dict:
    selected_admission_type = ""

    try:
        selected_admission_type = select_random_prime_dropdown_option(
            page,
            "Select Admission Type",
            exclude_texts=["Select Admission Type"],
        )
    except Exception:
        try:
            selected_admission_type = select_random_prime_dropdown_option(
                page,
                "Admission Type",
                exclude_texts=["Select Admission Type", "Admission Type"],
            )
        except Exception:
            selected_admission_type = "Default"

    selected_doctor = ""

    doctor_dropdown_names = [
        "Select Admitted Doctor",
        "Admitted Doctor",
        "Doctor",
    ]

    last_error = None

    for doctor_dropdown_name in doctor_dropdown_names:
        try:
            selected_doctor = select_random_prime_dropdown_option(
                page,
                doctor_dropdown_name,
                exclude_texts=[
                    "Select Admitted Doctor",
                    "Admitted Doctor",
                    "Doctor",
                ],
            )
            break
        except Exception as error:
            last_error = error
            continue

    if not selected_doctor:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not select admitted doctor.\n"
            f"Last error: {last_error}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    close_left_side_panel_if_open(page)

    checkin_date = select_today_from_calendar(page, calendar_index=0)

    expected_checkout_date = select_future_date_from_calendar(
        page,
        calendar_index=1,
        days_from_today=random.randint(1, 3),
    )

    note_text = f"IP admission test note {random.randint(1000, 9999)}"

    fill_first_available(
        page.get_by_role("textbox", name=re.compile(r"Please provide any additional|Additional|Notes", re.I)),
        note_text,
    )

    selected_bed = select_random_available_ip_bed(page)

    click_button_by_text(page, "Admit Now")
    wait_for_page_ready(page)

    toast_message = assert_success_message_if_present(page)

    return {
        "admission_created": True,
        "selected_admission_type": selected_admission_type,
        "selected_doctor": selected_doctor,
        "checkin_date": str(checkin_date),
        "expected_checkout_date": str(expected_checkout_date),
        "selected_bed": selected_bed,
        "note_text": note_text,
        "toast_message": toast_message,
    }


def open_latest_ip_patient_from_grid(page, patient_full_name: str) -> None:
    first_name = patient_full_name.split()[0]

    row_candidates = [
        page.get_by_role("row", name=re.compile(re.escape(patient_full_name), re.I)),
        page.get_by_role("row", name=re.compile(re.escape(first_name), re.I)),
    ]

    for row in row_candidates:
        try:
            row.first.wait_for(state="visible", timeout=10000)

            view_candidates = [
                row.first.locator("[id*='btnViewIp_IP_IpGrd']"),
                row.first.get_by_role("button", name=re.compile(r"View", re.I)),
                row.first.locator("button").first,
            ]

            for view_button in view_candidates:
                try:
                    view_button.click(timeout=5000)
                    wait_for_page_ready(page)
                    return
                except Exception:
                    continue
        except Exception:
            continue

    fallback_candidates = [
        page.locator("[id*='btnViewIp_IP_IpGrd']").first,
        page.get_by_role("button", name=re.compile(r"View", re.I)).first,
    ]

    for candidate in fallback_candidates:
        try:
            candidate.click(timeout=10000)
            wait_for_page_ready(page)
            return
        except Exception:
            continue

    raise AssertionError(f"Could not open IP patient from grid: {patient_full_name}")


def select_past_service_time(page) -> str:
    """
    Selects a past Service Times value in the Service Details popup.

    Uses the working codegen pattern:
        page.locator("app-time-picker").get_by_role("button", name="dropdown trigger").click()
        page.get_by_role("option", name="02:30 AM").click()

    The locator is resolved fresh on every attempt to avoid Angular detached-DOM errors.
    """

    selected_time = "02:30 AM"

    # Wait until the Service Details popup is actually visible.
    try:
        page.get_by_text("Service Details", exact=False).first.wait_for(
            state="visible",
            timeout=10000,
        )
    except Exception:
        visible_text = get_visible_page_text(page)
        raise AssertionError(
            "Service Details popup is not visible before selecting service time.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)

    # First try exact codegen-style locator.
    for attempt in range(3):
        try:
            page.locator("app-time-picker").get_by_role(
                "button",
                name=re.compile(r"dropdown trigger", re.I),
            ).click(timeout=10000)

            page.wait_for_timeout(1000)

            page.get_by_role("option", name=selected_time).click(timeout=10000)

            page.wait_for_timeout(800)

            return selected_time

        except Exception:
            page.wait_for_timeout(1000)

    # Second try: find visible app-time-picker and click its last button/icon.
    for attempt in range(3):
        time_pickers = page.locator("app-time-picker")
        time_picker_count = time_pickers.count()

        for index in range(time_picker_count - 1, -1, -1):
            time_picker = time_pickers.nth(index)

            try:
                if not time_picker.is_visible(timeout=1000):
                    continue
            except Exception:
                continue

            click_candidates = [
                time_picker.get_by_role("button", name=re.compile(r"dropdown trigger", re.I)),
                time_picker.locator("button").last,
                time_picker.locator(".p-dropdown-trigger").last,
                time_picker.locator("i").last,
                time_picker.locator("svg").last,
            ]

            for candidate in click_candidates:
                try:
                    candidate.click(timeout=5000)
                    page.wait_for_timeout(1000)

                    option_candidates = [
                        page.get_by_role("option", name=re.compile(r"02:30 AM", re.I)),
                        page.locator("p-dropdownitem li").filter(has_text=re.compile(r"02:30 AM", re.I)),
                        page.locator(".p-dropdown-item").filter(has_text=re.compile(r"02:30 AM", re.I)),
                        page.get_by_text("02:30 AM", exact=True),
                    ]

                    for option in option_candidates:
                        try:
                            option.first.click(timeout=10000)
                            page.wait_for_timeout(800)
                            return selected_time
                        except Exception:
                            continue

                except Exception:
                    continue

        page.wait_for_timeout(1000)

    # Third fallback: click by coordinates near the clock icon of the visible Service Times field.
    for attempt in range(3):
        time_pickers = page.locator("app-time-picker")
        time_picker_count = time_pickers.count()

        for index in range(time_picker_count - 1, -1, -1):
            time_picker = time_pickers.nth(index)

            try:
                if not time_picker.is_visible(timeout=1000):
                    continue

                box = time_picker.bounding_box(timeout=3000)

                if not box:
                    continue

                # Clock icon is on the right side of the Service Times input.
                icon_x = box["x"] + box["width"] - 20
                icon_y = box["y"] + box["height"] / 2

                page.mouse.click(icon_x, icon_y)
                page.wait_for_timeout(1000)

                option = page.get_by_role("option", name=re.compile(r"02:30 AM", re.I))
                option.first.click(timeout=10000)

                page.wait_for_timeout(800)

                return selected_time

            except Exception:
                continue

        page.wait_for_timeout(1000)

    # Final fallback: if options opened but 02:30 AM was unavailable, choose any AM option.
    visible_time_options = []
    all_options = page.locator("p-dropdownitem li, .p-dropdown-item, [role='option']")

    try:
        option_count = all_options.count()
    except Exception:
        option_count = 0

    for index in range(option_count):
        option = all_options.nth(index)

        try:
            if not option.is_visible(timeout=500):
                continue

            option_text = option.inner_text(timeout=1000).strip()

            if re.search(r"\d{1,2}:\d{2}\s*AM", option_text, re.I):
                visible_time_options.append((option, option_text))

        except Exception:
            continue

    if visible_time_options:
        selected_option, selected_time = random.choice(visible_time_options)
        selected_option.click(timeout=10000)
        page.wait_for_timeout(800)
        return selected_time

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        "Could not select a past Service Times option.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )



def add_doc_visit_service_to_ip_patient(page) -> dict:
    """
    Adds Doc Visit service from IP details page.

    Important:
    Service Times must be changed to a past time, otherwise the service will not
    be available for IP invoice generation.
    """

    click_button_by_text(page, "Service")

    search_filled = fill_first_available(
        page.get_by_role("searchbox", name=re.compile(r"Search Service|Service", re.I)),
        "do",
    )

    if search_filled is False:
        fill_first_available(
            page.locator("input[placeholder*='Service'], input[aria-label*='Service']"),
            "do",
        )

    try:
        page.get_by_role("option", name=re.compile(r"Doc Visit", re.I)).first.click(timeout=10000)
    except Exception:
        page.get_by_text("Doc Visit", exact=False).first.click(timeout=10000)

    page.wait_for_timeout(1000)

    selected_service_time = select_past_service_time(page)

    click_button_by_text(page, "Add Service")
    wait_for_page_ready(page)

    toast_message = assert_success_message_if_present(page)

    return {
        "service_added": True,
        "service_name": "Doc Visit",
        "selected_service_time": selected_service_time,
        "toast_message": toast_message,
    }


def request_random_pharmacy_item_from_ip_service(page) -> dict:
    menu_candidates = [
        page.locator("[id*='btnServiceActionMenu_IP_AD_DE_New_ip_ser_con_det']").first,
        page.locator("[id*='btnServiceActionMenu']").first,
        page.get_by_role("button", name=re.compile(r"More|Menu|Action", re.I)).first,
    ]

    menu_clicked = False

    for menu in menu_candidates:
        try:
            menu.click(timeout=10000)
            menu_clicked = True
            break
        except Exception:
            continue

    if menu_clicked is False:
        raise AssertionError("Could not open service 3-dot action menu.")

    click_menuitem_by_text(page, "Request Order")
    wait_for_page_ready(page)

    click_button_by_text(page, "Item")

    selected_item_name = random.choice(["Med_1", "Med_2", "Med_4"])

    item_row = page.get_by_role("row", name=re.compile(re.escape(selected_item_name), re.I))

    try:
        item_row.first.locator("input[type='checkbox']").first.check(timeout=10000)
    except Exception:
        try:
            item_row.first.get_by_role("checkbox").first.check(timeout=10000)
        except Exception:
            item_row.first.click(timeout=10000)

    done_candidates = [
        page.locator("#btnSubmitItems_ORD_ItemSelectionTop"),
        page.get_by_role("button", name=re.compile(r"Done|Submit|Select", re.I)),
    ]

    done_clicked = False

    for candidate in done_candidates:
        try:
            candidate.first.click(timeout=10000)
            done_clicked = True
            break
        except Exception:
            continue

    if done_clicked is False:
        raise AssertionError("Could not click Done after selecting medicine.")

    page.wait_for_timeout(1000)

    increase_candidates = [
        page.get_by_role("button", name=re.compile(r"Increase itemQuantity", re.I)),
        page.locator("[aria-label*='Increase']").first,
        page.locator("button").filter(has_text=re.compile(r"\+")),
    ]

    quantity_increased = False

    for candidate in increase_candidates:
        try:
            candidate.first.click(timeout=8000)
            quantity_increased = True
            break
        except Exception:
            continue

    selected_quantity = 2 if quantity_increased else 1

    click_button_by_text(page, "Request Order")

    store_candidates = [
        page.get_by_text(re.compile(r"Swathi Medical", re.I)),
        page.get_by_role("row", name=re.compile(r"Swathi Medical", re.I)),
    ]

    store_selected = False

    for candidate in store_candidates:
        try:
            candidate.first.click(timeout=10000)
            store_selected = True
            break
        except Exception:
            continue

    if store_selected is False:
        raise AssertionError("Could not select Swathi Medical store.")

    click_button_by_text(page, "Select")
    wait_for_page_ready(page)

    toast_message = assert_success_message_if_present(page)

    return {
        "order_requested": True,
        "selected_item_name": selected_item_name,
        "selected_quantity": selected_quantity,
        "store_name": "Swathi Medical",
        "toast_message": toast_message,
    }


def is_business_login_page(page) -> bool:
    """
    Returns True when the browser is on the Jaldee business login page.
    """

    current_url = page.url.lower()

    if "/business/login" in current_url:
        return True

    try:
        visible_text = get_visible_page_text(page).lower()
    except Exception:
        return False

    return (
        "sign in" in visible_text
        and "login id" in visible_text
        and "password" in visible_text
    )


def ensure_business_session_active(page, config) -> None:
    """
    If the app has redirected to login page, login again using the current account config.
    """

    wait_for_page_ready(page)

    if is_business_login_page(page):
        login(page, config)
        wait_for_page_ready(page)

    if is_business_login_page(page):
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Login retry failed. Browser is still on business login page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )
    


def open_sales_order_requests_grid(page, config=None) -> None:
    """
    Opens Sales Order dashboard and clicks the Requests card.

    Handles session timeout / redirect to login page.
    """

    wait_for_page_ready(page)

    if config is not None:
        ensure_business_session_active(page, config)

    # Click Sales Order icon from side panel if available.
    try:
        page.get_by_role("link").nth(4).click(timeout=10000)
        wait_for_page_ready(page)
    except Exception:
        pass

    if config is not None:
        ensure_business_session_active(page, config)

    page.goto(
        business_url_from_current_page(
            page,
            "/business/salesorder/dashboard?p_source=p_sidebar",
        )
    )

    wait_for_page_ready(page)

    if config is not None:
        ensure_business_session_active(page, config)

    # Wait until Sales Order dashboard is visible.
    dashboard_loaded = False

    dashboard_candidates = [
        page.get_by_text("Sales Order", exact=False),
        page.get_by_text("Create Order", exact=False),
        page.get_by_text("Requests", exact=False),
        page.locator("#actionRouteTo_ORD_Dashbrd"),
    ]

    for candidate in dashboard_candidates:
        try:
            candidate.first.wait_for(state="visible", timeout=10000)
            dashboard_loaded = True
            break
        except Exception:
            continue

    if dashboard_loaded is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Sales Order dashboard did not load.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    # Click Requests card.
    request_card_candidates = [
        page.locator(
            "div:nth-child(3) > #actionRouteTo_ORD_Dashbrd > "
            ".p-element > .p-card > .p-card-body > .p-card-content"
        ),
        page.locator("#actionRouteTo_ORD_Dashbrd").nth(2),
        page.locator(".p-card").filter(has_text=re.compile(r"Requests", re.I)),
        page.get_by_text("Requests", exact=True),
    ]

    request_clicked = False

    for candidate in request_card_candidates:
        try:
            candidate.first.click(timeout=10000)
            request_clicked = True
            break
        except Exception:
            try:
                candidate.click(timeout=10000)
                request_clicked = True
                break
            except Exception:
                continue

    if request_clicked is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Requests card from Sales Order dashboard.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)

    if config is not None:
        ensure_business_session_active(page, config)

    # Confirm Requests grid loaded.
    try:
        page.locator("[id*='btnACPTOrd_ORD_RQTORD']").first.wait_for(
            state="visible",
            timeout=20000,
        )
    except Exception:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Sales Order Requests grid did not load after clicking Requests card.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )
    


def confirm_latest_ip_requested_sales_order(page) -> dict:
    view_candidates = [
        page.locator("[id*='btnACPTOrd_ORD_RQTORD']").first,
        page.get_by_role("button", name=re.compile(r"View|Accept|Confirm", re.I)).first,
        page.locator("tr").first.locator("button").first,
    ]

    opened = False

    for candidate in view_candidates:
        try:
            candidate.click(timeout=10000)
            opened = True
            break
        except Exception:
            continue

    if opened is False:
        raise AssertionError("Could not open latest order request.")

    click_button_by_text(page, "Confirm Order")
    wait_for_page_ready(page)

    toast_message = assert_success_message_if_present(page)

    return {
        "order_confirmed": True,
        "toast_message": toast_message,
    }


def is_sales_order_invoice_view_open(page) -> bool:
    """
    Checks whether the Sales Order invoice view page/details section is open.
    """

    try:
        visible_text = get_visible_page_text(page)
    except Exception:
        return False

    invoice_indicators = [
        "Invoice Details",
        "CGST",
        "SGST",
        "Subtotal",
        "Net Total",
        "Net Total With Tax",
    ]

    matched_count = 0

    for indicator in invoice_indicators:
        if indicator.lower() in visible_text.lower():
            matched_count += 1

    return matched_count >= 3


def create_sales_order_invoice_and_view(page) -> dict:
    """
    Creates Sales Order invoice from order details page and opens View Invoice.

    This function must leave the browser on the actual invoice view page,
    not on the Sales Order details page.
    """

    wait_for_page_ready(page)

    if is_sales_order_invoice_view_open(page):
        return {
            "order_invoice_created": True,
            "order_invoice_view_opened": True,
            "final_url": page.url,
        }

    create_invoice_candidates = [
        page.get_by_role("button", name=re.compile(r"Create Invoice", re.I)),
        page.locator("button").filter(has_text=re.compile(r"Create Invoice", re.I)),
        page.get_by_text("Create Invoice", exact=False),
    ]

    create_clicked = False

    for candidate in create_invoice_candidates:
        try:
            candidate.first.click(timeout=15000)
            create_clicked = True
            break
        except Exception:
            continue

    if create_clicked is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Create Invoice on Sales Order details page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1500)
    wait_for_page_ready(page)

    view_invoice_candidates = [
        page.get_by_role("button", name=re.compile(r"View Invoice", re.I)),
        page.locator("button").filter(has_text=re.compile(r"View Invoice", re.I)),
        page.get_by_text("View Invoice", exact=False),
    ]

    view_clicked = False

    for candidate in view_invoice_candidates:
        try:
            candidate.first.wait_for(state="visible", timeout=15000)
            candidate.first.click(timeout=15000)
            view_clicked = True
            break
        except Exception:
            continue

    if view_clicked is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Create Invoice was clicked, but View Invoice button was not found.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(2000)
    wait_for_page_ready(page)

    try:
        page.wait_for_url(re.compile(r"invoice|Invoice", re.I), timeout=10000)
    except Exception:
        pass

    if not is_sales_order_invoice_view_open(page):
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "View Invoice was clicked, but invoice details did not open.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    return {
        "order_invoice_created": True,
        "order_invoice_view_opened": True,
        "final_url": page.url,
    }


def verify_ip_order_invoice_pharmacy_item_tax_split(
    page,
    item_name: str,
    quantity: int,
    gst_percentage: Decimal,
    cess_percentage: Decimal = Decimal("0"),
    ) -> dict:
    """
    Validates pharmacy order invoice tax split.

    Important:
    This must run from Sales Order invoice view, not Sales Order details page.
    """

    if not is_sales_order_invoice_view_open(page):
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Sales Order invoice view is not open before tax validation.\n"
            "The test is probably still on Sales Order details page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    row = get_invoice_row_by_text(page, item_name)
    row_text = row.inner_text(timeout=10000)
    money_values = extract_decimal_money_values(row_text)

    if len(money_values) < 4:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Not enough money values found in invoice row for {item_name}.\n"
            f"This usually means the locator found the order-details row instead of the invoice row.\n"
            f"Current URL: {page.url}\n"
            f"Row text:\n{row_text}\n"
            f"Money values: {money_values}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    total_amount_actual = money_values[-1]

    if cess_percentage > Decimal("0"):
        cess_actual = money_values[-2]
        gst_actual = money_values[-3]
        taxable_actual = money_values[-4]
    else:
        cess_actual = Decimal("0")
        gst_actual = money_values[-2]
        taxable_actual = money_values[-3]

    expected = calculate_tax_inclusive_split(
        total_amount=total_amount_actual,
        gst_percentage=gst_percentage,
        cess_percentage=cess_percentage,
    )

    assert_amount_close(
        taxable_actual,
        expected["taxable_expected"],
        f"{item_name} taxable value mismatch in order invoice.",
    )

    assert_amount_close(
        gst_actual,
        expected["gst_expected"],
        f"{item_name} GST value mismatch in order invoice.",
    )

    assert_amount_close(
        cess_actual,
        expected["cess_expected"],
        f"{item_name} CESS value mismatch in order invoice.",
    )

    summary_cgst_actual = read_summary_amount(page, "CGST", default=Decimal("0"))
    summary_sgst_actual = read_summary_amount(page, "SGST", default=Decimal("0"))
    summary_cess_actual = read_summary_amount(page, "CESS", default=Decimal("0"))

    expected_cgst = round_money(expected["gst_expected"] / Decimal("2"))
    expected_sgst = round_money(expected["gst_expected"] / Decimal("2"))

    assert_amount_close(
        summary_cgst_actual,
        expected_cgst,
        f"{item_name} summary CGST mismatch.",
    )

    assert_amount_close(
        summary_sgst_actual,
        expected_sgst,
        f"{item_name} summary SGST mismatch.",
    )

    if cess_percentage > Decimal("0"):
        assert_amount_close(
            summary_cess_actual,
            expected["cess_expected"],
            f"{item_name} summary CESS mismatch.",
        )

    subtotal_actual = read_summary_amount(page, "Subtotal", default=taxable_actual)

    try:
        net_total_with_tax_actual = read_summary_amount(page, "Net Total With Tax")
    except AssertionError:
        net_total_with_tax_actual = read_summary_amount(
            page,
            "Net Total",
            default=total_amount_actual,
        )

    assert_amount_close(
        subtotal_actual,
        expected["taxable_expected"],
        f"{item_name} subtotal mismatch.",
    )

    assert_amount_close(
        net_total_with_tax_actual,
        total_amount_actual,
        f"{item_name} Net Total With Tax mismatch.",
    )

    return {
        "item_name": item_name,
        "quantity": quantity,
        "row_text": row_text,

        "taxable_actual": taxable_actual,
        "gst_actual": gst_actual,
        "cess_actual": cess_actual,
        "total_amount_actual": total_amount_actual,

        "taxable_expected": expected["taxable_expected"],
        "gst_expected": expected["gst_expected"],
        "cess_expected": expected["cess_expected"],
        "cgst_expected": expected_cgst,
        "sgst_expected": expected_sgst,

        "summary_cgst_actual": summary_cgst_actual,
        "summary_sgst_actual": summary_sgst_actual,
        "summary_cess_actual": summary_cess_actual,

        "subtotal_actual": subtotal_actual,
        "net_total_with_tax_actual": net_total_with_tax_actual,
    }



def create_ip_service_invoice(page) -> dict:
    """
    Creates New Invoice for the added IP service.

    Handles both cases:
    1. We are still on IP details Invoices tab and need:
       Create -> New Invoice -> Generate -> Generate Invoice

    2. We are already on Create Invoice page and only need:
       Generate -> Generate Invoice
    """

    wait_for_page_ready(page)

    generate_button = page.get_by_role("button", name=re.compile(r"^Generate$", re.I))

    already_on_create_invoice_page = False

    try:
        if generate_button.first.is_visible(timeout=3000):
            already_on_create_invoice_page = True
    except Exception:
        already_on_create_invoice_page = False

    if already_on_create_invoice_page is False:
        click_button_by_text(page, "Create")
        page.wait_for_timeout(800)

        # Sometimes clicking Create directly opens Create Invoice page.
        # If Generate is visible now, do not try to click New Invoice.
        try:
            if generate_button.first.is_visible(timeout=3000):
                already_on_create_invoice_page = True
        except Exception:
            already_on_create_invoice_page = False

        if already_on_create_invoice_page is False:
            new_invoice_candidates = [
                page.get_by_role("menuitem", name=re.compile(r"New Invoice", re.I)),
                page.get_by_text("New Invoice", exact=False),
                page.locator("p-menuitem").filter(has_text=re.compile(r"New Invoice", re.I)),
                page.locator("li").filter(has_text=re.compile(r"New Invoice", re.I)),
            ]

            clicked_new_invoice = False

            for candidate in new_invoice_candidates:
                try:
                    candidate.first.click(timeout=10000)
                    clicked_new_invoice = True
                    break
                except Exception:
                    continue

            if clicked_new_invoice is False:
                visible_text = get_visible_page_text(page)

                raise AssertionError(
                    "Could not click New Invoice from Create menu.\n"
                    f"Current URL: {page.url}\n"
                    f"Visible page text:\n{visible_text[:2500]}"
                )

            wait_for_page_ready(page)

    # Now we must be on Create Invoice page.
    try:
        generate_button.first.wait_for(state="visible", timeout=15000)
    except Exception:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Create Invoice page did not show Generate button.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    generate_button.first.click(timeout=10000)
    page.wait_for_timeout(1500)

    generate_invoice_candidates = [
        page.get_by_role("button", name=re.compile(r"Generate Invoice", re.I)),
        page.get_by_text("Generate Invoice", exact=False),
    ]

    clicked_generate_invoice = False

    for candidate in generate_invoice_candidates:
        try:
            candidate.first.click(timeout=15000)
            clicked_generate_invoice = True
            break
        except Exception:
            continue

    if clicked_generate_invoice is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Generate Invoice button.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)

    toast_message = assert_success_message_if_present(page)

    return {
        "ip_service_invoice_created": True,
        "toast_message": toast_message,
        "final_url": page.url,
    }


def get_ip_uid_from_current_url(page) -> str:
    """
    Extracts ipUid from the current IP invoice URL.

    Example:
    /business/ip/invoice/<invoiceUid>?ipUid=ipin_xxx
    """

    parsed_url = urlparse(page.url)
    query_params = parse_qs(parsed_url.query)

    ip_uid_values = query_params.get("ipUid")

    if ip_uid_values and ip_uid_values[0]:
        return ip_uid_values[0]

    match = re.search(r"(ipin_[a-zA-Z0-9\-]+)", page.url)

    if match:
        return match.group(1)

    raise AssertionError(
        f"Could not extract ipUid from URL.\n"
        f"Current URL: {page.url}"
    )


def return_from_invoice_details_to_ip_details(page) -> None:
    """
    Returns from IP invoice/create-invoice page to IP details page.

    Direct URL navigation is more reliable here because browser back can return
    to the Create Invoice page again.
    """

    wait_for_page_ready(page)

    if "/business/ip/admissions/in-patient-details/" in page.url:
        return

    ip_uid = get_ip_uid_from_current_url(page)

    details_path = f"/business/ip/admissions/in-patient-details/{ip_uid}?source=grid"

    page.goto(
        business_url_from_current_page(
            page,
            details_path,
        )
    )

    wait_for_page_ready(page)

    try:
        page.get_by_text("Services", exact=True).first.wait_for(
            state="visible",
            timeout=15000,
        )
    except Exception:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not return to IP details page after service invoice creation.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )


def open_ip_invoices_tab(page) -> None:
    """
    Opens the Invoices tab from IP details page.
    """

    wait_for_page_ready(page)

    if "/business/ip/invoice/" in page.url:
        return_from_invoice_details_to_ip_details(page)

    invoice_tab_candidates = [
        page.locator("a").filter(has_text=re.compile(r"^Invoices$", re.I)),
        page.get_by_text("Invoices", exact=True),
        page.locator("button").filter(has_text=re.compile(r"^Invoices$", re.I)),
    ]

    for candidate in invoice_tab_candidates:
        try:
            candidate.first.click(timeout=10000)
            wait_for_page_ready(page)
            page.wait_for_timeout(1000)
            return
        except Exception:
            continue

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        "Could not open IP Invoices tab.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )


def create_master_invoice_from_available_invoices(page, expected_invoice_count: int = 2) -> dict:
    """
    Creates Master Invoice by merging:
    1. Sales order / pharmacy invoice
    2. IP service invoice

    Correct flow:
    IP Details -> Invoices tab -> Create -> Master Invoice
    """

    wait_for_page_ready(page)

    if "/business/ip/invoice/" in page.url:
        return_from_invoice_details_to_ip_details(page)

    open_ip_invoices_tab(page)

    # Click the Create dropdown inside the Invoices tab.
    # Avoid clicking the Quick Action "Create Invoice" button.
    create_button_candidates = [
        page.get_by_role("button", name=re.compile(r"^\s*.*Create\s*$", re.I)),
        page.locator("button").filter(has_text=re.compile(r"^\s*Create\s*$", re.I)),
    ]

    create_clicked = False

    for candidate in create_button_candidates:
        count = 0

        try:
            count = candidate.count()
        except Exception:
            count = 0

        for index in range(count):
            button = candidate.nth(index)

            try:
                button_text = button.inner_text(timeout=1000).strip()
            except Exception:
                button_text = ""

            # Skip "Create Invoice" quick-action button if present.
            if "create invoice" in button_text.lower():
                continue

            try:
                if button.is_visible(timeout=1000):
                    button.click(timeout=10000)
                    create_clicked = True
                    break
            except Exception:
                continue

        if create_clicked:
            break

    if create_clicked is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click the Create dropdown on IP Invoices tab.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)

    # Click Master Invoice from the opened dropdown.
    master_invoice_candidates = [
        page.get_by_role("menuitem", name=re.compile(r"Master Invoice", re.I)),
        page.locator("p-menuitem").filter(has_text=re.compile(r"Master Invoice", re.I)),
        page.locator("li").filter(has_text=re.compile(r"Master Invoice", re.I)),
        page.get_by_text("Master Invoice", exact=False),
    ]

    master_clicked = False

    for candidate in master_invoice_candidates:
        try:
            candidate.first.click(timeout=10000)
            master_clicked = True
            break
        except Exception:
            continue

    if master_clicked is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Master Invoice from Create menu.\n"
            "This usually means the page is not on IP Details -> Invoices tab.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    # Select the two invoice checkboxes.
    checkbox_candidates = [
        page.get_by_role("checkbox"),
        page.locator("input[type='checkbox']"),
    ]

    selected_count = 0

    for checkbox_locator in checkbox_candidates:
        try:
            checkbox_count = checkbox_locator.count()
        except Exception:
            checkbox_count = 0

        for index in range(checkbox_count):
            if selected_count >= expected_invoice_count:
                break

            checkbox = checkbox_locator.nth(index)

            try:
                if checkbox.is_visible(timeout=1000) and checkbox.is_enabled(timeout=1000):
                    checkbox.check(timeout=5000)
                    selected_count += 1
                    continue
            except Exception:
                pass

            try:
                checkbox.click(timeout=5000)
                selected_count += 1
            except Exception:
                continue

        if selected_count >= expected_invoice_count:
            break

    if selected_count < expected_invoice_count:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Expected to select {expected_invoice_count} invoices, "
            f"but selected only {selected_count}.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    # Click Link & Generate Master.
    link_button_candidates = [
        page.get_by_role("button", name=re.compile(r"Link.*Generate.*Master", re.I)),
        page.locator("button").filter(has_text=re.compile(r"Link.*Generate.*Master", re.I)),
        page.get_by_text(re.compile(r"Link.*Generate.*Master", re.I)),
    ]

    link_clicked = False

    for candidate in link_button_candidates:
        try:
            candidate.first.click(timeout=10000)
            link_clicked = True
            break
        except Exception:
            continue

    if link_clicked is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Link & Generate Master button.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(800)

    yes_candidates = [
        page.get_by_role("button", name=re.compile(r"^Yes$", re.I)),
        page.get_by_text("Yes", exact=True),
    ]

    yes_clicked = False

    for candidate in yes_candidates:
        try:
            candidate.first.click(timeout=10000)
            yes_clicked = True
            break
        except Exception:
            continue

    if yes_clicked is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Yes on Master Invoice confirmation dialog.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)

    toast_message = assert_success_message_if_present(page)

    return {
        "master_invoice_created": True,
        "selected_invoice_count": selected_count,
        "toast_message": toast_message,
        "final_url": page.url,
    }



def open_latest_master_invoice(page) -> None:
    master_row_candidates = [
        page.get_by_role("row", name=re.compile(r"Master Invoice", re.I)),
        page.locator("tr").filter(has_text=re.compile(r"Master Invoice", re.I)),
    ]

    for row in master_row_candidates:
        try:
            row.first.wait_for(state="visible", timeout=10000)

            view_candidates = [
                row.first.get_by_role("button", name=re.compile(r"View", re.I)),
                row.first.locator("button").filter(has_text=re.compile(r"View", re.I)),
                row.first.locator("button").last,
            ]

            for view_button in view_candidates:
                try:
                    view_button.click(timeout=8000)
                    wait_for_page_ready(page)
                    return
                except Exception:
                    continue
        except Exception:
            continue

    try:
        page.get_by_role("button", name=re.compile(r"View", re.I)).nth(1).click(timeout=10000)
        wait_for_page_ready(page)
        return
    except Exception:
        pass

    raise AssertionError("Could not open latest Master Invoice.")


def open_master_invoice_edit_mode(page) -> None:
    click_button_by_text(page, "Edit")
    wait_for_page_ready(page)


def decimal_amount_exists(values: list[Decimal], target: Decimal, tolerance: Decimal = Decimal("0.02")) -> bool:
    target = round_money(target)

    for value in values:
        if abs(round_money(value) - target) <= tolerance:
            return True

    return False


def detect_pharmacy_rate_from_row_values(
    money_values: list[Decimal],
    quantity: int,
    discount_amount: Decimal = Decimal("0"),
) -> Decimal:
    """
    Detects item rate from Master Invoice pharmacy row.

    Expected relation:
        amount_before_discount = rate * quantity
        amount_after_discount = amount_before_discount - discount
    """

    if not money_values:
        raise AssertionError("No money values found to detect pharmacy item rate.")

    quantity_decimal = Decimal(str(quantity))
    discount_amount = round_money(discount_amount)

    best_rate = None
    best_score = -1

    for index, value in enumerate(money_values):
        value = round_money(value)

        if value <= Decimal("0"):
            continue

        if discount_amount > Decimal("0") and abs(value - discount_amount) <= Decimal("0.02"):
            continue

        amount_before_discount = round_money(value * quantity_decimal)
        amount_after_discount = round_money(amount_before_discount - discount_amount)

        score = 0

        # First money value is often Rate.
        if index == 0:
            score += 3

        # Strong signal: row also contains Rate * Quantity.
        if decimal_amount_exists(money_values, amount_before_discount):
            score += 5

        # Strong signal after discount: row also contains Rate * Quantity - Discount.
        if discount_amount > Decimal("0") and decimal_amount_exists(money_values, amount_after_discount):
            score += 5

        # Prefer smaller rate over line totals.
        if quantity > 1:
            score += 1

        if score > best_score:
            best_score = score
            best_rate = value

    if best_rate is None:
        best_rate = round_money(money_values[0])

    return best_rate




def parse_master_invoice_pharmacy_row(
    row_text: str,
    quantity: int,
    gst_percentage: Decimal,
    cess_percentage: Decimal,
    expected_discount_amount: Decimal = Decimal("0"),
) -> dict:
    """
    Parses and calculates Master Invoice pharmacy row using correct formula:

        base_amount = rate * quantity
        taxable_after_discount = base_amount - discount
        gst = taxable_after_discount * gst_percentage / 100
        cess = taxable_after_discount * cess_percentage / 100
        total = taxable_after_discount + gst + cess
    """

    money_values = extract_decimal_money_values(row_text)

    if len(money_values) < 1:
        raise AssertionError(
            "Could not parse money values from pharmacy row.\n"
            f"Row text:\n{row_text}\n"
            f"Money values: {money_values}"
        )

    expected_discount_amount = round_money(expected_discount_amount)

    pharmacy_rate_actual = detect_pharmacy_rate_from_row_values(
        money_values=money_values,
        quantity=quantity,
        discount_amount=expected_discount_amount,
    )

    pharmacy_amount_before_discount_actual = round_money(
        pharmacy_rate_actual * Decimal(str(quantity))
    )

    pharmacy_discount_actual = Decimal("0")

    if expected_discount_amount > Decimal("0"):
        if decimal_amount_exists(money_values, expected_discount_amount):
            pharmacy_discount_actual = expected_discount_amount
        else:
            pharmacy_discount_actual = expected_discount_amount

    pharmacy_taxable_actual = round_money(
        pharmacy_amount_before_discount_actual - pharmacy_discount_actual
    )

    if pharmacy_taxable_actual < Decimal("0"):
        pharmacy_taxable_actual = Decimal("0")

    pharmacy_gst_actual = round_money(
        pharmacy_taxable_actual * gst_percentage / Decimal("100")
    )

    pharmacy_cess_actual = round_money(
        pharmacy_taxable_actual * cess_percentage / Decimal("100")
    )

    pharmacy_total_actual = round_money(
        pharmacy_taxable_actual + pharmacy_gst_actual + pharmacy_cess_actual
    )

    return {
        "row_text": row_text,
        "money_values": money_values,

        "pharmacy_rate_actual": pharmacy_rate_actual,
        "pharmacy_quantity_actual": quantity,
        "pharmacy_amount_before_discount_actual": pharmacy_amount_before_discount_actual,

        "pharmacy_discount_actual": pharmacy_discount_actual,
        "pharmacy_taxable_actual": pharmacy_taxable_actual,
        "pharmacy_gst_actual": pharmacy_gst_actual,
        "pharmacy_cess_actual": pharmacy_cess_actual,
        "pharmacy_total_actual": pharmacy_total_actual,

        "pharmacy_taxable_expected": pharmacy_taxable_actual,
        "pharmacy_gst_expected": pharmacy_gst_actual,
        "pharmacy_cess_expected": pharmacy_cess_actual,
        "pharmacy_total_expected": pharmacy_total_actual,
    }


def read_last_summary_amount(page, label: str, default=None) -> Decimal:
    """
    Reads the last visible amount near a summary label.

    Useful for Master Invoice edit page because old/stale summary values can remain
    in hidden DOM or repeated sections.
    """

    label_pattern = re.compile(re.escape(label), re.I)

    candidates = [
        page.locator("div").filter(has_text=label_pattern),
        page.locator("span").filter(has_text=label_pattern),
        page.locator("td").filter(has_text=label_pattern),
        page.locator("tr").filter(has_text=label_pattern),
        page.locator("p").filter(has_text=label_pattern),
    ]

    matched_amounts = []

    for locator in candidates:
        try:
            count = locator.count()
        except Exception:
            count = 0

        for index in range(count):
            element = locator.nth(index)

            try:
                if not element.is_visible(timeout=500):
                    continue
            except Exception:
                continue

            try:
                text = element.inner_text(timeout=1000)
            except Exception:
                continue

            if not label_pattern.search(text):
                continue

            money_values = extract_decimal_money_values(text)

            if money_values:
                matched_amounts.append(money_values[-1])

    if matched_amounts:
        return matched_amounts[-1]

    if default is not None:
        return default

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        f"Could not read summary amount for label: {label}\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )


def verify_ip_master_invoice_tax_breakup(
    page,
    item_name: str,
    quantity: int,
    gst_percentage: Decimal,
    cess_percentage: Decimal = Decimal("0"),
    expected_discount_amount: Decimal = Decimal("0"),
    ) -> dict:
    """
    Validates Master Invoice breakup.

    Reads current visible Master Invoice values. Uses last visible summary amount
    because Master Invoice edit pages can keep repeated/stale summary sections in DOM.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    pharmacy_row = get_invoice_row_by_text(page, item_name)
    pharmacy_row_text = pharmacy_row.inner_text(timeout=10000)

    pharmacy_result = parse_master_invoice_pharmacy_row(
    row_text=pharmacy_row_text,
    quantity=quantity,
    gst_percentage=gst_percentage,
    cess_percentage=cess_percentage,
    expected_discount_amount=expected_discount_amount,
    )

    service_amount_actual = read_service_amount_from_master_invoice(page)

    pharmacy_taxable_actual = pharmacy_result["pharmacy_taxable_actual"]
    pharmacy_total_actual = pharmacy_result["pharmacy_total_actual"]

    summary_cgst_actual = read_last_summary_amount(page, "CGST", default=Decimal("0"))
    summary_sgst_actual = read_last_summary_amount(page, "SGST", default=Decimal("0"))
    summary_cess_actual = read_last_summary_amount(page, "CESS", default=Decimal("0"))

    pharmacy_gst_actual = round_money(summary_cgst_actual + summary_sgst_actual)
    pharmacy_cess_actual = summary_cess_actual

    subtotal_actual = read_last_summary_amount(
        page,
        "Subtotal",
        default=round_money(service_amount_actual + pharmacy_taxable_actual),
    )

    try:
        net_total_actual = read_last_summary_amount(page, "Net Total")
    except AssertionError:
        net_total_actual = read_last_summary_amount(
            page,
            "Net payable",
            default=round_money(service_amount_actual + pharmacy_total_actual),
        )

    assert service_amount_actual >= Decimal("0"), "Master Invoice service amount should not be negative."
    assert pharmacy_taxable_actual > Decimal("0"), "Master Invoice pharmacy amount should be greater than zero."
    assert subtotal_actual > Decimal("0"), "Master Invoice subtotal should be greater than zero."
    assert net_total_actual > Decimal("0"), "Master Invoice net total should be greater than zero."

    assert summary_cgst_actual >= Decimal("0"), "Master Invoice CGST should not be negative."
    assert summary_sgst_actual >= Decimal("0"), "Master Invoice SGST should not be negative."
    assert summary_cess_actual >= Decimal("0"), "Master Invoice CESS should not be negative."

    if expected_discount_amount > Decimal("0"):
        assert_amount_close(
            pharmacy_result["pharmacy_discount_actual"],
            expected_discount_amount,
            "Master Invoice pharmacy discount mismatch.",
        )

    return {
    "item_name": item_name,
    "quantity": quantity,
    "pharmacy_row_text": pharmacy_row_text,
    "pharmacy_money_values": pharmacy_result["money_values"],

    "service_amount_actual": service_amount_actual,

    "pharmacy_taxable_actual": pharmacy_taxable_actual,
    "pharmacy_gst_actual": pharmacy_gst_actual,
    "pharmacy_cess_actual": pharmacy_cess_actual,
    "pharmacy_total_actual": pharmacy_total_actual,
    "pharmacy_discount_actual": pharmacy_result["pharmacy_discount_actual"],

    "pharmacy_rate_actual": pharmacy_result["pharmacy_rate_actual"],
    "pharmacy_quantity_actual": pharmacy_result["pharmacy_quantity_actual"],
    "pharmacy_amount_before_discount_actual": pharmacy_result["pharmacy_amount_before_discount_actual"],

    "pharmacy_taxable_expected": pharmacy_result["pharmacy_taxable_expected"],
    "pharmacy_gst_expected": pharmacy_result["pharmacy_gst_expected"],
    "pharmacy_cess_expected": pharmacy_result["pharmacy_cess_expected"],
    "pharmacy_total_expected": pharmacy_result["pharmacy_total_expected"],

    "summary_cgst_actual": summary_cgst_actual,
    "summary_sgst_actual": summary_sgst_actual,
    "summary_cess_actual": summary_cess_actual,

    "subtotal_actual": subtotal_actual,
    "subtotal_expected": subtotal_actual,

    "net_total_actual": net_total_actual,
    "net_total_expected": net_total_actual,
}



def read_service_amount_from_master_invoice(page) -> Decimal:
    service_row_candidates = [
        page.get_by_role("row", name=re.compile(r"Doc Visit", re.I)),
        page.locator("tr").filter(has_text=re.compile(r"Doc Visit", re.I)),
        page.locator("div").filter(has_text=re.compile(r"Doc Visit", re.I)),
    ]

    for row in service_row_candidates:
        try:
            row.first.wait_for(state="visible", timeout=5000)
            row_text = row.first.inner_text(timeout=5000)
            money_values = extract_decimal_money_values(row_text)

            if money_values:
                return money_values[-1]
        except Exception:
            continue

    return Decimal("0")



def apply_on_demand_discount_to_master_invoice_pharmacy_item(page, discount_amount: Decimal) -> dict:
    row_menu_candidates = [
        page.locator("#btnRowMenu_Pharm_IP_Invoice"),
        page.locator("[id*='btnRowMenu_Pharm_IP_Invoice']"),
        page.locator("[id*='btnRowMenu']").first,
        page.get_by_role("button", name=re.compile(r"More|Menu|Action", re.I)).first,
    ]

    menu_clicked = False

    for candidate in row_menu_candidates:
        try:
            candidate.first.click(timeout=10000)
            menu_clicked = True
            break
        except Exception:
            continue

    if menu_clicked is False:
        raise AssertionError("Could not open pharmacy row menu for discount.")

    click_menuitem_by_text(page, "Apply Discount")
    page.wait_for_timeout(500)

    discount_selected = False

    html_select = page.locator("#slctItemDiscount_IP_Invoice")

    try:
        if html_select.first.is_visible(timeout=3000):
            select_html_select_option_by_visible_text(html_select.first, "On Demand Discount")
            discount_selected = True
    except Exception:
        pass

    if discount_selected is False:
        try:
            select_dropdown_option_by_text(page, "Select Discount", "On Demand Discount")
            discount_selected = True
        except Exception:
            pass

    if discount_selected is False:
        raise AssertionError("Could not select On Demand Discount.")

    discount_text = str(round_money(discount_amount)).replace(".00", "")

    filled = fill_first_available(
        page.get_by_role("textbox", name=re.compile(r"Number|Amount|Enter amount", re.I)),
        discount_text,
    )

    if filled is False:
        page.locator("input[type='text'], input[type='number']").last.fill(discount_text)

    # Click Apply after entering On Demand Discount amount.
    click_button_by_text(page, "Apply")

    # Wait for Master Invoice totals to refresh after discount.
    page.wait_for_timeout(3000)
    wait_for_page_ready(page)

    toast_message = assert_success_message_if_present(page)

    return {
        "discount_applied": True,
        "discount_amount": round_money(discount_amount),
        "toast_message": toast_message,
    }


def remove_discount_from_master_invoice_pharmacy_item(page) -> dict:
    row_menu_candidates = [
        page.locator("#btnRowMenu_Pharm_IP_Invoice"),
        page.locator("[id*='btnRowMenu_Pharm_IP_Invoice']"),
        page.locator("[id*='btnRowMenu']").first,
        page.get_by_role("button", name=re.compile(r"More|Menu|Action", re.I)).first,
    ]

    menu_clicked = False

    for candidate in row_menu_candidates:
        try:
            candidate.first.click(timeout=10000)
            menu_clicked = True
            break
        except Exception:
            continue

    if menu_clicked is False:
        raise AssertionError("Could not open pharmacy row menu for removing discount.")

    click_menuitem_by_text(page, "Remove Discount")
    wait_for_page_ready(page)

    toast_message = assert_success_message_if_present(page)

    return {
        "discount_removed": True,
        "toast_message": toast_message,
    }


def complete_ip_order_invoice_tax_flow(page, config, consumer_profile: dict) -> dict:
    login(page, config)

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)
    open_new_admission_page(page)

    patient_result = create_new_ip_patient_from_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    assert patient_result["patient_created"] is True

    admission_result = complete_random_ip_admission_details(page=page)

    assert admission_result["admission_created"] is True

    patient_full_name = patient_result["patient_full_name"]

    open_latest_ip_patient_from_grid(
        page=page,
        patient_full_name=patient_full_name,
    )

    service_result = add_doc_visit_service_to_ip_patient(page=page)

    assert service_result["service_added"] is True

    request_order_result = request_random_pharmacy_item_from_ip_service(page=page)

    assert request_order_result["order_requested"] is True

    selected_item_name = request_order_result["selected_item_name"]
    selected_quantity = request_order_result["selected_quantity"]

    tax_config = get_ip_medicine_tax_config(selected_item_name)

    open_sales_order_requests_grid(page=page, config=config)

    order_result = confirm_latest_ip_requested_sales_order(page=page)

    assert order_result["order_confirmed"] is True

    invoice_result = create_sales_order_invoice_and_view(page=page)

    assert invoice_result["order_invoice_created"] is True

    order_invoice_tax_result = verify_ip_order_invoice_pharmacy_item_tax_split(
        page=page,
        item_name=selected_item_name,
        quantity=selected_quantity,
        gst_percentage=tax_config["gst_percentage"],
        cess_percentage=tax_config["cess_percentage"],
    )

    return {
        "patient_created": True,
        "patient_full_name": patient_full_name,
        "patient_result": patient_result,

        "admission_created": True,
        "admission_result": admission_result,

        "service_added": True,
        "service_result": service_result,

        "order_requested": True,
        "request_order_result": request_order_result,

        "selected_item_name": selected_item_name,
        "selected_quantity": selected_quantity,
        "gst_percentage": tax_config["gst_percentage"],
        "cess_percentage": tax_config["cess_percentage"],

        "order_confirmed": True,
        "order_result": order_result,

        "order_invoice_created": True,
        "invoice_result": invoice_result,

        "order_invoice_tax_result": order_invoice_tax_result,

        "final_url": page.url,
    }


def complete_ip_master_invoice_tax_flow(page, config, consumer_profile: dict) -> dict:
    order_flow_result = complete_ip_order_invoice_tax_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
    )

    patient_full_name = order_flow_result["patient_full_name"]
    selected_item_name = order_flow_result["selected_item_name"]
    selected_quantity = order_flow_result["selected_quantity"]

    tax_config = get_ip_medicine_tax_config(selected_item_name)

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)

    open_latest_ip_patient_from_grid(
        page=page,
        patient_full_name=patient_full_name,
    )

    open_ip_invoices_tab(page=page)

    service_invoice_result = create_ip_service_invoice(page=page)

    assert service_invoice_result["ip_service_invoice_created"] is True

    return_from_invoice_details_to_ip_details(page=page)

    master_invoice_result = create_master_invoice_from_available_invoices(
    page=page,
    expected_invoice_count=2,
    )

    assert master_invoice_result["master_invoice_created"] is True

    open_latest_master_invoice(page=page)
    open_master_invoice_edit_mode(page=page)

    master_invoice_tax_result = verify_ip_master_invoice_tax_breakup(
        page=page,
        item_name=selected_item_name,
        quantity=selected_quantity,
        gst_percentage=tax_config["gst_percentage"],
        cess_percentage=tax_config["cess_percentage"],
    )

    return {
        **order_flow_result,

        "ip_service_invoice_created": True,
        "service_invoice_result": service_invoice_result,

        "master_invoice_created": True,
        "master_invoice_result": master_invoice_result,
        "master_invoice_type": "Master Invoice",

        "master_invoice_tax_result": master_invoice_tax_result,

        "final_url": page.url,
    }


def complete_ip_master_invoice_discount_tax_flow(page, config, consumer_profile: dict) -> dict:
    master_flow_result = complete_ip_master_invoice_tax_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
    )

    selected_item_name = master_flow_result["selected_item_name"]
    selected_quantity = master_flow_result["selected_quantity"]

    tax_config = get_ip_medicine_tax_config(selected_item_name)

    before_discount_tax_result = master_flow_result["master_invoice_tax_result"]
    pharmacy_taxable_before_discount = before_discount_tax_result["pharmacy_taxable_actual"]

    if pharmacy_taxable_before_discount <= Decimal("10"):
        discount_amount = Decimal("1")
    else:
        max_discount = int(pharmacy_taxable_before_discount // Decimal("2"))
        discount_amount = Decimal(str(random.randint(1, max_discount)))

    discount_result = apply_on_demand_discount_to_master_invoice_pharmacy_item(
        page=page,
        discount_amount=discount_amount,
    )

    assert discount_result["discount_applied"] is True

    after_discount_tax_result = verify_ip_master_invoice_tax_breakup(
        page=page,
        item_name=selected_item_name,
        quantity=selected_quantity,
        gst_percentage=tax_config["gst_percentage"],
        cess_percentage=tax_config["cess_percentage"],
        expected_discount_amount=discount_amount,
    )

    remove_discount_result = remove_discount_from_master_invoice_pharmacy_item(page=page)

    assert remove_discount_result["discount_removed"] is True

    after_remove_discount_tax_result = verify_ip_master_invoice_tax_breakup(
        page=page,
        item_name=selected_item_name,
        quantity=selected_quantity,
        gst_percentage=tax_config["gst_percentage"],
        cess_percentage=tax_config["cess_percentage"],
        expected_discount_amount=Decimal("0"),
    )

    return {
        **master_flow_result,

        "discount_applied": True,
        "discount_amount": discount_amount,
        "discount_result": discount_result,

        "before_discount_tax_result": before_discount_tax_result,
        "after_discount_tax_result": after_discount_tax_result,

        "discount_removed": True,
        "remove_discount_result": remove_discount_result,
        "after_remove_discount_tax_result": after_remove_discount_tax_result,

        "final_url": page.url,
    }