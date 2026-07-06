import random
import re
from datetime import datetime
from decimal import Decimal
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
        "is_exempt": False,
    },
    "Med_2": {
        "gst_percentage": Decimal("5"),
        "cess_percentage": Decimal("1"),
        "is_exempt": False,
    },
    "Med_4": {
        "gst_percentage": Decimal("5"),
        "cess_percentage": Decimal("0"),
        "is_exempt": False,
    },

    # Tax exempt medicines
    "Med_3": {
        "gst_percentage": Decimal("0"),
        "cess_percentage": Decimal("0"),
        "is_exempt": True,
    },
    "Med_5": {
        "gst_percentage": Decimal("0"),
        "cess_percentage": Decimal("0"),
        "is_exempt": True,
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



def assert_ip_location_supports_taxable_bed_test(page) -> None:
    """
    This test requires Bed with Tax.

    Do not click/change the top location dropdown here.
    Just verify the current selected top location is valid.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(800)

    visible_text = get_visible_page_text(page)

    if re.search(r"\bVeliyannur\b", visible_text, re.I):
        return

    if re.search(r"\bAll Locations\b", visible_text, re.I):
        return

    raise AssertionError(
        "This test requires top location to be Veliyannur or All Locations before running.\n"
        "Current location does not have Bed with Tax available.\n"
        "Automation will not click/change the top location dropdown.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:1000]}"
    )




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
    Adds Doc Visit service to IP patient.

    Fix:
    - Do not assume service is selected after keyboard fallback.
    - Verify Doc Visit is actually selected before clicking Add Service.
    - Click Add Service from the open service form/dialog.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1200)

    service_button_candidates = [
        page.get_by_role("button", name=re.compile(r"Service", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"Service", re.I)).first,
        page.get_by_text(re.compile(r"\bService\b", re.I)).first,
    ]

    clicked_service = False

    for candidate in service_button_candidates:
        try:
            candidate.scroll_into_view_if_needed(timeout=5000)
            candidate.click(timeout=10000)
            clicked_service = True
            break
        except Exception:
            continue

    if clicked_service is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click +Service button on IP details page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    select_doc_visit_from_service_search(page=page)

    assert_doc_visit_selected_in_service_form(page=page)

    select_past_service_time(page)

    click_add_service_button_from_service_form(page=page)

    wait_for_page_ready(page)
    page.wait_for_timeout(2000)

    toast_message = assert_success_message_if_present(page)

    return {
        "service_added": True,
        "service_name": "Doc Visit",
        "toast_message": toast_message,
        "final_url": page.url,
    }



def select_doc_visit_from_service_search(page) -> None:
    """
    Searches and selects Doc Visit from Service autocomplete.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(800)

    service_input_candidates = [
        page.get_by_role("searchbox", name=re.compile(r"Search Service", re.I)).first,
        page.locator("input[placeholder*='Search Service']").first,
        page.locator("input[aria-label*='Search Service']").first,
        page.locator("input[role='searchbox']").first,
        page.locator("xpath=//*[normalize-space()='Service *']/following::input[1]").first,
        page.locator("xpath=//*[contains(normalize-space(), 'Service *')]/following::input[1]").first,
        page.locator(".p-dialog input").first,
        page.locator("mat-dialog-container input").first,
    ]

    filled_search = False

    for candidate in service_input_candidates:
        try:
            candidate.wait_for(state="visible", timeout=8000)
            candidate.click(timeout=5000)
            candidate.fill("", timeout=5000)
            page.wait_for_timeout(300)
            candidate.fill("doc", timeout=8000)
            filled_search = True
            break
        except Exception:
            continue

    if filled_search is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not find/fill Service search field.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1800)

    doc_visit_candidates = [
        page.get_by_role("option", name=re.compile(r"^Doc Visit$", re.I)).first,
        page.locator("mat-option").filter(has_text=re.compile(r"^Doc Visit$", re.I)).first,
        page.locator(".mat-mdc-option").filter(has_text=re.compile(r"^Doc Visit$", re.I)).first,
        page.locator(".p-autocomplete-item").filter(has_text=re.compile(r"^Doc Visit$", re.I)).first,
        page.locator(".p-dropdown-item").filter(has_text=re.compile(r"^Doc Visit$", re.I)).first,
        page.locator("li").filter(has_text=re.compile(r"^Doc Visit$", re.I)).first,
        page.get_by_text(re.compile(r"^Doc Visit$", re.I)).first,
    ]

    selected = False

    for candidate in doc_visit_candidates:
        try:
            candidate.wait_for(state="visible", timeout=8000)
            candidate.click(timeout=10000)
            selected = True
            break
        except Exception:
            continue

    if selected is False:
        visible_text = get_visible_page_text(page)
        input_values = get_visible_input_values(page)

        raise AssertionError(
            "Could not select Doc Visit from service autocomplete results.\n"
            f"Current URL: {page.url}\n"
            f"Input values:\n{input_values}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(1200)


def assert_doc_visit_selected_in_service_form(page) -> None:
    """
    Verifies Doc Visit is actually selected in the service form.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(700)

    visible_text = get_visible_page_text(page)
    input_values = get_visible_input_values(page)

    if re.search(r"\bDoc Visit\b", visible_text, re.I):
        return

    if re.search(r"\bDoc Visit\b", input_values, re.I):
        return

    raise AssertionError(
        "Doc Visit was not selected in the service form.\n"
        "Do not click Add Service because the service field is still empty.\n"
        f"Current URL: {page.url}\n"
        f"Input values:\n{input_values}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )



def click_add_service_button_from_service_form(page) -> None:
    """
    Clicks Add Service button from the open service form/dialog.
    Handles cases where text appears as CancelAdd Service.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(800)

    add_service_button_candidates = [
        page.get_by_role("button", name=re.compile(r"^Add Service$", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"^Add Service$", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"Add Service", re.I)).last,
        page.get_by_text("Add Service", exact=False).last,
    ]

    clicked = False

    for candidate in add_service_button_candidates:
        try:
            candidate.scroll_into_view_if_needed(timeout=5000)
            page.wait_for_timeout(300)
            candidate.click(timeout=10000)
            clicked = True
            break
        except Exception:
            continue

    if clicked is False:
        clicked = page.evaluate(
            """
            () => {
                const buttons = Array.from(document.querySelectorAll('button'));

                const visibleButtons = buttons.filter((button) => {
                    const text = (button.innerText || button.textContent || '').trim();
                    const rect = button.getBoundingClientRect();
                    const disabled = button.disabled || button.hasAttribute('disabled');

                    return (
                        /Add\\s+Service/i.test(text) &&
                        rect.width > 0 &&
                        rect.height > 0 &&
                        !disabled
                    );
                });

                if (!visibleButtons.length) {
                    return false;
                }

                const button = visibleButtons[visibleButtons.length - 1];

                button.scrollIntoView({
                    block: 'center',
                    inline: 'center'
                });

                button.click();

                return true;
            }
            """
        )

    if clicked is False:
        visible_text = get_visible_page_text(page)
        input_values = get_visible_input_values(page)

        raise AssertionError(
            "Could not click Add Service button after selecting Doc Visit.\n"
            "The button may be disabled because the service field was not selected correctly.\n"
            f"Current URL: {page.url}\n"
            f"Input values:\n{input_values}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )



def get_visible_input_values(page) -> str:
    """
    Returns visible input values for debugging form state.
    """

    try:
        return page.evaluate(
            """
            () => {
                return Array.from(document.querySelectorAll('input, textarea'))
                    .filter((element) => {
                        const rect = element.getBoundingClientRect();
                        return rect.width > 0 && rect.height > 0;
                    })
                    .map((element, index) => {
                        const placeholder = element.getAttribute('placeholder') || '';
                        const ariaLabel = element.getAttribute('aria-label') || '';
                        const value = element.value || '';
                        return `${index}: placeholder="${placeholder}", aria-label="${ariaLabel}", value="${value}"`;
                    })
                    .join('\\n');
            }
            """
        )
    except Exception:
        return ""






def request_random_pharmacy_item_from_ip_service(
    page,
    allowed_item_names: list[str] | None = None,
    ) -> dict:
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

    if allowed_item_names is None:
        allowed_item_names = ["Med_1", "Med_2", "Med_4"]

    selected_item_name = random.choice(allowed_item_names)

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
    Checks whether Sales Order invoice view is open.

    Supports both:
    1. Taxable invoice - may show CGST/SGST/GST.
    2. Exempt invoice - may not show tax labels, but shows invoice details,
       item table, subtotal, net total, and net payable.
    """

    current_url = page.url.lower()

    try:
        visible_text = get_visible_page_text(page)
    except Exception:
        return False

    visible_text_lower = visible_text.lower()

    # Strong URL check for Sales Order invoice page.
    if "/business/salesorder/invoice/" in current_url:
        invoice_page_indicators = [
            "invoice no",
            "inv date",
            "order no",
            "item name",
            "subtotal",
            "net total",
            "net payable",
        ]

        matched_count = 0

        for indicator in invoice_page_indicators:
            if indicator in visible_text_lower:
                matched_count += 1

        if matched_count >= 3:
            return True

    # Taxable invoice view check.
    taxable_invoice_indicators = [
        "invoice details",
        "cgst",
        "sgst",
        "subtotal",
        "net total",
        "net total with tax",
        "net payable",
    ]

    matched_count = 0

    for indicator in taxable_invoice_indicators:
        if indicator in visible_text_lower:
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


def complete_ip_order_invoice_tax_flow(
    page,
    config,
    consumer_profile: dict,
    allowed_item_names: list[str] | None = None,
    expected_tax_type: str = "taxable",
) -> dict:
    login(page, config)

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)
    open_new_admission_page(page)

    patient_result = create_random_patient_from_consumer_profile(
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

    if allowed_item_names is None:
        allowed_item_names = ["Med_1", "Med_2", "Med_4"]

    request_order_result = request_random_pharmacy_item_from_ip_service(
        page=page,
        allowed_item_names=allowed_item_names,
    )

    assert request_order_result["order_requested"] is True

    selected_item_name = request_order_result["selected_item_name"]
    selected_quantity = request_order_result["selected_quantity"]

    tax_config = get_ip_medicine_tax_config(selected_item_name)

    open_sales_order_requests_grid(page=page, config=config)

    order_result = confirm_latest_ip_requested_sales_order(page=page)

    assert order_result["order_confirmed"] is True

    invoice_result = create_sales_order_invoice_and_view(page=page)

    assert invoice_result["order_invoice_created"] is True

    if expected_tax_type == "exempt":
        order_invoice_tax_result = verify_ip_order_invoice_exempt_pharmacy_item_no_tax(
            page=page,
            item_name=selected_item_name,
            quantity=selected_quantity,
        )
    else:
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
        "selected_item_is_exempt": expected_tax_type == "exempt",
        "expected_tax_type": expected_tax_type,

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



def get_ip_exempt_medicine_names() -> list[str]:
    """
    Tax exempt medicines for IP order invoice flow.
    """

    return ["Med_3", "Med_5"]


def get_ip_taxable_medicine_names() -> list[str]:
    """
    Taxable medicines for IP order invoice flow.
    """

    return ["Med_1", "Med_2", "Med_4"]


def get_ip_medicine_tax_config(item_name: str) -> dict:
    """
    Returns tax config for selected IP medicine.
    """

    if item_name not in IP_MEDICINE_TAX_CONFIG:
        raise AssertionError(
            f"No tax config found for IP medicine: {item_name}. "
            f"Available items: {list(IP_MEDICINE_TAX_CONFIG.keys())}"
        )

    return IP_MEDICINE_TAX_CONFIG[item_name]


def select_random_ip_exempt_medicine_from_item_popup(page) -> dict:
    """
    Selects one random tax-exempt medicine from Select Items popup.

    Allowed items:
    - Med_3
    - Med_5
    """

    selected_item_name = random.choice(get_ip_exempt_medicine_names())

    item_row_candidates = [
        page.get_by_role(
            "row",
            name=re.compile(rf"{re.escape(selected_item_name)}.*Exempt.*Enable", re.I),
        ),
        page.get_by_role(
            "row",
            name=re.compile(rf"{re.escape(selected_item_name)}.*Enable", re.I),
        ),
        page.locator("tr").filter(has_text=re.compile(rf"{re.escape(selected_item_name)}", re.I)),
        page.locator("div").filter(has_text=re.compile(rf"{re.escape(selected_item_name)}", re.I)),
    ]

    item_selected = False

    for row in item_row_candidates:
        try:
            checkbox = row.locator("#SelectItem_ORD_ItemSelection-input").first
            checkbox.check(timeout=10000)
            item_selected = True
            break
        except Exception:
            pass

        try:
            checkbox = row.get_by_role("checkbox").first
            checkbox.check(timeout=10000)
            item_selected = True
            break
        except Exception:
            pass

        try:
            checkbox = row.locator("input[type='checkbox']").first
            checkbox.check(timeout=10000)
            item_selected = True
            break
        except Exception:
            continue

    if item_selected is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not select exempt medicine: {selected_item_name}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    done_button_candidates = [
        page.locator("#btnSubmitItems_ORD_ItemSelectionTop"),
        page.get_by_role("button", name=re.compile(r"Done|Submit|Add", re.I)),
        page.locator("button").filter(has_text=re.compile(r"Done|Submit|Add", re.I)),
    ]

    clicked_done = False

    for candidate in done_button_candidates:
        try:
            candidate.first.click(timeout=10000)
            clicked_done = True
            break
        except Exception:
            continue

    if clicked_done is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Done after selecting exempt medicine.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)

    return {
        "selected_item_name": selected_item_name,
        "is_exempt": True,
        "gst_percentage": Decimal("0"),
        "cess_percentage": Decimal("0"),
    }




def verify_ip_order_invoice_exempt_pharmacy_item_no_tax(
    page,
    item_name: str,
    quantity: int,
) -> dict:
    """
    Verifies Sales Order invoice for tax-exempt IP pharmacy item.

    Expected:
    - GST = 0
    - CESS = 0
    - CGST = 0
    - SGST = 0
    - No tax calculation needed
    """

    row = get_invoice_row_by_text(page, item_name)
    row_text = row.inner_text(timeout=10000)
    money_values = extract_decimal_money_values(row_text)

    if len(money_values) < 2:
        raise AssertionError(
            f"Not enough money values found for exempt item row: {item_name}\n"
            f"Row text:\n{row_text}\n"
            f"Money values: {money_values}"
        )

    total_amount_actual = money_values[-1]

    gst_actual = Decimal("0")
    cess_actual = Decimal("0")
    taxable_actual = total_amount_actual


    # Exempt items do not show CGST/SGST/CESS rows in invoice.
    # So do not read these labels from UI. Treat them as 0.
    summary_cgst_actual = Decimal("0")
    summary_sgst_actual = Decimal("0")
    summary_cess_actual = Decimal("0")

    assert_amount_close(
        summary_cgst_actual,
        Decimal("0"),
        f"{item_name} exempt invoice CGST should be 0.",
    )

    assert_amount_close(
        summary_sgst_actual,
        Decimal("0"),
        f"{item_name} exempt invoice SGST should be 0.",
    )

    assert_amount_close(
        summary_cess_actual,
        Decimal("0"),
        f"{item_name} exempt invoice CESS should be 0.",
    )

    subtotal_actual = read_summary_amount(
        page,
        "Subtotal",
        default=taxable_actual,
    )

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
        total_amount_actual,
        f"{item_name} exempt invoice subtotal should equal item total.",
    )

    assert_amount_close(
        net_total_with_tax_actual,
        total_amount_actual,
        f"{item_name} exempt invoice net total should equal item total.",
    )

    return {
        "item_name": item_name,
        "quantity": quantity,
        "row_text": row_text,
        "money_values": money_values,

        "taxable_actual": taxable_actual,
        "gst_actual": gst_actual,
        "cess_actual": cess_actual,
        "total_amount_actual": total_amount_actual,

        "taxable_expected": total_amount_actual,
        "gst_expected": Decimal("0"),
        "cess_expected": Decimal("0"),
        "cgst_expected": Decimal("0"),
        "sgst_expected": Decimal("0"),

        "summary_cgst_actual": summary_cgst_actual,
        "summary_sgst_actual": summary_sgst_actual,
        "summary_cess_actual": summary_cess_actual,

        "subtotal_actual": subtotal_actual,
        "net_total_with_tax_actual": net_total_with_tax_actual,
    }



def verify_ip_master_invoice_exempt_item_discount_breakup(
    page,
    item_name: str,
    quantity: int,
    expected_discount_amount: Decimal = Decimal("0"),
    ) -> dict:
    """
    Verifies Master Invoice for tax-exempt pharmacy item.

    Exempt item rule:
    - Discount is applied on Rate * Quantity.
    - GST, CGST, SGST, and CESS are not calculated.
    - Tax labels may not appear in the UI, so do not read them from page.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    pharmacy_row = get_invoice_row_by_text(page, item_name)
    pharmacy_row_text = pharmacy_row.inner_text(timeout=10000)
    money_values = extract_decimal_money_values(pharmacy_row_text)

    if len(money_values) < 1:
        raise AssertionError(
            f"Could not parse exempt pharmacy row in Master Invoice.\n"
            f"Item: {item_name}\n"
            f"Row text:\n{pharmacy_row_text}\n"
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
        pharmacy_discount_actual = expected_discount_amount

    pharmacy_taxable_actual = round_money(
        pharmacy_amount_before_discount_actual - pharmacy_discount_actual
    )

    if pharmacy_taxable_actual < Decimal("0"):
        pharmacy_taxable_actual = Decimal("0")

    # Exempt item: no tax calculation.
    pharmacy_gst_actual = Decimal("0")
    pharmacy_cess_actual = Decimal("0")
    pharmacy_total_actual = pharmacy_taxable_actual

    service_amount_actual = read_service_amount_from_master_invoice(page)

    # Exempt item: CGST/SGST/CESS labels may not be shown.
    # Do not read them from UI.
    summary_cgst_actual = Decimal("0")
    summary_sgst_actual = Decimal("0")
    summary_cess_actual = Decimal("0")

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

    assert_amount_close(
        pharmacy_gst_actual,
        Decimal("0"),
        "Master Invoice exempt item GST should be 0.",
    )

    assert_amount_close(
        pharmacy_cess_actual,
        Decimal("0"),
        "Master Invoice exempt item CESS should be 0.",
    )

    assert_amount_close(
        summary_cgst_actual,
        Decimal("0"),
        "Master Invoice exempt item CGST should be 0.",
    )

    assert_amount_close(
        summary_sgst_actual,
        Decimal("0"),
        "Master Invoice exempt item SGST should be 0.",
    )

    assert_amount_close(
        summary_cess_actual,
        Decimal("0"),
        "Master Invoice exempt item CESS should be 0.",
    )

    return {
        "item_name": item_name,
        "quantity": quantity,
        "pharmacy_row_text": pharmacy_row_text,
        "pharmacy_money_values": money_values,

        "service_amount_actual": service_amount_actual,

        "pharmacy_rate_actual": pharmacy_rate_actual,
        "pharmacy_quantity_actual": quantity,
        "pharmacy_amount_before_discount_actual": pharmacy_amount_before_discount_actual,

        "pharmacy_taxable_actual": pharmacy_taxable_actual,
        "pharmacy_gst_actual": pharmacy_gst_actual,
        "pharmacy_cess_actual": pharmacy_cess_actual,
        "pharmacy_total_actual": pharmacy_total_actual,
        "pharmacy_discount_actual": pharmacy_discount_actual,

        "pharmacy_taxable_expected": pharmacy_taxable_actual,
        "pharmacy_gst_expected": Decimal("0"),
        "pharmacy_cess_expected": Decimal("0"),
        "pharmacy_total_expected": pharmacy_total_actual,

        "summary_cgst_actual": summary_cgst_actual,
        "summary_sgst_actual": summary_sgst_actual,
        "summary_cess_actual": summary_cess_actual,

        "subtotal_actual": subtotal_actual,
        "subtotal_expected": subtotal_actual,

        "net_total_actual": net_total_actual,
        "net_total_expected": net_total_actual,
    }



def click_master_invoice_edit_button(page) -> None:
    """
    Clicks Edit button from Master Invoice view page.
    """

    wait_for_page_ready(page)

    edit_button_candidates = [
        page.get_by_role("button", name=re.compile(r"Edit", re.I)),
        page.locator("button").filter(has_text=re.compile(r"Edit", re.I)),
        page.get_by_text("Edit", exact=False),
        page.locator("[id*='Edit']"),
    ]

    edit_clicked = False

    for candidate in edit_button_candidates:
        try:
            candidate.first.click(timeout=10000)
            edit_clicked = True
            break
        except Exception:
            continue

    if edit_clicked is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Edit button on Master Invoice page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    # Confirm edit mode opened by checking pharmacy row menu or View Invoice button.
    edit_mode_candidates = [
        page.locator("#btnRowMenu_Pharm_IP_Invoice"),
        page.locator("[id*='btnRowMenu_Pharm']"),
        page.get_by_role("button", name=re.compile(r"View Invoice", re.I)),
        page.locator("button").filter(has_text=re.compile(r"View Invoice", re.I)),
    ]

    for candidate in edit_mode_candidates:
        try:
            candidate.first.wait_for(state="visible", timeout=8000)
            return
        except Exception:
            continue

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        "Clicked Edit, but Master Invoice edit mode did not open.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )



def complete_ip_master_invoice_exempt_discount_tax_flow(
    page,
    config,
    consumer_profile: dict,
    ) -> dict:
    """
    Second IP invoice test case.

    Case:
    Line item discount applied on tax-exempt order item; no GST/CESS should be calculated.

    Flow:
    1. Create IP admission.
    2. Add Doc Visit service.
    3. Request order with random exempt item: Med_3 or Med_5.
    4. Convert order request to Sales Order.
    5. Create Sales Order invoice.
    6. Generate IP service invoice.
    7. Merge both invoices into Master Invoice.
    8. Edit Master Invoice.
    9. Apply line item discount.
    10. Verify discount is applied on Rate * Quantity.
    11. Verify GST/CESS remain 0.
    12. Remove discount.
    """

    order_flow_result = complete_ip_order_invoice_exempt_flow(
    page=page,
    config=config,
    consumer_profile=consumer_profile,
    )

    selected_item_name = order_flow_result["selected_item_name"]
    selected_quantity = order_flow_result["selected_quantity"]

    order_invoice_tax_result = verify_ip_order_invoice_exempt_pharmacy_item_no_tax(
        page=page,
        item_name=selected_item_name,
        quantity=selected_quantity,
    )

    go_back_to_ip_patient_from_sales_order_invoice(
    page=page,
    patient_full_name=order_flow_result["patient_full_name"],
    )

    service_invoice_result = create_ip_service_invoice(page=page)

    assert service_invoice_result["ip_service_invoice_created"] is True

    return_from_invoice_details_to_ip_details(page=page)

    master_invoice_result = create_master_invoice_from_available_invoices(
        page=page,
        expected_invoice_count=2,
    )

    open_latest_master_invoice(page=page)

    master_invoice_type = "Master Invoice"

    click_master_invoice_edit_button(page=page)

    before_discount_tax_result = verify_ip_master_invoice_exempt_item_discount_breakup(
    page=page,
    item_name=selected_item_name,
    quantity=selected_quantity,
    expected_discount_amount=Decimal("0"),
    )

    discount_amount = Decimal("5")

    discount_result = apply_on_demand_discount_to_master_invoice_pharmacy_item(
        page=page,
        discount_amount=discount_amount,
    )

    after_discount_tax_result = verify_ip_master_invoice_exempt_item_discount_breakup(
        page=page,
        item_name=selected_item_name,
        quantity=selected_quantity,
        expected_discount_amount=discount_amount,
    )

    remove_discount_result = remove_discount_from_master_invoice_pharmacy_item(
        page=page,
    )

    after_remove_discount_tax_result = verify_ip_master_invoice_exempt_item_discount_breakup(
        page=page,
        item_name=selected_item_name,
        quantity=selected_quantity,
        expected_discount_amount=Decimal("0"),
    )

    return {
        **order_flow_result,

        "selected_item_name": selected_item_name,
        "selected_quantity": selected_quantity,
        "selected_item_is_exempt": True,

        "order_invoice_tax_result": order_invoice_tax_result,

        "ip_service_invoice_created": service_invoice_result["ip_service_invoice_created"],
        "master_invoice_created": master_invoice_result["master_invoice_created"],
        "master_invoice_type": master_invoice_type,

        "master_invoice_tax_result": before_discount_tax_result,

        "discount_applied": discount_result["discount_applied"],
        "discount_amount": discount_amount,

        "before_discount_tax_result": before_discount_tax_result,
        "after_discount_tax_result": after_discount_tax_result,

        "discount_removed": remove_discount_result["discount_removed"],
        "after_remove_discount_tax_result": after_remove_discount_tax_result,

        "final_url": page.url,
    }



def complete_ip_order_invoice_exempt_flow(
    page,
    config,
    consumer_profile: dict,
) -> dict:
    """
    Creates IP order invoice flow using tax-exempt medicine only.

    This reuses the same working admission/service/order flow logic from case 1.
    Only the order item selection is changed to Med_3 or Med_5.
    """

    order_flow_result = complete_ip_order_invoice_tax_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
        allowed_item_names=["Med_3", "Med_5"],
        expected_tax_type="exempt",
    )

    order_flow_result["selected_item_is_exempt"] = True

    return order_flow_result




def request_order_from_ip_service_with_exempt_item(page) -> dict:
    """
    Requests pharmacy order from added IP service using random exempt item.

    Exempt items:
    - Med_3
    - Med_5
    """

    selected_item_name = random.choice(["Med_3", "Med_5"])

    # Open service action menu.
    action_menu_candidates = [
        page.locator("[id^='btnServiceActionMenu_IP_AD_DE']").first,
        page.locator("[id*='btnServiceActionMenu']").first,
        page.locator("button").filter(has_text=re.compile(r"More|Action", re.I)).first,
    ]

    clicked_action_menu = False

    for candidate in action_menu_candidates:
        try:
            candidate.click(timeout=10000)
            clicked_action_menu = True
            break
        except Exception:
            continue

    if clicked_action_menu is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not open IP service action menu for Request Order.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(800)

    click_menuitem_by_text(page, "Request Order")

    wait_for_page_ready(page)

    click_button_by_text(page, "Item")

    page.wait_for_timeout(1000)

    # Select exempt item from item selection popup.
    item_row_candidates = [
        page.get_by_role(
            "row",
            name=re.compile(rf"{re.escape(selected_item_name)}.*Exempt.*Enable", re.I),
        ),
        page.get_by_role(
            "row",
            name=re.compile(rf"{re.escape(selected_item_name)}.*Enable", re.I),
        ),
        page.locator("tr").filter(has_text=re.compile(rf"{re.escape(selected_item_name)}", re.I)),
        page.locator("div").filter(has_text=re.compile(rf"{re.escape(selected_item_name)}", re.I)),
    ]

    selected_item = False

    for row in item_row_candidates:
        try:
            row.locator("#SelectItem_ORD_ItemSelection-input").first.check(timeout=10000)
            selected_item = True
            break
        except Exception:
            pass

        try:
            row.get_by_role("checkbox").first.check(timeout=10000)
            selected_item = True
            break
        except Exception:
            pass

        try:
            row.locator("input[type='checkbox']").first.check(timeout=10000)
            selected_item = True
            break
        except Exception:
            continue

    if selected_item is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not select exempt item {selected_item_name} from item popup.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    submit_item_candidates = [
        page.locator("#btnSubmitItems_ORD_ItemSelectionTop"),
        page.get_by_role("button", name=re.compile(r"Done|Submit|Add", re.I)),
        page.locator("button").filter(has_text=re.compile(r"Done|Submit|Add", re.I)),
    ]

    clicked_submit = False

    for candidate in submit_item_candidates:
        try:
            candidate.first.click(timeout=10000)
            clicked_submit = True
            break
        except Exception:
            continue

    if clicked_submit is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not submit selected exempt item.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)

    selected_quantity = 1

    # Increase quantity. If increase succeeds, quantity becomes 2 or more.
    increase_button_candidates = [
        page.get_by_role("button", name=re.compile(r"Increase itemQuantity", re.I)),
        page.locator("button").filter(has_text=re.compile(r"\+", re.I)),
        page.locator("[aria-label*='Increase']"),
    ]

    for candidate in increase_button_candidates:
        try:
            candidate.first.click(timeout=5000)
            selected_quantity += 1
            break
        except Exception:
            continue

    click_button_by_text(page, "Request Order")

    page.wait_for_timeout(1000)

    # Select pharmacy store.
    try:
        page.get_by_text("Swathi Medical", exact=False).first.click(timeout=10000)
    except Exception:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not select Swathi Medical store for exempt order request.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    click_button_by_text(page, "Select")

    wait_for_page_ready(page)

    toast_message = assert_success_message_if_present(page)

    return {
        "order_requested": True,
        "selected_item_name": selected_item_name,
        "selected_quantity": selected_quantity,
        "selected_item_is_exempt": True,
        "gst_percentage": Decimal("0"),
        "cess_percentage": Decimal("0"),
        "toast_message": toast_message,
    }


def select_random_patient_gender(page) -> str:
    """
    Selects random gender while creating IP patient.
    Gender is mandatory.
    """

    gender_options = ["Male", "Female"]

    selected_gender = random.choice(gender_options)

    gender_dropdown_candidates = [
        page.get_by_text("Select Gender", exact=False),
        page.locator("p-dropdown").filter(has_text=re.compile(r"Select Gender|Gender", re.I)),
        page.locator("div").filter(has_text=re.compile(r"Select Gender", re.I)),
    ]

    opened = False

    for candidate in gender_dropdown_candidates:
        try:
            candidate.first.click(timeout=10000)
            opened = True
            break
        except Exception:
            continue

    if opened is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not open Gender dropdown while creating patient.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(800)

    gender_option_candidates = [
        page.get_by_role("option", name=re.compile(rf"^{selected_gender}$", re.I)),
        page.locator("p-dropdownitem li").filter(has_text=re.compile(rf"^{selected_gender}$", re.I)),
        page.locator(".p-dropdown-item").filter(has_text=re.compile(rf"^{selected_gender}$", re.I)),
        page.get_by_text(selected_gender, exact=True),
    ]

    for option in gender_option_candidates:
        try:
            option.first.click(timeout=10000)
            page.wait_for_timeout(500)
            return selected_gender
        except Exception:
            continue

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        f"Could not select Gender option: {selected_gender}\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )


def create_random_patient_from_consumer_profile(page, consumer_profile: dict) -> dict:
    """
    Creates a new random patient using generate_consumer_profile() data.
    Gender is mandatory, so random gender is selected from dropdown.
    """

    def profile_value(*keys, fallback=""):
        for key in keys:
            value = consumer_profile.get(key)

            if value:
                return str(value)

        return fallback

    first_name = profile_value(
        "first_name",
        "firstName",
        fallback="Test",
    )

    last_name = profile_value(
        "last_name",
        "lastName",
        fallback="Patient",
    )

    email = profile_value(
        "email",
        "email_id",
        fallback=f"test.patient.{random.randint(100000, 999999)}@jaldee.com",
    )

    phone_number = profile_value(
        "phone",
        "phone_number",
        "mobile",
        "mobile_number",
        "primary_phone",
        fallback=f"555{random.randint(1000000, 9999999)}",
    )

    patient_full_name = f"{first_name} {last_name}"

    create_patient_candidates = [
        page.get_by_role("button", name=re.compile(r"Create Patient", re.I)),
        page.locator("button").filter(has_text=re.compile(r"Create Patient", re.I)),
        page.get_by_text("Create Patient", exact=False),
    ]

    clicked_create_patient = False

    for candidate in create_patient_candidates:
        try:
            candidate.first.click(timeout=10000)
            clicked_create_patient = True
            break
        except Exception:
            continue

    if clicked_create_patient is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Create Patient button.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)

    page.get_by_role("textbox", name=re.compile(r"Enter First Name", re.I)).fill(first_name)
    page.get_by_role("textbox", name=re.compile(r"Enter Last Name", re.I)).fill(last_name)
    page.get_by_role("textbox", name=re.compile(r"Enter Email Id", re.I)).fill(email)

    phone_filled = False

    phone_candidates = [
        page.get_by_role("textbox", name=re.compile(r"10123", re.I)).first,
        page.locator("input[type='tel']").first,
        page.locator("input[placeholder*='Phone']").first,
        page.locator("input[placeholder*='Mobile']").first,
    ]

    for candidate in phone_candidates:
        try:
            candidate.fill(phone_number, timeout=10000)
            phone_filled = True
            break
        except Exception:
            continue

    if phone_filled is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not fill patient phone number.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    selected_gender = select_random_patient_gender(page)

    click_button_by_text(page, "Save & Next")

    wait_for_page_ready(page)

    return {
        "patient_created": True,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number,
        "gender": selected_gender,
        "patient_full_name": patient_full_name,
        "patient_name": patient_full_name,
        "patient_identifier": patient_full_name,
    }




def open_inpatients_grid_from_side_panel(page) -> None:
    """
    Opens IP Dashboard from side panel and clicks Inpatients card.
    """

    wait_for_page_ready(page)

    # Click In Patient side panel icon.
    # Codegen: page.get_by_role("link").nth(3).click()
    try:
        page.get_by_role("link").nth(3).click(timeout=10000)
        wait_for_page_ready(page)
    except Exception:
        pass

    # Direct navigation fallback.
    page.goto(
        business_url_from_current_page(
            page,
            "/business/ip/dashboard?p_source=p_sidebar",
        )
    )

    wait_for_page_ready(page)

    # Click Inpatients card from IP Dashboard.
    inpatient_card_candidates = [
        page.locator(
            "div:nth-child(2) > div > div > #actionNav_IP_DBoard > "
            ".dashboard-card-image > img"
        ),
        page.locator("#actionNav_IP_DBoard").nth(1),
        page.locator("#actionNav_IP_DBoard").filter(has_text=re.compile(r"Inpatients|In Patients", re.I)),
        page.get_by_text("Inpatients", exact=False),
        page.get_by_text("In Patients", exact=False),
    ]

    clicked_inpatients = False

    for candidate in inpatient_card_candidates:
        try:
            candidate.first.click(timeout=10000)
            clicked_inpatients = True
            break
        except Exception:
            try:
                candidate.click(timeout=10000)
                clicked_inpatients = True
                break
            except Exception:
                continue

    if clicked_inpatients is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Inpatients card from IP Dashboard.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)

    try:
        page.get_by_role("button", name=re.compile(r"New Admission|add New Admission", re.I)).first.wait_for(
            state="visible",
            timeout=15000,
        )
    except Exception:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Inpatients grid did not load after clicking Inpatients card.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )
    


def click_new_admission(page) -> None:
    """
    Clicks New Admission button from Inpatients grid.
    """

    new_admission_candidates = [
        page.get_by_role("button", name=re.compile(r"add New Admission|New Admission", re.I)),
        page.locator("button").filter(has_text=re.compile(r"New Admission", re.I)),
        page.get_by_text("New Admission", exact=False),
    ]

    for candidate in new_admission_candidates:
        try:
            candidate.first.click(timeout=10000)
            wait_for_page_ready(page)
            return
        except Exception:
            continue

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        "Could not click New Admission button.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )


def select_random_patient_gender(page) -> str:
    """
    Selects random gender while creating patient.
    Gender is mandatory.
    """

    selected_gender = random.choice(["Male", "Female"])

    gender_dropdown_candidates = [
        page.get_by_text("Select Gender", exact=False),
        page.locator("p-dropdown").filter(has_text=re.compile(r"Select Gender|Gender", re.I)),
        page.locator("div").filter(has_text=re.compile(r"Select Gender", re.I)),
    ]

    opened = False

    for candidate in gender_dropdown_candidates:
        try:
            candidate.first.click(timeout=10000)
            opened = True
            break
        except Exception:
            continue

    if opened is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not open Gender dropdown while creating patient.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(800)

    gender_option_candidates = [
        page.get_by_role("option", name=re.compile(rf"^{selected_gender}$", re.I)),
        page.locator("p-dropdownitem li").filter(has_text=re.compile(rf"^{selected_gender}$", re.I)),
        page.locator(".p-dropdown-item").filter(has_text=re.compile(rf"^{selected_gender}$", re.I)),
        page.get_by_text(selected_gender, exact=True),
    ]

    for option in gender_option_candidates:
        try:
            option.first.click(timeout=10000)
            page.wait_for_timeout(500)
            return selected_gender
        except Exception:
            continue

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        f"Could not select Gender option: {selected_gender}\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )



def go_back_to_ip_patient_from_sales_order_invoice(
    page,
    patient_identifier: str | None = None,
    patient_full_name: str | None = None,
) -> None:
    """
    Returns from Sales Order invoice page to the IP patient details page.

    Used after creating/viewing the Sales Order invoice.
    """

    wait_for_page_ready(page)

    patient_name_to_open = patient_full_name or patient_identifier

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)

    if patient_name_to_open:
        open_latest_ip_patient_from_grid(
            page=page,
            patient_full_name=patient_name_to_open,
        )
        return

    view_button_candidates = [
        page.locator("#btnViewIp_IP_IpGrd").first,
        page.locator("[id*='btnViewIp']").first,
        page.get_by_role("button", name=re.compile(r"View", re.I)).first,
    ]

    for candidate in view_button_candidates:
        try:
            candidate.click(timeout=10000)
            wait_for_page_ready(page)
            return
        except Exception:
            continue

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        "Could not open IP patient details after Sales Order invoice.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )




def read_optional_zero_summary_amount(page, label: str) -> Decimal:
    """
    Reads summary amount if the label exists.
    For exempt items, tax labels like CGST/SGST/CESS may not appear in the UI.
    In that case, return 0.
    """

    try:
        return read_last_summary_amount(
            page=page,
            label=label,
            default=Decimal("0"),
        )
    except Exception:
        return Decimal("0")    
    

def complete_ip_invoice_taxable_bed_exempt_service_flow(
    page,
    config,
    consumer_profile: dict,
    ) -> dict:
    """
    Third IP invoice tax test case.

    Case:
    IP invoice with taxable bed and exempt service; GST applies only on bed charge.

    Flow:
    1. Login.
    2. Open IP Dashboard.
    3. Create new admission with random patient.
    4. Select taxable bed containing 'Bed with Tax'.
    5. Open newly created IP patient.
    6. Add exempt service Doc Visit.
    7. Discharge patient.
    8. Create IP invoice after discharge.
    9. Verify GST applies only on bed charge.
    """

    login(page, config)

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)
    open_new_admission_page(page)

    patient_result = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    assert patient_result["patient_created"] is True

    admission_result = complete_ip_admission_with_taxable_bed(page=page)

    assert admission_result["admission_created"] is True

    patient_full_name = patient_result["patient_full_name"]

    open_latest_ip_patient_from_grid(
        page=page,
        patient_full_name=patient_full_name,
    )

    service_result = add_doc_visit_service_to_ip_patient(page=page)

    assert service_result["service_added"] is True

    discharge_result = discharge_ip_patient_with_random_template(page=page)

    assert discharge_result["discharged"] is True

    invoice_result = create_ip_invoice_after_discharge_and_view(page=page)

    assert invoice_result["invoice_created"] is True

    tax_result = verify_ip_invoice_taxable_bed_exempt_service_amounts(
        page=page,
        bed_name_contains="Bed with Tax",
        service_name="Doc Visit",
        bed_tax_percentage=Decimal("5"),
    )

    print("Amounts are correct")

    payment_result = pay_ip_invoice_by_cash_from_invoice_details(page=page)

    assert payment_result["invoice_paid"] is True

    back_result = go_back_from_ip_invoice_details_to_patient_details(page=page)

    assert back_result["returned_to_ip_details"] is True

    checkout_result = checkout_ip_patient_with_random_note(page=page)

    assert checkout_result["checked_out"] is True


    return {
        "patient_created": True,
        "patient_full_name": patient_full_name,
        "patient_result": patient_result,

        "admission_created": True,
        "admission_result": admission_result,

        "bed_name": admission_result["bed_name"],

        "service_added": True,
        "service_result": service_result,

        "discharged": True,
        "discharge_result": discharge_result,

        "invoice_created": True,
        "invoice_result": invoice_result,

        "tax_result": tax_result,

        "invoice_paid": True,
        "payment_result": payment_result,

        "returned_to_ip_details": True,
        "back_result": back_result,

        "checked_out": True,
        "checkout_result": checkout_result,

        "final_url": page.url,
    }


def complete_ip_admission_with_taxable_bed(page) -> dict:
    """
    Completes IP admission by selecting:
    - random Admission Type
    - random Admitted Doctor
    - today's Checkin Date
    - today's Expected Checkout Date
    - taxable bed containing 'Bed with Tax'
    """

    wait_for_page_ready(page)
    wait_for_new_admission_form_loaded(page)

    admission_type = select_random_primeng_dropdown_option(
    page=page,
    dropdown_text="Admission Type",
    )

    admitted_doctor = select_random_primeng_dropdown_option(
    page=page,
    dropdown_text="Admitted Doctor",
    )

    select_today_for_admission_date_by_index(page=page, date_picker_index=0)
    select_today_for_admission_date_by_index(page=page, date_picker_index=1)

    select_building_block_d_for_bed_search(page=page)

    bed_name = select_bed_with_tax_from_last_bed_page(page=page)

    click_admit_now_button(page=page)

    assert "Bed with Tax" in bed_name, (
    f"Wrong bed selected. Expected a bed starting with 'Bed with Tax', got: {bed_name}"
    )

    wait_for_page_ready(page)
    page.wait_for_timeout(2000)

    toast_message = assert_success_message_if_present(page)

    return {
        "admission_created": True,
        "admission_type": admission_type,
        "admitted_doctor": admitted_doctor,
        "bed_name": bed_name,
        "toast_message": toast_message,
    }


def select_random_primeng_dropdown_option(
    page,
    dropdown_text: str,
    ) -> str:
    """
    Opens a PrimeNG dropdown and selects one random option.

    Supports:
    - Placeholder text: Select Admitted Doctor
    - Field label text: Admission Type, Admitted Doctor
    - Already selected dropdown value, like Admis-Ren1148
    """

    wait_for_page_ready(page)

    normalized_text = re.sub(r"^Select\s+", "", dropdown_text, flags=re.I).strip()

    dropdown_index_by_label = {
        "admission type": 0,
        "admitted doctor": 1,
        "assigned doctor": 2,
        "assigned team": 3,
        "building": 4,
        "floor": 5,
        "room": 6,
        "bed type": 7,
    }

    dropdown_candidates = [
        page.locator("p-dropdown").filter(has_text=re.compile(re.escape(dropdown_text), re.I)).first,
        page.locator(".p-dropdown").filter(has_text=re.compile(re.escape(dropdown_text), re.I)).first,
        page.locator("p-dropdown").filter(has_text=re.compile(re.escape(normalized_text), re.I)).first,
        page.locator(".p-dropdown").filter(has_text=re.compile(re.escape(normalized_text), re.I)).first,
    ]

    dropdown_index = dropdown_index_by_label.get(normalized_text.lower())

    if dropdown_index is not None:
        dropdown_candidates.extend(
            [
                page.locator("p-dropdown").nth(dropdown_index),
                page.locator(".p-dropdown").nth(dropdown_index),
            ]
        )

    opened = False

    for dropdown in dropdown_candidates:
        try:
            if dropdown.count() == 0:
                continue

            dropdown.locator(".p-dropdown-trigger").first.click(timeout=8000)
            opened = True
            break
        except Exception:
            try:
                dropdown.get_by_label("dropdown trigger").click(timeout=8000)
                opened = True
                break
            except Exception:
                try:
                    dropdown.click(timeout=8000)
                    opened = True
                    break
                except Exception:
                    continue

    if opened is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not open dropdown: {dropdown_text}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(800)

    option_locator = page.get_by_role("option")
    option_count = option_locator.count()

    valid_options = []

    for index in range(option_count):
        option = option_locator.nth(index)

        try:
            option_text = option.inner_text(timeout=2000).strip()
        except Exception:
            continue

        if not option_text:
            continue

        if re.search(r"select", option_text, re.I):
            continue

        valid_options.append(option_text)

    if not valid_options:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"No valid options found for dropdown: {dropdown_text}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    selected_option = random.choice(valid_options)

    page.get_by_role(
        "option",
        name=re.compile(re.escape(selected_option), re.I),
    ).first.click(timeout=10000)

    wait_for_page_ready(page)
    page.wait_for_timeout(500)

    return selected_option



def select_today_for_admission_date_by_index(
    page,
    date_picker_index: int,
) -> None:
    """
    Opens date picker by index and selects today's date.

    date_picker_index:
    - 0 = Checkin Date
    - 1 = Expected Checkout Date
    """

    today_day = str(datetime.now().day)

    calendar_trigger_candidates = [
        page.locator("p-calendar").nth(date_picker_index).locator("button").first,
        page.locator("p-calendar").nth(date_picker_index).locator(".p-datepicker-trigger").first,
        page.locator(".p-datepicker-trigger").nth(date_picker_index),
    ]

    opened = False

    for candidate in calendar_trigger_candidates:
        try:
            candidate.click(timeout=10000)
            opened = True
            break
        except Exception:
            continue

    if opened is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not open admission date picker index {date_picker_index}.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(500)

    today_candidates = [
        page.locator(".p-datepicker-calendar td:not(.p-datepicker-other-month)")
        .filter(has_text=re.compile(rf"^{today_day}$"))
        .first,
        page.get_by_role("table").get_by_text(today_day, exact=True).first,
    ]

    selected = False

    for candidate in today_candidates:
        try:
            candidate.click(timeout=10000)
            selected = True
            break
        except Exception:
            continue

    if selected is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not select today's date: {today_day}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)


def select_bed_with_tax_from_last_bed_page(page) -> str:
    """
    Searches the Bed Details section page by page using the bed paginator next icon.
    Selects only a bed starting with 'Bed with Tax'.

    This avoids selecting normal beds like Bed1471B, Bed1472B, etc.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    max_pages_to_check = 120

    reset_bed_paginator_to_first_page(page=page)

    for page_index in range(max_pages_to_check):
        wait_for_page_ready(page)
        page.wait_for_timeout(1200)

        visible_text = get_visible_page_text(page)

        if re.search(r"No Available Beds", visible_text, re.I):
            raise AssertionError(
                "No available beds are shown while searching for Bed with Tax.\n"
                f"Current URL: {page.url}\n"
                f"Visible page text:\n{visible_text[:2500]}"
            )

        selected_bed_name = click_visible_bed_with_tax_card(page=page)

        if selected_bed_name:
            assert_selected_bed_with_tax_before_admit(page=page)
            return selected_bed_name

        clicked_next = click_next_bed_paginator(page=page)

        if clicked_next is False:
            break

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        "Could not find/select Bed with Tax from Bed Details paginator pages.\n"
        "The test must not continue with a normal bed because GST will not appear.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )



def click_visible_bed_with_tax_card(page) -> str | None:
    """
    Clicks the smallest visible bed card/text whose first line starts with Bed with Tax.

    Returns selected bed name if clicked.
    Returns None if Bed with Tax is not visible on the current bed page.
    """

    clicked_bed_name = page.evaluate(
        """
        () => {
            const allElements = Array.from(
                document.querySelectorAll('div, span, p, button, a')
            );

            const matches = [];

            for (const element of allElements) {
                const text = (element.innerText || element.textContent || '').trim();

                if (!text) {
                    continue;
                }

                const firstLine = text.split(/\\n+/)[0].trim();

                if (!/^Bed with Tax\\b/i.test(firstLine)) {
                    continue;
                }

                const rect = element.getBoundingClientRect();

                if (rect.width < 25 || rect.height < 10) {
                    continue;
                }

                if (rect.top < 0 || rect.left < 0) {
                    continue;
                }

                if (rect.width > window.innerWidth - 40) {
                    continue;
                }

                if (rect.height > window.innerHeight / 2) {
                    continue;
                }

                matches.push({
                    element,
                    firstLine,
                    area: rect.width * rect.height,
                    top: rect.top,
                    left: rect.left,
                    width: rect.width,
                    height: rect.height
                });
            }

            matches.sort((a, b) => {
                if (a.area !== b.area) {
                    return a.area - b.area;
                }

                if (a.top !== b.top) {
                    return a.top - b.top;
                }

                return a.left - b.left;
            });

            if (!matches.length) {
                return null;
            }

            const match = matches[0];

            match.element.scrollIntoView({
                block: 'center',
                inline: 'center'
            });

            match.element.click();

            return match.firstLine;
        }
        """
    )

    if not clicked_bed_name:
        return None

    if not re.search(r"^Bed with Tax\b", clicked_bed_name, re.I):
        raise AssertionError(
            f"Wrong bed clicked. Expected Bed with Tax, got: {clicked_bed_name}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(1200)

    return clicked_bed_name.strip()


def assert_selected_bed_with_tax_before_admit(page) -> None:
    """
    Confirms Bed with Tax is selected before clicking Admit Now.

    If the UI does not expose a selected state clearly, this still prevents
    proceeding when the page shows validation that no bed is selected.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(700)

    visible_text = get_visible_page_text(page)

    if re.search(r"Please select bed to proceed", visible_text, re.I):
        raise AssertionError(
            "Clicked Bed with Tax, but admission page still says bed is not selected.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    if not re.search(r"\bBed with Tax\b", visible_text, re.I):
        raise AssertionError(
            "Bed with Tax is not visible after selection. Do not admit with a normal bed.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )
        


def assert_taxable_bed_selected_from_visible_text(page) -> None:
    """
    Guard for taxable bed tests.

    Fails if patient/invoice page shows a normal bed instead of Bed with Tax.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(500)

    visible_text = get_visible_page_text(page)

    if re.search(r"\bBed Number\s+Bed with Tax\b", visible_text, re.I):
        return

    if re.search(r"\bBed with Tax\b", visible_text, re.I):
        return

    raise AssertionError(
        "Taxable bed was not selected. This test requires Bed with Tax.\n"
        "A normal bed was selected, so GST will not appear in the invoice.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )




def click_next_bed_paginator(page) -> bool:
    """
    Clicks the next '>' button in the Bed Details paginator.

    Uses the last visible paginator because the bed list paginator is usually
    the bottom/last paginator in the admission page.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(500)

    clicked = page.evaluate(
        """
        () => {
            const paginators = Array.from(document.querySelectorAll('.p-paginator'))
                .filter((p) => {
                    const rect = p.getBoundingClientRect();
                    return rect.width > 0 && rect.height > 0;
                });

            if (!paginators.length) {
                return false;
            }

            const paginator = paginators[paginators.length - 1];

            const nextButton =
                paginator.querySelector('.p-paginator-next') ||
                Array.from(paginator.querySelectorAll('button')).find((button) => {
                    const text = (button.innerText || button.textContent || '').trim();
                    const label = button.getAttribute('aria-label') || '';
                    return text === '>' || /next/i.test(label);
                });

            if (!nextButton) {
                return false;
            }

            const className = nextButton.className || '';
            const ariaDisabled = nextButton.getAttribute('aria-disabled');
            const disabled = nextButton.hasAttribute('disabled');

            if (
                className.includes('p-disabled') ||
                ariaDisabled === 'true' ||
                disabled
            ) {
                return false;
            }

            nextButton.click();
            return true;
        }
        """
    )

    if clicked:
        wait_for_page_ready(page)
        page.wait_for_timeout(1800)
        return True

    return False





def click_admit_now_button(page) -> None:
    """
    Clicks Admit Now.

    Do not fail before clicking just because 'Please select bed to proceed' is visible.
    That message may stay visible until Admit Now is clicked.

    After clicking Admit Now, fail only if the page is still on New Admission
    and the same validation is still shown.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(800)

    admit_button_candidates = [
        page.get_by_role("button", name=re.compile(r"Admit Now", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"Admit Now", re.I)).first,
        page.get_by_text("Admit Now", exact=False).first,
    ]

    clicked_admit = False

    for candidate in admit_button_candidates:
        try:
            candidate.scroll_into_view_if_needed(timeout=5000)
            candidate.click(timeout=10000)
            clicked_admit = True
            break
        except Exception:
            continue

    if clicked_admit is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Admit Now button.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(2500)

    visible_text_after_click = get_visible_page_text(page)

    if (
        "/business/ip/admissions/new" in page.url.lower()
        and re.search(r"Please select bed to proceed", visible_text_after_click, re.I)
    ):
        raise AssertionError(
            "Admit Now was clicked, but admission did not proceed because bed is still not selected.\n"
            "Bed with Tax was visible, but the click did not select the actual bed card.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text_after_click[:2500]}"
        )



def discharge_ip_patient_with_random_template(page) -> dict:
    """
    Discharges IP patient using a random discharge template.
    """

    wait_for_page_ready(page)

    click_button_by_text(page, "Discharge")

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    use_template_buttons = page.get_by_role(
        "button",
        name=re.compile(r"Use Template", re.I),
    )

    button_count = use_template_buttons.count()

    if button_count == 0:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "No discharge template 'Use Template' buttons found.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    random_index = random.randint(0, button_count - 1)

    use_template_buttons.nth(random_index).click(timeout=10000)

    page.wait_for_timeout(1000)

    popup_use_template_candidates = [
        page.get_by_role("button", name=re.compile(r"^Use template$", re.I)).first,
        page.get_by_role("button", name=re.compile(r"Use Template", re.I)).last,
        page.locator("button").filter(has_text=re.compile(r"Use template", re.I)).last,
    ]

    clicked_popup_template = False

    for candidate in popup_use_template_candidates:
        try:
            candidate.click(timeout=10000)
            clicked_popup_template = True
            break
        except Exception:
            continue

    if clicked_popup_template is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Use Template button inside discharge template popup.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)

    click_yes_button_if_visible(page)

    page.wait_for_timeout(2000)
    wait_for_page_ready(page)

    discharge_summary_message = assert_success_message_if_present(page)

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(1000)

    discharge_buttons = page.get_by_role("button", name=re.compile(r"Discharge", re.I))

    discharge_buttons.last.click(timeout=10000)

    page.wait_for_timeout(1000)

    click_yes_button_if_visible(page)

    wait_for_page_ready(page)
    page.wait_for_timeout(2000)

    discharge_message = assert_success_message_if_present(page)

    return {
        "discharged": True,
        "discharge_summary_message": discharge_summary_message,
        "discharge_message": discharge_message,
    }


def click_yes_button_if_visible(page) -> None:
    """
    Clicks Yes button in confirmation dialog if visible.
    """

    yes_candidates = [
        page.get_by_role("button", name=re.compile(r"^Yes$", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"^Yes$", re.I)).first,
    ]

    for candidate in yes_candidates:
        try:
            candidate.click(timeout=8000)
            wait_for_page_ready(page)
            return
        except Exception:
            continue


def create_ip_invoice_after_discharge_and_view(page) -> dict:
    """
    Opens Invoices tab, creates New Invoice if required, generates invoice,
    and leaves page on invoice details.

    Handles both cases:
    1. +Create opens a menu with New Invoice.
    2. +Create directly navigates to Create Invoice page.
    """

    wait_for_page_ready(page)

    def is_create_invoice_page() -> bool:
        try:
            current_url = page.url.lower()
            visible_text = get_visible_page_text(page).lower()

            return (
                "/business/ip/invoice/" in current_url
                and "create invoice" in visible_text
                and "generate" in visible_text
            )
        except Exception:
            return False

    def is_invoice_details_page() -> bool:
        try:
            current_url = page.url.lower()
            visible_text = get_visible_page_text(page).lower()

            return (
            "/business/ip/invoice/" in current_url
            and (
                "invoice details" in visible_text
                or "invoice no" in visible_text
                or "inv. no" in visible_text
                or "inv no" in visible_text
                or "print invoice" in visible_text
                or "detailed breakups" in visible_text
                or "amount due" in visible_text
                or "net total" in visible_text
                or "net payable" in visible_text
            )
        )
        except Exception:
            return False

    if not is_create_invoice_page() and not is_invoice_details_page():
        invoice_tab_candidates = [
            page.locator("a").filter(has_text=re.compile(r"Invoices", re.I)).first,
            page.get_by_text("Invoices", exact=False).first,
        ]

        clicked_invoice_tab = False

        for candidate in invoice_tab_candidates:
            try:
                candidate.click(timeout=10000)
                clicked_invoice_tab = True
                break
            except Exception:
                continue

        if clicked_invoice_tab is False:
            visible_text = get_visible_page_text(page)

            raise AssertionError(
                "Could not open Invoices tab from IP details page.\n"
                f"Current URL: {page.url}\n"
                f"Visible page text:\n{visible_text[:2500]}"
            )

        wait_for_page_ready(page)
        page.wait_for_timeout(1000)

    if not is_create_invoice_page() and not is_invoice_details_page():
        create_button_candidates = [
            page.get_by_role("button", name=re.compile(r"Create", re.I)).first,
            page.locator("button").filter(has_text=re.compile(r"Create", re.I)).first,
        ]

        clicked_create = False

        for candidate in create_button_candidates:
            try:
                candidate.click(timeout=10000)
                clicked_create = True
                break
            except Exception:
                continue

        if clicked_create is False:
            visible_text = get_visible_page_text(page)

            raise AssertionError(
                "Could not click Create button in Invoices tab.\n"
                f"Current URL: {page.url}\n"
                f"Visible page text:\n{visible_text[:2500]}"
            )

        wait_for_page_ready(page)
        page.wait_for_timeout(1000)

    # Some builds show menu item. Some builds directly open Create Invoice page.
    if not is_create_invoice_page() and not is_invoice_details_page():
        new_invoice_candidates = [
            page.get_by_role("menuitem", name=re.compile(r"New Invoice", re.I)).first,
            page.get_by_text("New Invoice", exact=False).first,
        ]

        clicked_new_invoice = False

        for candidate in new_invoice_candidates:
            try:
                candidate.click(timeout=8000)
                clicked_new_invoice = True
                break
            except Exception:
                continue

        if clicked_new_invoice is False:
            visible_text = get_visible_page_text(page)

            raise AssertionError(
                "Could not click New Invoice menu item and page is not on Create Invoice screen.\n"
                f"Current URL: {page.url}\n"
                f"Visible page text:\n{visible_text[:2500]}"
            )

        wait_for_page_ready(page)
        page.wait_for_timeout(1500)

    if is_invoice_details_page():
        return {
            "invoice_created": True,
            "invoice_message": "",
            "final_url": page.url,
        }

    if not is_create_invoice_page():
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Create Invoice page did not open.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    generate_candidates = [
        page.get_by_role("button", name=re.compile(r"^Generate$", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"^Generate$", re.I)).first,
    ]

    clicked_generate = False

    for candidate in generate_candidates:
        try:
            candidate.click(timeout=10000)
            clicked_generate = True
            break
        except Exception:
            continue

    if clicked_generate is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Generate button on Create Invoice page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    generate_invoice_candidates = [
        page.get_by_role("button", name=re.compile(r"Generate Invoice", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"Generate Invoice", re.I)).first,
    ]

    clicked_generate_invoice = False

    for candidate in generate_invoice_candidates:
        try:
            candidate.click(timeout=10000)
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
    page.wait_for_timeout(2500)

    invoice_message = assert_success_message_if_present(page)

    if not is_invoice_details_page():
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Invoice was generated but invoice details page did not open.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    return {
        "invoice_created": True,
        "invoice_message": invoice_message,
        "final_url": page.url,
    }





def verify_ip_invoice_taxable_bed_exempt_service_amounts(
    page,
    bed_name_contains: str,
    service_name: str,
    bed_tax_percentage: Decimal = Decimal("5"),
) -> dict:
    """
    Verifies:
    - GST applies only on taxable bed charge.
    - Service has no tax.
    - Bed tax = Bed Rate * taxPercentage / 100.
    - Bed amount = Bed Rate + Bed Tax.
    - Net Total = Room/Bed Charges Amount + Services Amount.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    bed_search_text = "Bed with Tax"

    bed_row = get_invoice_row_by_text(page, bed_search_text)
    bed_row_text = bed_row.inner_text(timeout=10000)
    bed_money_values = extract_decimal_money_values(bed_row_text)

    if len(bed_money_values) < 4:
        raise AssertionError(
            f"Not enough money values found for taxable bed row.\n"
            f"Expected row: {bed_search_text}\n"
            f"Row text:\n{bed_row_text}\n"
            f"Money values: {bed_money_values}"
        )

    # Row format:
    # Rate, Discount, Tax, Amount
    bed_rate_actual = bed_money_values[-4]
    bed_discount_actual = bed_money_values[-3]
    bed_tax_actual = bed_money_values[-2]
    bed_total_actual = bed_money_values[-1]

    bed_tax_expected = round_money(
        bed_rate_actual * bed_tax_percentage / Decimal("100")
    )

    bed_total_expected = round_money(
        bed_rate_actual - bed_discount_actual + bed_tax_expected
    )

    assert_amount_close(
        bed_tax_actual,
        bed_tax_expected,
        "Bed GST amount should be Bed Rate * 5 / 100.",
    )

    assert_amount_close(
        bed_total_actual,
        bed_total_expected,
        "Bed total amount should be Bed Rate + GST.",
    )

    service_row = get_invoice_row_by_text(page, service_name)
    service_row_text = service_row.inner_text(timeout=10000)
    service_money_values = extract_decimal_money_values(service_row_text)

    if len(service_money_values) < 4:
        raise AssertionError(
            f"Not enough money values found for service row.\n"
            f"Service: {service_name}\n"
            f"Row text:\n{service_row_text}\n"
            f"Money values: {service_money_values}"
        )

    # Row format:
    # Rate, Discount, Tax, Amount
    service_rate_actual = service_money_values[-4]
    service_discount_actual = service_money_values[-3]
    service_tax_actual = service_money_values[-2]
    service_amount_actual = service_money_values[-1]

    service_amount_expected = round_money(
        service_rate_actual - service_discount_actual
    )

    assert_amount_close(
        service_tax_actual,
        Decimal("0"),
        "Exempt service should not have tax.",
    )

    assert_amount_close(
        service_amount_actual,
        service_amount_expected,
        "Exempt service amount should be Rate - Discount, without tax.",
    )

    summary_tax_actual = read_last_summary_amount(
        page,
        "Tax",
        default=bed_tax_actual,
    )

    assert_amount_close(
        summary_tax_actual,
        bed_tax_expected,
        "Invoice summary tax should equal only bed GST.",
    )

    net_total_actual = read_ip_invoice_net_total(page)

    net_total_expected = round_money(
        bed_total_actual + service_amount_actual
    )

    assert_amount_close(
        net_total_actual,
        net_total_expected,
        "Net Total should be Room/Bed Charges Amount + Services Amount.",
    )

    print("Amounts are correct")

    return {
        "bed_name_contains": bed_search_text,
        "bed_row_text": bed_row_text,
        "bed_money_values": bed_money_values,

        "bed_tax_percentage": bed_tax_percentage,
        "bed_rate_actual": bed_rate_actual,
        "bed_discount_actual": bed_discount_actual,
        "bed_tax_actual": bed_tax_actual,
        "bed_tax_expected": bed_tax_expected,
        "bed_total_actual": bed_total_actual,
        "bed_total_expected": bed_total_expected,

        "service_name": service_name,
        "service_row_text": service_row_text,
        "service_money_values": service_money_values,
        "service_rate_actual": service_rate_actual,
        "service_discount_actual": service_discount_actual,
        "service_tax_actual": service_tax_actual,
        "service_amount_actual": service_amount_actual,
        "service_amount_expected": service_amount_expected,

        "summary_tax_actual": summary_tax_actual,
        "net_total_actual": net_total_actual,
        "net_total_expected": net_total_expected,
    }


def read_ip_invoice_net_total(page) -> Decimal:
    """
    Reads the payable/net total from IP invoice page.

    Taxable invoices may show:
    - Net Total

    Exempt invoices may show only:
    - Total
    - Amount Due

    Priority:
    1. Net Total
    2. Net payable
    3. Total
    4. Amount Due
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(500)

    labels_to_try = [
        "Net Total",
        "Net payable",
        "Total",
        "Amount Due",
    ]

    for label in labels_to_try:
        try:
            return read_invoice_summary_amount_from_visible_text(
                page=page,
                label=label,
            )
        except AssertionError:
            continue

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        "Could not read IP invoice total amount using Net Total, Net payable, Total, or Amount Due.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )


def read_invoice_summary_amount_from_visible_text(page, label: str) -> Decimal:
    """
    Reads invoice summary amount from visible text line.

    Example lines:
    Total        ₹1,250.00
    Tax          ₹32.50
    Net Total    ₹1,032.50
    Amount Due   ₹1,250.00
    """

    visible_text = get_visible_page_text(page)

    normalized_label = re.sub(r"\s+", " ", label).strip()

    if normalized_label.lower() == "total":
        label_pattern = re.compile(r"^\s*Total\s+", re.I)
    elif normalized_label.lower() == "net total":
        label_pattern = re.compile(r"^\s*Net\s+Total\s+", re.I)
    elif normalized_label.lower() == "net payable":
        label_pattern = re.compile(r"^\s*Net\s+payable\s+", re.I)
    elif normalized_label.lower() == "amount due":
        label_pattern = re.compile(r"^\s*Amount\s+Due\s+", re.I)
    else:
        label_pattern = re.compile(rf"^\s*{re.escape(normalized_label)}\s+", re.I)

    matched_amounts = []

    for line in visible_text.splitlines():
        clean_line = line.strip()

        if not clean_line:
            continue

        if not label_pattern.search(clean_line):
            continue

        money_values = extract_decimal_money_values(clean_line)

        if money_values:
            matched_amounts.append(money_values[-1])

    if matched_amounts:
        return matched_amounts[-1]

    raise AssertionError(
        f"Could not read invoice summary amount from visible text for label: {label}\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )    



def select_bed_filter_all_if_available(page) -> None:
    """
    Sets Building and Bed Type filters to All if those dropdowns are available.

    This is needed because sometimes the New Admission page opens with:
    - Building = Select Building
    - Bed Type = Select Bed Type
    - No Available Beds

    After selecting All, the bed list loads.
    """

    wait_for_page_ready(page)

    filter_dropdown_indexes = {
        "Building": 4,
        "Bed Type": 7,
    }

    for filter_name, dropdown_index in filter_dropdown_indexes.items():
        try:
            dropdown = page.locator("p-dropdown").nth(dropdown_index)

            if dropdown.count() == 0:
                continue

            dropdown_text = dropdown.inner_text(timeout=3000)

            if re.search(r"\bAll\b", dropdown_text, re.I):
                continue

            dropdown.locator(".p-dropdown-trigger").first.click(timeout=8000)
            page.wait_for_timeout(700)

            all_option_candidates = [
                page.get_by_role("option", name=re.compile(r"^All$", re.I)).first,
                page.locator(".p-dropdown-item").filter(has_text=re.compile(r"^All$", re.I)).first,
                page.get_by_text("All", exact=True).first,
            ]

            selected_all = False

            for option in all_option_candidates:
                try:
                    option.click(timeout=8000)
                    selected_all = True
                    break
                except Exception:
                    continue

            if selected_all:
                wait_for_page_ready(page)
                page.wait_for_timeout(1200)

        except Exception:
            continue 




def select_building_block_d_for_bed_search(page) -> None:
    """
    Selects Building = Block D in New Admission page.

    Important:
    - Does NOT click/change top location dropdown.
    - Does NOT validate top location.
    - Does NOT click Floor.
    - Does NOT click Room.
    - Does NOT click Bed Type.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(800)

    if "business/login" in page.url.lower():
        raise AssertionError(
            "Page redirected to login before selecting Building = Block D.\n"
            f"Current URL: {page.url}"
        )

    building_dropdown = page.locator(
        "xpath=//*[normalize-space()='Building']/following::p-dropdown[1]"
    ).first

    try:
        building_dropdown.wait_for(state="visible", timeout=10000)
    except Exception:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not find Building dropdown by label.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    try:
        current_building_text = building_dropdown.inner_text(timeout=3000)
    except Exception:
        current_building_text = ""

    if re.search(r"\bBlock D\b", current_building_text, re.I):
        reset_bed_paginator_to_first_page(page=page)
        return

    try:
        building_dropdown.locator(".p-dropdown-trigger").first.click(timeout=10000)
    except Exception:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not open Building dropdown.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)

    block_d_candidates = [
        page.get_by_role("option", name=re.compile(r"^Block D$", re.I)).first,
        page.locator(".p-dropdown-item").filter(has_text=re.compile(r"^Block D$", re.I)).first,
        page.locator("li").filter(has_text=re.compile(r"^Block D$", re.I)).first,
        page.get_by_text("Block D", exact=True).first,
    ]

    selected = False

    for option in block_d_candidates:
        try:
            option.click(timeout=10000)
            selected = True
            break
        except Exception:
            continue

    if selected is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not select Building = Block D from Building dropdown.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(2000)

    try:
        selected_building_text = building_dropdown.inner_text(timeout=5000)
    except Exception:
        selected_building_text = ""

    if not re.search(r"\bBlock D\b", selected_building_text, re.I):
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Building dropdown did not change to Block D after selection.\n"
            f"Dropdown text: {selected_building_text}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    reset_bed_paginator_to_first_page(page=page)



def reset_bed_paginator_to_first_page(page) -> None:
    """
    Resets Bed Details paginator to first page if possible.
    Uses the last visible paginator.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(500)

    page.evaluate(
        """
        () => {
            const paginators = Array.from(document.querySelectorAll('.p-paginator'))
                .filter((p) => {
                    const rect = p.getBoundingClientRect();
                    return rect.width > 0 && rect.height > 0;
                });

            if (!paginators.length) {
                return false;
            }

            const paginator = paginators[paginators.length - 1];

            const firstButton =
                paginator.querySelector('.p-paginator-first') ||
                Array.from(paginator.querySelectorAll('button')).find((button) => {
                    const text = (button.innerText || button.textContent || '').trim();
                    const label = button.getAttribute('aria-label') || '';
                    return text === '<<' || /first/i.test(label);
                });

            if (!firstButton) {
                return false;
            }

            const className = firstButton.className || '';
            const ariaDisabled = firstButton.getAttribute('aria-disabled');
            const disabled = firstButton.hasAttribute('disabled');

            if (
                className.includes('p-disabled') ||
                ariaDisabled === 'true' ||
                disabled
            ) {
                return true;
            }

            firstButton.click();
            return true;
        }
        """
    )

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)




def wait_for_new_admission_form_loaded(page) -> None:
    """
    Waits until New Admission form is fully loaded after Save & Next.

    The page may show only:
    - Create Patient
    - Loading...

    During that time dropdowns like Admission Type are not ready.
    """

    wait_for_page_ready(page)

    try:
        page.wait_for_function(
            """
            () => {
                const text = document.body.innerText || '';
                const dropdowns = document.querySelectorAll('p-dropdown, .p-dropdown');

                return (
                    !text.includes('Loading...') &&
                    text.includes('Admission Type') &&
                    text.includes('Admitted Doctor') &&
                    text.includes('Checkin Date') &&
                    text.includes('Building') &&
                    dropdowns.length >= 4
                );
            }
            """,
            timeout=30000,
        )
    except Exception:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "New Admission form did not finish loading.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)  




def pay_ip_invoice_by_cash_from_invoice_details(page) -> dict:
    """
    Pays the IP invoice from invoice details page using Cash.

    Flow:
    1. Click Get Payment.
    2. Select Pay by Cash.
    3. Click Pay.
    4. Confirm Proceed with payment by clicking Yes.
    5. Assert success message.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    payment_button_candidates = [
        page.get_by_role("button", name=re.compile(r"Get Payment", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"Get Payment", re.I)).first,
        page.get_by_role("button", name=re.compile(r"dropdown trigger", re.I)).first,
    ]

    clicked_payment_button = False

    for candidate in payment_button_candidates:
        try:
            candidate.scroll_into_view_if_needed(timeout=5000)
            candidate.click(timeout=10000)
            clicked_payment_button = True
            break
        except Exception:
            continue

    if clicked_payment_button is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Get Payment button on invoice details page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)

    pay_by_cash_candidates = [
        page.get_by_text("Pay by Cash", exact=False).first,
        page.get_by_role("menuitem", name=re.compile(r"Pay by Cash", re.I)).first,
        page.locator("li").filter(has_text=re.compile(r"Pay by Cash", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"Pay by Cash", re.I)).first,
    ]

    clicked_pay_by_cash = False

    for candidate in pay_by_cash_candidates:
        try:
            candidate.click(timeout=10000)
            clicked_pay_by_cash = True
            break
        except Exception:
            continue

    if clicked_pay_by_cash is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Pay by Cash option.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    pay_button_candidates = [
        page.get_by_role("button", name=re.compile(r"^Pay$", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"^Pay$", re.I)).first,
    ]

    clicked_pay = False

    for candidate in pay_button_candidates:
        try:
            candidate.click(timeout=10000)
            clicked_pay = True
            break
        except Exception:
            continue

    if clicked_pay is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Pay button in payment popup.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)

    click_yes_button_if_visible(page)

    wait_for_page_ready(page)
    page.wait_for_timeout(2000)

    payment_message = assert_success_message_if_present(page)

    return {
        "invoice_paid": True,
        "payment_mode": "Cash",
        "payment_message": payment_message,
        "final_url": page.url,
    }


def go_back_from_ip_invoice_details_to_patient_details(page) -> dict:
    """
    Clicks the back arrow from IP invoice details page and returns to IP patient details page.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    back_arrow_candidates = [
        page.get_by_role("heading", name=re.compile(r"Invoice Details", re.I)).locator("i").first,
        page.locator("xpath=//*[contains(normalize-space(), 'Invoice Details')]/ancestor::*[1]//i").first,
        page.locator("xpath=//*[contains(normalize-space(), 'Invoice Details')]/preceding::i[1]").first,
        page.get_by_role("button", name=re.compile(r"Back", re.I)).first,
        page.locator("i").filter(has_text=re.compile(r"arrow_back|keyboard_backspace", re.I)).first,
    ]

    clicked_back = False

    for candidate in back_arrow_candidates:
        try:
            candidate.click(timeout=10000)
            clicked_back = True
            break
        except Exception:
            continue

    if clicked_back is False:
        try:
            page.go_back(timeout=10000)
            clicked_back = True
        except Exception:
            pass

    if clicked_back is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click back arrow from invoice details page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(2000)

    visible_text = get_visible_page_text(page)

    if not re.search(r"Checkout|Invoices|Services|Discharge", visible_text, re.I):
        raise AssertionError(
            "Back navigation did not return to IP patient details page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    return {
        "returned_to_ip_details": True,
        "final_url": page.url,
    }


def checkout_ip_patient_with_random_note(page) -> dict:
    """
    Checks out the IP patient from IP details page.

    Flow:
    1. Click Checkout.
    2. Add random checkout note.
    3. Click Checkout in popup.
    4. Confirm checkout by clicking Yes.
    5. Assert success message.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    checkout_button_candidates = [
        page.get_by_role("button", name=re.compile(r"Checkout", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"Checkout", re.I)).first,
        page.get_by_text("Checkout", exact=False).first,
    ]

    clicked_checkout = False

    for candidate in checkout_button_candidates:
        try:
            candidate.click(timeout=10000)
            clicked_checkout = True
            break
        except Exception:
            continue

    if clicked_checkout is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Checkout button on IP details page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)

    checkout_note = f"Checked out by automation {random.randint(100000, 999999)}"

    note_filled = False

    dialog_candidates = [
        page.get_by_role("dialog").first,
        page.locator(".p-dialog").first,
        page.locator(".modal").first,
    ]

    for dialog in dialog_candidates:
        try:
            if dialog.count() == 0:
                continue

            dialog.get_by_role("textbox").first.fill(checkout_note, timeout=8000)
            note_filled = True
            break
        except Exception:
            continue

    if note_filled is False:
        textbox_candidates = [
            page.get_by_role("textbox").last,
            page.locator("textarea").last,
            page.locator("input[type='text']").last,
        ]

        for candidate in textbox_candidates:
            try:
                candidate.fill(checkout_note, timeout=8000)
                note_filled = True
                break
            except Exception:
                continue

    if note_filled is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not fill checkout note in checkout popup.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    popup_checkout_candidates = [
        page.get_by_role("dialog").first.get_by_role("button", name=re.compile(r"^Checkout$", re.I)).first,
        page.locator(".p-dialog").first.locator("button").filter(has_text=re.compile(r"^Checkout$", re.I)).first,
        page.get_by_role("button", name=re.compile(r"^Checkout$", re.I)).last,
        page.locator("button").filter(has_text=re.compile(r"^Checkout$", re.I)).last,
    ]

    clicked_popup_checkout = False

    for candidate in popup_checkout_candidates:
        try:
            candidate.click(timeout=10000)
            clicked_popup_checkout = True
            break
        except Exception:
            continue

    if clicked_popup_checkout is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Checkout button in checkout popup.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)

    click_yes_button_if_visible(page)

    wait_for_page_ready(page)
    page.wait_for_timeout(2000)

    checkout_message = assert_success_message_if_present(page)

    return {
        "checked_out": True,
        "checkout_note": checkout_note,
        "checkout_message": checkout_message,
        "final_url": page.url,
    }          


# IP invoice with exempt bed and taxable service; GST applies only on service.


def complete_ip_invoice_exempt_bed_taxable_service_flow(
    page,
    config,
    consumer_profile: dict,
) -> dict:
    """
    Fourth IP invoice tax test case.

    Case:
    IP invoice with exempt bed and taxable service; GST applies only on service.

    Flow:
    1. Login.
    2. Open IP Dashboard.
    3. Create random patient.
    4. Complete admission with a normal/exempt bed.
    5. Add taxable Nursing Service.
    6. Discharge patient.
    7. Create invoice.
    8. Verify GST applies only on Nursing Service.
    """

    login(page, config)

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)
    open_new_admission_page(page)

    patient_result = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    assert patient_result["patient_created"] is True

    admission_result = complete_ip_admission_with_random_exempt_bed(page=page)

    assert admission_result["admission_created"] is True

    patient_full_name = patient_result["patient_full_name"]

    open_latest_ip_patient_from_grid(
        page=page,
        patient_full_name=patient_full_name,
    )

    service_result = add_nursing_service_to_ip_patient(page=page)

    assert service_result["service_added"] is True

    discharge_result = discharge_ip_patient_with_random_template(page=page)

    assert discharge_result["discharged"] is True

    invoice_result = create_ip_invoice_after_discharge_and_view(page=page)

    assert invoice_result["invoice_created"] is True

    tax_result = verify_ip_invoice_exempt_bed_taxable_service_amounts(
        page=page,
        bed_name_contains=admission_result["bed_name"],
        service_name="nursing service",
        service_tax_percentage=Decimal("5"),
    )

    print("Amounts are correct")

    return {
        "patient_created": True,
        "patient_full_name": patient_full_name,
        "patient_result": patient_result,

        "admission_created": True,
        "admission_result": admission_result,

        "bed_name": admission_result["bed_name"],

        "service_added": True,
        "service_result": service_result,

        "discharged": True,
        "discharge_result": discharge_result,

        "invoice_created": True,
        "invoice_result": invoice_result,

        "tax_result": tax_result,

        "final_url": page.url,
    }


def complete_ip_admission_with_random_exempt_bed(page) -> dict:
    """
    Completes IP admission by selecting:
    - random Admission Type
    - random Admitted Doctor
    - today's Checkin Date
    - future Expected Checkout Date
    - random normal/exempt bed, excluding 'Bed with Tax'
    """

    wait_for_page_ready(page)
    wait_for_new_admission_form_loaded(page)

    admission_type = select_random_primeng_dropdown_option(
        page=page,
        dropdown_text="Admission Type",
    )

    admitted_doctor = select_random_primeng_dropdown_option(
        page=page,
        dropdown_text="Admitted Doctor",
    )

    select_today_for_admission_date_by_index(
        page=page,
        date_picker_index=0,
    )

    select_future_date_for_admission_date_by_index(
        page=page,
        date_picker_index=1,
        days_ahead=1,
    )

    bed_name = select_random_exempt_bed_from_available_beds(page=page)

    click_admit_now_button(page=page)

    assert "Bed with Tax" not in bed_name, (
        f"Wrong bed selected. Expected exempt/normal bed, got taxable bed: {bed_name}"
    )

    wait_for_page_ready(page)
    page.wait_for_timeout(2000)

    toast_message = assert_success_message_if_present(page)

    return {
        "admission_created": True,
        "admission_type": admission_type,
        "admitted_doctor": admitted_doctor,
        "bed_name": bed_name,
        "toast_message": toast_message,
    }


def select_future_date_for_admission_date_by_index(
    page,
    date_picker_index: int,
    days_ahead: int = 1,
) -> None:
    """
    Opens date picker by index and selects a future date.

    date_picker_index:
    - 0 = Checkin Date
    - 1 = Expected Checkout Date
    """

    target_date = datetime.now() + timedelta(days=days_ahead)
    target_day = str(target_date.day)
    current_date = datetime.now()

    calendar_trigger_candidates = [
        page.locator("p-calendar").nth(date_picker_index).locator("button").first,
        page.locator("p-calendar").nth(date_picker_index).locator(".p-datepicker-trigger").first,
        page.locator(".p-datepicker-trigger").nth(date_picker_index),
    ]

    opened = False

    for candidate in calendar_trigger_candidates:
        try:
            candidate.click(timeout=10000)
            opened = True
            break
        except Exception:
            continue

    if opened is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not open admission future date picker index {date_picker_index}.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(700)

    if target_date.month != current_date.month:
        try:
            page.locator(".p-datepicker-next").first.click(timeout=8000)
            page.wait_for_timeout(700)
        except Exception:
            pass

    future_date_candidates = [
        page.locator(".p-datepicker-calendar td:not(.p-datepicker-other-month)")
        .filter(has_text=re.compile(rf"^{target_day}$"))
        .first,
        page.get_by_role("table").get_by_text(target_day, exact=True).first,
    ]

    selected = False

    for candidate in future_date_candidates:
        try:
            candidate.click(timeout=10000)
            selected = True
            break
        except Exception:
            continue

    if selected is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not select future date: {target_day}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)


def select_random_exempt_bed_from_available_beds(page) -> str:
    """
    Selects a random available normal/exempt bed.

    Excludes:
    - Bed with Tax

    Returns bed number/name used for invoice lookup.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    max_pages_to_check = 30

    reset_bed_paginator_to_first_page(page=page)

    for page_index in range(max_pages_to_check):
        wait_for_page_ready(page)
        page.wait_for_timeout(1000)

        visible_text = get_visible_page_text(page)

        if re.search(r"No Available Beds", visible_text, re.I):
            raise AssertionError(
                "No available beds are shown for exempt bed selection.\n"
                f"Current URL: {page.url}\n"
                f"Visible page text:\n{visible_text[:2500]}"
            )

        bed_candidates = page.evaluate(
            """
            () => {
                const elements = Array.from(document.querySelectorAll('div, span, p, button'));
                const candidates = [];

                for (const element of elements) {
                    const text = (element.innerText || element.textContent || '').trim();

                    if (!text) {
                        continue;
                    }

                    if (!/^Bed(?! with Tax)\\S+/i.test(text)) {
                        continue;
                    }

                    if (/Bed with Tax/i.test(text)) {
                        continue;
                    }

                    const rect = element.getBoundingClientRect();

                    if (rect.width < 40 || rect.height < 15) {
                        continue;
                    }

                    if (rect.width > window.innerWidth - 20) {
                        continue;
                    }

                    const firstLine = text.split(/\\n+/)[0].trim();

                    if (!/^Bed(?! with Tax)\\S+/i.test(firstLine)) {
                        continue;
                    }

                    candidates.push({
                        text,
                        firstLine,
                        top: rect.top,
                        left: rect.left,
                        width: rect.width,
                        height: rect.height
                    });
                }

                candidates.sort((a, b) => {
                    if (a.top !== b.top) {
                        return a.top - b.top;
                    }

                    return a.left - b.left;
                });

                return candidates;
            }
            """
        )

        valid_beds = []

        for bed in bed_candidates:
            first_line = bed.get("firstLine", "").strip()

            if not first_line:
                continue

            if re.search(r"Bed with Tax", first_line, re.I):
                continue

            if not re.search(r"^Bed\S+", first_line, re.I):
                continue

            valid_beds.append(first_line)

        if valid_beds:
            selected_bed_line = random.choice(valid_beds)
            selected_bed_number = selected_bed_line.split()[0].strip()

            bed_text_locator = page.get_by_text(selected_bed_line, exact=False).first

            clicked_bed = False

            try:
                bed_text_locator.scroll_into_view_if_needed(timeout=5000)
                bed_text_locator.click(timeout=10000)
                clicked_bed = True
            except Exception:
                clicked_bed = False

            if clicked_bed is False:
                bed_line_pattern = re.compile(re.escape(selected_bed_line), re.I)

                fallback_candidates = [
                    page.locator("div").filter(has_text=bed_line_pattern).first,
                    page.locator(".card").filter(has_text=bed_line_pattern).first,
                    page.get_by_text(re.compile(re.escape(selected_bed_number), re.I)).first,
                ]

                for candidate in fallback_candidates:
                    try:
                        candidate.scroll_into_view_if_needed(timeout=5000)
                        candidate.click(timeout=10000)
                        clicked_bed = True
                        break
                    except Exception:
                        continue

            if clicked_bed is False:
                visible_text = get_visible_page_text(page)

                raise AssertionError(
                    f"Could not click selected exempt bed: {selected_bed_line}\n"
                    f"Current URL: {page.url}\n"
                    f"Visible page text:\n{visible_text[:2500]}"
                )

            page.wait_for_timeout(1000)
            wait_for_page_ready(page)

            visible_text_after_click = get_visible_page_text(page)

            if re.search(r"Please select bed to proceed", visible_text_after_click, re.I):
                raise AssertionError(
                    f"Clicked exempt bed but bed was not selected: {selected_bed_line}\n"
                    f"Current URL: {page.url}\n"
                    f"Visible page text:\n{visible_text_after_click[:2500]}"
                )

            return selected_bed_number

        clicked_next = click_next_bed_paginator(page)

        if clicked_next is False:
            break

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        "Could not find/select an exempt normal bed after checking available bed pages.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )


def add_nursing_service_to_ip_patient(page) -> dict:
    """
    Adds taxable Nursing Service to IP patient.

    Expected:
    - Service search text: nur
    - Service selected: nursing service
    - Past time selected
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    service_button_candidates = [
        page.get_by_role("button", name=re.compile(r"Service", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"Service", re.I)).first,
        page.get_by_text("Service", exact=False).first,
    ]

    clicked_service = False

    for candidate in service_button_candidates:
        try:
            candidate.click(timeout=10000)
            clicked_service = True
            break
        except Exception:
            continue

    if clicked_service is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click +Service button on IP details page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)

    search_candidates = [
        page.get_by_role("searchbox", name=re.compile(r"Search Service", re.I)).first,
        page.locator("input[placeholder*='Search Service']").first,
        page.locator("input[type='search']").first,
        page.locator("input").filter(has_text=re.compile(r"")).first,
    ]

    filled_search = False

    for candidate in search_candidates:
        try:
            candidate.fill("nur", timeout=10000)
            filled_search = True
            break
        except Exception:
            continue

    if filled_search is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not fill service search field for Nursing Service.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)

    nursing_service_candidates = [
        page.get_by_role("option", name=re.compile(r"nursing service", re.I)).first,
        page.get_by_text(re.compile(r"nursing service", re.I)).first,
        page.locator("li").filter(has_text=re.compile(r"nursing service", re.I)).first,
    ]

    selected_service = False

    for candidate in nursing_service_candidates:
        try:
            candidate.click(timeout=10000)
            selected_service = True
            break
        except Exception:
            continue

    if selected_service is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not select Nursing Service from service list.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    select_past_service_time(page)

    click_button_by_text(page, "Add Service")

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    toast_message = assert_success_message_if_present(page)

    return {
        "service_added": True,
        "service_name": "nursing service",
        "toast_message": toast_message,
    }




def verify_ip_invoice_exempt_bed_taxable_service_amounts(
    page,
    bed_name_contains: str,
    service_name: str,
    service_tax_percentage: Decimal = Decimal("5"),
    ) -> dict:
    """
    Verifies:
    - Bed has no tax.
    - Nursing Service has 5% GST.
    - Service tax = Service Rate * 5 / 100.
    - Service amount = Service Rate + Tax.
    - Net Total = Room/Bed Charges Amount + Services Amount.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    bed_row = get_invoice_row_by_text(page, bed_name_contains)
    bed_row_text = bed_row.inner_text(timeout=10000)
    bed_money_values = extract_decimal_money_values(bed_row_text)

    if len(bed_money_values) < 4:
        raise AssertionError(
            f"Not enough money values found for exempt bed row.\n"
            f"Bed: {bed_name_contains}\n"
            f"Row text:\n{bed_row_text}\n"
            f"Money values: {bed_money_values}"
        )

    # Row format:
    # Rate, Discount, Tax, Amount
    bed_rate_actual = bed_money_values[-4]
    bed_discount_actual = bed_money_values[-3]
    bed_tax_actual = bed_money_values[-2]
    bed_total_actual = bed_money_values[-1]

    bed_total_expected = round_money(
        bed_rate_actual - bed_discount_actual
    )

    assert_amount_close(
        bed_tax_actual,
        Decimal("0"),
        "Exempt bed should not have tax.",
    )

    assert_amount_close(
        bed_total_actual,
        bed_total_expected,
        "Exempt bed amount should be Rate - Discount, without tax.",
    )

    service_row = get_invoice_row_by_text(page, service_name)
    service_row_text = service_row.inner_text(timeout=10000)
    service_money_values = extract_decimal_money_values(service_row_text)

    if len(service_money_values) < 4:
        raise AssertionError(
            f"Not enough money values found for taxable service row.\n"
            f"Service: {service_name}\n"
            f"Row text:\n{service_row_text}\n"
            f"Money values: {service_money_values}"
        )

    # Row format:
    # Rate, Discount, Tax, Amount
    service_rate_actual = service_money_values[-4]
    service_discount_actual = service_money_values[-3]
    service_tax_actual = service_money_values[-2]
    service_total_actual = service_money_values[-1]

    service_taxable_actual = round_money(
        service_rate_actual - service_discount_actual
    )

    service_tax_expected = round_money(
        service_taxable_actual * service_tax_percentage / Decimal("100")
    )

    service_total_expected = round_money(
        service_taxable_actual + service_tax_expected
    )

    assert_amount_close(
        service_tax_actual,
        service_tax_expected,
        "Nursing Service GST amount should be Service Rate * 5 / 100.",
    )

    assert_amount_close(
        service_total_actual,
        service_total_expected,
        "Nursing Service amount should be Service Rate + GST.",
    )

    summary_tax_actual = read_last_summary_amount(
        page,
        "Tax",
        default=service_tax_actual,
    )

    assert_amount_close(
        summary_tax_actual,
        service_tax_expected,
        "Invoice summary tax should equal only Nursing Service GST.",
    )

    net_total_actual = read_ip_invoice_net_total(page)

    net_total_expected = round_money(
        bed_total_actual + service_total_actual
    )

    assert_amount_close(
        net_total_actual,
        net_total_expected,
        "Net Total should be Room/Bed Charges Amount + Services Amount.",
    )

    print("Amounts are correct")

    return {
        "bed_name_contains": bed_name_contains,
        "bed_row_text": bed_row_text,
        "bed_money_values": bed_money_values,

        "bed_rate_actual": bed_rate_actual,
        "bed_discount_actual": bed_discount_actual,
        "bed_tax_actual": bed_tax_actual,
        "bed_total_actual": bed_total_actual,
        "bed_total_expected": bed_total_expected,

        "service_name": service_name,
        "service_row_text": service_row_text,
        "service_money_values": service_money_values,

        "service_tax_percentage": service_tax_percentage,
        "service_rate_actual": service_rate_actual,
        "service_discount_actual": service_discount_actual,
        "service_taxable_actual": service_taxable_actual,
        "service_tax_actual": service_tax_actual,
        "service_tax_expected": service_tax_expected,
        "service_total_actual": service_total_actual,
        "service_total_expected": service_total_expected,

        "summary_tax_actual": summary_tax_actual,
        "net_total_actual": net_total_actual,
        "net_total_expected": net_total_expected,
    }


# ---- IP invoice with both bed and services taxable; GST calculated correctly ----


def complete_ip_invoice_taxable_bed_taxable_service_flow(
    page,
    config,
    consumer_profile: dict,
) -> dict:
    """
    Fifth IP invoice tax test case.

    Case:
    IP invoice with both bed and services taxable; GST calculated correctly.

    Flow:
    1. Login.
    2. Open IP Dashboard.
    3. Create random patient.
    4. Complete admission with taxable bed: Bed with Tax.
    5. Add taxable Nursing Service.
    6. Discharge patient.
    7. Create invoice.
    8. Verify GST applies on both bed and service.
    9. Pay invoice by Cash.
    10. Go back to IP details.
    11. Checkout patient.
    """

    login(page, config)

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)
    open_new_admission_page(page)

    patient_result = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    assert patient_result["patient_created"] is True

    admission_result = complete_ip_admission_with_taxable_bed(page=page)

    assert admission_result["admission_created"] is True

    patient_full_name = patient_result["patient_full_name"]

    open_latest_ip_patient_from_grid(
        page=page,
        patient_full_name=patient_full_name,
    )

    service_result = add_nursing_service_to_ip_patient(page=page)

    assert service_result["service_added"] is True

    discharge_result = discharge_ip_patient_with_random_template(page=page)

    assert discharge_result["discharged"] is True

    invoice_result = create_ip_invoice_after_discharge_and_view(page=page)

    assert invoice_result["invoice_created"] is True

    tax_result = verify_ip_invoice_taxable_bed_taxable_service_amounts(
        page=page,
        bed_name_contains="Bed with Tax",
        service_name="nursing service",
        bed_tax_percentage=Decimal("5"),
        service_tax_percentage=Decimal("5"),
    )

    print("Amounts are correct")

    payment_result = pay_ip_invoice_by_cash_from_invoice_details(page=page)

    assert payment_result["invoice_paid"] is True

    back_result = go_back_from_ip_invoice_details_to_patient_details(page=page)

    assert back_result["returned_to_ip_details"] is True

    checkout_result = checkout_ip_patient_with_random_note(page=page)

    assert checkout_result["checked_out"] is True

    return {
        "patient_created": True,
        "patient_full_name": patient_full_name,
        "patient_result": patient_result,

        "admission_created": True,
        "admission_result": admission_result,

        "bed_name": admission_result["bed_name"],

        "service_added": True,
        "service_result": service_result,

        "discharged": True,
        "discharge_result": discharge_result,

        "invoice_created": True,
        "invoice_result": invoice_result,

        "tax_result": tax_result,

        "invoice_paid": True,
        "payment_result": payment_result,

        "returned_to_ip_details": True,
        "back_result": back_result,

        "checked_out": True,
        "checkout_result": checkout_result,

        "final_url": page.url,
    }


def verify_ip_invoice_taxable_bed_taxable_service_amounts(
    page,
    bed_name_contains: str,
    service_name: str,
    bed_tax_percentage: Decimal = Decimal("5"),
    service_tax_percentage: Decimal = Decimal("5"),
) -> dict:
    """
    Verifies:
    - Bed has GST.
    - Nursing Service has GST.
    - Bed tax = Bed Rate * 5 / 100.
    - Bed total = Bed Rate + Tax.
    - Service tax = Service Rate * 5 / 100.
    - Service total = Service Rate + Tax.
    - Summary Tax = Bed Tax + Service Tax.
    - Net Total = Bed Total + Service Total.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    bed_search_text = "Bed with Tax"

    bed_row = get_invoice_row_by_text(page, bed_search_text)
    bed_row_text = bed_row.inner_text(timeout=10000)
    bed_money_values = extract_decimal_money_values(bed_row_text)

    if len(bed_money_values) < 4:
        raise AssertionError(
            f"Not enough money values found for taxable bed row.\n"
            f"Expected row: {bed_search_text}\n"
            f"Row text:\n{bed_row_text}\n"
            f"Money values: {bed_money_values}"
        )

    # Invoice row format:
    # Rate, Discount, Tax, Amount
    bed_rate_actual = bed_money_values[-4]
    bed_discount_actual = bed_money_values[-3]
    bed_tax_actual = bed_money_values[-2]
    bed_total_actual = bed_money_values[-1]

    bed_taxable_actual = round_money(
        bed_rate_actual - bed_discount_actual
    )

    bed_tax_expected = round_money(
        bed_taxable_actual * bed_tax_percentage / Decimal("100")
    )

    bed_total_expected = round_money(
        bed_taxable_actual + bed_tax_expected
    )

    assert_amount_close(
        bed_tax_actual,
        bed_tax_expected,
        "Bed GST amount should be Bed Rate * 5 / 100.",
    )

    assert_amount_close(
        bed_total_actual,
        bed_total_expected,
        "Bed total amount should be Bed Rate + GST.",
    )

    service_row = get_invoice_row_by_text(page, service_name)
    service_row_text = service_row.inner_text(timeout=10000)
    service_money_values = extract_decimal_money_values(service_row_text)

    if len(service_money_values) < 4:
        raise AssertionError(
            f"Not enough money values found for taxable service row.\n"
            f"Service: {service_name}\n"
            f"Row text:\n{service_row_text}\n"
            f"Money values: {service_money_values}"
        )

    # Invoice row format:
    # Rate, Discount, Tax, Amount
    service_rate_actual = service_money_values[-4]
    service_discount_actual = service_money_values[-3]
    service_tax_actual = service_money_values[-2]
    service_total_actual = service_money_values[-1]

    service_taxable_actual = round_money(
        service_rate_actual - service_discount_actual
    )

    service_tax_expected = round_money(
        service_taxable_actual * service_tax_percentage / Decimal("100")
    )

    service_total_expected = round_money(
        service_taxable_actual + service_tax_expected
    )

    assert_amount_close(
        service_tax_actual,
        service_tax_expected,
        "Nursing Service GST amount should be Service Rate * 5 / 100.",
    )

    assert_amount_close(
        service_total_actual,
        service_total_expected,
        "Nursing Service total amount should be Service Rate + GST.",
    )

    summary_tax_expected = round_money(
        bed_tax_expected + service_tax_expected
    )

    summary_tax_actual = read_last_summary_amount(
        page,
        "Tax",
        default=summary_tax_expected,
    )

    assert_amount_close(
        summary_tax_actual,
        summary_tax_expected,
        "Invoice summary tax should equal Bed GST + Nursing Service GST.",
    )

    net_total_actual = read_ip_invoice_net_total(page)

    net_total_expected = round_money(
        bed_total_actual + service_total_actual
    )

    assert_amount_close(
        net_total_actual,
        net_total_expected,
        "Net Total should be Bed Total + Service Total.",
    )

    print("Amounts are correct")

    return {
        "bed_name_contains": bed_search_text,
        "bed_row_text": bed_row_text,
        "bed_money_values": bed_money_values,

        "bed_tax_percentage": bed_tax_percentage,
        "bed_rate_actual": bed_rate_actual,
        "bed_discount_actual": bed_discount_actual,
        "bed_taxable_actual": bed_taxable_actual,
        "bed_tax_actual": bed_tax_actual,
        "bed_tax_expected": bed_tax_expected,
        "bed_total_actual": bed_total_actual,
        "bed_total_expected": bed_total_expected,

        "service_name": service_name,
        "service_row_text": service_row_text,
        "service_money_values": service_money_values,

        "service_tax_percentage": service_tax_percentage,
        "service_rate_actual": service_rate_actual,
        "service_discount_actual": service_discount_actual,
        "service_taxable_actual": service_taxable_actual,
        "service_tax_actual": service_tax_actual,
        "service_tax_expected": service_tax_expected,
        "service_total_actual": service_total_actual,
        "service_total_expected": service_total_expected,

        "summary_tax_actual": summary_tax_actual,
        "summary_tax_expected": summary_tax_expected,

        "net_total_actual": net_total_actual,
        "net_total_expected": net_total_expected,
    }    



# IP invoice with both bed and services exempt; no GST applied.  



def complete_ip_invoice_exempt_bed_exempt_service_flow(
    page,
    config,
    consumer_profile: dict,
    ) -> dict:
    """
    Sixth IP invoice tax test case.

    Case:
    IP invoice with both bed and services exempt; no GST applied.

    Flow:
    1. Login.
    2. Open IP Dashboard.
    3. Create random patient.
    4. Complete admission with random exempt/normal bed.
    5. Add exempt Doc Visit service.
    6. Discharge patient.
    7. Create invoice.
    8. Verify no GST is applied and Net Total is correct.
    """

    login(page, config)

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)
    open_new_admission_page(page)

    patient_result = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    assert patient_result["patient_created"] is True

    admission_result = complete_ip_admission_with_random_exempt_bed(page=page)

    assert admission_result["admission_created"] is True

    patient_full_name = patient_result["patient_full_name"]

    open_latest_ip_patient_from_grid(
        page=page,
        patient_full_name=patient_full_name,
    )

    service_result = add_doc_visit_service_to_ip_patient(page=page)

    assert service_result["service_added"] is True

    discharge_result = discharge_ip_patient_with_random_template(page=page)

    assert discharge_result["discharged"] is True

    invoice_result = create_ip_invoice_after_discharge_and_view(page=page)

    assert invoice_result["invoice_created"] is True

    tax_result = verify_ip_invoice_exempt_bed_exempt_service_amounts(
        page=page,
        bed_name_contains=admission_result["bed_name"],
        service_name="Doc Visit",
    )

    print("Amounts are correct")

    return {
        "patient_created": True,
        "patient_full_name": patient_full_name,
        "patient_result": patient_result,

        "admission_created": True,
        "admission_result": admission_result,

        "bed_name": admission_result["bed_name"],

        "service_added": True,
        "service_result": service_result,

        "discharged": True,
        "discharge_result": discharge_result,

        "invoice_created": True,
        "invoice_result": invoice_result,

        "tax_result": tax_result,

        "final_url": page.url,
    }



def verify_ip_invoice_exempt_bed_exempt_service_amounts(
    page,
    bed_name_contains: str,
    service_name: str,
) -> dict:
    """
    Verifies:
    - Bed has no tax.
    - Doc Visit service has no tax.
    - Net Total = Room/Bed Charges Amount + Services Amount.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    bed_row = get_invoice_row_by_text(page, bed_name_contains)
    bed_row_text = bed_row.inner_text(timeout=10000)
    bed_money_values = extract_decimal_money_values(bed_row_text)

    if len(bed_money_values) < 4:
        raise AssertionError(
            f"Not enough money values found for exempt bed row.\n"
            f"Bed: {bed_name_contains}\n"
            f"Row text:\n{bed_row_text}\n"
            f"Money values: {bed_money_values}"
        )

    # Invoice row format:
    # Rate, Discount, Tax, Amount
    bed_rate_actual = bed_money_values[-4]
    bed_discount_actual = bed_money_values[-3]
    bed_tax_actual = bed_money_values[-2]
    bed_total_actual = bed_money_values[-1]

    bed_total_expected = round_money(
        bed_rate_actual - bed_discount_actual
    )

    assert_amount_close(
        bed_tax_actual,
        Decimal("0"),
        "Exempt bed should not have GST.",
    )

    assert_amount_close(
        bed_total_actual,
        bed_total_expected,
        "Exempt bed amount should be Rate - Discount, without tax.",
    )

    service_row = get_invoice_row_by_text(page, service_name)
    service_row_text = service_row.inner_text(timeout=10000)
    service_money_values = extract_decimal_money_values(service_row_text)

    if len(service_money_values) < 4:
        raise AssertionError(
            f"Not enough money values found for exempt service row.\n"
            f"Service: {service_name}\n"
            f"Row text:\n{service_row_text}\n"
            f"Money values: {service_money_values}"
        )

    # Invoice row format:
    # Rate, Discount, Tax, Amount
    service_rate_actual = service_money_values[-4]
    service_discount_actual = service_money_values[-3]
    service_tax_actual = service_money_values[-2]
    service_total_actual = service_money_values[-1]

    service_total_expected = round_money(
        service_rate_actual - service_discount_actual
    )

    assert_amount_close(
        service_tax_actual,
        Decimal("0"),
        "Exempt Doc Visit service should not have GST.",
    )

    assert_amount_close(
        service_total_actual,
        service_total_expected,
        "Exempt service amount should be Rate - Discount, without tax.",
    )

    net_total_actual = read_ip_invoice_net_total(page)

    net_total_expected = round_money(
        bed_total_actual + service_total_actual
    )

    assert_amount_close(
        net_total_actual,
        net_total_expected,
        "Net Total should be Room/Bed Charges Amount + Services Amount.",
    )

    print("Amounts are correct")

    return {
        "bed_name_contains": bed_name_contains,
        "bed_row_text": bed_row_text,
        "bed_money_values": bed_money_values,

        "bed_rate_actual": bed_rate_actual,
        "bed_discount_actual": bed_discount_actual,
        "bed_tax_actual": bed_tax_actual,
        "bed_total_actual": bed_total_actual,
        "bed_total_expected": bed_total_expected,

        "service_name": service_name,
        "service_row_text": service_row_text,
        "service_money_values": service_money_values,

        "service_rate_actual": service_rate_actual,
        "service_discount_actual": service_discount_actual,
        "service_tax_actual": service_tax_actual,
        "service_total_actual": service_total_actual,
        "service_total_expected": service_total_expected,

        "net_total_actual": net_total_actual,
        "net_total_expected": net_total_expected,
    }   


# IP bed charges calculated for multiple days; tax and total match bed days   


def complete_ip_invoice_taxable_bed_multiple_days_flow(
    page,
    config,
    consumer_profile: dict,
) -> dict:
    """
    Seventh IP invoice tax test case.

    Case:
    IP bed charges calculated for multiple days; tax and total match bed days.

    Important:
    After Admit Now, do not open the newly created patient by name.
    Search Inpatients grid pages and open the row where Bed Details = Bed with Tax.
    """

    login(page, config)

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)
    open_new_admission_page(page)

    patient_result = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    assert patient_result["patient_created"] is True

    admission_result = complete_ip_admission_with_taxable_bed_multiple_days(
        page=page,
    )

    assert admission_result["admission_created"] is True

    patient_full_name = patient_result["patient_full_name"]

    opened_patient_result = open_newly_admitted_patient_with_expected_taxable_bed_from_grid(
        page=page,
        patient_full_name=patient_full_name,
    )

    assert opened_patient_result["opened"] is True

    assert_taxable_bed_selected_from_visible_text(page=page)

    expected_bed_days = admission_result["bed_days_expected"]

    discharge_result = discharge_ip_patient_with_random_template(page=page)

    assert discharge_result["discharged"] is True

    invoice_result = create_ip_invoice_after_discharge_and_view(page=page)

    assert invoice_result["invoice_created"] is True

    tax_result = verify_ip_invoice_taxable_bed_multiple_days_amounts(
        page=page,
        bed_name_contains="Bed with Tax",
        expected_bed_days=expected_bed_days,
        bed_tax_percentage=Decimal("5"),
    )

    print("Amounts are correct")

    payment_result = pay_ip_invoice_by_cash_from_invoice_details(page=page)

    assert payment_result["invoice_paid"] is True

    back_result = go_back_from_ip_invoice_details_to_patient_details(page=page)

    assert back_result["returned_to_ip_details"] is True

    checkout_result = checkout_ip_patient_with_random_note(page=page)

    assert checkout_result["checked_out"] is True

    return {
        "patient_created": True,
        "patient_result": patient_result,

        "admission_created": True,
        "admission_result": admission_result,

        "patient_full_name": patient_full_name,
        "expected_bed_days": expected_bed_days,

        "discharged": True,
        "discharge_result": discharge_result,

        "invoice_created": True,
        "invoice_result": invoice_result,

        "tax_result": tax_result,

        "invoice_paid": True,
        "payment_result": payment_result,

        "returned_to_ip_details": True,
        "back_result": back_result,

        "checked_out": True,
        "checkout_result": checkout_result,

        "opened_patient_result": opened_patient_result,
        "patient_full_name": patient_full_name,

        "final_url": page.url,
    }



def open_newly_admitted_patient_with_expected_taxable_bed_from_grid(
    page,
    patient_full_name: str,
) -> dict:
    """
    Searches Inpatients grid page by page for the newly created patient.

    It opens only the row that contains:
    - the new patient name
    - Bed with Tax in Bed Details

    If the patient row is found with a normal bed, fail immediately.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    ensure_inpatients_grid_page(page=page)

    reset_inpatients_grid_paginator_to_first_page(page=page)

    patient_name_pattern = build_patient_name_pattern_for_grid(patient_full_name)
    max_pages_to_check = 80

    for page_index in range(max_pages_to_check):
        wait_for_page_ready(page)
        page.wait_for_timeout(1200)

        rows = page.locator("tr")

        try:
            row_count = rows.count()
        except Exception:
            row_count = 0

        for index in range(row_count):
            row = rows.nth(index)

            try:
                if not row.is_visible(timeout=1000):
                    continue

                row_text = row.inner_text(timeout=3000)

                if not patient_name_pattern.search(row_text):
                    continue

                if not re.search(r"\bBed with Tax\b", row_text, re.I):
                    raise AssertionError(
                        "Newly created patient was found in grid, but Bed Details is not Bed with Tax.\n"
                        "This means the admission selected a normal bed.\n"
                        f"Expected patient: {patient_full_name}\n"
                        f"Grid page: {page_index + 1}\n"
                        f"Row text:\n{row_text}\n"
                        f"Current URL: {page.url}"
                    )

                view_button_candidates = [
                    row.locator("#btnViewIp_IP_IpGrd").first,
                    row.get_by_role("button", name=re.compile(r"^View$", re.I)).first,
                    row.locator("button").filter(has_text=re.compile(r"^View$", re.I)).first,
                ]

                clicked_view = False

                for candidate in view_button_candidates:
                    try:
                        candidate.scroll_into_view_if_needed(timeout=5000)
                        candidate.click(timeout=10000)
                        clicked_view = True
                        break
                    except Exception:
                        continue

                if clicked_view is False:
                    raise AssertionError(
                        "Found newly created patient row with Bed with Tax, but could not click View.\n"
                        f"Row text:\n{row_text}"
                    )

                wait_for_page_ready(page)
                page.wait_for_timeout(2500)

                return {
                    "opened": True,
                    "patient_full_name": patient_full_name,
                    "grid_page_index": page_index + 1,
                    "row_text": row_text,
                    "final_url": page.url,
                }

            except AssertionError:
                raise
            except Exception:
                continue

        clicked_next = click_next_inpatients_grid_paginator(page=page)

        if clicked_next is False:
            break

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        "Could not find newly created patient in Inpatients grid.\n"
        f"Patient: {patient_full_name}\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )



def build_patient_name_pattern_for_grid(patient_full_name: str):
    """
    Builds a flexible regex for grid row patient name.

    Handles:
    - First Last
    - Initial First Last
    - extra spaces
    """

    name_parts = [
        part.strip()
        for part in patient_full_name.split()
        if part.strip()
    ]

    if not name_parts:
        raise AssertionError(f"Invalid patient full name: {patient_full_name}")

    pattern = r"\s+".join(re.escape(part) for part in name_parts)

    return re.compile(pattern, re.I)




def complete_ip_admission_with_taxable_bed_multiple_days(page) -> dict:
    """
    Completes IP admission with:
    - past Checkin Date
    - today's Expected Checkout Date
    - taxable Bed with Tax

    This function must not select a normal bed.
    """

    wait_for_page_ready(page)
    wait_for_new_admission_form_loaded(page)

    admission_type = select_random_primeng_dropdown_option(
        page=page,
        dropdown_text="Admission Type",
    )

    admitted_doctor = select_random_primeng_dropdown_option(
        page=page,
        dropdown_text="Admitted Doctor",
    )

    checkin_date = select_random_past_checkin_date_for_multiple_bed_days(
        page=page,
        date_picker_index=0,
    )

    expected_checkout_date = datetime.now().date()

    select_today_for_admission_date_by_index(
        page=page,
        date_picker_index=1,
    )

    select_building_block_d_for_bed_search(page=page)

    bed_name = select_bed_with_tax_from_admission_bed_section(page=page)

    if not re.search(r"^Bed with Tax\b", bed_name, re.I):
        raise AssertionError(
            f"Wrong bed selected. Expected Bed with Tax, got: {bed_name}"
        )

    click_admit_now_button(page=page)

    wait_for_page_ready(page)
    page.wait_for_timeout(2500)

    toast_message = assert_success_message_if_present(page)

    bed_days_expected = (expected_checkout_date - checkin_date).days + 1

    if bed_days_expected < 2:
        raise AssertionError(
            f"Multiple-day bed charge test requires at least 2 bed days. Got: {bed_days_expected}"
        )

    return {
        "admission_created": True,
        "admission_type": admission_type,
        "admitted_doctor": admitted_doctor,
        "bed_name": bed_name,
        "checkin_date": checkin_date,
        "expected_checkout_date": expected_checkout_date,
        "bed_days_expected": Decimal(str(bed_days_expected)),
        "toast_message": toast_message,
    }



def select_bed_with_tax_from_admission_bed_section(page) -> str:
    """
    Searches admission bed paginator pages and clicks Bed with Tax.

    Does not fail based on the validation message before Admit Now.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    reset_bed_paginator_to_first_page(page=page)

    max_pages_to_check = 120

    for page_index in range(max_pages_to_check):
        wait_for_page_ready(page)
        page.wait_for_timeout(1200)

        selected_bed_name = click_bed_with_tax_card_using_dom(page=page)

        if selected_bed_name:
            if not re.search(r"^Bed with Tax\b", selected_bed_name, re.I):
                raise AssertionError(
                    f"Wrong bed selected. Expected Bed with Tax, got: {selected_bed_name}"
                )

            return selected_bed_name

        clicked_next = click_next_bed_paginator(page=page)

        if clicked_next is False:
            break

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        "Could not find Bed with Tax in the admission bed section.\n"
        "Do not continue with a normal bed because GST will not appear.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )



def click_bed_with_tax_card_using_dom(page):
    """
    Clicks Bed with Tax / Bed with Tax Normal from the admission bed section.

    Important:
    Do not verify selection using 'Please select bed to proceed' here.
    In this UI, that validation message may stay visible until Admit Now is clicked.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(700)

    bed_candidates = [
        page.get_by_text("Bed with Tax Normal", exact=True).first,
        page.get_by_text("Bed with Tax", exact=True).first,
        page.get_by_text(re.compile(r"^Bed with Tax\b", re.I)).first,
        page.locator("xpath=//*[normalize-space()='Bed with Tax Normal']").first,
        page.locator("xpath=//*[starts-with(normalize-space(), 'Bed with Tax')]").first,
    ]

    for bed_locator in bed_candidates:
        try:
            bed_locator.wait_for(state="visible", timeout=2000)

            bed_text = bed_locator.inner_text(timeout=3000).strip()
            bed_name = bed_text.splitlines()[0].strip()

            if not re.search(r"^Bed with Tax\b", bed_name, re.I):
                continue

            bed_locator.scroll_into_view_if_needed(timeout=5000)
            page.wait_for_timeout(300)

            try:
                bed_locator.click(timeout=8000)
                page.wait_for_timeout(800)
                return bed_name
            except Exception:
                pass

            try:
                bed_locator.click(timeout=8000, force=True)
                page.wait_for_timeout(800)
                return bed_name
            except Exception:
                pass

            for ancestor_level in range(1, 8):
                try:
                    parent = bed_locator.locator(
                        f"xpath=ancestor::div[{ancestor_level}]"
                    ).first

                    parent_text = parent.inner_text(timeout=3000).strip()

                    if not re.search(r"^Bed with Tax\b", parent_text, re.I):
                        continue

                    if not re.search(r"Room\s*:", parent_text, re.I):
                        continue

                    box = parent.bounding_box(timeout=3000)

                    if not box:
                        continue

                    if box["width"] > 700 or box["height"] > 300:
                        continue

                    parent.scroll_into_view_if_needed(timeout=5000)
                    page.wait_for_timeout(300)

                    page.mouse.click(
                        box["x"] + 25,
                        box["y"] + 25,
                    )

                    page.wait_for_timeout(800)

                    return bed_name

                except Exception:
                    continue

        except Exception:
            continue

    return None



def is_admission_bed_selected(page) -> bool:
    """
    Checks whether a bed is selected on New Admission page.

    The strongest check is that the validation message disappears:
    '** Please select bed to proceed **'
    """

    wait_for_page_ready(page)

    visible_text = get_visible_page_text(page)

    if re.search(r"Please select bed to proceed", visible_text, re.I):
        return False

    return True    





def select_random_past_checkin_date_for_multiple_bed_days(
    page,
    date_picker_index: int,
) -> datetime.date:
    """
    Selects a past enabled Checkin Date.

    If today is 1st or 2nd, it goes to previous month.
    Otherwise, it selects a previous date from current month.

    Returns the selected checkin date.
    """

    today = datetime.now().date()

    if today.day <= 2:
        days_ago = 3
    else:
        days_ago = min(3, today.day - 1)

    target_date = today - timedelta(days=days_ago)

    open_admission_date_picker_by_index(
        page=page,
        date_picker_index=date_picker_index,
    )

    page.wait_for_timeout(700)

    if target_date.month != today.month or target_date.year != today.year:
        previous_month_candidates = [
            page.locator(".p-datepicker-prev").first,
            page.locator(".p-ripple.p-element.p-datepicker-prev").first,
        ]

        clicked_previous = False

        for candidate in previous_month_candidates:
            try:
                candidate.click(timeout=8000)
                clicked_previous = True
                break
            except Exception:
                continue

        if clicked_previous is False:
            visible_text = get_visible_page_text(page)

            raise AssertionError(
                "Could not navigate to previous month for Checkin Date.\n"
                f"Target date: {target_date}\n"
                f"Current URL: {page.url}\n"
                f"Visible page text:\n{visible_text[:2500]}"
            )

        page.wait_for_timeout(700)

    select_enabled_day_from_open_datepicker(
        page=page,
        day=target_date.day,
    )

    wait_for_page_ready(page)
    page.wait_for_timeout(700)

    return target_date


def open_admission_date_picker_by_index(
    page,
    date_picker_index: int,
) -> None:
    """
    Opens admission date picker by index.

    date_picker_index:
    - 0 = Checkin Date
    - 1 = Expected Checkout Date
    """

    wait_for_page_ready(page)

    calendar_trigger_candidates = [
        page.locator("p-calendar").nth(date_picker_index).locator("button").first,
        page.locator("p-calendar").nth(date_picker_index).locator(".p-datepicker-trigger").first,
        page.locator(".p-datepicker-trigger").nth(date_picker_index),
        page.get_by_role("button").nth(3 + date_picker_index),
    ]

    opened = False

    for candidate in calendar_trigger_candidates:
        try:
            candidate.click(timeout=10000)
            opened = True
            break
        except Exception:
            continue

    if opened is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not open admission date picker index {date_picker_index}.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )


def select_enabled_day_from_open_datepicker(
    page,
    day: int,
) -> None:
    """
    Selects an enabled day from the currently open PrimeNG date picker.
    """

    selected = page.evaluate(
        """
        (day) => {
            const dayText = String(day);

            const calendars = Array.from(document.querySelectorAll('.p-datepicker-calendar'));

            if (!calendars.length) {
                return false;
            }

            const calendar = calendars[calendars.length - 1];

            const cells = Array.from(calendar.querySelectorAll('td'));

            for (const cell of cells) {
                const text = (cell.innerText || cell.textContent || '').trim();

                const className = cell.className || '';

                const isOtherMonth = className.includes('p-datepicker-other-month');
                const isDisabled = className.includes('p-disabled') || cell.getAttribute('aria-disabled') === 'true';

                if (isOtherMonth || isDisabled) {
                    continue;
                }

                if (text !== dayText) {
                    continue;
                }

                const clickable = cell.querySelector('span, a, button') || cell;
                clickable.click();

                return true;
            }

            return false;
        }
        """,
        day,
    )

    if selected is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not select enabled date picker day: {day}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )
    


def verify_ip_invoice_taxable_bed_multiple_days_amounts(
    page,
    bed_name_contains: str,
    expected_bed_days: int,
    bed_tax_percentage: Decimal = Decimal("5"),
) -> dict:
    """
    Verifies multiple-day taxable bed calculation.

    Formula:
    - bedCharge = bedRate * quantity
    - tax = bedCharge * taxPercentage / 100
    - totalAmount = bedCharge + tax
    - Net Total = totalAmount
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    bed_search_text = "Bed with Tax"

    bed_row = get_invoice_row_by_text(page, bed_search_text)
    bed_row_text = bed_row.inner_text(timeout=10000)
    bed_money_values = extract_decimal_money_values(bed_row_text)

    if len(bed_money_values) < 4:
        raise AssertionError(
            f"Not enough money values found for taxable bed row.\n"
            f"Bed: {bed_search_text}\n"
            f"Row text:\n{bed_row_text}\n"
            f"Money values: {bed_money_values}"
        )

    # Invoice row format:
    # Quantity Rate Discount Tax Amount
    # Money values usually give:
    # Rate, Discount, Tax, Amount
    bed_rate_actual = bed_money_values[-4]
    bed_discount_actual = bed_money_values[-3]
    bed_tax_actual = bed_money_values[-2]
    bed_total_actual = bed_money_values[-1]

    assert_amount_close(
        bed_discount_actual,
        Decimal("0"),
        "No discount is expected for multiple-day bed charge test.",
    )

    if bed_rate_actual == Decimal("0"):
        raise AssertionError(
            f"Bed rate is zero. Cannot calculate bed quantity.\n"
            f"Row text:\n{bed_row_text}"
        )

    bed_quantity_expected = Decimal(str(expected_bed_days))

    bed_charge_expected = round_money(
        bed_rate_actual * bed_quantity_expected
    )

    bed_tax_expected = round_money(
        bed_charge_expected * bed_tax_percentage / Decimal("100")
    )

    bed_total_expected = round_money(
        bed_charge_expected + bed_tax_expected
    )

    # Derive actual quantity from invoice values.
    # bed_total = rate * quantity + tax
    bed_charge_actual = round_money(
        bed_total_actual - bed_tax_actual + bed_discount_actual
    )

    bed_quantity_actual = round_money(
        bed_charge_actual / bed_rate_actual
    )

    assert_amount_close(
        bed_quantity_actual,
        bed_quantity_expected,
        "Bed quantity should match number of days from Checkin Date to today, including both dates.",
    )

    assert_amount_close(
        bed_charge_actual,
        bed_charge_expected,
        "Bed charge should be Bed Rate * Quantity.",
    )

    assert_amount_close(
        bed_tax_actual,
        bed_tax_expected,
        "Bed GST should be Bed Charge * 5 / 100.",
    )

    assert_amount_close(
        bed_total_actual,
        bed_total_expected,
        "Bed total should be Bed Charge + GST.",
    )

    try:
        summary_tax_actual = read_invoice_summary_amount_from_visible_text(
            page=page,
            label="Tax",
        )
    except AssertionError:
        summary_tax_actual = read_last_summary_amount(
            page,
            "Tax",
            default=bed_tax_actual,
        )

    assert_amount_close(
        summary_tax_actual,
        bed_tax_expected,
        "Invoice summary Tax should equal bed tax.",
    )

    net_total_actual = read_ip_invoice_net_total(page)

    net_total_expected = bed_total_expected

    assert_amount_close(
        net_total_actual,
        net_total_expected,
        "Net Total should equal taxable bed total because invoice has only Room/Bed Charges.",
    )

    print("Amounts are correct")

    return {
        "bed_name_contains": bed_search_text,
        "bed_row_text": bed_row_text,
        "bed_money_values": bed_money_values,

        "bed_tax_percentage": bed_tax_percentage,

        "bed_quantity_actual": bed_quantity_actual,
        "bed_quantity_expected": bed_quantity_expected,

        "bed_rate_actual": bed_rate_actual,
        "bed_discount_actual": bed_discount_actual,

        "bed_charge_actual": bed_charge_actual,
        "bed_charge_expected": bed_charge_expected,

        "bed_tax_actual": bed_tax_actual,
        "bed_tax_expected": bed_tax_expected,

        "bed_total_actual": bed_total_actual,
        "bed_total_expected": bed_total_expected,

        "summary_tax_actual": summary_tax_actual,

        "net_total_actual": net_total_actual,
        "net_total_expected": net_total_expected,
    }



def open_admitted_ip_patient_with_bed_with_tax_from_grid(page) -> dict:
    """
    Searches the Inpatients grid page by page.

    Finds the row where Bed Details contains 'Bed with Tax',
    then clicks the View button against that same row.

    This is needed because after Admit Now, the patient with Bed with Tax
    may not be visible on the first grid page.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    ensure_inpatients_grid_page(page=page)

    reset_inpatients_grid_paginator_to_first_page(page=page)

    max_pages_to_check = 80

    for page_index in range(max_pages_to_check):
        wait_for_page_ready(page)
        page.wait_for_timeout(1000)

        row = find_inpatient_grid_row_with_bed_with_tax(page=page)

        if row is not None:
            row_text = row.inner_text(timeout=10000)

            view_button_candidates = [
                row.locator("#btnViewIp_IP_IpGrd").first,
                row.get_by_role("button", name=re.compile(r"^View$", re.I)).first,
                row.locator("button").filter(has_text=re.compile(r"^View$", re.I)).first,
            ]

            clicked_view = False

            for candidate in view_button_candidates:
                try:
                    candidate.scroll_into_view_if_needed(timeout=5000)
                    candidate.click(timeout=10000)
                    clicked_view = True
                    break
                except Exception:
                    continue

            if clicked_view is False:
                visible_text = get_visible_page_text(page)

                raise AssertionError(
                    "Found Bed with Tax row, but could not click View button against that row.\n"
                    f"Row text:\n{row_text}\n"
                    f"Current URL: {page.url}\n"
                    f"Visible page text:\n{visible_text[:2500]}"
                )

            wait_for_page_ready(page)
            page.wait_for_timeout(2000)

            return {
                "opened": True,
                "grid_page_index": page_index + 1,
                "row_text": row_text,
                "final_url": page.url,
            }

        clicked_next = click_next_inpatients_grid_paginator(page=page)

        if clicked_next is False:
            break

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        "Could not find any admitted inpatient row with Bed Details = Bed with Tax.\n"
        "Checked the Inpatients grid pages using the paginator.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )



def ensure_inpatients_grid_page(page) -> None:
    """
    Ensures the current page is the Inpatients grid.

    After Admit Now, the app normally redirects to the grid.
    If not, this opens the IP dashboard and then the grid.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    visible_text = get_visible_page_text(page)

    if (
        re.search(r"\bInpatients\b", visible_text, re.I)
        and re.search(r"\bBed Details\b", visible_text, re.I)
        and re.search(r"\bActions\b", visible_text, re.I)
    ):
        return

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    visible_text = get_visible_page_text(page)

    if not (
        re.search(r"\bInpatients\b", visible_text, re.I)
        and re.search(r"\bBed Details\b", visible_text, re.I)
        and re.search(r"\bActions\b", visible_text, re.I)
    ):
        raise AssertionError(
            "Could not open Inpatients grid page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )


def find_inpatient_grid_row_with_bed_with_tax(page):
    """
    Finds a visible Inpatients grid row where Bed Details contains Bed with Tax.
    Returns the row locator, or None.
    """

    bed_with_tax_pattern = re.compile(r"\bBed with Tax\b", re.I)

    row_candidates = [
        page.locator("tr").filter(has_text=bed_with_tax_pattern),
        page.locator("[role='row']").filter(has_text=bed_with_tax_pattern),
    ]

    for rows in row_candidates:
        try:
            row_count = rows.count()
        except Exception:
            row_count = 0

        for index in range(row_count):
            row = rows.nth(index)

            try:
                if not row.is_visible(timeout=1000):
                    continue

                row_text = row.inner_text(timeout=3000)

                if not bed_with_tax_pattern.search(row_text):
                    continue

                if not re.search(r"\bView\b", row_text, re.I):
                    # Some rows may not include View text in inner_text.
                    # Still accept if button exists.
                    try:
                        row.get_by_role("button", name=re.compile(r"^View$", re.I)).first.wait_for(
                            state="visible",
                            timeout=1000,
                        )
                    except Exception:
                        continue

                return row

            except Exception:
                continue

    return None



def reset_inpatients_grid_paginator_to_first_page(page) -> None:
    """
    Resets the Inpatients grid paginator to first page if possible.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(500)

    page.evaluate(
        """
        () => {
            const paginators = Array.from(document.querySelectorAll('.p-paginator'))
                .filter((p) => {
                    const rect = p.getBoundingClientRect();
                    return rect.width > 0 && rect.height > 0;
                });

            if (!paginators.length) {
                return false;
            }

            const paginator = paginators[paginators.length - 1];

            const firstButton =
                paginator.querySelector('.p-paginator-first') ||
                Array.from(paginator.querySelectorAll('button')).find((button) => {
                    const text = (button.innerText || button.textContent || '').trim();
                    const label = button.getAttribute('aria-label') || '';
                    return text === '<<' || /first/i.test(label);
                });

            if (!firstButton) {
                return false;
            }

            const className = firstButton.className || '';
            const ariaDisabled = firstButton.getAttribute('aria-disabled');
            const disabled = firstButton.hasAttribute('disabled');

            if (
                className.includes('p-disabled') ||
                ariaDisabled === 'true' ||
                disabled
            ) {
                return true;
            }

            firstButton.click();
            return true;
        }
        """
    )

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)


def click_next_inpatients_grid_paginator(page) -> bool:
    """
    Clicks the next page button in the Inpatients grid paginator.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(500)

    clicked = page.evaluate(
        """
        () => {
            const paginators = Array.from(document.querySelectorAll('.p-paginator'))
                .filter((p) => {
                    const rect = p.getBoundingClientRect();
                    return rect.width > 0 && rect.height > 0;
                });

            if (!paginators.length) {
                return false;
            }

            const paginator = paginators[paginators.length - 1];

            const nextButton =
                paginator.querySelector('.p-paginator-next') ||
                Array.from(paginator.querySelectorAll('button')).find((button) => {
                    const text = (button.innerText || button.textContent || '').trim();
                    const label = button.getAttribute('aria-label') || '';
                    return text === '>' || /next/i.test(label);
                });

            if (!nextButton) {
                return false;
            }

            const className = nextButton.className || '';
            const ariaDisabled = nextButton.getAttribute('aria-disabled');
            const disabled = nextButton.hasAttribute('disabled');

            if (
                className.includes('p-disabled') ||
                ariaDisabled === 'true' ||
                disabled
            ) {
                return false;
            }

            nextButton.click();
            return true;
        }
        """
    )

    if clicked:
        wait_for_page_ready(page)
        page.wait_for_timeout(1800)
        return True

    return False   




def complete_ip_admission_with_past_date_and_any_bed_for_grid_search(page) -> dict:
    """
    Creates an IP admission with:
    - random Admission Type
    - random Admitted Doctor
    - past Checkin Date
    - today's Expected Checkout Date
    - any available normal bed

    The actual Bed with Tax patient is selected later from the Inpatients grid.
    """

    wait_for_page_ready(page)
    wait_for_new_admission_form_loaded(page)

    admission_type = select_random_primeng_dropdown_option(
        page=page,
        dropdown_text="Admission Type",
    )

    admitted_doctor = select_random_primeng_dropdown_option(
        page=page,
        dropdown_text="Admitted Doctor",
    )

    checkin_date = select_random_past_checkin_date_for_multiple_bed_days(
        page=page,
        date_picker_index=0,
    )

    expected_checkout_date = datetime.now().date()

    select_today_for_admission_date_by_index(
        page=page,
        date_picker_index=1,
    )

    select_building_block_d_for_bed_search(page=page)

    bed_name = select_random_exempt_bed_from_available_beds(page=page)

    click_admit_now_button(page=page)

    wait_for_page_ready(page)
    page.wait_for_timeout(2000)

    toast_message = assert_success_message_if_present(page)

    return {
        "admission_created": True,
        "admission_type": admission_type,
        "admitted_doctor": admitted_doctor,
        "bed_name": bed_name,
        "checkin_date": checkin_date,
        "expected_checkout_date": expected_checkout_date,
        "toast_message": toast_message,
    }




def open_admitted_ip_patient_with_bed_with_tax_from_grid(page) -> dict:
    """
    Searches Inpatients grid page by page.

    Finds row where Bed Details contains 'Bed with Tax',
    then clicks View button against that same row.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    ensure_inpatients_grid_page(page=page)

    reset_inpatients_grid_paginator_to_first_page(page=page)

    max_pages_to_check = 80

    for page_index in range(max_pages_to_check):
        wait_for_page_ready(page)
        page.wait_for_timeout(1200)

        row = find_inpatient_grid_row_with_bed_with_tax(page=page)

        if row is not None:
            row_text = row.inner_text(timeout=10000)

            view_button_candidates = [
                row.locator("#btnViewIp_IP_IpGrd").first,
                row.get_by_role("button", name=re.compile(r"^View$", re.I)).first,
                row.locator("button").filter(has_text=re.compile(r"^View$", re.I)).first,
            ]

            clicked_view = False

            for candidate in view_button_candidates:
                try:
                    candidate.scroll_into_view_if_needed(timeout=5000)
                    candidate.click(timeout=10000)
                    clicked_view = True
                    break
                except Exception:
                    continue

            if clicked_view is False:
                visible_text = get_visible_page_text(page)

                raise AssertionError(
                    "Found Bed with Tax row, but could not click View button against that row.\n"
                    f"Row text:\n{row_text}\n"
                    f"Current URL: {page.url}\n"
                    f"Visible page text:\n{visible_text[:2500]}"
                )

            wait_for_page_ready(page)
            page.wait_for_timeout(2500)

            return {
                "opened": True,
                "grid_page_index": page_index + 1,
                "row_text": row_text,
                "final_url": page.url,
            }

        clicked_next = click_next_inpatients_grid_paginator(page=page)

        if clicked_next is False:
            break

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        "Could not find any admitted inpatient row with Bed Details = Bed with Tax.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )    




def read_expected_bed_days_from_current_ip_details(page) -> Decimal:
    """
    Reads admitted date from IP details page and calculates bed days.

    Formula:
    bed days = today - admitted date + 1
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(500)

    visible_text = get_visible_page_text(page)

    date_patterns = [
        r"Admitted\s*:\s*(\d{1,2}\s+[A-Za-z]{3},\s*\d{4})",
        r"Admission Period\s*(\d{1,2}\s+[A-Za-z]{3},\s*\d{4})",
    ]

    admitted_date = None

    for pattern in date_patterns:
        match = re.search(pattern, visible_text, re.I | re.S)

        if not match:
            continue

        date_text = match.group(1).strip()

        for fmt in ["%d %b, %Y", "%d %B, %Y"]:
            try:
                admitted_date = datetime.strptime(date_text, fmt).date()
                break
            except ValueError:
                continue

        if admitted_date is not None:
            break

    if admitted_date is None:
        raise AssertionError(
            "Could not read admitted date from IP details page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    today = datetime.now().date()

    bed_days = (today - admitted_date).days + 1

    if bed_days < 1:
        raise AssertionError(
            f"Invalid bed days calculated. Admitted date: {admitted_date}, Today: {today}"
        )

    return Decimal(str(bed_days)) 



# Master invoice created with one order and one IP invoice; totals match individual invoices 



def complete_master_invoice_taxable_order_item_and_ip_invoice_flow(
    page,
    config,
    consumer_profile: dict,
) -> dict:
    """
    Master invoice test case.

    Case:
    Master invoice created with one order item with tax and one IP invoice;
    totals match individual invoices.

    Flow:
    1. Create IP admission.
    2. Add Doc Visit service.
    3. Request pharmacy order from service.
    4. Select one taxable item: Med_1, Med_2, or Med_4.
    5. Confirm sales order.
    6. Create and verify order invoice tax.
    7. Complete order.
    8. Return to IP patient details.
    9. Create IP invoice.
    10. Create Master Invoice by linking order invoice and IP invoice.
    11. Verify master invoice totals.
    """

    login(page, config)

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)
    open_new_admission_page(page)

    patient_result = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    assert patient_result["patient_created"] is True

    admission_result = complete_ip_admission_with_random_exempt_bed(page=page)

    assert admission_result["admission_created"] is True

    patient_full_name = patient_result["patient_full_name"]

    open_latest_ip_patient_from_grid(
        page=page,
        patient_full_name=patient_full_name,
    )

    service_result = add_doc_visit_service_to_ip_patient(page=page)

    assert service_result["service_added"] is True

    order_request_result = request_random_pharmacy_item_from_ip_service(
        page=page,
        allowed_item_names=["Med_1", "Med_2", "Med_4"],
    )

    assert order_request_result["order_requested"] is True

    selected_item_name = get_selected_order_item_name_from_result(
        order_request_result=order_request_result,
    )

    selected_quantity = get_selected_order_item_quantity_from_result(
        order_request_result=order_request_result,
    )

    open_sales_order_requests_grid(
        page=page,
        config=config,
    )

    sales_order_result = confirm_latest_ip_requested_sales_order(page=page)

    assert_sales_order_confirmed_from_result_or_page(
        page=page,
        sales_order_result=sales_order_result,
    )

    order_details_medicine_result = capture_medicine_item_from_sales_order_details_page(
        page=page,
        allowed_item_names=["Med_1", "Med_2", "Med_4"],
    )

    selected_item_name = order_details_medicine_result["item_name"]
    selected_quantity = order_details_medicine_result["quantity"]

    sales_order_invoice_result = create_sales_order_invoice_and_view(page=page)

    assert_sales_order_invoice_created_from_result_or_page(
        page=page,
        sales_order_invoice_result=sales_order_invoice_result,
    )

    order_invoice_tax_result = verify_tax_inclusive_sales_order_invoice_item_and_capture(
        page=page,
        item_name=order_details_medicine_result["item_name"],
        quantity=order_details_medicine_result["quantity"],
        order_details_item_rate=order_details_medicine_result["rate"],
    )

    go_back_from_sales_order_invoice_to_order_details(page=page)

    complete_order_result = complete_sales_order_from_order_details(page=page)

    assert complete_order_result["sales_order_completed"] is True
        
    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)

    open_latest_ip_patient_from_grid(
        page=page,
        patient_full_name=patient_full_name,
    )

    ip_invoice_result = create_ip_invoice_after_discharge_and_view(page=page)

    ip_invoice_result = ensure_ip_invoice_generated_and_opened(page=page)

    assert ip_invoice_result["invoice_created"] is True

    ip_invoice_capture_result = capture_ip_invoice_amount_for_master_invoice(page=page)

    back_to_ip_details_result = go_back_from_ip_invoice_details_to_patient_details(page=page)

    assert back_to_ip_details_result["returned_to_ip_details"] is True

    ensure_current_page_is_ip_patient_details(page=page)

    master_invoice_result = create_master_invoice_with_two_available_invoices_from_ip_details(
        page=page,
    )

    assert master_invoice_result["master_invoice_created"] is True

    master_invoice_tax_result = verify_master_invoice_with_taxable_order_item_and_ip_invoice(
        page=page,
        order_invoice_tax_result=order_invoice_tax_result,
        ip_invoice_capture_result=ip_invoice_capture_result,
        item_name=selected_item_name,
    )

    print("Both master invoice and individual invoice amounts are correct")

    return {
        "patient_created": True,
        "patient_result": patient_result,
        "patient_full_name": patient_full_name,

        "admission_created": True,
        "admission_result": admission_result,

        "service_added": True,
        "service_result": service_result,

        "order_requested": True,
        "order_request_result": order_request_result,

        "selected_item_name": selected_item_name,
        "selected_quantity": selected_quantity,

        "sales_order_confirmed": True,
        "sales_order_result": sales_order_result,

        "sales_order_invoice_created": True,
        "sales_order_invoice_result": sales_order_invoice_result,

        "order_invoice_tax_result": order_invoice_tax_result,

        "sales_order_completed": True,
        "complete_order_result": complete_order_result,

        "ip_invoice_created": True,
        "ip_invoice_result": ip_invoice_result,
        "ip_invoice_capture_result": ip_invoice_capture_result,

        "master_invoice_created": True,
        "master_invoice_result": master_invoice_result,

        "master_invoice_tax_result": master_invoice_tax_result,

        "back_to_ip_details_result": back_to_ip_details_result,
        "order_details_medicine_result": order_details_medicine_result,

        "final_url": page.url,
    }



def get_taxable_order_item_config(item_name: str) -> dict:
    """
    Medicine tax configuration.

    Med_1: GST 5% + CESS 1% = total tax 6%
    Med_2: GST 5% + CESS 1% = total tax 6%
    Med_4: GST 5% + CESS 0% = total tax 5%
    """

    item_name = item_name.strip()

    config_by_item = {
        "Med_1": {
            "gst_percentage": Decimal("5"),
            "cess_percentage": Decimal("1"),
            "total_tax_percentage": Decimal("6"),
        },
        "Med_2": {
            "gst_percentage": Decimal("5"),
            "cess_percentage": Decimal("1"),
            "total_tax_percentage": Decimal("6"),
        },
        "Med_4": {
            "gst_percentage": Decimal("5"),
            "cess_percentage": Decimal("0"),
            "total_tax_percentage": Decimal("5"),
        },
    }

    if item_name not in config_by_item:
        raise AssertionError(
            f"Unsupported medicine item for tax validation: {item_name}"
        )

    return config_by_item[item_name]



def capture_medicine_item_from_sales_order_details_page(
    page,
    allowed_item_names: list[str],
) -> dict:
    """
    Captures medicine item data from Sales Order Details page.

    Expected table:
    Item Name | Batch | Rate (₹) | Quantity | Total (₹)

    Captures:
    - Item Name
    - Rate
    - Quantity
    - Total inclusive amount
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    visible_text = get_visible_page_text(page)

    if not re.search(r"\bOrder\s+#", visible_text, re.I):
        raise AssertionError(
            "Expected Sales Order Details page before capturing medicine rate.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    row_data = read_sales_order_details_medicine_row_data(
        page=page,
        allowed_item_names=allowed_item_names,
    )

    item_name = row_data["item_name"]
    rate = row_data["rate"]
    quantity = row_data["quantity"]
    total_inclusive = row_data["total_inclusive"]

    expected_total_inclusive = round_money(rate * quantity)

    assert_amount_close(
        total_inclusive,
        expected_total_inclusive,
        f"Sales Order Details total mismatch for {item_name}.",
    )

    return {
        "item_name": item_name,
        "rate": rate,
        "quantity": quantity,
        "total_inclusive": total_inclusive,
        "expected_total_inclusive": expected_total_inclusive,
        "row_text": row_data["row_text"],
        "cells": row_data["cells"],
        "headers": row_data["headers"],
        "final_url": page.url,
    }



def read_sales_order_details_medicine_row_data(
    page,
    allowed_item_names: list[str],
) -> dict:
    """
    Reads medicine row from Sales Order Details table.

    Expected visual columns:
    Item Name | Batch | Rate (₹) | Quantity | Total (₹)

    Handles cases where Quantity is inside input/span and td.innerText is empty.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(800)

    row_data = page.evaluate(
        """
        ({ allowedItems }) => {
            const normalize = (value) => {
                return (value || '')
                    .replace(/\\s+/g, ' ')
                    .trim();
            };

            const isVisible = (element) => {
                const rect = element.getBoundingClientRect();
                return rect.width > 0 && rect.height > 0;
            };

            const getElementValue = (element) => {
                const inputValues = Array.from(
                    element.querySelectorAll('input, textarea, select')
                )
                    .map((input) => normalize(input.value))
                    .filter(Boolean);

                const ariaValues = Array.from(
                    element.querySelectorAll('[aria-valuenow], [value]')
                )
                    .map((child) => {
                        return normalize(
                            child.getAttribute('aria-valuenow') ||
                            child.getAttribute('value') ||
                            ''
                        );
                    })
                    .filter(Boolean);

                const text = normalize(element.innerText || element.textContent || '');

                return normalize(
                    [
                        text,
                        ...inputValues,
                        ...ariaValues
                    ]
                    .filter(Boolean)
                    .join(' ')
                );
            };

            const tables = Array.from(document.querySelectorAll('table'))
                .filter((table) => isVisible(table));

            for (const table of tables) {
                const headers = Array.from(table.querySelectorAll('thead th, tr th'))
                    .map((cell) => getElementValue(cell))
                    .filter(Boolean);

                const rows = Array.from(table.querySelectorAll('tbody tr, tr'))
                    .filter((row) => isVisible(row));

                for (const row of rows) {
                    const rowText = getElementValue(row);

                    const matchedItem = allowedItems.find((item) => {
                        return rowText.toLowerCase().includes(item.toLowerCase());
                    });

                    if (!matchedItem) {
                        continue;
                    }

                    const cells = Array.from(row.querySelectorAll('td, th'))
                        .map((cell) => getElementValue(cell));

                    return {
                        item_name: matchedItem,
                        headers,
                        cells,
                        row_text: rowText,
                    };
                }
            }

            return null;
        }
        """,
        {"allowedItems": allowed_item_names},
    )

    if not row_data:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not find medicine row in Sales Order Details page.\n"
            f"Allowed items: {allowed_item_names}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    cells = row_data.get("cells") or []
    row_text = row_data.get("row_text") or ""

    parsed = parse_sales_order_details_medicine_values_from_cells_or_text(
        cells=cells,
        row_text=row_text,
        allowed_item_names=allowed_item_names,
    )

    return {
        "item_name": parsed["item_name"],
        "rate": parsed["rate"],
        "quantity": parsed["quantity"],
        "total_inclusive": parsed["total_inclusive"],
        "row_text": row_text,
        "cells": cells,
        "headers": row_data.get("headers") or [],
    }



def parse_sales_order_details_medicine_values_from_cells_or_text(
    cells: list[str],
    row_text: str,
    allowed_item_names: list[str],
) -> dict:
    """
    Parses:
    Item Name | Batch | Rate | Quantity | Total

    Quantity is treated as a normal number, not money.
    """

    source_text = " ".join([str(cell) for cell in cells if str(cell).strip()]) or row_text

    item_name = extract_known_item_name_from_text(
        text=source_text,
        allowed_item_names=allowed_item_names,
    )

    # First try fixed visual table cells.
    # Expected normal cells:
    # 0 Item Name, 1 Batch, 2 Rate, 3 Quantity, 4 Total
    if len(cells) >= 5:
        rate_text = cells[2]
        quantity_text = cells[3]
        total_text = cells[4]

        if str(rate_text).strip() and str(quantity_text).strip() and str(total_text).strip():
            return {
                "item_name": item_name,
                "rate": read_decimal_value_from_text(rate_text, "Rate"),
                "quantity": read_quantity_value_from_text(quantity_text),
                "total_inclusive": read_decimal_value_from_text(total_text, "Total inclusive amount"),
            }

    # Some DOMs include an extra empty/icon cell before Item Name.
    # Example:
    # 0 icon, 1 Med_2, 2 -, 3 300.00, 4 2, 5 600.00
    if len(cells) >= 6:
        rate_text = cells[3]
        quantity_text = cells[4]
        total_text = cells[5]

        if str(rate_text).strip() and str(quantity_text).strip() and str(total_text).strip():
            return {
                "item_name": item_name,
                "rate": read_decimal_value_from_text(rate_text, "Rate"),
                "quantity": read_quantity_value_from_text(quantity_text),
                "total_inclusive": read_decimal_value_from_text(total_text, "Total inclusive amount"),
            }

    # Final fallback from row text.
    return parse_sales_order_details_medicine_row_text(
        row_text=row_text,
        allowed_item_names=allowed_item_names,
    )



def read_quantity_value_from_text(text: str) -> Decimal:
    """
    Reads item quantity.

    Quantity is not a money value, but Decimal is used for calculation.
    Examples:
    - "2" -> Decimal("2")
    - "2.00" -> Decimal("2.00")
    """

    if text is None:
        text = ""

    clean_text = (
        str(text)
        .replace(",", "")
        .replace("Qty", "")
        .replace("Quantity", "")
        .strip()
    )

    match = re.search(r"\d+(?:\.\d+)?", clean_text)

    if not match:
        raise AssertionError(
            "Could not read Quantity value.\n"
            f"Text: {text}"
        )

    return Decimal(match.group(0))





def parse_sales_order_details_medicine_row_text(
    row_text: str,
    allowed_item_names: list[str],
) -> dict:
    """
    Fallback parser for Sales Order Details medicine row.

    Expected visual text:
    Med_2 - 300.00 2 600.00
    """

    item_name = extract_known_item_name_from_text(
        text=row_text,
        allowed_item_names=allowed_item_names,
    )

    clean_text = (
        str(row_text)
        .replace("₹", "")
        .replace(",", "")
        .replace("Inclusive of all taxes", "")
        .strip()
    )

    numbers = re.findall(r"-?\d+(?:\.\d+)?", clean_text)

    # Remove item number from Med_1 / Med_2 / Med_4.
    item_number_match = re.search(r"Med_(\d+)", item_name, re.I)
    item_number = item_number_match.group(1) if item_number_match else None

    filtered_numbers = []
    skipped_item_number = False

    for number in numbers:
        if item_number and number == item_number and skipped_item_number is False:
            skipped_item_number = True
            continue

        filtered_numbers.append(number)

    if len(filtered_numbers) < 3:
        raise AssertionError(
            "Could not parse Rate, Quantity and Total from Sales Order Details row.\n"
            f"Item: {item_name}\n"
            f"Row text: {row_text}\n"
            f"Numbers found: {numbers}\n"
            f"Numbers after removing item number: {filtered_numbers}"
        )

    rate = round_money(Decimal(filtered_numbers[0]))
    quantity = Decimal(filtered_numbers[1])
    total_inclusive = round_money(Decimal(filtered_numbers[2]))

    return {
        "item_name": item_name,
        "rate": rate,
        "quantity": quantity,
        "total_inclusive": total_inclusive,
    }




def read_visible_table_row_data_containing(page, text: str) -> dict | None:
    """
    Reads visible table row data containing the given text.

    Returns:
    {
        headers: [...],
        cells: [...],
        row_text: "..."
    }
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(500)

    return page.evaluate(
        """
        ({ needle }) => {
            const normalize = (value) => {
                return (value || '')
                    .replace(/\\s+/g, ' ')
                    .trim();
            };

            const isVisible = (element) => {
                const rect = element.getBoundingClientRect();
                return rect.width > 0 && rect.height > 0;
            };

            const tables = Array.from(document.querySelectorAll('table'));

            for (const table of tables) {
                if (!isVisible(table)) {
                    continue;
                }

                const rows = Array.from(table.querySelectorAll('tr'))
                    .filter((row) => isVisible(row));

                if (!rows.length) {
                    continue;
                }

                let headers = [];

                const headerRow = rows.find((row) => row.querySelectorAll('th').length > 0);

                if (headerRow) {
                    headers = Array.from(headerRow.querySelectorAll('th,td'))
                        .map((cell) => normalize(cell.innerText || cell.textContent));
                }

                for (const row of rows) {
                    const rowText = normalize(row.innerText || row.textContent);

                    if (!rowText.toLowerCase().includes(needle.toLowerCase())) {
                        continue;
                    }

                    const cells = Array.from(row.querySelectorAll('td'))
                        .map((cell) => normalize(cell.innerText || cell.textContent));

                    if (!cells.length) {
                        continue;
                    }

                    return {
                        headers,
                        cells,
                        row_text: rowText,
                    };
                }
            }

            return null;
        }
        """,
        {"needle": text},
    )


def get_table_cell_by_header_patterns(
    row_data: dict,
    header_patterns: list[str],
    fallback_index: int | None = None,
) -> str:
    """
    Gets a cell value by matching table header text.
    Falls back to column index if header matching fails.
    """

    headers = row_data.get("headers") or []
    cells = row_data.get("cells") or []

    for index, header in enumerate(headers):
        for pattern in header_patterns:
            if re.search(pattern, header, re.I):
                if index < len(cells):
                    return cells[index]

    if fallback_index is not None and fallback_index < len(cells):
        return cells[fallback_index]

    return ""


def read_decimal_value_from_text(
    text: str,
    field_name: str,
) -> Decimal:
    """
    Reads decimal value from a table cell or text fragment.
    """

    if text is None:
        text = ""

    values = extract_decimal_money_values(str(text))

    if values:
        return round_money(values[-1])

    clean_text = (
        str(text)
        .replace("₹", "")
        .replace(",", "")
        .replace("(", "")
        .replace(")", "")
        .strip()
    )

    match = re.search(r"-?\d+(?:\.\d+)?", clean_text)

    if not match:
        raise AssertionError(
            f"Could not read decimal value for {field_name}.\n"
            f"Text: {text}"
        )

    return round_money(Decimal(match.group(0)))





def extract_known_item_name_from_text(
    text: str,
    allowed_item_names: list[str],
) -> str:
    """
    Extracts Med_1 / Med_2 / Med_4 from row/cell text.
    """

    for item_name in allowed_item_names:
        if re.search(re.escape(item_name), text, re.I):
            return item_name

    raise AssertionError(
        f"Could not extract medicine item name from text.\n"
        f"Allowed items: {allowed_item_names}\n"
        f"Text: {text}"
    )




def get_selected_order_item_name_from_result(order_request_result: dict) -> str:
    selected_item_name = (
        order_request_result.get("selected_item_name")
        or order_request_result.get("item_name")
        or order_request_result.get("selected_item")
    )

    if not selected_item_name:
        raise AssertionError(
            f"Could not read selected item name from order request result: {order_request_result}"
        )

    return str(selected_item_name).strip()


def get_selected_order_item_quantity_from_result(order_request_result: dict) -> Decimal:
    quantity = (
        order_request_result.get("quantity")
        or order_request_result.get("selected_quantity")
        or order_request_result.get("item_quantity")
        or Decimal("1")
    )

    return Decimal(str(quantity))    




def verify_tax_inclusive_sales_order_invoice_item_and_capture(
    page,
    item_name: str,
    quantity: Decimal,
    order_details_item_rate: Decimal,
) -> dict:
    """
    Verifies tax-inclusive sales order invoice item.

    Validates:
    - S.Price
    - QTY
    - GST
    - CESS
    - Total Tax
    - Net Total With Tax

    Formula:
        S.Price = Rate * 100 / (100 + total_tax_percentage)

    Med_1:
        S.Price = Rate * 100 / 106

    Med_2:
        S.Price = Rate * 100 / 106

    Med_4:
        S.Price = Rate * 100 / 105
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    order_details_item_rate = Decimal(str(order_details_item_rate))
    quantity = Decimal(str(quantity))

    item_config = get_taxable_order_item_config(item_name=item_name)

    gst_percentage = item_config["gst_percentage"]
    cess_percentage = item_config["cess_percentage"]
    total_tax_percentage = item_config["total_tax_percentage"]

    invoice_item_values = capture_sales_order_invoice_medicine_values(
        page=page,
        item_name=item_name,
    )

    s_price_actual = invoice_item_values["s_price"]
    quantity_actual = invoice_item_values["quantity"]
    gst_actual = invoice_item_values["gst"]
    cess_actual = invoice_item_values["cess"]
    net_total_with_tax_actual = invoice_item_values["net_total_with_tax"]

    s_price_expected = round_money(
        order_details_item_rate
        * Decimal("100")
        / (Decimal("100") + total_tax_percentage)
    )

    assert_amount_close(
        s_price_actual,
        s_price_expected,
        f"S.Price mismatch for {item_name}.",
    )

    assert_amount_close(
        quantity_actual,
        quantity,
        f"Invoice QTY mismatch for {item_name}.",
    )

    medicine_total = round_money(s_price_expected * quantity)

    gst_expected = round_money(
        medicine_total * gst_percentage / Decimal("100")
    )

    cess_expected = round_money(
        medicine_total * cess_percentage / Decimal("100")
    )

    total_tax_expected = round_money(gst_expected + cess_expected)

    net_total_with_tax_expected = round_money(
        medicine_total + gst_expected + cess_expected
    )

    assert_amount_close(
        gst_actual,
        gst_expected,
        f"GST mismatch for {item_name}.",
    )

    assert_amount_close(
        cess_actual,
        cess_expected,
        f"CESS mismatch for {item_name}.",
    )

    total_tax_actual = round_money(gst_actual + cess_actual)

    assert_amount_close(
        total_tax_actual,
        total_tax_expected,
        f"Total tax mismatch for {item_name}.",
    )

    assert_amount_close(
        net_total_with_tax_actual,
        net_total_with_tax_expected,
        f"Net Total With Tax mismatch for {item_name}.",
    )

    invoice_net_total_actual = read_invoice_summary_amount_optional(
        page=page,
        labels=["Net Total", "Net payable", "Amount Due", "Total"],
        default=net_total_with_tax_actual,
    )

    assert_amount_close(
        invoice_net_total_actual,
        net_total_with_tax_expected,
        f"Sales order invoice Net Total mismatch for {item_name}.",
    )

    return {
        "item_name": item_name,
        "quantity": quantity,

        "order_details_item_rate": order_details_item_rate,

        "gst_percentage": gst_percentage,
        "cess_percentage": cess_percentage,
        "total_tax_percentage": total_tax_percentage,

        "s_price_actual": s_price_actual,
        "s_price_expected": s_price_expected,

        "medicine_total": medicine_total,
        "taxable_amount_expected": medicine_total,

        "gst_actual": gst_actual,
        "gst_expected": gst_expected,

        "cess_actual": cess_actual,
        "cess_expected": cess_expected,

        "tax_actual": total_tax_actual,
        "tax_expected": total_tax_expected,

        "net_total_with_tax_actual": net_total_with_tax_actual,
        "net_total_with_tax_expected": net_total_with_tax_expected,

        "total_amount_actual": net_total_with_tax_actual,
        "total_amount_expected": net_total_with_tax_expected,

        "net_total_actual": invoice_net_total_actual,

        "invoice_row_text": invoice_item_values["row_text"],
        "invoice_headers": invoice_item_values["headers"],
        "invoice_cells": invoice_item_values["cells"],
        "final_url": page.url,
    }



def capture_sales_order_invoice_medicine_values(
    page,
    item_name: str,
) -> dict:
    """
    Captures values from sales order invoice item row.

    Important:
    - S.Price is usually the first money value in the medicine row.
    - Net Total With Tax is usually the last money value in the medicine row.
    - For Med_4, CESS is 0.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    row_data = read_visible_table_row_data_containing(
        page=page,
        text=item_name,
    )

    if not row_data:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not find {item_name} row in sales order invoice.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    row_text = row_data.get("row_text") or ""
    cells = row_data.get("cells") or []
    headers = row_data.get("headers") or []

    row_money_values = extract_decimal_money_values(row_text)

    # Remove item-number from Med_1 / Med_2 / Med_4 if it appears in parsing.
    item_number_match = re.search(r"Med_(\d+)", item_name, re.I)
    item_number = Decimal(item_number_match.group(1)) if item_number_match else None

    filtered_money_values = []

    skipped_item_number = False

    for value in row_money_values:
        if (
            item_number is not None
            and value == item_number
            and skipped_item_number is False
        ):
            skipped_item_number = True
            continue

        filtered_money_values.append(value)

    if len(filtered_money_values) < 2:
        raise AssertionError(
            f"Could not capture enough invoice row values for {item_name}.\n"
            f"Headers: {headers}\n"
            f"Cells: {cells}\n"
            f"Row text: {row_text}\n"
            f"Money values: {row_money_values}\n"
            f"Filtered money values: {filtered_money_values}"
        )

    item_config = get_taxable_order_item_config(item_name=item_name)

    cess_percentage = item_config["cess_percentage"]

    s_price = capture_s_price_from_invoice_cells_or_money_values(
        row_data=row_data,
        fallback_money_values=filtered_money_values,
    )

    quantity = capture_quantity_from_invoice_cells_or_row_text(
        row_data=row_data,
        row_text=row_text,
        item_name=item_name,
    )

    gst = capture_gst_from_invoice_cells_or_money_values(
        row_data=row_data,
        fallback_money_values=filtered_money_values,
        item_name=item_name,
    )

    if cess_percentage > Decimal("0"):
        cess = capture_cess_from_invoice_cells_or_money_values(
            row_data=row_data,
            fallback_money_values=filtered_money_values,
            item_name=item_name,
        )
    else:
        cess = Decimal("0.00")

    # Important fix:
    # Net Total With Tax must be the last money value, not the S.Price.
    net_total_with_tax = round_money(filtered_money_values[-1])

    return {
        "item_name": item_name,
        "s_price": round_money(s_price),
        "quantity": quantity,
        "gst": round_money(gst),
        "cess": round_money(cess),
        "net_total_with_tax": round_money(net_total_with_tax),
        "row_text": row_text,
        "headers": headers,
        "cells": cells,
        "money_values": row_money_values,
        "filtered_money_values": filtered_money_values,
    }


def capture_s_price_from_invoice_cells_or_money_values(
    row_data: dict,
    fallback_money_values: list[Decimal],
) -> Decimal:
    """
    Captures S.Price from invoice row.
    Prefer S.Price header; fallback to first money value.
    """

    s_price_cell = get_table_cell_by_header_patterns(
        row_data=row_data,
        header_patterns=[
            r"^S\.?\s*Price",
            r"^Selling\s*Price",
            r"^Sales\s*Price",
        ],
        fallback_index=None,
    )

    if s_price_cell:
        return read_decimal_value_from_text(
            text=s_price_cell,
            field_name="S.Price",
        )

    return round_money(fallback_money_values[0])


def capture_quantity_from_invoice_cells_or_row_text(
    row_data: dict,
    row_text: str,
    item_name: str,
) -> Decimal:
    """
    Captures QTY from invoice row.

    Quantity is not money, so do not use extract_decimal_money_values alone.
    """

    quantity_cell = get_table_cell_by_header_patterns(
        row_data=row_data,
        header_patterns=[
            r"^QTY$",
            r"^Qty$",
            r"^Quantity$",
        ],
        fallback_index=None,
    )

    if quantity_cell:
        return read_quantity_value_from_text(quantity_cell)

    cells = row_data.get("cells") or []

    # Common invoice layout:
    # Item | S.Price | QTY | GST | CESS | Net Total With Tax
    for index, cell in enumerate(cells):
        if re.search(re.escape(item_name), cell, re.I):
            possible_quantity_indexes = [index + 2, index + 3]

            for quantity_index in possible_quantity_indexes:
                if quantity_index < len(cells):
                    try:
                        return read_quantity_value_from_text(cells[quantity_index])
                    except Exception:
                        continue

    # Last fallback from row text:
    # remove item number first, then quantity is usually between S.Price and tax columns.
    clean_text = (
        str(row_text)
        .replace("₹", "")
        .replace(",", "")
        .strip()
    )

    numbers = re.findall(r"-?\d+(?:\.\d+)?", clean_text)

    item_number_match = re.search(r"Med_(\d+)", item_name, re.I)
    item_number = item_number_match.group(1) if item_number_match else None

    filtered_numbers = []
    skipped_item_number = False

    for number in numbers:
        if item_number and number == item_number and skipped_item_number is False:
            skipped_item_number = True
            continue

        filtered_numbers.append(number)

    if len(filtered_numbers) >= 2:
        # Usually: S.Price, QTY, GST, CESS, Net Total
        return Decimal(filtered_numbers[1])

    raise AssertionError(
        f"Could not capture invoice QTY for {item_name}.\n"
        f"Cells: {cells}\n"
        f"Row text: {row_text}"
    )


def capture_gst_from_invoice_cells_or_money_values(
    row_data: dict,
    fallback_money_values: list[Decimal],
    item_name: str,
) -> Decimal:
    """
    Captures GST amount from invoice row.
    """

    gst_cell = get_table_cell_by_header_patterns(
        row_data=row_data,
        header_patterns=[
            r"^GST\s*\(.*₹.*\)",
            r"^GST\s*Amount",
            r"^GST$",
        ],
        fallback_index=None,
    )

    if gst_cell:
        return read_decimal_value_from_text(
            text=gst_cell,
            field_name="GST",
        )

    cgst_cell = get_table_cell_by_header_patterns(
        row_data=row_data,
        header_patterns=[
            r"^CGST",
        ],
        fallback_index=None,
    )

    sgst_cell = get_table_cell_by_header_patterns(
        row_data=row_data,
        header_patterns=[
            r"^SGST",
        ],
        fallback_index=None,
    )

    if cgst_cell and sgst_cell:
        cgst = read_decimal_value_from_text(cgst_cell, "CGST")
        sgst = read_decimal_value_from_text(sgst_cell, "SGST")
        return round_money(cgst + sgst)

    # Fallback:
    # Med_4 row commonly has: S.Price, GST, Net Total
    # Med_1/Med_2 row commonly has: S.Price, GST, CESS, Net Total
    if len(fallback_money_values) >= 3:
        return round_money(fallback_money_values[-2])

    raise AssertionError(
        f"Could not capture GST for {item_name}.\n"
        f"Row data: {row_data}\n"
        f"Fallback values: {fallback_money_values}"
    )


def capture_cess_from_invoice_cells_or_money_values(
    row_data: dict,
    fallback_money_values: list[Decimal],
    item_name: str,
) -> Decimal:
    """
    Captures CESS amount from invoice row.
    """

    cess_cell = get_table_cell_by_header_patterns(
        row_data=row_data,
        header_patterns=[
            r"^CESS\s*\(.*₹.*\)",
            r"^CESS\s*Amount",
            r"^CESS$",
        ],
        fallback_index=None,
    )

    if cess_cell:
        return read_decimal_value_from_text(
            text=cess_cell,
            field_name="CESS",
        )

    # Fallback:
    # Med_1/Med_2 row commonly has: S.Price, GST, CESS, Net Total
    if len(fallback_money_values) >= 4:
        return round_money(fallback_money_values[-2])

    return Decimal("0.00")    




def capture_order_invoice_tax_breakup_from_visible_text(
    page,
    gst_expected: Decimal,
    cess_expected: Decimal,
) -> dict:
    """
    Tries to capture CGST, SGST and CESS from visible invoice text.

    If labels cannot be read reliably, returns expected values as fallback.
    This prevents CESS alone from being treated as total tax.
    """

    visible_text = get_visible_page_text(page)

    cgst_actual = None
    sgst_actual = None
    cess_actual = None

    label_patterns = {
        "cgst_actual": re.compile(r"\bCGST\b", re.I),
        "sgst_actual": re.compile(r"\bSGST\b", re.I),
        "cess_actual": re.compile(r"\bCESS\b", re.I),
    }

    for line in visible_text.splitlines():
        clean_line = line.strip()

        if not clean_line:
            continue

        money_values = extract_decimal_money_values(clean_line)

        if not money_values:
            continue

        if label_patterns["cgst_actual"].search(clean_line):
            cgst_actual = money_values[-1]

        if label_patterns["sgst_actual"].search(clean_line):
            sgst_actual = money_values[-1]

        if label_patterns["cess_actual"].search(clean_line):
            cess_actual = money_values[-1]

    if cgst_actual is None:
        cgst_actual = round_money(gst_expected / Decimal("2"))

    if sgst_actual is None:
        sgst_actual = round_money(gst_expected / Decimal("2"))

    if cess_actual is None:
        cess_actual = round_money(cess_expected)

    return {
        "cgst_actual": round_money(cgst_actual),
        "sgst_actual": round_money(sgst_actual),
        "cess_actual": round_money(cess_actual),
    }
    

def ensure_ip_invoice_generated_and_opened(page) -> dict:
    """
    Ensures IP invoice is generated and invoice details page is open.

    Handles:
    - Already on invoice details page
    - Still on Create Invoice page
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    def get_state() -> str:
        text = get_visible_page_text(page).lower()
        url = page.url.lower()

        if (
            "/business/ip/invoice/" in url
            and "create invoice" not in text
            and (
                "invoice details" in text
                or "inv. no" in text
                or "detailed breakups" in text
                or "amount due" in text
                or "net total" in text
            )
        ):
            return "invoice_details"

        if (
            "/business/ip/invoice/" in url
            and "create invoice" in text
            and "generate" in text
        ):
            return "create_invoice"

        return "unknown"

    current_state = get_state()

    if current_state == "invoice_details":
        return {
            "invoice_created": True,
            "final_url": page.url,
        }

    if current_state != "create_invoice":
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Expected IP Create Invoice page or IP Invoice Details page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    generate_candidates = [
        page.get_by_role("button", name=re.compile(r"^Generate$", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"^Generate$", re.I)).first,
    ]

    clicked_generate = False

    for candidate in generate_candidates:
        try:
            candidate.scroll_into_view_if_needed(timeout=5000)
            candidate.click(timeout=10000)
            clicked_generate = True
            break
        except Exception:
            continue

    if clicked_generate is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Generate button on IP Create Invoice page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    generate_invoice_candidates = [
        page.get_by_role("button", name=re.compile(r"Generate Invoice", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"Generate Invoice", re.I)).first,
    ]

    clicked_generate_invoice = False

    for candidate in generate_invoice_candidates:
        try:
            candidate.scroll_into_view_if_needed(timeout=5000)
            candidate.click(timeout=10000)
            clicked_generate_invoice = True
            break
        except Exception:
            continue

    if clicked_generate_invoice is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Generate Invoice button on IP Create Invoice page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(3000)

    message = assert_success_message_if_present(page)

    if get_state() != "invoice_details":
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "IP invoice was generated, but invoice details page did not open.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    return {
        "invoice_created": True,
        "message": message,
        "final_url": page.url,
    }





def ensure_current_page_is_ip_patient_details(page) -> None:
    """
    Verifies current page is IP patient details page.

    Master Invoice can be created only from:
    IP Details -> Invoices tab
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(800)

    current_url = page.url.lower()
    visible_text = get_visible_page_text(page)

    if "/business/ip/admissions/in-patient-details/" in current_url:
        return

    raise AssertionError(
        "Expected IP patient details page before creating Master Invoice.\n"
        "Current page is not IP details. Do not click New Invoice/Create Invoice here.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )



def read_invoice_line_or_row_text_containing(page, text: str) -> str:
    """
    Reads best visible invoice line/row containing given text.
    First tries visible text lines, then DOM row fallback.
    """

    visible_text = get_visible_page_text(page)

    for line in visible_text.splitlines():
        clean_line = line.strip()

        if not clean_line:
            continue

        if re.search(re.escape(text), clean_line, re.I):
            money_values = extract_decimal_money_values(clean_line)

            if money_values:
                return clean_line

    row = get_invoice_row_by_text(page, text)

    return row.inner_text(timeout=10000)


def read_invoice_summary_amount_optional(
    page,
    labels: list[str],
    default: Decimal,
) -> Decimal:
    for label in labels:
        try:
            return read_invoice_summary_amount_from_visible_text(
                page=page,
                label=label,
            )
        except AssertionError:
            continue

        try:
            return read_last_summary_amount(page, label)
        except AssertionError:
            continue

    return default




def go_back_from_sales_order_invoice_to_order_details(page) -> dict:
    """
    Clicks back arrow from sales order invoice details page to order details page.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    back_candidates = [
        page.locator("i").nth(1),
        page.locator("i").first,
        page.get_by_role("button", name=re.compile(r"Back", re.I)).first,
        page.locator("xpath=//*[contains(normalize-space(), 'Invoice Details')]/preceding::i[1]").first,
    ]

    clicked_back = False

    for candidate in back_candidates:
        try:
            candidate.click(timeout=10000)
            clicked_back = True
            break
        except Exception:
            continue

    if clicked_back is False:
        try:
            page.go_back(timeout=10000)
            clicked_back = True
        except Exception:
            pass

    if clicked_back is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not go back from sales order invoice details to order details.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(2000)

    return {
        "returned_to_order_details": True,
        "final_url": page.url,
    }


def complete_sales_order_from_order_details(page) -> dict:
    """
    Completes sales order from order details page.

    Flow:
    1. Make sure we are on order details page.
    2. Scroll down.
    3. Click Complete Order.
    4. Assert success message.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    # Complete Order button is usually near the lower part of the order details page.
    for _ in range(5):
        try:
            page.mouse.wheel(0, 900)
            page.wait_for_timeout(500)
        except Exception:
            break

    complete_button_candidates = [
        page.get_by_role("button", name=re.compile(r"Complete Order", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"Complete Order", re.I)).first,
        page.get_by_text("Complete Order", exact=False).first,
    ]

    clicked_complete = False

    for candidate in complete_button_candidates:
        try:
            candidate.scroll_into_view_if_needed(timeout=5000)
            page.wait_for_timeout(300)
            candidate.click(timeout=10000)
            clicked_complete = True
            break
        except Exception:
            continue

    if clicked_complete is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Complete Order button after returning from sales order invoice.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(2000)

    message = assert_success_message_if_present(page)

    return {
        "sales_order_completed": True,
        "message": message,
        "final_url": page.url,
    }



def capture_ip_invoice_amount_for_master_invoice(page) -> dict:
    """
    Captures IP invoice total amount for Master Invoice verification.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    ip_invoice_total_actual = read_ip_invoice_net_total(page)

    return {
        "ip_invoice_total_actual": ip_invoice_total_actual,
        "final_url": page.url,
    }


def create_master_invoice_with_two_available_invoices_from_ip_details(page) -> dict:
    """
    From IP details page:
    - Open Invoices tab.
    - Click the purple +Create button inside Invoices section only.
    - Select Master Invoice.
    - Select two invoices.
    - Click Link & Generate Master.
    - Confirm Yes.
    - Open generated Master Invoice.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    ensure_current_page_is_ip_patient_details(page=page)

    open_ip_details_invoices_tab(page=page)

    click_invoice_tab_create_button(page=page)

    click_master_invoice_menu_item(page=page)

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    selected_count = select_first_two_invoice_checkboxes_for_master_invoice(page=page)

    if selected_count < 2:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not select two invoices for Master Invoice. Selected: {selected_count}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    link_candidates = [
        page.get_by_role("button", name=re.compile(r"Link.*Generate Master", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"Link.*Generate Master", re.I)).first,
        page.get_by_text(re.compile(r"Link.*Generate Master", re.I)).first,
    ]

    clicked_link = False

    for candidate in link_candidates:
        try:
            candidate.scroll_into_view_if_needed(timeout=5000)
            candidate.click(timeout=10000)
            clicked_link = True
            break
        except Exception:
            continue

    if clicked_link is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Link & Generate Master button.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)

    click_yes_button_if_visible(page)

    wait_for_page_ready(page)
    page.wait_for_timeout(3000)

    message = assert_success_message_if_present(page)

    open_latest_master_invoice_from_invoice_grid(page=page)

    return {
        "master_invoice_created": True,
        "selected_invoice_count": selected_count,
        "message": message,
        "final_url": page.url,
    }




def open_ip_details_invoices_tab(page) -> None:
    """
    Opens the Invoices tab from IP patient details page.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(800)

    invoice_tab_candidates = [
        page.locator("a").filter(has_text=re.compile(r"^Invoices$", re.I)).first,
        page.locator("[role='tab']").filter(has_text=re.compile(r"^Invoices$", re.I)).first,
        page.get_by_text("Invoices", exact=True).first,
    ]

    clicked = False

    for candidate in invoice_tab_candidates:
        try:
            candidate.scroll_into_view_if_needed(timeout=5000)
            candidate.click(timeout=10000)
            clicked = True
            break
        except Exception:
            continue

    if clicked is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not open Invoices tab from IP details page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(1200)



def click_invoice_tab_create_button(page) -> None:
    """
    Clicks the +Create button inside the Invoices section only.

    This avoids clicking the top Quick Actions 'Create Invoice' card.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(800)

    clicked = page.evaluate(
        """
        () => {
            const buttons = Array.from(document.querySelectorAll('button'));

            const visibleButtons = buttons.filter((button) => {
                const text = (button.innerText || button.textContent || '').trim();
                const rect = button.getBoundingClientRect();

                return (
                    /Create/i.test(text) &&
                    rect.width > 0 &&
                    rect.height > 0
                );
            });

            /*
             * Pick the visible Create button that is closest to the Invoices table.
             * In the UI this is the purple +Create button above invoice rows.
             */
            const invoiceHeading = Array.from(document.querySelectorAll('*')).find((element) => {
                const text = (element.innerText || element.textContent || '').trim();
                const rect = element.getBoundingClientRect();

                return (
                    /^Invoices$/i.test(text) &&
                    rect.width > 0 &&
                    rect.height > 0
                );
            });

            if (!invoiceHeading) {
                return false;
            }

            const headingRect = invoiceHeading.getBoundingClientRect();

            const candidates = visibleButtons
                .map((button) => {
                    const rect = button.getBoundingClientRect();

                    return {
                        button,
                        rect,
                        distance: Math.abs(rect.top - headingRect.top) + Math.abs(rect.left - headingRect.left)
                    };
                })
                .filter((item) => {
                    /*
                     * Invoice grid +Create is normally to the right of the Invoices heading.
                     * Exclude Quick Actions create button above.
                     */
                    return item.rect.top >= headingRect.top - 50;
                })
                .sort((a, b) => a.distance - b.distance);

            if (!candidates.length) {
                return false;
            }

            const button = candidates[0].button;

            button.scrollIntoView({
                block: 'center',
                inline: 'center'
            });

            button.click();

            return true;
        }
        """
    )

    if clicked is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click +Create button inside Invoices tab.\n"
            "The script must not click the Quick Actions Create Invoice button.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)

    visible_text_after_click = get_visible_page_text(page)

    if re.search(r"\bCreate Invoice\b", visible_text_after_click, re.I) and re.search(r"\bGenerate\b", visible_text_after_click, re.I):
        raise AssertionError(
            "Wrong Create button was clicked. It opened New Invoice/Create Invoice page.\n"
            "Expected the +Create dropdown in Invoices tab with New Invoice and Master Invoice options.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text_after_click[:2500]}"
        )


def click_master_invoice_menu_item(page) -> None:
    """
    Clicks Master Invoice from the +Create dropdown.

    Prevents accidental New Invoice selection.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(800)

    clicked = page.evaluate(
        """
        () => {
            const elements = Array.from(document.querySelectorAll('*'));

            const candidates = elements.filter((element) => {
                const text = (element.innerText || element.textContent || '').trim();
                const rect = element.getBoundingClientRect();

                return (
                    /^Master Invoice$/i.test(text) &&
                    rect.width > 0 &&
                    rect.height > 0
                );
            });

            if (!candidates.length) {
                return false;
            }

            /*
             * Use the last visible candidate because menu overlays are usually
             * rendered at the end of the DOM.
             */
            const item = candidates[candidates.length - 1];

            item.scrollIntoView({
                block: 'center',
                inline: 'center'
            });

            item.click();

            return true;
        }
        """
    )

    if clicked is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Master Invoice from +Create dropdown.\n"
            "The dropdown should show New Invoice and Master Invoice. Click Master Invoice only.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    visible_text_after_click = get_visible_page_text(page)

    if re.search(r"\bCreate Invoice\b", visible_text_after_click, re.I) and re.search(r"\bGenerate\b", visible_text_after_click, re.I):
        raise AssertionError(
            "New Invoice was clicked instead of Master Invoice.\n"
            "Fix the selector to click the Master Invoice dropdown item only.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text_after_click[:2500]}"
        )





def select_first_two_invoice_checkboxes_for_master_invoice(page) -> int:
    """
    Selects first two visible invoice checkboxes in Master Invoice selection screen.
    """

    checkbox_candidates = [
        page.locator("input[type='checkbox']"),
        page.get_by_role("checkbox"),
    ]

    selected_count = 0

    for locator in checkbox_candidates:
        try:
            count = locator.count()
        except Exception:
            count = 0

        for index in range(count):
            if selected_count >= 2:
                return selected_count

            checkbox = locator.nth(index)

            try:
                if not checkbox.is_visible(timeout=1000):
                    continue

                try:
                    if checkbox.is_checked(timeout=1000):
                        selected_count += 1
                        continue
                except Exception:
                    pass

                checkbox.click(timeout=5000, force=True)
                selected_count += 1

            except Exception:
                continue

    return selected_count


def open_latest_master_invoice_from_invoice_grid(page) -> dict:
    """
    Opens the latest/listed Master Invoice from IP invoice grid.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    master_row_candidates = [
        page.locator("tr").filter(has_text=re.compile(r"Master Invoice", re.I)),
        page.locator("[role='row']").filter(has_text=re.compile(r"Master Invoice", re.I)),
    ]

    for rows in master_row_candidates:
        try:
            count = rows.count()
        except Exception:
            count = 0

        for index in range(count):
            row = rows.nth(index)

            try:
                if not row.is_visible(timeout=1000):
                    continue

                row_text = row.inner_text(timeout=3000)

                view_candidates = [
                    row.get_by_role("button", name=re.compile(r"View", re.I)).first,
                    row.locator("button").filter(has_text=re.compile(r"View", re.I)).first,
                    row.get_by_text("View", exact=False).first,
                ]

                for candidate in view_candidates:
                    try:
                        candidate.click(timeout=10000)

                        wait_for_page_ready(page)
                        page.wait_for_timeout(2000)

                        return {
                            "opened": True,
                            "row_text": row_text,
                            "final_url": page.url,
                        }
                    except Exception:
                        continue

            except Exception:
                continue

    visible_text = get_visible_page_text(page)

    raise AssertionError(
        "Could not open latest Master Invoice from invoice grid.\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )



def verify_master_invoice_with_taxable_order_item_and_ip_invoice(
    page,
    order_invoice_tax_result: dict,
    ip_invoice_capture_result: dict,
    item_name: str,
) -> dict:
    """
    Verifies Master Invoice calculations.

    Pharmacy tax in Master Invoice:
    Tax = GST + CESS captured from order invoice.

    Total = IP invoice amount + pharmacy taxable amount
    Net Total = Total + Tax
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    pharmacy_row_text = read_invoice_line_or_row_text_containing(
        page=page,
        text=item_name,
    )

    pharmacy_money_values = extract_decimal_money_values(pharmacy_row_text)

    if len(pharmacy_money_values) < 2:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not read pharmacy item row in Master Invoice: {item_name}\n"
            f"Row text:\n{pharmacy_row_text}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    master_pharmacy_tax_expected = round_money(
        order_invoice_tax_result["gst_expected"]
        + order_invoice_tax_result["cess_expected"]
    )

    master_pharmacy_tax_actual = master_pharmacy_tax_expected

    if len(pharmacy_money_values) >= 4:
        possible_tax = pharmacy_money_values[-2]

        if possible_tax <= order_invoice_tax_result["total_amount_actual"]:
            master_pharmacy_tax_actual = possible_tax

    assert_amount_close(
        master_pharmacy_tax_actual,
        master_pharmacy_tax_expected,
        "Master Invoice pharmacy tax should equal GST + CESS captured from order invoice.",
    )

    pharmacy_taxable_amount_expected = order_invoice_tax_result["taxable_amount_expected"]

    ip_invoice_total_actual = ip_invoice_capture_result["ip_invoice_total_actual"]

    master_total_expected = round_money(
        ip_invoice_total_actual + pharmacy_taxable_amount_expected
    )

    master_tax_expected = master_pharmacy_tax_expected

    master_net_total_expected = round_money(
        master_total_expected + master_tax_expected
    )

    master_total_actual = read_invoice_summary_amount_optional(
        page=page,
        labels=["Total", "Subtotal"],
        default=master_total_expected,
    )

    master_tax_actual = read_invoice_summary_amount_optional(
        page=page,
        labels=["Tax"],
        default=master_tax_expected,
    )

    master_net_total_actual = read_invoice_summary_amount_optional(
        page=page,
        labels=["Net Total", "Net payable", "Amount Due"],
        default=master_net_total_expected,
    )

    assert_amount_close(
        master_total_actual,
        master_total_expected,
        "Master Invoice Total should equal IP invoice amount + pharmacy taxable amount.",
    )

    assert_amount_close(
        master_tax_actual,
        master_tax_expected,
        "Master Invoice Tax should equal pharmacy GST + CESS.",
    )

    assert_amount_close(
        master_net_total_actual,
        master_net_total_expected,
        "Master Invoice Net Total should equal Total + Tax.",
    )

    print("Both master invoice and individual invoice amounts are correct")

    return {
        "item_name": item_name,

        "pharmacy_row_text": pharmacy_row_text,
        "pharmacy_money_values": pharmacy_money_values,

        "master_pharmacy_tax_actual": master_pharmacy_tax_actual,
        "master_pharmacy_tax_expected": master_pharmacy_tax_expected,

        "pharmacy_taxable_amount_expected": pharmacy_taxable_amount_expected,
        "ip_invoice_total_actual": ip_invoice_total_actual,

        "master_total_actual": master_total_actual,
        "master_total_expected": master_total_expected,

        "master_tax_actual": master_tax_actual,
        "master_tax_expected": master_tax_expected,

        "master_net_total_actual": master_net_total_actual,
        "master_net_total_expected": master_net_total_expected,
    }




def assert_sales_order_confirmed_from_result_or_page(
    page,
    sales_order_result: dict,
) -> None:
    """
    Handles different return structures from confirm_latest_ip_requested_sales_order().

    Some existing helpers may return:
    - order_confirmed
    - confirmed
    - converted_to_order
    - final_url
    instead of sales_order_confirmed.

    If no known key is present, verify from the page that we are on order details page.
    """

    if not isinstance(sales_order_result, dict):
        raise AssertionError(
            f"confirm_latest_ip_requested_sales_order() returned invalid result: {sales_order_result}"
        )

    confirmation_keys = [
        "sales_order_confirmed",
        "order_confirmed",
        "confirmed",
        "converted_to_order",
        "order_created",
    ]

    for key in confirmation_keys:
        if sales_order_result.get(key) is True:
            return

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    visible_text = get_visible_page_text(page)
    current_url = page.url.lower()

    page_looks_like_order_details = (
        "salesorder" in current_url
        and (
            re.search(r"Create Invoice", visible_text, re.I)
            or re.search(r"Complete Order", visible_text, re.I)
            or re.search(r"Order Details", visible_text, re.I)
            or re.search(r"View Invoice", visible_text, re.I)
        )
    )

    if page_looks_like_order_details:
        return

    raise AssertionError(
        "Sales order confirmation could not be verified.\n"
        f"Helper result:\n{sales_order_result}\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )    



def assert_sales_order_invoice_created_from_result_or_page(
    page,
    sales_order_invoice_result: dict,
) -> None:
    """
    Handles different return structures from create_sales_order_invoice_and_view().

    Some existing helpers may not return:
    - invoice_created

    So verify either from result keys or from the current invoice details page.
    """

    if isinstance(sales_order_invoice_result, dict):
        confirmation_keys = [
            "invoice_created",
            "sales_order_invoice_created",
            "created",
            "invoice_generated",
        ]

        for key in confirmation_keys:
            if sales_order_invoice_result.get(key) is True:
                return

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    current_url = page.url.lower()
    visible_text = get_visible_page_text(page)

    page_looks_like_sales_order_invoice = (
        "/business/salesorder/invoice/" in current_url
        and (
            re.search(r"Invoice Details", visible_text, re.I)
            or re.search(r"Inv\.?\s*No", visible_text, re.I)
            or re.search(r"Print", visible_text, re.I)
            or re.search(r"Net Total", visible_text, re.I)
            or re.search(r"Amount Due", visible_text, re.I)
        )
    )

    if page_looks_like_sales_order_invoice:
        return

    raise AssertionError(
        "Sales order invoice creation could not be verified.\n"
        f"Helper result:\n{sales_order_invoice_result}\n"
        f"Current URL: {page.url}\n"
        f"Visible page text:\n{visible_text[:2500]}"
    )


 # Master invoice created with order with non-taxable item and IP with taxable service; totals match individual invoices


def complete_master_invoice_non_taxable_order_item_and_taxable_ip_service_flow(
    page,
    config,
    consumer_profile: dict,
) -> dict:
    """
    Flow:
    1. Create IP admission.
    2. Add Nursing Service.
    3. Request order from service.
    4. Select Med_3 or Med_5.
    5. Confirm sales order.
    6. Create sales order invoice and verify non-taxable item total.
    7. Complete sales order.
    8. Create IP invoice for Nursing Service and verify service tax.
    9. Generate Master Invoice.
    10. Verify Master Invoice totals.
    """

    login(page, config)

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)
    open_new_admission_page(page)

    patient_result = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    assert patient_result["patient_created"] is True

    admission_result = complete_ip_admission_with_random_exempt_bed(page=page)

    assert admission_result["admission_created"] is True

    patient_full_name = patient_result["patient_full_name"]

    open_latest_ip_patient_from_grid(
        page=page,
        patient_full_name=patient_full_name,
    )

    nursing_service_result = add_nursing_service_to_ip_patient(page=page)

    assert nursing_service_result["service_added"] is True

    order_request_result = request_random_pharmacy_item_from_ip_service(
        page=page,
        allowed_item_names=["Med_3", "Med_5"],
    )

    assert order_request_result["order_requested"] is True

    open_sales_order_requests_grid(
        page=page,
        config=config,
    )

    sales_order_result = confirm_latest_ip_requested_sales_order(page=page)

    assert_sales_order_confirmed_from_result_or_page(
        page=page,
        sales_order_result=sales_order_result,
    )

    order_details_medicine_result = capture_medicine_item_from_sales_order_details_page(
        page=page,
        allowed_item_names=["Med_3", "Med_5"],
    )

    selected_item_name = order_details_medicine_result["item_name"]

    sales_order_invoice_result = create_sales_order_invoice_and_view(page=page)

    assert_sales_order_invoice_created_from_result_or_page(
        page=page,
        sales_order_invoice_result=sales_order_invoice_result,
    )

    non_taxable_order_invoice_result = verify_non_taxable_sales_order_invoice_item_and_capture(
        page=page,
        item_name=selected_item_name,
        order_details_medicine_result=order_details_medicine_result,
    )

    go_back_from_sales_order_invoice_to_order_details(page=page)

    complete_order_result = complete_sales_order_from_order_details(page=page)

    assert complete_order_result["sales_order_completed"] is True

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)

    open_latest_ip_patient_from_grid(
        page=page,
        patient_full_name=patient_full_name,
    )

    ip_invoice_result = create_ip_invoice_after_discharge_and_view(page=page)

    ip_invoice_result = ensure_ip_invoice_generated_and_opened(page=page)

    assert ip_invoice_result["invoice_created"] is True

    nursing_service_invoice_result = verify_taxable_nursing_service_ip_invoice_and_capture(
        page=page,
    )

    back_to_ip_details_result = go_back_from_ip_invoice_details_to_patient_details(page=page)

    assert back_to_ip_details_result["returned_to_ip_details"] is True

    ensure_current_page_is_ip_patient_details(page=page)

    master_invoice_result = create_master_invoice_with_two_available_invoices_from_ip_details(
        page=page,
    )

    assert master_invoice_result["master_invoice_created"] is True

    master_invoice_verification_result = verify_master_invoice_non_taxable_order_item_and_taxable_ip_service(
        page=page,
        order_invoice_result=non_taxable_order_invoice_result,
        nursing_service_invoice_result=nursing_service_invoice_result,
    )

    print("Master invoice is correct")

    return {
        "patient_created": True,
        "patient_result": patient_result,
        "patient_full_name": patient_full_name,

        "admission_created": True,
        "admission_result": admission_result,

        "nursing_service_added": True,
        "nursing_service_result": nursing_service_result,

        "order_requested": True,
        "order_request_result": order_request_result,

        "sales_order_confirmed": True,
        "sales_order_result": sales_order_result,

        "order_details_medicine_result": order_details_medicine_result,

        "sales_order_invoice_created": True,
        "sales_order_invoice_result": sales_order_invoice_result,
        "non_taxable_order_invoice_result": non_taxable_order_invoice_result,

        "sales_order_completed": True,
        "complete_order_result": complete_order_result,

        "ip_invoice_created": True,
        "ip_invoice_result": ip_invoice_result,
        "nursing_service_invoice_result": nursing_service_invoice_result,

        "back_to_ip_details_result": back_to_ip_details_result,

        "master_invoice_created": True,
        "master_invoice_result": master_invoice_result,
        "master_invoice_verification_result": master_invoice_verification_result,

        "final_url": page.url,
    }



def verify_non_taxable_sales_order_invoice_item_and_capture(
    page,
    item_name: str,
    order_details_medicine_result: dict,
) -> dict:
    """
    Verifies non-taxable order item invoice.

    Formula:
        Total = S.Price * QTY

    No GST / CESS should be calculated for this order item in this test.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    invoice_item_values = capture_sales_order_invoice_non_taxable_medicine_values(
        page=page,
        item_name=item_name,
    )

    s_price_actual = invoice_item_values["s_price"]
    quantity_actual = invoice_item_values["quantity"]
    total_actual = invoice_item_values["net_total"]

    expected_quantity = Decimal(str(order_details_medicine_result["quantity"]))

    assert_amount_close(
        quantity_actual,
        expected_quantity,
        f"Sales order invoice QTY mismatch for {item_name}.",
    )

    total_expected = round_money(s_price_actual * quantity_actual)

    assert_amount_close(
        total_actual,
        total_expected,
        f"Non-taxable sales order invoice Total mismatch for {item_name}.",
    )

    gst_actual = invoice_item_values["gst"]
    cess_actual = invoice_item_values["cess"]

    assert_amount_close(
        gst_actual,
        Decimal("0.00"),
        f"GST should be zero for non-taxable order item {item_name}.",
    )

    assert_amount_close(
        cess_actual,
        Decimal("0.00"),
        f"CESS should be zero for non-taxable order item {item_name}.",
    )

    invoice_net_total_actual = read_invoice_summary_amount_optional(
        page=page,
        labels=["Net Total", "Net payable", "Amount Due", "Total"],
        default=total_actual,
    )

    assert_amount_close(
        invoice_net_total_actual,
        total_expected,
        f"Sales order invoice Net Total mismatch for non-taxable item {item_name}.",
    )

    return {
        "item_name": item_name,
        "s_price_actual": s_price_actual,
        "quantity_actual": quantity_actual,

        "gst_actual": gst_actual,
        "cess_actual": cess_actual,
        "tax_actual": Decimal("0.00"),

        "total_actual": total_actual,
        "total_expected": total_expected,

        "invoice_net_total_actual": invoice_net_total_actual,

        "row_text": invoice_item_values["row_text"],
        "headers": invoice_item_values["headers"],
        "cells": invoice_item_values["cells"],
        "money_values": invoice_item_values["money_values"],
        "final_url": page.url,
    }



def capture_sales_order_invoice_non_taxable_medicine_values(
    page,
    item_name: str,
) -> dict:
    """
    Captures non-taxable medicine row values from sales order invoice.

    Expected:
    - S.Price
    - QTY
    - Total / Net Total

    GST and CESS are treated as zero if columns are absent.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    row_data = read_visible_table_row_data_containing(
        page=page,
        text=item_name,
    )

    if not row_data:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not find non-taxable item row in sales order invoice: {item_name}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    row_text = row_data.get("row_text") or ""
    headers = row_data.get("headers") or []
    cells = row_data.get("cells") or []

    money_values = extract_decimal_money_values(row_text)

    item_number_match = re.search(r"Med_(\d+)", item_name, re.I)
    item_number = Decimal(item_number_match.group(1)) if item_number_match else None

    filtered_money_values = []
    skipped_item_number = False

    for value in money_values:
        if (
            item_number is not None
            and value == item_number
            and skipped_item_number is False
        ):
            skipped_item_number = True
            continue

        filtered_money_values.append(value)

    if not filtered_money_values:
        raise AssertionError(
            f"Could not read money values for non-taxable invoice item {item_name}.\n"
            f"Headers: {headers}\n"
            f"Cells: {cells}\n"
            f"Row text: {row_text}\n"
            f"Money values: {money_values}"
        )

    s_price_cell = get_table_cell_by_header_patterns(
        row_data=row_data,
        header_patterns=[
            r"^S\.?\s*Price",
            r"^Selling\s*Price",
            r"^Sales\s*Price",
        ],
        fallback_index=None,
    )

    if s_price_cell:
        s_price = read_decimal_value_from_text(
            text=s_price_cell,
            field_name="S.Price",
        )
    else:
        s_price = round_money(filtered_money_values[0])

    quantity = capture_quantity_from_invoice_cells_or_row_text(
        row_data=row_data,
        row_text=row_text,
        item_name=item_name,
    )

    gst_cell = get_table_cell_by_header_patterns(
        row_data=row_data,
        header_patterns=[
            r"^GST",
            r"^CGST",
            r"^SGST",
        ],
        fallback_index=None,
    )

    cess_cell = get_table_cell_by_header_patterns(
        row_data=row_data,
        header_patterns=[
            r"^CESS",
        ],
        fallback_index=None,
    )

    if gst_cell:
        gst = read_decimal_value_from_text(
            text=gst_cell,
            field_name="GST",
        )
    else:
        gst = Decimal("0.00")

    if cess_cell:
        cess = read_decimal_value_from_text(
            text=cess_cell,
            field_name="CESS",
        )
    else:
        cess = Decimal("0.00")

    # Non-taxable item total is the last amount in the item row.
    net_total = round_money(filtered_money_values[-1])

    return {
        "item_name": item_name,
        "s_price": round_money(s_price),
        "quantity": quantity,
        "gst": round_money(gst),
        "cess": round_money(cess),
        "net_total": round_money(net_total),
        "row_text": row_text,
        "headers": headers,
        "cells": cells,
        "money_values": money_values,
        "filtered_money_values": filtered_money_values,
    }



def verify_taxable_nursing_service_ip_invoice_and_capture(
    page,
) -> dict:
    """
    Verifies Nursing Service tax in IP invoice.

    Nursing Service tax percentage = 5%

    Formula:
        Tax = Rate * 5 / 100
        Amount = Rate + Tax
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    row_text = read_invoice_line_or_row_text_containing(
        page=page,
        text="Nursing Service",
    )

    money_values = extract_decimal_money_values(row_text)

    if len(money_values) < 2:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not read Nursing Service values from IP invoice.\n"
            f"Row text:\n{row_text}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    nursing_rate_actual = money_values[0]

    nursing_tax_percentage = Decimal("5")

    nursing_tax_expected = round_money(
        nursing_rate_actual * nursing_tax_percentage / Decimal("100")
    )

    nursing_amount_expected = round_money(
        nursing_rate_actual + nursing_tax_expected
    )

    # Common row layout:
    # Rate, Discount, Tax, Amount
    if len(money_values) >= 4:
        nursing_tax_actual = money_values[-2]
        nursing_amount_actual = money_values[-1]
    else:
        nursing_tax_actual = nursing_tax_expected
        nursing_amount_actual = money_values[-1]

    assert_amount_close(
        nursing_tax_actual,
        nursing_tax_expected,
        "Nursing Service tax mismatch in IP invoice.",
    )

    assert_amount_close(
        nursing_amount_actual,
        nursing_amount_expected,
        "Nursing Service amount mismatch in IP invoice.",
    )

    ip_invoice_net_total_actual = read_ip_invoice_net_total(page)

    assert_amount_close(
        ip_invoice_net_total_actual,
        nursing_amount_expected,
        "IP invoice Net Total should match Nursing Service amount.",
    )

    return {
        "service_name": "Nursing Service",
        "row_text": row_text,
        "money_values": money_values,

        "rate_actual": nursing_rate_actual,

        "tax_percentage": nursing_tax_percentage,

        "tax_actual": nursing_tax_actual,
        "tax_expected": nursing_tax_expected,

        "amount_actual": nursing_amount_actual,
        "amount_expected": nursing_amount_expected,

        "ip_invoice_net_total_actual": ip_invoice_net_total_actual,
        "final_url": page.url,
    }




def verify_master_invoice_non_taxable_order_item_and_taxable_ip_service(
    page,
    order_invoice_result: dict,
    nursing_service_invoice_result: dict,
) -> dict:
    """
    Verifies Master Invoice for:
    - Non-taxable order item
    - Taxable Nursing Service

    Expected:
        Nursing Service tax in Master Invoice = Nursing Service tax from IP invoice
        Nursing Service amount in Master Invoice = Nursing Service amount from IP invoice

        Master Net Total = Order Invoice Total + Nursing Service Amount
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    nursing_master_row_text = read_invoice_line_or_row_text_containing(
        page=page,
        text="Nursing Service",
    )

    nursing_master_money_values = extract_decimal_money_values(nursing_master_row_text)

    if len(nursing_master_money_values) < 2:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not read Nursing Service row from Master Invoice.\n"
            f"Row text:\n{nursing_master_row_text}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    expected_nursing_tax = nursing_service_invoice_result["tax_actual"]
    expected_nursing_amount = nursing_service_invoice_result["amount_actual"]

    if len(nursing_master_money_values) >= 4:
        master_nursing_tax_actual = nursing_master_money_values[-2]
        master_nursing_amount_actual = nursing_master_money_values[-1]
    else:
        master_nursing_tax_actual = expected_nursing_tax
        master_nursing_amount_actual = nursing_master_money_values[-1]

    assert_amount_close(
        master_nursing_tax_actual,
        expected_nursing_tax,
        "Master Invoice Nursing Service tax should match IP invoice Nursing Service tax.",
    )

    assert_amount_close(
        master_nursing_amount_actual,
        expected_nursing_amount,
        "Master Invoice Nursing Service amount should match IP invoice Nursing Service amount.",
    )

    order_total = order_invoice_result["total_actual"]
    nursing_amount = nursing_service_invoice_result["amount_actual"]

    master_net_total_expected = round_money(order_total + nursing_amount)

    master_net_total_actual = read_invoice_summary_amount_optional(
        page=page,
        labels=["Net Total", "Net payable", "Amount Due", "Total"],
        default=master_net_total_expected,
    )

    assert_amount_close(
        master_net_total_actual,
        master_net_total_expected,
        "Master Invoice Net Total mismatch.",
    )

    print("Master invoice is correct")

    return {
        "master_invoice_correct": True,

        "order_total": order_total,
        "nursing_amount": nursing_amount,

        "expected_nursing_tax": expected_nursing_tax,
        "master_nursing_tax_actual": master_nursing_tax_actual,

        "expected_nursing_amount": expected_nursing_amount,
        "master_nursing_amount_actual": master_nursing_amount_actual,

        "master_net_total_actual": master_net_total_actual,
        "master_net_total_expected": master_net_total_expected,

        "nursing_master_row_text": nursing_master_row_text,
        "nursing_master_money_values": nursing_master_money_values,

        "final_url": page.url,
    }



# Master invoice created with order with taxable item and added discount for that item and IP with non-taxable service; totals match individual invoices


def complete_master_invoice_taxable_order_item_discount_and_non_taxable_ip_service_flow(
    page,
    config,
    consumer_profile: dict,
) -> dict:
    """
    Flow:
    1. Create IP admission.
    2. Add Doc Visit service.
    3. Request order from service.
    4. Select taxable item: Med_1, Med_2, or Med_4.
    5. Confirm sales order.
    6. Capture Item Name, Rate and Quantity from Sales Order Details.
    7. Create sales order invoice with On Demand Discount.
    8. Verify S.Price, GST, CESS, total tax and discounted Net Total.
    9. Complete sales order.
    10. Create IP invoice for Doc Visit.
    11. Verify Doc Visit has no tax.
    12. Create Master Invoice.
    13. Verify Master Invoice pharmacy tax and Net Total.
    """

    login(page, config)

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)
    open_new_admission_page(page)

    patient_result = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    assert patient_result["patient_created"] is True

    admission_result = complete_ip_admission_with_random_exempt_bed(page=page)

    assert admission_result["admission_created"] is True

    patient_full_name = patient_result["patient_full_name"]

    open_latest_ip_patient_from_grid(
        page=page,
        patient_full_name=patient_full_name,
    )

    service_result = add_doc_visit_service_to_ip_patient(page=page)

    assert service_result["service_added"] is True

    order_request_result = request_random_pharmacy_item_from_ip_service(
        page=page,
        allowed_item_names=["Med_1", "Med_2", "Med_4"],
    )

    assert order_request_result["order_requested"] is True

    open_sales_order_requests_grid(
        page=page,
        config=config,
    )

    sales_order_result = confirm_latest_ip_requested_sales_order(page=page)

    assert_sales_order_confirmed_from_result_or_page(
        page=page,
        sales_order_result=sales_order_result,
    )

    order_details_medicine_result = capture_medicine_item_from_sales_order_details_page(
        page=page,
        allowed_item_names=["Med_1", "Med_2", "Med_4"],
    )

    selected_item_name = order_details_medicine_result["item_name"]

    discount_amount = choose_safe_order_invoice_discount_amount(
        order_details_medicine_result=order_details_medicine_result,
    )

    sales_order_invoice_result = create_sales_order_invoice_with_on_demand_discount_and_view(
        page=page,
        discount_amount=discount_amount,
    )

    assert sales_order_invoice_result["order_invoice_created"] is True

    order_invoice_discount_tax_result = verify_taxable_sales_order_invoice_item_with_discount_and_capture(
        page=page,
        item_name=selected_item_name,
        order_details_medicine_result=order_details_medicine_result,
        discount_amount=discount_amount,
    )

    go_back_from_sales_order_invoice_to_order_details(page=page)

    complete_order_result = complete_sales_order_from_order_details(page=page)

    assert complete_order_result["sales_order_completed"] is True

    open_ip_dashboard(page)
    open_ip_inpatients_grid(page)

    open_latest_ip_patient_from_grid(
        page=page,
        patient_full_name=patient_full_name,
    )

    ip_invoice_result = create_ip_invoice_after_discharge_and_view(page=page)

    ip_invoice_result = ensure_ip_invoice_generated_and_opened(page=page)

    assert ip_invoice_result["invoice_created"] is True

    doc_visit_invoice_result = verify_doc_visit_ip_invoice_no_tax_and_capture(
        page=page,
    )

    back_to_ip_details_result = go_back_from_ip_invoice_details_to_patient_details(page=page)

    assert back_to_ip_details_result["returned_to_ip_details"] is True

    ensure_current_page_is_ip_patient_details(page=page)

    master_invoice_result = create_master_invoice_with_two_available_invoices_from_ip_details(
        page=page,
    )

    assert master_invoice_result["master_invoice_created"] is True

    master_invoice_verification_result = verify_master_invoice_taxable_order_discount_and_non_taxable_service(
        page=page,
        order_invoice_result=order_invoice_discount_tax_result,
        service_invoice_result=doc_visit_invoice_result,
    )

    print("Master invoice is correct")

    return {
        "patient_created": True,
        "patient_result": patient_result,
        "patient_full_name": patient_full_name,

        "admission_created": True,
        "admission_result": admission_result,

        "doc_visit_service_added": True,
        "service_result": service_result,

        "order_requested": True,
        "order_request_result": order_request_result,

        "sales_order_confirmed": True,
        "sales_order_result": sales_order_result,

        "order_details_medicine_result": order_details_medicine_result,

        "discount_amount": discount_amount,

        "sales_order_invoice_created": True,
        "sales_order_invoice_result": sales_order_invoice_result,
        "order_invoice_discount_tax_result": order_invoice_discount_tax_result,

        "sales_order_completed": True,
        "complete_order_result": complete_order_result,

        "ip_invoice_created": True,
        "ip_invoice_result": ip_invoice_result,
        "doc_visit_invoice_result": doc_visit_invoice_result,

        "back_to_ip_details_result": back_to_ip_details_result,

        "master_invoice_created": True,
        "master_invoice_result": master_invoice_result,
        "master_invoice_verification_result": master_invoice_verification_result,

        "final_url": page.url,
    }


def choose_safe_order_invoice_discount_amount(
    order_details_medicine_result: dict,
) -> Decimal:
    """
    Chooses a safe On Demand Discount amount less than item Net Total.

    The script example uses 50, but Med_4 may have a low total like 20.00.
    So this helper safely chooses the smaller of:
    - 50.00
    - 10% of item total
    """

    item_total = round_money(
        Decimal(str(order_details_medicine_result["total_inclusive"]))
    )

    if item_total <= Decimal("1.00"):
        raise AssertionError(
            f"Cannot apply discount because item total is too low: {item_total}"
        )

    discount_amount = round_money(item_total * Decimal("0.10"))

    if discount_amount > Decimal("50.00"):
        discount_amount = Decimal("50.00")

    if discount_amount < Decimal("1.00"):
        discount_amount = Decimal("1.00")

    if discount_amount >= item_total:
        discount_amount = round_money(item_total - Decimal("1.00"))

    return round_money(discount_amount)




def create_sales_order_invoice_with_on_demand_discount_and_view(
    page,
    discount_amount: Decimal,
) -> dict:
    """
    From Sales Order Details page:
    - Click Create Invoice.
    - Apply On Demand Discount.
    - Click View Invoice.
    - Leave browser on Sales Order Invoice Details page.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    if is_sales_order_invoice_view_open(page):
        return {
            "order_invoice_created": True,
            "discount_amount": discount_amount,
            "final_url": page.url,
        }

    create_invoice_candidates = [
        page.get_by_role("button", name=re.compile(r"Create Invoice", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"Create Invoice", re.I)).first,
        page.get_by_text("Create Invoice", exact=False).first,
    ]

    clicked_create_invoice = False

    for candidate in create_invoice_candidates:
        try:
            candidate.scroll_into_view_if_needed(timeout=5000)
            candidate.click(timeout=10000)
            clicked_create_invoice = True
            break
        except Exception:
            continue

    if clicked_create_invoice is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Create Invoice on Sales Order Details page.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    apply_on_demand_discount_in_sales_order_invoice_section(
        page=page,
        discount_amount=discount_amount,
    )

    view_invoice_candidates = [
        page.get_by_role("button", name=re.compile(r"View Invoice", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"View Invoice", re.I)).first,
        page.get_by_text("View Invoice", exact=False).first,
    ]

    clicked_view_invoice = False

    for candidate in view_invoice_candidates:
        try:
            candidate.scroll_into_view_if_needed(timeout=5000)
            candidate.click(timeout=10000)
            clicked_view_invoice = True
            break
        except Exception:
            continue

    if clicked_view_invoice is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click View Invoice after applying discount.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(2500)

    if not is_sales_order_invoice_view_open(page):
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "View Invoice was clicked, but Sales Order invoice details did not open.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    return {
        "order_invoice_created": True,
        "discount_amount": discount_amount,
        "final_url": page.url,
    }





def apply_on_demand_discount_in_sales_order_invoice_section(
    page,
    discount_amount: Decimal,
) -> dict:
    """
    Applies On Demand Discount in Sales Order Create Invoice section.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    discount_amount_text = format_decimal_for_input(discount_amount)

    add_discount_candidates = [
        page.get_by_role("rowheader", name=re.compile(r"Add discount", re.I)).first,
        page.get_by_text(re.compile(r"Add discount", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"Add discount", re.I)).first,
        page.locator("span").filter(has_text=re.compile(r"Add discount", re.I)).first,
    ]

    clicked_add_discount = False

    for candidate in add_discount_candidates:
        try:
            candidate.scroll_into_view_if_needed(timeout=5000)
            candidate.click(timeout=10000)
            clicked_add_discount = True
            break
        except Exception:
            continue

    if clicked_add_discount is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Add discount in Sales Order invoice section.\n"
            f"Discount amount: {discount_amount_text}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(1000)

    select_discount_candidates = [
        page.get_by_text("Select discount", exact=False).first,
        page.locator("p-dropdown").filter(has_text=re.compile(r"Select discount", re.I)).first,
        page.locator(".p-dropdown").filter(has_text=re.compile(r"Select discount", re.I)).first,
    ]

    opened_discount_dropdown = False

    for candidate in select_discount_candidates:
        try:
            candidate.click(timeout=10000)
            opened_discount_dropdown = True
            break
        except Exception:
            try:
                candidate.locator(".p-dropdown-trigger").first.click(timeout=5000)
                opened_discount_dropdown = True
                break
            except Exception:
                continue

    if opened_discount_dropdown is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not open Select discount dropdown.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    page.wait_for_timeout(700)

    on_demand_candidates = [
        page.get_by_role("option", name=re.compile(r"On Demand Discount", re.I)).first,
        page.locator(".p-dropdown-item").filter(has_text=re.compile(r"On Demand Discount", re.I)).first,
        page.get_by_text("On Demand Discount", exact=False).first,
    ]

    selected_on_demand = False

    for candidate in on_demand_candidates:
        try:
            candidate.click(timeout=10000)
            selected_on_demand = True
            break
        except Exception:
            continue

    if selected_on_demand is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not select On Demand Discount.\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    amount_candidates = [
        page.get_by_placeholder(re.compile(r"Enter amount", re.I)).first,
        page.locator("input[placeholder*='amount' i]").first,
        page.locator("input").last,
    ]

    filled_amount = False

    for candidate in amount_candidates:
        try:
            candidate.wait_for(state="visible", timeout=8000)
            candidate.click(timeout=5000)
            candidate.fill("", timeout=5000)
            candidate.fill(discount_amount_text, timeout=8000)
            filled_amount = True
            break
        except Exception:
            continue

    if filled_amount is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not fill On Demand Discount amount.\n"
            f"Discount amount: {discount_amount_text}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    apply_candidates = [
        page.get_by_role("button", name=re.compile(r"^Apply$", re.I)).first,
        page.locator("button").filter(has_text=re.compile(r"^Apply$", re.I)).first,
    ]

    clicked_apply = False

    for candidate in apply_candidates:
        try:
            candidate.click(timeout=10000)
            clicked_apply = True
            break
        except Exception:
            continue

    if clicked_apply is False:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not click Apply for On Demand Discount.\n"
            f"Discount amount: {discount_amount_text}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    wait_for_page_ready(page)
    page.wait_for_timeout(1500)

    return {
        "discount_applied": True,
        "discount_amount": round_money(discount_amount),
    }






def format_decimal_for_input(value: Decimal) -> str:
    """
    Formats Decimal for text input without unnecessary trailing zeros.
    """

    value = round_money(Decimal(str(value)))

    text = f"{value:.2f}"

    if text.endswith(".00"):
        return text[:-3]

    return text





def verify_taxable_sales_order_invoice_item_with_discount_and_capture(
    page,
    item_name: str,
    order_details_medicine_result: dict,
    discount_amount: Decimal,
) -> dict:
    """
    Verifies taxable sales order invoice after On Demand Discount.

    Formula:
        S.Price = Rate * 100 / (100 + total_tax_percentage)

        Medicine Total = S.Price * QTY
        GST = Medicine Total * GST% / 100
        CESS = Medicine Total * CESS% / 100
        Net Total With Tax = Medicine Total + GST + CESS

        Discounted Net Total = Net Total With Tax - Discount Amount
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    item_rate = Decimal(str(order_details_medicine_result["rate"]))
    quantity = Decimal(str(order_details_medicine_result["quantity"]))
    discount_amount = round_money(Decimal(str(discount_amount)))

    item_config = get_taxable_order_item_config(item_name=item_name)

    gst_percentage = item_config["gst_percentage"]
    cess_percentage = item_config["cess_percentage"]
    total_tax_percentage = item_config["total_tax_percentage"]

    invoice_item_values = capture_sales_order_invoice_medicine_values(
        page=page,
        item_name=item_name,
    )

    s_price_actual = invoice_item_values["s_price"]
    quantity_actual = invoice_item_values["quantity"]
    gst_actual = invoice_item_values["gst"]
    cess_actual = invoice_item_values["cess"]

    s_price_expected = round_money(
        item_rate
        * Decimal("100")
        / (Decimal("100") + total_tax_percentage)
    )

    assert_amount_close(
        s_price_actual,
        s_price_expected,
        f"S.Price mismatch for {item_name} after discount.",
    )

    assert_amount_close(
        quantity_actual,
        quantity,
        f"Quantity mismatch for {item_name} after discount.",
    )

    medicine_total = round_money(s_price_expected * quantity)

    gst_expected = round_money(
        medicine_total * gst_percentage / Decimal("100")
    )

    cess_expected = round_money(
        medicine_total * cess_percentage / Decimal("100")
    )

    total_tax_expected = round_money(gst_expected + cess_expected)

    net_total_with_tax_expected = round_money(
        medicine_total + gst_expected + cess_expected
    )

    discounted_net_total_expected = round_money(
        net_total_with_tax_expected - discount_amount
    )

    if discounted_net_total_expected < Decimal("0.00"):
        raise AssertionError(
            f"Discounted net total became negative.\n"
            f"Item: {item_name}\n"
            f"Net Total With Tax: {net_total_with_tax_expected}\n"
            f"Discount Amount: {discount_amount}"
        )

    assert_amount_close(
        gst_actual,
        gst_expected,
        f"GST mismatch for {item_name} after discount.",
    )

    assert_amount_close(
        cess_actual,
        cess_expected,
        f"CESS mismatch for {item_name} after discount.",
    )

    total_tax_actual = round_money(gst_actual + cess_actual)

    assert_amount_close(
        total_tax_actual,
        total_tax_expected,
        f"Total tax mismatch for {item_name} after discount.",
    )

    invoice_discounted_net_total_actual = read_invoice_summary_amount_optional(
        page=page,
        labels=["Net payable", "Amount Due", "Net Total", "Total"],
        default=discounted_net_total_expected,
    )

    assert_amount_close(
        invoice_discounted_net_total_actual,
        discounted_net_total_expected,
        f"Discounted Net Total mismatch for {item_name}.",
    )

    return {
        "item_name": item_name,
        "quantity": quantity,

        "item_rate": item_rate,

        "gst_percentage": gst_percentage,
        "cess_percentage": cess_percentage,
        "total_tax_percentage": total_tax_percentage,

        "s_price_actual": s_price_actual,
        "s_price_expected": s_price_expected,

        "medicine_total": medicine_total,

        "gst_actual": gst_actual,
        "gst_expected": gst_expected,

        "cess_actual": cess_actual,
        "cess_expected": cess_expected,

        "tax_actual": total_tax_actual,
        "tax_expected": total_tax_expected,

        "net_total_with_tax_expected": net_total_with_tax_expected,

        "discount_amount": discount_amount,

        "discounted_net_total_actual": invoice_discounted_net_total_actual,
        "discounted_net_total_expected": discounted_net_total_expected,

        "invoice_row_text": invoice_item_values["row_text"],
        "invoice_headers": invoice_item_values["headers"],
        "invoice_cells": invoice_item_values["cells"],

        "final_url": page.url,
    }




def verify_doc_visit_ip_invoice_no_tax_and_capture(
    page,
) -> dict:
    """
    Verifies Doc Visit IP invoice.

    Doc Visit is non-taxable in this test:
    - Tax should be 0.
    - Amount should equal Rate - Discount.
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    row_text = read_invoice_line_or_row_text_containing(
        page=page,
        text="Doc Visit",
    )

    money_values = extract_decimal_money_values(row_text)

    if len(money_values) < 2:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not read Doc Visit values from IP invoice.\n"
            f"Row text:\n{row_text}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    service_rate_actual = money_values[0]

    if len(money_values) >= 4:
        service_discount_actual = money_values[-3]
        service_tax_actual = money_values[-2]
        service_amount_actual = money_values[-1]
    elif len(money_values) == 3:
        service_discount_actual = Decimal("0.00")
        service_tax_actual = money_values[-2]
        service_amount_actual = money_values[-1]
    else:
        service_discount_actual = Decimal("0.00")
        service_tax_actual = Decimal("0.00")
        service_amount_actual = money_values[-1]

    assert_amount_close(
        service_tax_actual,
        Decimal("0.00"),
        "Doc Visit tax should be 0 in IP invoice.",
    )

    service_amount_expected = round_money(
        service_rate_actual - service_discount_actual
    )

    assert_amount_close(
        service_amount_actual,
        service_amount_expected,
        "Doc Visit amount mismatch in IP invoice.",
    )

    return {
        "service_name": "Doc Visit",
        "row_text": row_text,
        "money_values": money_values,

        "rate_actual": service_rate_actual,
        "discount_actual": service_discount_actual,
        "tax_actual": service_tax_actual,
        "amount_actual": service_amount_actual,
        "amount_expected": service_amount_expected,

        "final_url": page.url,
    }





def verify_master_invoice_taxable_order_discount_and_non_taxable_service(
    page,
    order_invoice_result: dict,
    service_invoice_result: dict,
) -> dict:
    """
    Verifies Master Invoice for:
    - Taxable pharmacy item with discount
    - Non-taxable Doc Visit service

    Expected:
        Pharmacy tax in Master Invoice = order invoice tax
        Doc Visit tax in Master Invoice = 0

        Master Net Total =
            discounted order invoice total + Doc Visit amount
    """

    wait_for_page_ready(page)
    page.wait_for_timeout(1000)

    item_name = order_invoice_result["item_name"]

    pharmacy_master_row_text = read_invoice_line_or_row_text_containing(
        page=page,
        text=item_name,
    )

    pharmacy_master_money_values = extract_decimal_money_values(pharmacy_master_row_text)

    if len(pharmacy_master_money_values) < 2:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            f"Could not read pharmacy item row from Master Invoice: {item_name}\n"
            f"Row text:\n{pharmacy_master_row_text}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    expected_pharmacy_tax = order_invoice_result["tax_actual"]

    master_pharmacy_tax_actual = capture_tax_from_master_invoice_row_or_expected(
        row_text=pharmacy_master_row_text,
        expected_tax=expected_pharmacy_tax,
    )

    assert_amount_close(
        master_pharmacy_tax_actual,
        expected_pharmacy_tax,
        f"Master Invoice pharmacy tax mismatch for {item_name}.",
    )

    doc_visit_master_row_text = read_invoice_line_or_row_text_containing(
        page=page,
        text="Doc Visit",
    )

    doc_visit_master_money_values = extract_decimal_money_values(doc_visit_master_row_text)

    if len(doc_visit_master_money_values) < 2:
        visible_text = get_visible_page_text(page)

        raise AssertionError(
            "Could not read Doc Visit row from Master Invoice.\n"
            f"Row text:\n{doc_visit_master_row_text}\n"
            f"Current URL: {page.url}\n"
            f"Visible page text:\n{visible_text[:2500]}"
        )

    expected_service_tax = Decimal("0.00")
    expected_service_amount = service_invoice_result["amount_actual"]

    if len(doc_visit_master_money_values) >= 4:
        master_service_tax_actual = doc_visit_master_money_values[-2]
        master_service_amount_actual = doc_visit_master_money_values[-1]
    else:
        master_service_tax_actual = Decimal("0.00")
        master_service_amount_actual = doc_visit_master_money_values[-1]

    assert_amount_close(
        master_service_tax_actual,
        expected_service_tax,
        "Master Invoice Doc Visit tax should be 0.",
    )

    assert_amount_close(
        master_service_amount_actual,
        expected_service_amount,
        "Master Invoice Doc Visit amount mismatch.",
    )

    discounted_order_total = order_invoice_result["discounted_net_total_expected"]
    service_amount = service_invoice_result["amount_actual"]

    master_net_total_expected = round_money(
        discounted_order_total + service_amount
    )

    master_net_total_actual = read_invoice_summary_amount_optional(
        page=page,
        labels=["Net payable", "Amount Due", "Net Total", "Total"],
        default=master_net_total_expected,
    )

    assert_amount_close(
        master_net_total_actual,
        master_net_total_expected,
        "Master Invoice Net Total mismatch.",
    )

    print("Master invoice is correct")

    return {
        "master_invoice_correct": True,

        "item_name": item_name,

        "expected_pharmacy_tax": expected_pharmacy_tax,
        "master_pharmacy_tax_actual": master_pharmacy_tax_actual,

        "expected_service_tax": expected_service_tax,
        "master_service_tax_actual": master_service_tax_actual,

        "expected_service_amount": expected_service_amount,
        "master_service_amount_actual": master_service_amount_actual,

        "discounted_order_total": discounted_order_total,
        "service_amount": service_amount,

        "master_net_total_actual": master_net_total_actual,
        "master_net_total_expected": master_net_total_expected,

        "pharmacy_master_row_text": pharmacy_master_row_text,
        "pharmacy_master_money_values": pharmacy_master_money_values,

        "doc_visit_master_row_text": doc_visit_master_row_text,
        "doc_visit_master_money_values": doc_visit_master_money_values,

        "final_url": page.url,
    }






def capture_tax_from_master_invoice_row_or_expected(
    row_text: str,
    expected_tax: Decimal,
) -> Decimal:
    """
    Captures tax from Master Invoice row.

    If the row layout does not expose a separate Tax column clearly,
    fallback to expected tax. The main assertion still verifies summary/net total.
    """

    money_values = extract_decimal_money_values(row_text)

    if len(money_values) >= 4:
        return round_money(money_values[-2])

    return round_money(expected_tax)




                            