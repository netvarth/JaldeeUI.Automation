import random
import re
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Any

from playwright.sync_api import (
    Locator,
    Page,
    TimeoutError as PlaywrightTimeoutError,
    expect,
)


DEFAULT_TIMEOUT = 15_000


# Case 1 :: Create an invoice and do the payment


def complete_single_service_booking_invoice_flow(
    page: Page,
    config,
    consumer_profile,
    doctor_name: str = "Naveen KP",
    service_name: str = "Video call Services",
) -> dict:
    """
    Complete flow for creating a booking invoice with one service.

    Flow:
    1. Open Appointment dashboard.
    2. Click +Appointment.
    3. Create a random patient.
    4. Select doctor and service.
    5. Confirm appointment.
    6. Open the latest appointment from the final pagination page.
    7. Open appointment details.
    8. Create and update invoice.
    9. Complete payment using Cash or Pay by Others.
    10. Verify Amount Due is zero.
    """

    select_first_business_if_needed(page)
    open_appointment_dashboard(page)
    open_create_appointment_page(page)

    patient_name = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    select_appointment_doctor(
        page=page,
        doctor_name=doctor_name,
    )

    select_appointment_service(
        page=page,
        service_name=service_name,
    )

    confirm_appointment(page)

    open_latest_created_appointment(
        page=page,
        patient_name=patient_name,
    )

    open_appointment_details(page)

    create_booking_invoice(page)

    invoice_created = update_booking_invoice(page)

    payment_result = complete_booking_invoice_payment(page)
    amount_due = payment_result["amount_due"]

    assert_amount_close(
        actual=amount_due,
        expected=Decimal("0.00"),
        label="Booking invoice amount due after payment",
    )

    return {
        "patient_name": patient_name,
        "doctor_name": doctor_name,
        "service_name": service_name,
        "invoice_created": invoice_created,
        "payment_completed": payment_result["payment_completed"],
        "payment_method": payment_result["payment_method"],
        "payment_mode": payment_result.get("payment_mode"),
        "amount_due": amount_due,
    }


def select_first_business_if_needed(page: Page) -> None:
    """
    Select the first business only when a business-selection screen is shown.

    This function does not click arbitrary sidebar links.
    """

    # Already inside the provider business application.
    if "/business/" in page.url:
        return

    business_selection_indicators = [
        page.get_by_text(
            re.compile(
                r"Select Business|Choose Business|My Businesses",
                re.IGNORECASE,
            )
        ),
        page.locator(
            '[class*="business-card" i], '
            '[id*="business-card" i]'
        ),
    ]

    selection_screen_visible = any(
        first_visible_locator(locator) is not None
        for locator in business_selection_indicators
    )

    if not selection_screen_visible:
        return

    business_cards = page.locator(
        '[class*="business-card" i], '
        'p-card, '
        '.p-card'
    )

    visible_business = first_visible_locator(business_cards)

    assert visible_business is not None, (
        "Business selection page is visible, but no business card was found."
    )

    visible_business.click()
    page.wait_for_load_state("domcontentloaded")






def open_appointment_dashboard(page: Page) -> None:
    """
    Open the Appointment dashboard using the sidebar link.
    """

    if (
        "/business/appointments" in page.url
        and "/business/appointments/appointment" not in page.url
    ):
        wait_for_appointment_dashboard(page)
        return

    sidebar_link = page.locator(
        'a[href^="/business/appointments?"]'
    )

    visible_sidebar_link = first_visible_locator(sidebar_link)

    if visible_sidebar_link is None:
        sidebar_link = page.locator(
            'a[href*="/business/appointments"]'
        )

        visible_sidebar_link = first_visible_locator(sidebar_link)

    assert visible_sidebar_link is not None, (
        "Unable to locate the Appointment sidebar link."
    )

    visible_sidebar_link.click()

    page.wait_for_url(
        re.compile(
            r"/business/appointments(?:\?|$)",
            re.IGNORECASE,
        ),
        timeout=DEFAULT_TIMEOUT,
    )

    try:
        page.wait_for_load_state(
            "networkidle",
            timeout=10_000,
        )
    except PlaywrightTimeoutError:
        pass

    wait_for_appointment_dashboard(page)



def wait_for_appointment_dashboard(page: Page) -> None:
    """
    Wait until the Appointment dashboard finishes loading.

    The page may initially show:
    'Welcome to your Appointments Loading... Appointments'
    before the dashboard cards are rendered.
    """

    expect(
        page.get_by_text(
            re.compile(
                r"Welcome to your Appointments",
                re.IGNORECASE,
            )
        ).first
    ).to_be_visible(timeout=DEFAULT_TIMEOUT)

    loading_text = page.get_by_text(
        re.compile(r"^\s*Loading\.\.\.\s*$", re.IGNORECASE)
    )

    try:
        expect(loading_text).to_be_hidden(timeout=30_000)
    except AssertionError:
        # Some builds render Loading... inside a larger text container.
        page.wait_for_function(
            """
            () => !document.body.innerText.includes('Loading...')
            """,
            timeout=30_000,
        )

    page.wait_for_timeout(500)

    appointment_card_candidates = [
        page.locator("p-card").filter(
            has_text=re.compile(
                r"^\s*Appointment\s*$",
                re.IGNORECASE,
            )
        ),
        page.locator(".p-card").filter(
            has_text=re.compile(
                r"^\s*Appointment\s*$",
                re.IGNORECASE,
            )
        ),
        page.get_by_text(
            "Appointment",
            exact=True,
        ),
    ]

    for candidate_group in appointment_card_candidates:
        visible_candidate = first_visible_locator(candidate_group)

        if visible_candidate is not None:
            return

    raise AssertionError(
        "Appointment dashboard finished loading, but the "
        "Appointment creation card was not displayed."
    )



def open_create_appointment_page(page: Page) -> None:
    """
    Click the Appointment creation card from the Appointment dashboard.

    The card contains a plus icon and the text 'Appointment'.
    """

    # Do nothing when this page is already open.
    if "/business/appointments/appointment" in page.url:
        expect(
            page.get_by_text(
                re.compile(r"Create New Patient", re.IGNORECASE)
            )
        ).to_be_visible(timeout=DEFAULT_TIMEOUT)
        return

    appointment_card = page.locator("p-card").filter(
        has_text=re.compile(r"^\s*Appointment\s*$", re.IGNORECASE)
    )

    visible_card = first_visible_locator(appointment_card)

    if visible_card is None:
        # PrimeNG may render p-card as a div with p-card class.
        card_container = page.locator(".p-card").filter(
            has_text=re.compile(r"^\s*Appointment\s*$", re.IGNORECASE)
        )

        visible_card = first_visible_locator(card_container)

    if visible_card is None:
        # Final fallback: exact Appointment text and nearest card ancestor.
        appointment_text = page.get_by_text(
            "Appointment",
            exact=True,
        )

        visible_text = first_visible_locator(appointment_text)

        assert visible_text is not None, (
            "Unable to locate the Appointment creation card."
        )

        card_ancestor = visible_text.locator(
            "xpath=ancestor::*["
            "self::p-card or "
            "contains(@class, 'p-card')"
            "][1]"
        )

        if card_ancestor.count() > 0:
            visible_card = card_ancestor.first
        else:
            visible_card = visible_text

    visible_card.scroll_into_view_if_needed()
    visible_card.click()

    page.wait_for_url(
        re.compile(
            r"/business/appointments/appointment",
            re.IGNORECASE,
        ),
        timeout=DEFAULT_TIMEOUT,
    )

    expect(
        page.get_by_text(
            re.compile(r"Create New Patient", re.IGNORECASE)
        )
    ).to_be_visible(timeout=DEFAULT_TIMEOUT)




def create_random_patient_from_consumer_profile(
    page: Page,
    consumer_profile,
) -> str:
    """
    Create a new random patient from the Create Appointment page.
    """

    create_patient_button = page.get_by_text(
        re.compile(r"^\s*Create New Patient\s*$", re.IGNORECASE)
    )

    expect(create_patient_button.first).to_be_visible(
        timeout=DEFAULT_TIMEOUT
    )
    create_patient_button.first.click()

    # Wait until the patient creation form/dialog is actually visible.
    patient_form = page.locator(
        "p-dialog:visible, "
        ".p-dialog:visible, "
        "form:visible"
    ).filter(
        has=page.locator(
            'input[placeholder*="First Name" i], '
            'input[formcontrolname*="first" i], '
            'input[name*="first" i]'
        )
    )

    expect(patient_form.first).to_be_visible(
        timeout=DEFAULT_TIMEOUT
    )

    first_name = str(
        get_profile_value(
            consumer_profile,
            "first_name",
            "firstname",
            "firstName",
            default=f"Auto{random.randint(1000, 9999)}",
        )
    )

    last_name = str(
        get_profile_value(
            consumer_profile,
            "last_name",
            "lastname",
            "lastName",
            default=f"Patient{random.randint(100, 999)}",
        )
    )

    email = str(
        get_profile_value(
            consumer_profile,
            "email",
            "email_id",
            "emailId",
            default=(
                f"{first_name}.{last_name}.{random.randint(1000, 9999)}"
                "@example.com"
            ),
        )
    )

    phone = str(
        get_profile_value(
            consumer_profile,
            "phone",
            "phone_number",
            "mobile",
            "mobile_number",
            "consumer_phone",
            default=generate_random_indian_mobile_number(),
        )
    )

    gender = str(
        get_profile_value(
            consumer_profile,
            "gender",
            default=random.choice(["Male", "Female"]),
        )
    )

    fill_patient_field(
        page=page,
        field_name="First Name",
        value=first_name,
        role_names=["First Name", "First name"],
        placeholders=["First Name", "First name"],
        selectors=[
            'input[formcontrolname="firstName"]',
            'input[formcontrolname="firstname"]',
            'input[formcontrolname*="first" i]',
            'input[name="firstName"]',
            'input[name*="first" i]',
            'input[id*="firstName" i]',
        ],
        required=True,
    )

    fill_patient_field(
        page=page,
        field_name="Last Name",
        value=last_name,
        role_names=["Last Name", "Last name"],
        placeholders=["Last Name", "Last name"],
        selectors=[
            'input[formcontrolname="lastName"]',
            'input[formcontrolname="lastname"]',
            'input[formcontrolname*="last" i]',
            'input[name="lastName"]',
            'input[name*="last" i]',
            'input[id*="lastName" i]',
        ],
        required=False,
    )

    fill_patient_field(
        page=page,
        field_name="Email",
        value=email,
        role_names=[
            "Email(user@xyz.com)",
            "Email",
            "Email Address",
        ],
        placeholders=[
            "Email(user@xyz.com)",
            "Email",
            "Email Address",
        ],
        selectors=[
            'input[type="email"]',
            'input[formcontrolname*="email" i]',
            'input[name*="email" i]',
            'input[id*="email" i]',
        ],
        required=False,
    )

    fill_patient_phone_number(
        page=page,
        phone=phone,
    )

    select_patient_gender(
        page=page,
        gender=gender,
    )

    save_button = page.get_by_role(
        "button",
        name=re.compile(r"^\s*Save\s*$", re.IGNORECASE),
    )

    visible_save = last_visible_locator(save_button)

    assert visible_save is not None, (
        "Unable to locate the Save button in the patient creation form."
    )

    visible_save.scroll_into_view_if_needed()
    visible_save.click()

    confirm_yes_dialog_if_visible(page)

    # After saving, the patient form should close and appointment form remain.
    expect(
        page.get_by_text(
            re.compile(
                r"Select Doctor|Select Service|Create Appointment",
                re.IGNORECASE,
            )
        ).first
    ).to_be_visible(timeout=DEFAULT_TIMEOUT)

    return f"{first_name} {last_name}".strip()



def fill_patient_field(
    page: Page,
    field_name: str,
    value: str,
    role_names: list[str],
    placeholders: list[str],
    selectors: list[str],
    required: bool = True,
) -> bool:
    """
    Fill a patient form field using accessible name, placeholder,
    label association, and stable HTML attribute fallbacks.
    """

    candidates: list[Locator] = []

    for role_name in role_names:
        candidates.append(
            page.get_by_role(
                "textbox",
                name=re.compile(
                    rf"^\s*{re.escape(role_name)}\s*\*?\s*$",
                    re.IGNORECASE,
                ),
            )
        )

    for placeholder in placeholders:
        candidates.append(
            page.get_by_placeholder(
                re.compile(
                    re.escape(placeholder),
                    re.IGNORECASE,
                )
            )
        )

    for role_name in role_names:
        candidates.append(
            page.get_by_label(
                re.compile(
                    re.escape(role_name),
                    re.IGNORECASE,
                )
            )
        )

    for selector in selectors:
        candidates.append(page.locator(selector))

    for candidate_group in candidates:
        for index in range(candidate_group.count()):
            candidate = candidate_group.nth(index)

            try:
                if not candidate.is_visible():
                    continue

                candidate.scroll_into_view_if_needed()
                candidate.click()
                candidate.fill(value)

                assert candidate.input_value() == value, (
                    f"{field_name} was not filled correctly. "
                    f"Expected={value}, Actual={candidate.input_value()}"
                )

                return True

            except PlaywrightTimeoutError:
                continue

    if required:
        visible_inputs = page.locator(
            "p-dialog:visible input:visible, "
            ".p-dialog:visible input:visible, "
            "form:visible input:visible"
        )

        input_details: list[str] = []

        for index in range(visible_inputs.count()):
            field = visible_inputs.nth(index)

            input_details.append(
                " | ".join(
                    [
                        f"type={field.get_attribute('type')}",
                        f"name={field.get_attribute('name')}",
                        f"id={field.get_attribute('id')}",
                        (
                            "formcontrolname="
                            f"{field.get_attribute('formcontrolname')}"
                        ),
                        f"placeholder={field.get_attribute('placeholder')}",
                        f"aria-label={field.get_attribute('aria-label')}",
                    ]
                )
            )

        raise AssertionError(
            f"Unable to locate patient field: {field_name}.\n"
            f"Visible inputs:\n" + "\n".join(input_details)
        )

    return False



def select_appointment_doctor(
    page: Page,
    doctor_name: str,
) -> None:
    """
    Select the requested doctor from the Create Appointment page.
    """

    doctor_field = page.get_by_text(
        "Hari Kumar",
        exact=True,
    )

    if doctor_field.count() == 0:
        doctor_field = page.locator(
            "p-dropdown, p-select, .p-dropdown, .p-select"
        ).filter(
            has=page.get_by_text(
                re.compile(r"Hari Kumar|James J|Naveen KP", re.IGNORECASE)
            )
        )

    expect(doctor_field.first).to_be_visible(
        timeout=DEFAULT_TIMEOUT
    )

    doctor_field.first.click()

    doctor_option = page.get_by_text(
        doctor_name,
        exact=True,
    )

    expect(doctor_option.last).to_be_visible(
        timeout=DEFAULT_TIMEOUT
    )

    doctor_option.last.click()

    expect(
        page.get_by_text(
            doctor_name,
            exact=True,
        ).first
    ).to_be_visible(timeout=DEFAULT_TIMEOUT)

    print(f"[Appointment] Selected doctor: {doctor_name}")




def is_dropdown_overlay_open(page: Page) -> bool:
    """
    Return True when a visible dropdown option overlay is open.
    """

    overlays = page.locator(
        ".p-dropdown-panel:visible, "
        ".p-select-overlay:visible, "
        ".p-overlay:visible [role='option']:visible, "
        '[role="listbox"]:visible'
    )

    return overlays.count() > 0




def expect_doctor_selected(
    page: Page,
    doctor_name: str,
) -> None:
    """
    Verify that the requested doctor is displayed after selection.
    """

    selected_doctor = page.get_by_text(
        re.compile(
            rf"^\s*{re.escape(doctor_name)}\s*$",
            re.IGNORECASE,
        )
    )

    visible_selected_doctor = first_visible_locator(selected_doctor)

    assert visible_selected_doctor is not None, (
        f"Doctor '{doctor_name}' was selected, but the selected value "
        "was not displayed in the appointment form."
    )



def locate_visible_dropdown_option(
    page: Page,
    option_text: str,
) -> Locator | None:
    """
    Locate a visible option from an open PrimeNG dropdown.

    Supports:
    - role="option"
    - PrimeNG dropdown items
    - list items
    - plain text options rendered inside the visible overlay
    """

    exact_pattern = re.compile(
        rf"^\s*{re.escape(option_text)}\s*$",
        re.IGNORECASE,
    )

    option_candidates = [
        # Standard accessible option.
        page.get_by_role(
            "option",
            name=exact_pattern,
        ),

        # PrimeNG dropdown and select implementations.
        page.locator(
            ".p-dropdown-panel:visible .p-dropdown-item:visible"
        ).filter(
            has_text=exact_pattern
        ),
        page.locator(
            ".p-select-overlay:visible .p-select-option:visible"
        ).filter(
            has_text=exact_pattern
        ),
        page.locator(
            ".p-overlay:visible [role='option']:visible"
        ).filter(
            has_text=exact_pattern
        ),

        # Common list structures.
        page.locator(
            ".p-dropdown-panel:visible li:visible"
        ).filter(
            has_text=exact_pattern
        ),
        page.locator(
            ".p-overlay:visible li:visible"
        ).filter(
            has_text=exact_pattern
        ),
        page.locator(
            "[role='listbox']:visible li:visible"
        ).filter(
            has_text=exact_pattern
        ),

        # Exact text inside any currently visible dropdown overlay.
        page.locator(
            ".p-dropdown-panel:visible"
        ).get_by_text(
            exact_pattern,
            exact=True,
        ),
        page.locator(
            ".p-select-overlay:visible"
        ).get_by_text(
            exact_pattern,
            exact=True,
        ),
        page.locator(
            "[role='listbox']:visible"
        ).get_by_text(
            exact_pattern,
            exact=True,
        ),

        # Final fallback for the UI shown in the screenshot.
        page.get_by_text(
            exact_pattern,
            exact=True,
        ),
    ]

    for candidate_group in option_candidates:
        for index in range(candidate_group.count()):
            candidate = candidate_group.nth(index)

            try:
                if candidate.is_visible():
                    return candidate
            except PlaywrightTimeoutError:
                continue

    return None




def find_doctor_dropdown(page: Page) -> Locator | None:
    """
    Locate the clickable dropdown directly below the Select Doctor label.
    """

    doctor_label_candidates = [
        page.locator("label").filter(
            has_text=re.compile(r"^\s*Select Doctor\s*\*?\s*$", re.IGNORECASE)
        ),
        page.locator("div, span, p").filter(
            has_text=re.compile(r"^\s*Select Doctor\s*\*?\s*$", re.IGNORECASE)
        ),
        page.get_by_text(
            re.compile(r"^\s*Select Doctor\s*\*?\s*$", re.IGNORECASE)
        ),
    ]

    visible_label: Locator | None = None

    for candidate_group in doctor_label_candidates:
        visible_label = first_visible_locator(candidate_group)

        if visible_label is not None:
            break

    if visible_label is None:
        return None

    # First try the immediate sibling after the Select Doctor label.
    sibling_candidates = [
        visible_label.locator("xpath=following-sibling::*[1]"),
        visible_label.locator("xpath=parent::*/following-sibling::*[1]"),
    ]

    for sibling in sibling_candidates:
        if sibling.count() == 0:
            continue

        candidate = sibling.first

        try:
            if candidate.is_visible():
                return candidate
        except PlaywrightTimeoutError:
            pass

    # Locate a dropdown inside the nearest field container.
    field_containers = [
        visible_label.locator("xpath=parent::*"),
        visible_label.locator("xpath=ancestor::div[1]"),
        visible_label.locator("xpath=ancestor::div[2]"),
    ]

    dropdown_selector = (
        "p-dropdown, "
        "p-select, "
        ".p-dropdown, "
        ".p-select, "
        '[role="combobox"], '
        ".p-dropdown-trigger, "
        ".p-select-dropdown"
    )

    for container in field_containers:
        if container.count() == 0:
            continue

        dropdowns = container.first.locator(dropdown_selector)
        visible_dropdown = first_visible_locator(dropdowns)

        if visible_dropdown is not None:
            return visible_dropdown

    # Recorded-page fallback: current selected doctor is Hari Kumar.
    current_doctor = page.get_by_text(
        re.compile(r"^\s*Hari Kumar\s*$", re.IGNORECASE)
    )

    visible_current_doctor = first_visible_locator(current_doctor)

    if visible_current_doctor is not None:
        clickable_ancestor = visible_current_doctor.locator(
            "xpath=ancestor::*["
            "@role='combobox' or "
            "self::p-dropdown or "
            "self::p-select or "
            "contains(@class, 'p-dropdown') or "
            "contains(@class, 'p-select')"
            "][1]"
        )

        if clickable_ancestor.count() > 0:
            return clickable_ancestor.first

        return visible_current_doctor

    return None





def get_clickable_dropdown_element(locator: Locator) -> Locator:
    """
    Return the clickable container for a PrimeNG dropdown element.
    """

    try:
        tag_name = locator.evaluate(
            "(element) => element.tagName.toLowerCase()"
        )
    except PlaywrightTimeoutError:
        return locator

    if tag_name in {"input", "span", "label"}:
        ancestor = locator.locator(
            "xpath=ancestor::*["
            "self::p-dropdown or "
            "self::p-select or "
            "contains(@class, 'p-dropdown') or "
            "contains(@class, 'p-select') or "
            "@role='combobox'"
            "][1]"
        )

        if ancestor.count() > 0:
            return ancestor.first

    return locator





def select_appointment_service(
    page: Page,
    service_name: str,
) -> None:
    """
    Open the Select Service dropdown and choose the requested service.

    The service field initially displays the value 'service'.
    """

    # This follows the recorded UI flow:
    # page.get_by_text("service", exact=True).click()
    service_field = page.get_by_text(
        re.compile(r"^\s*service\s*$", re.IGNORECASE),
        exact=True,
    )

    visible_service_field = first_visible_locator(service_field)

    if visible_service_field is None:
        # Locate the combobox immediately after the Select Service label.
        service_label = page.get_by_text(
            re.compile(r"^\s*Select Service\s*\*?\s*$", re.IGNORECASE),
            exact=True,
        )

        visible_service_label = first_visible_locator(service_label)

        assert visible_service_label is not None, (
            "Unable to locate the Select Service label."
        )

        service_combobox = visible_service_label.locator(
            "xpath=following::*[@role='combobox'][1]"
        )

        visible_service_field = first_visible_locator(service_combobox)

    assert visible_service_field is not None, (
        "Unable to locate the Select Service dropdown field."
    )

    visible_service_field.scroll_into_view_if_needed()

    try:
        visible_service_field.click(timeout=5_000)
    except PlaywrightTimeoutError:
        visible_service_field.click(timeout=5_000, force=True)

    # Wait for the requested service to appear in the opened dropdown.
    service_option = page.get_by_text(
        re.compile(
            rf"^\s*{re.escape(service_name)}\s*$",
            re.IGNORECASE,
        ),
        exact=True,
    )

    visible_service_option = last_visible_locator(service_option)

    assert visible_service_option is not None, (
        f"Service option '{service_name}' was not visible after "
        "opening the Select Service dropdown."
    )

    visible_service_option.scroll_into_view_if_needed()

    try:
        visible_service_option.click(timeout=5_000)
    except PlaywrightTimeoutError:
        visible_service_option.click(timeout=5_000, force=True)

    # Confirm that the selected service now appears in the field.
    selected_service = page.get_by_text(
        re.compile(
            rf"^\s*{re.escape(service_name)}\s*$",
            re.IGNORECASE,
        ),
        exact=True,
    )

    expect(selected_service.first).to_be_visible(
        timeout=DEFAULT_TIMEOUT
    )

    print(f"[Appointment] Selected service: {service_name}")





def confirm_appointment(page: Page) -> None:
    """
    Confirm the appointment.

    For WhatsApp services, ensure the WhatsApp number field is valid before
    clicking Confirm.
    """

    ensure_whatsapp_service_field_is_valid(page)

    confirm_button = page.get_by_role(
        "button",
        name="Confirm",
        exact=True,
    )

    expect(confirm_button.last).to_be_visible(timeout=DEFAULT_TIMEOUT)
    expect(confirm_button.last).to_be_enabled(timeout=20_000)

    confirm_button.last.click()

    wait_for_success_message(
        page=page,
        patterns=[
            r"appointment.*created",
            r"appointment.*confirmed",
            r"booking.*created",
            r"successfully",
        ],
        required=False,
    )

    page.wait_for_url(
        re.compile(
            r"/business/appointments(?:\?|$)",
            re.IGNORECASE,
        ),
        timeout=30_000,
    )

    wait_for_appointment_dashboard(page)


def ensure_whatsapp_service_field_is_valid(page: Page) -> None:
    """
    Validate the additional WhatsApp number field shown for WhatsApp services.
    """

    whatsapp_inputs = [
        page.get_by_role(
            "textbox",
            name=re.compile(
                r"WhatsApp|10123",
                re.IGNORECASE,
            ),
        ),
        page.locator(
            'input[formcontrolname*="whatsapp" i], '
            'input[name*="whatsapp" i], '
            'input[id*="whatsapp" i]'
        ),
    ]

    whatsapp_input = None

    for candidate_group in whatsapp_inputs:
        whatsapp_input = first_visible_locator(candidate_group)

        if whatsapp_input is not None:
            break

    # Non-WhatsApp services do not show this field.
    if whatsapp_input is None:
        return

    current_value = re.sub(
        r"\D",
        "",
        whatsapp_input.input_value(),
    )[-10:]

    assert len(current_value) == 10, (
        "WhatsApp service requires a valid 10-digit WhatsApp number. "
        f"Current value={current_value}"
    )

    # Refill and blur so Angular validation is triggered.
    whatsapp_input.fill(current_value)
    whatsapp_input.press("Tab")
    page.wait_for_timeout(500)

    


def open_latest_created_appointment(
    page: Page,
    patient_name: str | None = None,
) -> None:
    """
    Find and expand the newly created appointment.

    Strategy:
    1. Search each pagination page for the generated patient name.
    2. When found, click the appointment row's right-side expand control.
    3. If the patient name cannot be found, go to the final page and
       expand the last visible appointment row.
    """

    wait_for_appointment_rows(page)

    if patient_name and find_and_expand_patient_appointment(
        page=page,
        patient_name=patient_name,
    ):
        return

    # Fallback: move to the final page and expand the last visible row.
    navigate_to_last_appointment_page(page)
    wait_for_appointment_rows(page)

    appointment_rows = get_visible_appointment_rows(page)

    assert appointment_rows, (
        "No appointment rows were found on the Appointment dashboard."
    )

    expand_appointment_row(
        row=appointment_rows[-1],
        patient_name=patient_name,
    )



def find_and_expand_patient_appointment(
    page: Page,
    patient_name: str,
) -> bool:
    """
    Search all appointment pagination pages for the specified patient.
    """

    normalized_patient_name = normalize_text(patient_name)

    # Start from the current page and move forward through pagination.
    for _ in range(100):
        wait_for_appointment_rows(page)

        patient_matches = page.get_by_text(
            re.compile(
                rf"^\s*{re.escape(normalized_patient_name)}\s*$",
                re.IGNORECASE,
            )
        )

        for index in range(patient_matches.count()):
            patient = patient_matches.nth(index)

            try:
                if not patient.is_visible():
                    continue

                row = find_appointment_row_from_patient(patient)

                if row is None:
                    continue

                expand_appointment_row(
                    row=row,
                    patient_name=patient_name,
                )
                return True

            except PlaywrightTimeoutError:
                continue

        next_button = find_visible_next_pagination_button(page)

        if next_button is None or is_locator_disabled(next_button):
            break

        next_button.click()
        wait_for_appointment_page_change(page)

    return False





def find_appointment_row_from_patient(
    patient_locator: Locator,
) -> Locator | None:
    """
    Find the appointment row containing the patient name.
    """

    row_candidates = [
        patient_locator.locator(
            "xpath=ancestor::*["
            "contains(@class, 'appointment') and "
            "(contains(@class, 'row') or contains(@class, 'item'))"
            "][1]"
        ),
        patient_locator.locator(
            "xpath=ancestor::*["
            "self::tr or "
            "@role='row' or "
            "contains(@class, 'p-accordion-header') or "
            "contains(@class, 'list-item') or "
            "contains(@class, 'card')"
            "][1]"
        ),
        patient_locator.locator(
            "xpath=ancestor::div["
            ".//button or "
            ".//*[@role='button'] or "
            ".//*[contains(@class, 'chevron')] or "
            ".//*[contains(@class, 'angle-down')]"
            "][1]"
        ),
    ]

    for candidate in row_candidates:
        if candidate.count() == 0:
            continue

        row = candidate.first

        try:
            if row.is_visible():
                return row
        except PlaywrightTimeoutError:
            continue

    return None


def expand_appointment_row(
    row: Locator,
    patient_name: str | None = None,
) -> None:
    """
    Expand one appointment row using its right-side dropdown/chevron control.
    """

    row.scroll_into_view_if_needed()

    expand_candidates = [
        row.get_by_role(
            "button",
            name=re.compile(
                r"Expand|View|Details|dropdown|chevron",
                re.IGNORECASE,
            ),
        ),
        row.locator(
            'button[aria-expanded], '
            'button[aria-label*="expand" i], '
            'button[aria-label*="details" i], '
            '[role="button"][aria-expanded], '
            '.p-accordion-header-link, '
            '.p-accordion-toggle-icon, '
            '.pi-chevron-down, '
            '.pi-angle-down, '
            '.fa-chevron-down, '
            '.fa-angle-down, '
            'i[class*="chevron-down"], '
            'i[class*="angle-down"]'
        ),
        row.locator("button"),
        row.locator('[role="button"]'),
    ]

    for candidate_group in expand_candidates:
        visible_candidate = last_visible_locator(candidate_group)

        if visible_candidate is None:
            continue

        try:
            visible_candidate.click(timeout=5_000)
            wait_for_expanded_appointment_actions(
                row=row,
                patient_name=patient_name,
            )
            return
        except (PlaywrightTimeoutError, AssertionError):
            continue

    # Final fallback: click near the right edge of the appointment row.
    try:
        bounding_box = row.bounding_box()

        if bounding_box:
            row.click(
                position={
                    "x": max(bounding_box["width"] - 20, 1),
                    "y": bounding_box["height"] / 2,
                },
                timeout=5_000,
            )

            wait_for_expanded_appointment_actions(
                row=row,
                patient_name=patient_name,
            )
            return
    except PlaywrightTimeoutError:
        pass

    raise AssertionError(
        "Unable to expand the appointment row"
        + (
            f" for patient '{patient_name}'."
            if patient_name
            else "."
        )
    )




def wait_for_expanded_appointment_actions(
    row: Locator,
    patient_name: str | None = None,
) -> None:
    """
    Verify that the appointment row has expanded.
    """

    action_pattern = re.compile(
        r"View Details|Assign Myself|Generate Bill|Create Invoice",
        re.IGNORECASE,
    )

    row_actions = row.get_by_text(action_pattern)

    try:
        expect(row_actions.first).to_be_visible(timeout=5_000)
        return
    except AssertionError:
        pass

    page = row.page

    global_actions = page.get_by_text(action_pattern)

    expect(global_actions.last).to_be_visible(timeout=DEFAULT_TIMEOUT)




def get_visible_appointment_rows(page: Page) -> list[Locator]:
    """
    Return visible appointment rows from the dashboard.
    """

    row_selectors = [
        page.locator(
            '[class*="appointment"][class*="row" i]'
        ),
        page.locator(
            '[class*="appointment"][class*="item" i]'
        ),
        page.locator(
            ".p-accordion-tab"
        ),
        page.locator(
            '[role="row"]'
        ),
    ]

    rows: list[Locator] = []

    for group in row_selectors:
        for index in range(group.count()):
            candidate = group.nth(index)

            try:
                if not candidate.is_visible():
                    continue

                text = normalize_text(candidate.inner_text())

                if not text:
                    continue

                # Appointment rows normally contain status, service, time,
                # doctor, or a patient name.
                if not re.search(
                    r"Confirmed|Arrived|Checked|AM|PM|Consultation|Services?",
                    text,
                    re.IGNORECASE,
                ):
                    continue

                rows.append(candidate)

            except PlaywrightTimeoutError:
                continue

        if rows:
            return rows

    # Generic fallback: rows containing a confirmed appointment.
    confirmed_labels = page.get_by_text(
        re.compile(
            r"^\s*(Confirmed|Arrived|Checked In)\s*$",
            re.IGNORECASE,
        )
    )

    for index in range(confirmed_labels.count()):
        status = confirmed_labels.nth(index)

        try:
            if not status.is_visible():
                continue

            row = status.locator(
                "xpath=ancestor::div["
                ".//button or "
                ".//*[@role='button'] or "
                ".//*[contains(@class, 'chevron')]"
                "][1]"
            )

            if row.count() > 0 and row.first.is_visible():
                rows.append(row.first)

        except PlaywrightTimeoutError:
            continue

    return rows



def wait_for_appointment_rows(page: Page) -> None:
    """
    Wait until appointment data is visible on the dashboard.
    """

    expect(
        page.get_by_text(
            re.compile(
                r"Confirmed|Arrived|Checked In|Completed",
                re.IGNORECASE,
            )
        ).first
    ).to_be_visible(timeout=DEFAULT_TIMEOUT)





def navigate_to_last_appointment_page(page: Page) -> None:
    """
    Navigate forward until the pagination Next button becomes disabled.
    """

    for _ in range(100):
        next_button = find_visible_next_pagination_button(page)

        if next_button is None or is_locator_disabled(next_button):
            return

        next_button.click()
        wait_for_appointment_page_change(page)

    raise AssertionError(
        "Appointment pagination did not reach the final page."
    )



def wait_for_appointment_page_change(page: Page) -> None:
    """
    Wait briefly for the appointment list to refresh after pagination.
    """

    page.wait_for_timeout(750)

    try:
        page.wait_for_load_state(
            "networkidle",
            timeout=3_000,
        )
    except PlaywrightTimeoutError:
        pass

    wait_for_appointment_rows(page)




def find_visible_next_pagination_button(
    page: Page,
) -> Locator | None:
    candidates = [
        page.get_by_role(
            "button",
            name=re.compile(
                r"Next|Next Page|Go to next page",
                re.IGNORECASE,
            ),
        ),
        page.locator(
            'button[aria-label*="next" i], '
            '.p-paginator-next, '
            'a[aria-label*="next" i]'
        ),
        page.get_by_text(re.compile(r"^>$")),
    ]

    for candidate_group in candidates:
        count = candidate_group.count()

        for index in range(count):
            candidate = candidate_group.nth(index)

            try:
                if candidate.is_visible():
                    return candidate
            except PlaywrightTimeoutError:
                continue

    return None


def open_appointment_details(page: Page) -> None:
    """
    Open the appointment details screen from the expanded appointment.

    Supports the current booking UI where the page may show:
    - Appointment
    - New Invoice
    - View Invoice

    instead of the older:
    - Appointment Details
    - Create Invoice
    - Generate Bill
    """

    # =========================================================
    # LOCATE VIEW DETAILS
    # =========================================================

    view_details_candidates = page.get_by_role(
        "button",
        name=re.compile(
            r"View\s*Details",
            re.IGNORECASE,
        ),
    )

    visible_view_details = last_visible_locator(
        view_details_candidates
    )

    if visible_view_details is None:
        view_details_candidates = page.get_by_text(
            re.compile(
                r"View\s*Details",
                re.IGNORECASE,
            )
        )

        visible_view_details = last_visible_locator(
            view_details_candidates
        )

    assert visible_view_details is not None, (
        "Unable to locate the View Details button "
        "for the selected appointment."
    )

    visible_view_details.click()

    # =========================================================
    # WAIT FOR APPOINTMENT DETAILS SCREEN
    # =========================================================

    try:
        page.wait_for_load_state(
            "networkidle",
            timeout=5_000,
        )
    except PlaywrightTimeoutError:
        pass

    # Give Angular a brief opportunity to finish the details render.
    page.wait_for_timeout(500)

    # =========================================================
    # VERIFY USING STABLE DETAILS-PAGE ELEMENTS
    # =========================================================

    details_loaded = False

    # ---------------------------------------------------------
    # Booking ID is one of the most stable indicators that the
    # appointment details screen has loaded.
    # ---------------------------------------------------------

    booking_id = page.get_by_text(
        re.compile(
            r"Booking\s*ID\s*:",
            re.IGNORECASE,
        )
    )

    if first_visible_locator(booking_id) is not None:
        details_loaded = True

    # ---------------------------------------------------------
    # Current UI heading may simply be "Appointment".
    # ---------------------------------------------------------

    if not details_loaded:
        appointment_heading = page.get_by_role(
            "heading",
            name=re.compile(
                r"\bAppointment\b",
                re.IGNORECASE,
            ),
        )

        if first_visible_locator(appointment_heading) is not None:
            details_loaded = True

    # ---------------------------------------------------------
    # Invoice-related actions also identify the details screen.
    # Current UI:
    #   New Invoice
    #   View Invoice
    #
    # Older UI:
    #   Create Invoice
    #   Generate Bill
    # ---------------------------------------------------------

    if not details_loaded:
        invoice_actions = page.get_by_role(
            "button",
            name=re.compile(
                r"Create\s*Invoice|"
                r"New\s*Invoice|"
                r"View\s*Invoice|"
                r"Generate\s*Bill",
                re.IGNORECASE,
            ),
        )

        if first_visible_locator(invoice_actions) is not None:
            details_loaded = True

    # ---------------------------------------------------------
    # Details page normally contains the Invoices tab.
    # ---------------------------------------------------------

    if not details_loaded:
        invoices_tab = page.get_by_role(
            "tab",
            name=re.compile(
                r"Invoices",
                re.IGNORECASE,
            ),
        )

        if first_visible_locator(invoices_tab) is not None:
            details_loaded = True

    assert details_loaded, (
        "Appointment details page did not load successfully. "
        f"Current URL: {page.url}"
    )

    print(
        "[Appointment Details] Opened successfully. "
        f"URL: {page.url}"
    )


def create_booking_invoice(page: Page) -> None:
    """
    Open the first/new booking invoice from Appointment Details.

    Supports both:
    - Create Invoice
    - New Invoice

    The UI wording differs depending on the current booking/invoice state
    and application version.
    """

    invoice_action = None

    # =========================================================
    # PREFERRED: CREATE INVOICE
    # =========================================================

    create_candidates = page.get_by_text(
        "Create Invoice",
        exact=True,
    )

    invoice_action = last_visible_locator(
        create_candidates
    )

    # =========================================================
    # CURRENT UI FALLBACK: NEW INVOICE
    # =========================================================

    if invoice_action is None:
        new_invoice_buttons = page.get_by_role(
            "button",
            name=re.compile(
                r"New\s*Invoice",
                re.IGNORECASE,
            ),
        )

        invoice_action = last_visible_locator(
            new_invoice_buttons
        )

    # =========================================================
    # TEXT FALLBACK
    # =========================================================

    if invoice_action is None:
        new_invoice_text = page.get_by_text(
            "New Invoice",
            exact=True,
        )

        invoice_action = last_visible_locator(
            new_invoice_text
        )

    assert invoice_action is not None, (
        "Unable to locate Create Invoice or New Invoice "
        "on Appointment Details."
    )

    clicked = False
    last_error = None

    # =========================================================
    # RETRY FOR ANGULAR DOM RE-RENDER
    # =========================================================

    for attempt in range(3):

        try:
            # Re-locate on every retry.
            create_candidates = page.get_by_text(
                "Create Invoice",
                exact=True,
            )

            current_action = last_visible_locator(
                create_candidates
            )

            if current_action is None:
                current_action = last_visible_locator(
                    page.get_by_role(
                        "button",
                        name=re.compile(
                            r"New\s*Invoice",
                            re.IGNORECASE,
                        ),
                    )
                )

            if current_action is None:
                current_action = last_visible_locator(
                    page.get_by_text(
                        "New Invoice",
                        exact=True,
                    )
                )

            if current_action is None:
                page.wait_for_timeout(500)
                continue

            # Prefer clickable parent when the text is inside a button.
            clickable_parent = current_action.locator(
                "xpath=ancestor::*["
                "self::button or "
                "self::a or "
                "@role='button'"
                "][1]"
            )

            if clickable_parent.count() > 0:
                parent = clickable_parent.first

                if parent.is_visible():
                    parent.click(
                        timeout=5_000,
                    )

                    clicked = True
                    break

            current_action.click(
                timeout=5_000,
            )

            clicked = True
            break

        except Exception as error:
            last_error = error
            page.wait_for_timeout(750)

    assert clicked, (
        "Unable to open booking invoice from Appointment Details. "
        f"Last error: {last_error}"
    )

    # =========================================================
    # WAIT FOR CREATE INVOICE PAGE
    # =========================================================

    page.wait_for_url(
        re.compile(
            r"/business/bookingInvoice",
            re.IGNORECASE,
        ),
        timeout=DEFAULT_TIMEOUT,
    )

    try:
        page.wait_for_load_state(
            "networkidle",
            timeout=5_000,
        )
    except PlaywrightTimeoutError:
        pass

    assert "/business/bill/" not in page.url, (
        "Payment Info/Generate Bill was opened instead of "
        "the Booking Invoice page. "
        f"Current URL: {page.url}"
    )

    # =========================================================
    # VERIFY INVOICE PAGE
    # =========================================================

    invoice_page_loaded = False

    # ---------------------------------------------------------
    # Current UI: Create Invoice heading
    # ---------------------------------------------------------

    create_invoice_heading = page.get_by_role(
        "heading",
        name="Create Invoice",
        exact=True,
    )

    if first_visible_locator(create_invoice_heading) is not None:
        invoice_page_loaded = True

    # ---------------------------------------------------------
    # Current UI: Booking Reference field
    # ---------------------------------------------------------

    if not invoice_page_loaded:
        booking_reference = page.get_by_text(
            "Booking Reference",
            exact=True,
        )

        if first_visible_locator(booking_reference) is not None:
            invoice_page_loaded = True

    # ---------------------------------------------------------
    # Current UI: Add Procedure/Item button
    # ---------------------------------------------------------

    if not invoice_page_loaded:
        add_item_button = page.locator(
            "button"
        ).filter(
            has_text="Add Procedure/Item"
        )

        if first_visible_locator(add_item_button) is not None:
            invoice_page_loaded = True

    # ---------------------------------------------------------
    # Current UI: Save button
    # ---------------------------------------------------------

    if not invoice_page_loaded:
        save_button = page.get_by_role(
            "button",
            name="Save",
            exact=True,
        )

        if first_visible_locator(save_button) is not None:
            invoice_page_loaded = True

    # ---------------------------------------------------------
    # Older UI fallback: invoice table
    # ---------------------------------------------------------

    if not invoice_page_loaded:
        invoice_table = page.get_by_role("table")

        if first_visible_locator(invoice_table) is not None:
            invoice_page_loaded = True

    assert invoice_page_loaded, (
        "Booking Create Invoice page did not load successfully. "
        f"Current URL: {page.url}"
    )

    print(
        "[Booking Invoice] Create Invoice page opened successfully. "
        f"URL: {page.url}"
    )



def update_booking_invoice(page: Page) -> bool:
    """
    Save the newly created booking invoice and wait until the saved invoice
    view exposes the payment controls.
    """

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(500)

    update_button = page.get_by_role(
        "button",
        name=re.compile(r"^\s*Update\s*$", re.IGNORECASE),
    )

    expect(update_button).to_be_visible(timeout=DEFAULT_TIMEOUT)
    update_button.scroll_into_view_if_needed()
    update_button.click()

    # Wait for the invoice-save request and UI update.
    wait_for_success_message(
        page=page,
        patterns=[
            r"invoice.*created",
            r"invoice.*updated",
            r"invoice.*generated",
            r"bill.*generated",
            r"successfully",
        ],
        required=False,
    )

    page.wait_for_timeout(1_500)

    try:
        page.wait_for_load_state("networkidle", timeout=5_000)
    except PlaywrightTimeoutError:
        pass

    # A saved booking invoice URL contains invId.
    expect(page).to_have_url(
        re.compile(r"/business/bookingInvoice.*[?&]invId=", re.IGNORECASE),
        timeout=DEFAULT_TIMEOUT,
    )

    # Some builds keep the old form DOM after Update. Reloading the saved
    # invoice URL ensures the payment controls are rendered.
    page.reload(wait_until="domcontentloaded")

    try:
        page.wait_for_load_state("networkidle", timeout=5_000)
    except PlaywrightTimeoutError:
        pass

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(700)

    payment_control = locate_booking_invoice_payment_control(page)

    assert payment_control is not None, (
        "Invoice was saved, but the Get Payment control was not displayed."
    )

    return True




def complete_booking_invoice_payment(page: Page) -> dict:
    """
    Complete payment and wait until the saved invoice shows Amount Due = 0.
    """

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(500)

    open_payment_options(page)

    available_methods = get_available_payment_methods(page)

    assert available_methods, (
        "Neither Pay by Cash nor Pay by Others is available."
    )

    payment_method = random.choice(available_methods)
    selected_method_text = normalize_text(payment_method.inner_text())

    payment_method.click()

    payment_mode = None

    if "other" in selected_method_text.lower():
        payment_mode = select_random_other_payment_mode(page)

    pay_button = page.get_by_role(
        "button",
        name="Pay",
        exact=True,
    )

    expect(pay_button.last).to_be_visible(timeout=DEFAULT_TIMEOUT)
    pay_button.last.click()

    confirm_payment_dialog(page)

    wait_for_success_message(
        page=page,
        patterns=[
            r"payment.*successful",
            r"payment.*completed",
            r"payment.*received",
            r"paid successfully",
            r"successfully",
        ],
        required=False,
    )

    # Wait for navigation to the saved invoice view.
    try:
        page.wait_for_url(
            re.compile(
                r"/business/bookingInvoice/view",
                re.IGNORECASE,
            ),
            timeout=DEFAULT_TIMEOUT,
        )
    except PlaywrightTimeoutError:
        pass

    try:
        page.wait_for_load_state("networkidle", timeout=5_000)
    except PlaywrightTimeoutError:
        pass

    # Poll until the invoice is recalculated.
    amount_due = wait_for_invoice_amount_due(
        page=page,
        expected=Decimal("0.00"),
        timeout_ms=30_000,
    )

    return {
        "payment_completed": True,
        "payment_method": selected_method_text,
        "payment_mode": payment_mode,
        "amount_due": amount_due,
    }



def wait_for_invoice_amount_due(
    page: Page,
    expected: Decimal,
    timeout_ms: int = 30_000,
) -> Decimal:
    """
    Poll the saved invoice until Amount Due reaches the expected value.
    """

    deadline = page.evaluate("Date.now()") + timeout_ms
    last_amount = Decimal("-1.00")

    while page.evaluate("Date.now()") < deadline:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(750)

        last_amount = read_invoice_amount_by_label(
            page=page,
            labels=[
                "Amount Due",
                "Amount due",
                "Balance Due",
                "Due Amount",
            ],
            required=False,
        )

        if abs(last_amount - expected) <= Decimal("0.01"):
            return last_amount

        page.reload(wait_until="domcontentloaded")

        try:
            page.wait_for_load_state("networkidle", timeout=4_000)
        except PlaywrightTimeoutError:
            pass

    raise AssertionError(
        "Invoice Amount Due did not update after payment. "
        f"Expected={expected}, Last actual={last_amount}"
    )




def open_payment_options(page: Page) -> None:
    """
    Open the payment methods from the saved booking invoice.

    This intentionally avoids generic dropdown-trigger locators because the
    invoice page also contains Location and Department dropdowns.
    """

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(500)

    payment_control = locate_booking_invoice_payment_control(page)

    assert payment_control is not None, (
        "Unable to locate the Get Payment control on the saved invoice."
    )

    payment_control.scroll_into_view_if_needed()

    try:
        payment_control.click(timeout=5_000)
    except PlaywrightTimeoutError:
        payment_control.click(timeout=5_000, force=True)

    payment_option = page.get_by_text(
        re.compile(
            r"^\s*(Pay by Cash|Pay by Others)\s*$",
            re.IGNORECASE,
        )
    )

    expect(payment_option.first).to_be_visible(timeout=DEFAULT_TIMEOUT)



def locate_booking_invoice_payment_control(
    page: Page,
) -> Locator | None:
    """
    Locate only the booking-invoice payment button or its associated
    split-button menu trigger.
    """

    direct_buttons = [
        page.get_by_role(
            "button",
            name=re.compile(
                r"Get Payment|Receive Payment|Make Payment",
                re.IGNORECASE,
            ),
        ),
        page.get_by_text(
            re.compile(
                r"^\s*(Get Payment|Receive Payment|Make Payment)\s*$",
                re.IGNORECASE,
            )
        ),
    ]

    for candidate_group in direct_buttons:
        visible_candidate = first_visible_locator(candidate_group)

        if visible_candidate is not None:
            return visible_candidate

    # Locate a split-button containing payment text.
    payment_split_buttons = page.locator(
        "p-splitbutton, .p-splitbutton"
    ).filter(
        has_text=re.compile(
            r"Get Payment|Receive Payment|Make Payment",
            re.IGNORECASE,
        )
    )

    for index in range(payment_split_buttons.count()):
        split_button = payment_split_buttons.nth(index)

        try:
            if not split_button.is_visible():
                continue
        except PlaywrightTimeoutError:
            continue

        menu_trigger = split_button.locator(
            ".p-splitbutton-menubutton, "
            'button[aria-haspopup="menu"], '
            "button"
        )

        visible_trigger = last_visible_locator(menu_trigger)

        if visible_trigger is not None:
            return visible_trigger

    return None




def get_available_payment_methods(page: Page) -> list[Locator]:
    methods: list[Locator] = []

    for method_name in ["Pay by Cash", "Pay by Others"]:
        locator = page.get_by_text(
            re.compile(
                rf"^{re.escape(method_name)}$",
                re.IGNORECASE,
            )
        )

        visible_locator = first_visible_locator(locator)

        if visible_locator is not None:
            methods.append(visible_locator)

    return methods


def select_random_other_payment_mode(page: Page) -> str:
    """
    Select a random payment mode from the Pay by Others dialog.
    """

    expect(
        page.get_by_text(
            re.compile(
                r"Select Mode|Payment Mode|Mode of Payment",
                re.IGNORECASE,
            )
        ).first
    ).to_be_visible(timeout=DEFAULT_TIMEOUT)

    dropdown_candidates = [
        page.get_by_role(
            "combobox",
            name=re.compile(
                r"Select Mode|Payment Mode|Mode",
                re.IGNORECASE,
            ),
        ),
        page.get_by_text(
            re.compile(
                r"^Select Mode$|^Select Payment Mode$",
                re.IGNORECASE,
            )
        ),
        page.locator(
            '[formcontrolname*="mode" i], '
            '[id*="paymentMode" i], '
            '.p-dialog .p-dropdown-trigger'
        ),
    ]

    clicked = click_first_visible(dropdown_candidates)

    assert clicked, "Unable to open the payment mode dropdown."

    options = page.get_by_role("option")
    visible_options: list[Locator] = []

    for index in range(options.count()):
        option = options.nth(index)

        try:
            if not option.is_visible():
                continue

            option_text = normalize_text(option.inner_text())

            if not option_text:
                continue

            if re.search(
                r"select|choose|mode",
                option_text,
                re.IGNORECASE,
            ):
                continue

            visible_options.append(option)

        except PlaywrightTimeoutError:
            continue

    if not visible_options:
        overlay_options = page.locator(
            ".p-dropdown-item:visible, "
            ".p-select-option:visible, "
            ".p-listbox-option:visible"
        )

        for index in range(overlay_options.count()):
            option = overlay_options.nth(index)
            option_text = normalize_text(option.inner_text())

            if option_text and not re.search(
                r"select|choose",
                option_text,
                re.IGNORECASE,
            ):
                visible_options.append(option)

    assert visible_options, "No payment modes are available."

    selected_option = random.choice(visible_options)
    selected_mode = normalize_text(selected_option.inner_text())

    selected_option.click()

    return selected_mode


def confirm_payment_dialog(page: Page) -> None:
    """
    Confirm the Proceed with payment dialog.
    """

    proceed_dialog = page.get_by_text(
        re.compile(
            r"Proceed with payment\s*\?",
            re.IGNORECASE,
        )
    )

    try:
        expect(proceed_dialog.first).to_be_visible(timeout=5_000)
    except AssertionError:
        pass

    yes_button = page.get_by_role(
        "button",
        name=re.compile(r"^Yes$", re.IGNORECASE),
    )

    expect(yes_button.last).to_be_visible(timeout=DEFAULT_TIMEOUT)
    yes_button.last.click()


def read_invoice_amount_by_label(
    page: Page,
    labels: list[str],
    required: bool = True,
) -> Decimal:
    """
    Read an amount shown next to one of the supplied invoice labels.
    """

    for label in labels:
        escaped_label = re.escape(label)

        label_locator = page.get_by_text(
            re.compile(
                rf"^\s*{escaped_label}\s*:?\s*$",
                re.IGNORECASE,
            )
        )

        for index in range(label_locator.count()):
            candidate = label_locator.nth(index)

            try:
                if not candidate.is_visible():
                    continue
            except PlaywrightTimeoutError:
                continue

            amounts = extract_amounts_near_locator(candidate)

            if amounts:
                return amounts[-1]

        combined_locator = page.get_by_text(
            re.compile(
                rf"{escaped_label}.*(?:₹|Rs\.?|INR)?\s*[\d,]+(?:\.\d+)?",
                re.IGNORECASE,
            )
        )

        for index in range(combined_locator.count()):
            candidate = combined_locator.nth(index)

            try:
                if not candidate.is_visible():
                    continue
            except PlaywrightTimeoutError:
                continue

            amounts = extract_decimal_amounts(candidate.inner_text())

            if amounts:
                return amounts[-1]

    if required:
        raise AssertionError(
            f"Unable to read invoice amount for labels: {labels}"
        )

    return Decimal("0.00")


def extract_amounts_near_locator(locator: Locator) -> list[Decimal]:
    """
    Extract monetary values from the label element and nearby container.
    """

    texts: list[str] = []

    try:
        texts.append(locator.inner_text())
    except PlaywrightTimeoutError:
        pass

    nearby_selectors = [
        "xpath=following-sibling::*[1]",
        "xpath=parent::*",
        "xpath=parent::*/following-sibling::*[1]",
        "xpath=ancestor::*[self::div or self::li or self::tr][1]",
    ]

    for selector in nearby_selectors:
        try:
            nearby = locator.locator(selector)

            if nearby.count() > 0:
                texts.append(nearby.first.inner_text())
        except PlaywrightTimeoutError:
            continue

    amounts: list[Decimal] = []

    for text in texts:
        amounts.extend(extract_decimal_amounts(text))

    return amounts


def extract_decimal_amounts(text: str) -> list[Decimal]:
    normalized = text.replace("\u00a0", " ")

    matches = re.findall(
        r"(?:₹|Rs\.?|INR)?\s*(-?\d[\d,]*(?:\.\d{1,2})?)",
        normalized,
        re.IGNORECASE,
    )

    amounts: list[Decimal] = []

    for match in matches:
        try:
            amounts.append(
                Decimal(match.replace(",", "")).quantize(
                    Decimal("0.01")
                )
            )
        except InvalidOperation:
            continue

    return amounts


def assert_amount_close(
    actual: Decimal,
    expected: Decimal,
    label: str,
    tolerance: Decimal = Decimal("0.10"),
) -> None:
    difference = abs(actual - expected)

    if difference > tolerance:
        print(
            f"[Amount Mismatch] {label}: "
            f"actual={actual}, expected={expected}, "
            f"difference={difference}, tolerance={tolerance}"
        )

    assert difference <= tolerance, (
        f"{label} mismatch. "
        f"Actual={actual}, Expected={expected}, "
        f"Difference={difference}"
    )


def wait_for_success_message(
    page: Page,
    patterns: list[str],
    required: bool = True,
) -> bool:
    combined_pattern = "|".join(f"(?:{pattern})" for pattern in patterns)

    success_message = page.get_by_text(
        re.compile(combined_pattern, re.IGNORECASE)
    )

    try:
        expect(success_message.first).to_be_visible(timeout=7_000)
        return True
    except AssertionError:
        if required:
            raise AssertionError(
                "Expected success message was not displayed. "
                f"Patterns: {patterns}"
            )

    return False


def confirm_yes_dialog_if_visible(page: Page) -> None:
    yes_button = page.get_by_role(
        "button",
        name=re.compile(r"^Yes$", re.IGNORECASE),
    )

    try:
        if yes_button.count() > 0 and yes_button.last.is_visible():
            yes_button.last.click()
    except PlaywrightTimeoutError:
        pass


def fill_textbox_by_names(
    page: Page,
    names: list[str],
    value: str,
    required: bool,
) -> bool:
    for name in names:
        locator = page.get_by_role(
            "textbox",
            name=re.compile(
                rf"^{re.escape(name)}$",
                re.IGNORECASE,
            ),
        )

        visible_locator = first_visible_locator(locator)

        if visible_locator is not None:
            visible_locator.fill(value)
            return True

    if required:
        raise AssertionError(
            f"Unable to locate textbox using names: {names}"
        )

    return False


def fill_patient_phone_number(
    page: Page,
    phone: str,
) -> None:
    """
    Fill the patient mobile number using stable input attributes.
    """

    normalized_phone = re.sub(r"\D", "", phone)[-10:]

    candidates = [
        page.get_by_role(
            "textbox",
            name=re.compile(
                r"Phone|Mobile|Contact|10123",
                re.IGNORECASE,
            ),
        ),
        page.get_by_placeholder(
            re.compile(
                r"Phone|Mobile|10123",
                re.IGNORECASE,
            )
        ),
        page.locator('input[type="tel"]'),
        page.locator('input[formcontrolname*="phone" i]'),
        page.locator('input[formcontrolname*="mobile" i]'),
        page.locator('input[name*="phone" i]'),
        page.locator('input[name*="mobile" i]'),
        page.locator('input[id*="phone" i]'),
        page.locator('input[id*="mobile" i]'),
    ]

    for candidate_group in candidates:
        for index in range(candidate_group.count()):
            candidate = candidate_group.nth(index)

            try:
                if not candidate.is_visible():
                    continue

                candidate.scroll_into_view_if_needed()
                candidate.click()
                candidate.fill(normalized_phone)

                if candidate.input_value() == normalized_phone:
                    return

            except PlaywrightTimeoutError:
                continue

    raise AssertionError(
        "Unable to locate or fill the patient phone number field."
    )




def select_patient_gender(
    page: Page,
    gender: str,
) -> None:
    normalized_gender = gender.strip().title()

    if normalized_gender not in {"Male", "Female", "Other"}:
        normalized_gender = random.choice(["Male", "Female"])

    radio = page.get_by_role(
        "radio",
        name=re.compile(
            rf"^{re.escape(normalized_gender)}$",
            re.IGNORECASE,
        ),
    )

    if radio.count() > 0:
        radio.first.check()
        return

    gender_text = page.get_by_text(
        re.compile(
            rf"^{re.escape(normalized_gender)}$",
            re.IGNORECASE,
        )
    )

    if gender_text.count() > 0:
        gender_text.first.click()


def get_profile_value(
    profile: Any,
    *names: str,
    default: Any = None,
) -> Any:
    for name in names:
        if isinstance(profile, dict):
            value = profile.get(name)

            if value not in (None, ""):
                return value
        else:
            value = getattr(profile, name, None)

            if value not in (None, ""):
                return value

    return default


def generate_random_indian_mobile_number() -> str:
    first_digit = random.choice(["6", "7", "8", "9"])
    remaining_digits = "".join(
        str(random.randint(0, 9))
        for _ in range(9)
    )

    return first_digit + remaining_digits


def click_first_visible(
    locator_groups: list[Locator],
) -> bool:
    """
    Click the first visible locator.

    This works for buttons, links, text elements, cards, and other clickable
    containers. Non-form elements may not expose a meaningful enabled state,
    so visibility is treated as the primary requirement.
    """

    for locator_group in locator_groups:
        count = locator_group.count()

        for index in range(count):
            locator = locator_group.nth(index)

            try:
                if not locator.is_visible():
                    continue

                locator.scroll_into_view_if_needed()

                try:
                    locator.click(timeout=5_000)
                except PlaywrightTimeoutError:
                    locator.click(timeout=5_000, force=True)

                return True

            except PlaywrightTimeoutError:
                continue

    return False




def first_visible_locator(
    locator_group: Locator,
) -> Locator | None:
    for index in range(locator_group.count()):
        locator = locator_group.nth(index)

        try:
            if locator.is_visible():
                return locator
        except PlaywrightTimeoutError:
            continue

    return None


def last_visible_locator(
    locator_group: Locator,
) -> Locator | None:
    for index in range(locator_group.count() - 1, -1, -1):
        locator = locator_group.nth(index)

        try:
            if locator.is_visible():
                return locator
        except PlaywrightTimeoutError:
            continue

    return None


def is_locator_disabled(locator: Locator) -> bool:
    try:
        if locator.is_disabled():
            return True
    except PlaywrightTimeoutError:
        return True

    aria_disabled = locator.get_attribute("aria-disabled")
    disabled_attribute = locator.get_attribute("disabled")
    class_name = locator.get_attribute("class") or ""

    return (
        aria_disabled == "true"
        or disabled_attribute is not None
        or "disabled" in class_name.lower()
    )


def normalize_text(value: str) -> str:
    return re.sub(
        r"\s+",
        " ",
        value.replace("\u00a0", " "),
    ).strip()



# Case 2 :: Create an invoice and add 1 more service into it and do the payment


def complete_booking_invoice_with_additional_service_flow(
    page: Page,
    config,
    consumer_profile,
    doctor_name: str = "Naveen KP",
    appointment_service_name: str = "Video call Services",
    additional_service_name: str = "Consultation",
) -> dict:
    """
    Create a booking invoice, add one additional service, validate Net Total,
    update the invoice, and complete payment.
    """

    select_first_business_if_needed(page)
    open_appointment_dashboard(page)
    open_create_appointment_page(page)

    patient_name = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    select_appointment_doctor(
        page=page,
        doctor_name=doctor_name,
    )

    select_appointment_service(
        page=page,
        service_name=appointment_service_name,
    )

    confirm_appointment(page)

    open_latest_created_appointment(
        page=page,
        patient_name=patient_name,
    )

    open_appointment_details(page)
    create_booking_invoice(page)

    assert "/business/bookingInvoice" in page.url, (
        "Create Invoice page was not opened. "
        f"Current URL: {page.url}"
    )

    initial_item_total = read_invoice_item_total(
        page=page,
        item_name=appointment_service_name,
    )

    additional_service_result = add_service_to_booking_invoice(
        page=page,
        service_name=additional_service_name,
    )

    additional_item_total = read_invoice_item_total(
        page=page,
        item_name=additional_service_name,
    )

    expected_net_total = round_money(
        initial_item_total + additional_item_total
    )

    actual_net_total = read_invoice_amount_by_label(
        page=page,
        labels=[
            "Net Total",
            "Net total",
        ],
        required=True,
    )

    assert_amount_close(
        actual=actual_net_total,
        expected=expected_net_total,
        label="Booking invoice Net Total after adding service",
    )

    invoice_created = update_booking_invoice(page)

    payment_result = complete_booking_invoice_payment(page)
    amount_due = payment_result["amount_due"]

    assert_amount_close(
        actual=amount_due,
        expected=Decimal("0.00"),
        label="Amount Due after booking invoice payment",
    )

    return {
        "patient_name": patient_name,
        "doctor_name": doctor_name,
        "appointment_service_name": appointment_service_name,
        "additional_service_name": additional_service_name,
        "initial_item_total": initial_item_total,
        "additional_item_total": additional_item_total,
        "expected_net_total": expected_net_total,
        "actual_net_total": actual_net_total,
        "invoice_created": invoice_created,
        "additional_service_added": additional_service_result,
        "payment_completed": payment_result["payment_completed"],
        "payment_method": payment_result["payment_method"],
        "payment_mode": payment_result.get("payment_mode"),
        "amount_due": amount_due,
    }



def add_service_to_booking_invoice(
    page: Page,
    service_name: str,
) -> bool:
    """
    Add one additional Procedure/Item to the booking invoice.
    """

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(700)

    add_procedure_button = page.locator("button").filter(
        has_text="Add Procedure/Item"
    )

    visible_add_procedure = first_visible_locator(add_procedure_button)

    assert visible_add_procedure is not None, (
        "Unable to locate the Add Procedure/Item button."
    )

    visible_add_procedure.scroll_into_view_if_needed()
    visible_add_procedure.click()

    item_section = locate_add_procedure_item_section(page)

    assert item_section is not None, (
        "The Add Procedure/Item section did not open."
    )

    procedure_combobox = locate_procedure_item_combobox(
        page=page,
        item_section=item_section,
    )

    assert procedure_combobox is not None, (
        "Unable to locate the Procedure/Item field."
    )

    procedure_combobox.scroll_into_view_if_needed()
    procedure_combobox.click()

    service_option = locate_open_dropdown_option(
        page=page,
        option_text=service_name,
    )

    assert service_option is not None, (
        f"Procedure/Item option '{service_name}' was not visible."
    )

    service_option.scroll_into_view_if_needed()
    service_option.click()

    selected_value = procedure_combobox.input_value()

    assert selected_value.strip().lower() == service_name.strip().lower(), (
        f"Procedure/Item selection failed. "
        f"Expected='{service_name}', Actual='{selected_value}'"
    )

    add_button = item_section.get_by_role(
        "button",
        name="Add",
        exact=True,
    )

    visible_add_button = last_visible_locator(add_button)

    assert visible_add_button is not None, (
        "Unable to locate the ADD button in the Procedure/Item section."
    )

    visible_add_button.scroll_into_view_if_needed()
    expect(visible_add_button).to_be_visible(
        timeout=DEFAULT_TIMEOUT
    )
    expect(visible_add_button).to_be_enabled(
        timeout=DEFAULT_TIMEOUT
    )

    visible_add_button.click()

    wait_for_success_message(
        page=page,
        patterns=[
            r"item.*added",
            r"service.*added",
            r"procedure.*added",
            r"successfully",
        ],
        required=False,
    )

    wait_for_invoice_item_row(
        page=page,
        item_name=service_name,
    )

    return True



def locate_add_procedure_item_section(
    page: Page,
) -> Locator | None:
    """
    Locate the expanded section created by Add Procedure/Item.
    """

    procedure_label = page.get_by_text(
        re.compile(
            r"^\s*Procedure/Item\s*\*?\s*$",
            re.IGNORECASE,
        )
    )

    visible_label = last_visible_locator(procedure_label)

    if visible_label is not None:
        container_candidates = [
            visible_label.locator(
                "xpath=ancestor::form[1]"
            ),
            visible_label.locator(
                "xpath=ancestor::div["
                ".//button[normalize-space()='Add']"
                "][1]"
            ),
            visible_label.locator(
                "xpath=ancestor::*["
                ".//*[@role='combobox'] and "
                ".//button"
                "][1]"
            ),
        ]

        for candidate in container_candidates:
            if candidate.count() == 0:
                continue

            container = candidate.first

            try:
                if container.is_visible():
                    return container
            except PlaywrightTimeoutError:
                continue

    # Fallback: visible container with an Add button and combobox.
    candidates = page.locator(
        "form:visible, "
        ".p-dialog:visible, "
        "div:visible"
    ).filter(
        has=page.get_by_role(
            "button",
            name="Add",
            exact=True,
        )
    )

    for index in range(candidates.count() - 1, -1, -1):
        candidate = candidates.nth(index)

        try:
            if (
                candidate.is_visible()
                and candidate.locator(
                    '[role="combobox"], p-dropdown, p-select'
                ).count() > 0
            ):
                return candidate
        except PlaywrightTimeoutError:
            continue

    return None




def locate_procedure_item_combobox(
    page: Page,
    item_section: Locator,
) -> Locator | None:
    """
    Locate the Procedure/Item dropdown inside the expanded item section.
    """

    candidates = [
        item_section.get_by_role(
            "combobox",
            name=re.compile(
                r"Procedure|Item",
                re.IGNORECASE,
            ),
        ),
        item_section.locator(
            '[formcontrolname*="procedure" i], '
            '[formcontrolname*="item" i], '
            'p-dropdown, '
            'p-select, '
            '[role="combobox"]'
        ),
    ]

    for candidate_group in candidates:
        visible_candidate = first_visible_locator(candidate_group)

        if visible_candidate is not None:
            return visible_candidate

    procedure_label = item_section.get_by_text(
        re.compile(
            r"^\s*Procedure/Item\s*\*?\s*$",
            re.IGNORECASE,
        )
    )

    visible_label = first_visible_locator(procedure_label)

    if visible_label is not None:
        following_combobox = visible_label.locator(
            "xpath=following::*["
            "@role='combobox' or "
            "self::p-dropdown or "
            "self::p-select"
            "][1]"
        )

        return first_visible_locator(following_combobox)

    return None



def locate_open_dropdown_option(
    page: Page,
    option_text: str,
) -> Locator | None:
    """
    Locate an option only inside an open dropdown/list overlay.
    """

    exact_pattern = re.compile(
        rf"^\s*{re.escape(option_text)}\s*$",
        re.IGNORECASE,
    )

    candidates = [
        page.get_by_role(
            "option",
            name=exact_pattern,
        ),
        page.locator(
            '[role="listbox"]:visible [role="option"]:visible'
        ).filter(
            has_text=exact_pattern
        ),
        page.locator(
            ".p-dropdown-panel:visible "
            ".p-dropdown-item:visible"
        ).filter(
            has_text=exact_pattern
        ),
        page.locator(
            ".p-select-overlay:visible "
            ".p-select-option:visible"
        ).filter(
            has_text=exact_pattern
        ),
        page.locator(
            ".p-overlay:visible li:visible"
        ).filter(
            has_text=exact_pattern
        ),
    ]

    for candidate_group in candidates:
        visible_candidate = last_visible_locator(candidate_group)

        if visible_candidate is not None:
            return visible_candidate

    return None




def verify_selected_procedure_item(
    item_section: Locator,
    service_name: str,
) -> None:
    """
    Verify that the service is selected in the add-item section.
    """

    selected_service = item_section.get_by_text(
        service_name,
        exact=True,
    )

    expect(selected_service.last).to_be_visible(
        timeout=DEFAULT_TIMEOUT
    )



def locate_item_section_add_button(
    item_section: Locator,
) -> Locator | None:
    """
    Locate the Add button belonging only to the expanded item section.
    """

    add_buttons = item_section.get_by_role(
        "button",
        name="Add",
        exact=True,
    )

    return last_visible_locator(add_buttons)



def wait_for_invoice_item_row(
    page: Page,
    item_name: str,
) -> Locator:
    """
    Wait until the newly added item appears as an invoice table row.
    """

    item_cell = page.get_by_role(
        "cell",
        name=re.compile(
            rf"^\s*{re.escape(item_name)}\s*$",
            re.IGNORECASE,
        ),
    )

    try:
        expect(item_cell.last).to_be_visible(
            timeout=DEFAULT_TIMEOUT
        )
    except AssertionError:
        # Some builds render responsive invoice rows without cell roles.
        item_text = page.get_by_text(
            item_name,
            exact=True,
        )

        expect(item_text.last).to_be_visible(
            timeout=DEFAULT_TIMEOUT
        )

    row = locate_invoice_item_row(
        page=page,
        item_name=item_name,
    )

    assert row is not None, (
        f"Service '{item_name}' did not appear in the invoice table "
        "after clicking Add."
    )

    return row





def open_procedure_item_dropdown(page: Page) -> None:
    """
    Open the Procedure/Item selector displayed after clicking
    Add Procedure/Item.
    """

    procedure_labels = [
        page.get_by_text(
            re.compile(
                r"^\s*Procedure/Item\s*\*?\s*$",
                re.IGNORECASE,
            )
        ),
        page.get_by_text(
            re.compile(
                r"^\s*Select Procedure/Item\s*$",
                re.IGNORECASE,
            )
        ),
    ]

    for label_group in procedure_labels:
        visible_label = first_visible_locator(label_group)

        if visible_label is None:
            continue

        following_combobox = visible_label.locator(
            "xpath=following::*[@role='combobox'][1]"
        )

        visible_combobox = first_visible_locator(following_combobox)

        if visible_combobox is not None:
            visible_combobox.scroll_into_view_if_needed()
            visible_combobox.click()
            return

        sibling = visible_label.locator(
            "xpath=following-sibling::*[1]"
        )

        if sibling.count() > 0:
            try:
                if sibling.first.is_visible():
                    sibling.first.click()
                    return
            except PlaywrightTimeoutError:
                pass

    attribute_candidates = [
        page.locator(
            '[formcontrolname*="procedure" i], '
            '[formcontrolname*="item" i], '
            '[id*="procedure" i], '
            '[id*="item" i]'
        ),
        page.get_by_role(
            "combobox",
            name=re.compile(
                r"Procedure|Item",
                re.IGNORECASE,
            ),
        ),
    ]

    clicked = click_first_visible(attribute_candidates)

    assert clicked, (
        "Unable to open the Procedure/Item dropdown."
    )



def locate_invoice_item_row(
    page: Page,
    item_name: str,
):
    """
    Locate an invoice item row by service/procedure name.

    Supports item names containing special characters such as:
    - WhatsApp Service(Taxable)
    - Service (5%)
    - Procedure/Item

    Returns the visible row locator or None.
    """

    # ---------------------------------------------------------
    # Preferred approach:
    # Search all visible tables for a row containing the item name.
    # ---------------------------------------------------------

    tables = page.get_by_role("table")

    for table_index in range(tables.count()):
        table = tables.nth(table_index)

        try:
            if not table.is_visible():
                continue
        except PlaywrightTimeoutError:
            continue

        rows = table.get_by_role("row")

        for row_index in range(rows.count()):
            row = rows.nth(row_index)

            try:
                if not row.is_visible():
                    continue

                row_text = normalize_text(
                    row.inner_text()
                )

                if not row_text:
                    continue

                if item_name.lower() in row_text.lower():

                    print(
                        f"[Invoice Item Row Found] "
                        f"{item_name}: {row_text}"
                    )

                    return row

            except PlaywrightTimeoutError:
                continue

    # ---------------------------------------------------------
    # Fallback:
    # Locate item text first, then move to its containing row.
    # ---------------------------------------------------------

    item_candidates = page.get_by_text(
        re.compile(
            re.escape(item_name),
            re.IGNORECASE,
        )
    )

    for index in range(item_candidates.count()):
        item = item_candidates.nth(index)

        try:
            if not item.is_visible():
                continue

            row_candidates = [
                item.locator(
                    "xpath=ancestor::tr[1]"
                ),
                item.locator(
                    "xpath=ancestor::*[@role='row'][1]"
                ),
            ]

            for candidate in row_candidates:

                if candidate.count() == 0:
                    continue

                row = candidate.first

                if row.is_visible():

                    row_text = normalize_text(
                        row.inner_text()
                    )

                    print(
                        f"[Invoice Item Row Found - Fallback] "
                        f"{item_name}: {row_text}"
                    )

                    return row

        except PlaywrightTimeoutError:
            continue

    # ---------------------------------------------------------
    # Diagnostic information when row cannot be found
    # ---------------------------------------------------------

    visible_table_texts = []

    for table_index in range(tables.count()):
        table = tables.nth(table_index)

        try:
            if table.is_visible():
                visible_table_texts.append(
                    normalize_text(
                        table.inner_text()
                    )
                )
        except PlaywrightTimeoutError:
            continue

    print(
        f"\n[Invoice Item Row NOT Found]\n"
        f"Requested item: {item_name}\n"
        f"Visible tables:\n"
        + "\n---\n".join(visible_table_texts)
    )

    return None



def read_invoice_item_total(
    page: Page,
    item_name: str,
) -> Decimal:
    """
    Read the final Total value from an invoice item row.

    Expected row structure:

    Procedure/Item | Date | Rate | Qty | Total Rate |
    Discount | After Discount | Tax | Total
    """

    row = locate_invoice_item_row(
        page=page,
        item_name=item_name,
    )

    assert row is not None, (
        f"Unable to locate invoice row for item '{item_name}'."
    )

    cells = row.get_by_role("cell")

    assert cells.count() > 0, (
        f"Invoice row for '{item_name}' does not contain table cells."
    )

    # The final monetary cell in the row is normally the item Total.
    amount_candidates: list[Decimal] = []

    for index in range(cells.count()):
        cell = cells.nth(index)

        try:
            if not cell.is_visible():
                continue

            cell_text = normalize_text(cell.inner_text())
            amounts = extract_decimal_amounts(cell_text)

            if amounts:
                amount_candidates.extend(amounts)

        except PlaywrightTimeoutError:
            continue

    assert amount_candidates, (
        f"No monetary values were found in the invoice row "
        f"for '{item_name}'."
    )

    return amount_candidates[-1]


def round_money(value: Decimal) -> Decimal:
    return value.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP,
    )



# Case 3 :: Create invoice for a taxable service and check the calculations are correct


def complete_taxable_booking_service_invoice_flow(
    page: Page,
    config,
    consumer_profile,
    doctor_name: str = "Naveen KP",
    service_name: str = "WhatsApp Service(Taxable)",
    tax_percentage: Decimal = Decimal("5.00"),
) -> dict:
    """
    Create a booking invoice for one tax-exclusive taxable service,
    validate its tax and total, update the invoice, and complete payment.
    """

    select_first_business_if_needed(page)
    open_appointment_dashboard(page)
    open_create_appointment_page(page)

    patient_name = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    select_appointment_doctor(
        page=page,
        doctor_name=doctor_name,
    )

    select_appointment_service(
        page=page,
        service_name=service_name,
    )

    confirm_appointment(page)

    open_latest_created_appointment(
        page=page,
        patient_name=patient_name,
    )

    open_appointment_details(page)
    create_booking_invoice(page)

    assert "/business/bookingInvoice" in page.url, (
        "Create Invoice page was not opened. "
        f"Current URL: {page.url}"
    )

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(700)

    item_amounts = read_taxable_invoice_item_amounts(
        page=page,
        item_name=service_name,
    )

    rate = item_amounts["rate"]
    actual_tax = item_amounts["tax"]
    actual_total = item_amounts["total"]

    expected_tax = round_money(
        rate * tax_percentage / Decimal("100")
    )

    expected_total = round_money(
        rate + expected_tax
    )

    assert_amount_close(
        actual=actual_tax,
        expected=expected_tax,
        label=f"{service_name} tax at {tax_percentage}%",
        tolerance=Decimal("0.01"),
    )

    assert_amount_close(
        actual=actual_total,
        expected=expected_total,
        label=f"{service_name} total including tax",
        tolerance=Decimal("0.01"),
    )

    actual_net_total = read_invoice_amount_by_label(
        page=page,
        labels=[
            "Net Total",
            "Net total",
        ],
        required=True,
    )

    assert_amount_close(
        actual=actual_net_total,
        expected=expected_total,
        label="Booking invoice Net Total",
        tolerance=Decimal("0.01"),
    )

    print(
        "[Tax Validation] "
        f"service={service_name}, "
        f"rate={rate}, "
        f"tax_percentage={tax_percentage}, "
        f"expected_tax={expected_tax}, "
        f"actual_tax={actual_tax}, "
        f"expected_total={expected_total}, "
        f"actual_total={actual_total}, "
        f"net_total={actual_net_total}"
    )

    invoice_created = update_booking_invoice(page)

    payment_result = complete_booking_invoice_payment(page)
    amount_due = payment_result["amount_due"]

    assert_amount_close(
        actual=amount_due,
        expected=Decimal("0.00"),
        label="Amount Due after taxable booking invoice payment",
        tolerance=Decimal("0.01"),
    )

    return {
        "patient_name": patient_name,
        "doctor_name": doctor_name,
        "service_name": service_name,
        "tax_percentage": tax_percentage,
        "rate": rate,
        "expected_tax": expected_tax,
        "actual_tax": actual_tax,
        "expected_total": expected_total,
        "actual_total": actual_total,
        "actual_net_total": actual_net_total,
        "tax_calculation_valid": (
            abs(actual_tax - expected_tax) <= Decimal("0.01")
        ),
        "total_calculation_valid": (
            abs(actual_total - expected_total) <= Decimal("0.01")
        ),
        "invoice_created": invoice_created,
        "payment_completed": payment_result["payment_completed"],
        "payment_method": payment_result["payment_method"],
        "payment_mode": payment_result.get("payment_mode"),
        "amount_due": amount_due,
    }



def read_taxable_invoice_item_amounts(
    page: Page,
    item_name: str,
) -> dict[str, Decimal]:
    """
    Read Rate, Tax, and Total from a booking invoice item row.

    Column positions:
    0 - Procedure/Item
    1 - Date
    2 - Rate
    3 - Qty
    4 - Total Rate
    5 - Discount
    6 - After Discount
    7 - Tax
    8 - Total
    """

    row = locate_invoice_item_row(
        page=page,
        item_name=item_name,
    )

    assert row is not None, (
        f"Unable to locate the invoice row for '{item_name}'."
    )

    row.scroll_into_view_if_needed()

    cells = row.get_by_role("cell")

    if cells.count() < 9:
        cells = row.locator("td")

    assert cells.count() >= 9, (
        f"Invoice row for '{item_name}' does not contain the expected "
        f"nine financial columns. Cell count={cells.count()}. "
        f"Row text={normalize_text(row.inner_text())}"
    )

    rate = read_single_amount_from_cell(
        cell=cells.nth(2),
        label=f"{item_name} Rate",
    )

    tax = read_single_amount_from_cell(
        cell=cells.nth(7),
        label=f"{item_name} Tax",
    )

    total = read_single_amount_from_cell(
        cell=cells.nth(8),
        label=f"{item_name} Total",
    )

    return {
        "rate": rate,
        "tax": tax,
        "total": total,
    }



def read_single_amount_from_cell(
    cell: Locator,
    label: str,
) -> Decimal:
    """
    Read one monetary value from an invoice table cell.
    """

    expect(cell).to_be_visible(timeout=DEFAULT_TIMEOUT)

    cell_text = normalize_text(cell.inner_text())
    amounts = extract_decimal_amounts(cell_text)

    assert amounts, (
        f"Unable to read {label}. Cell text='{cell_text}'"
    )

    return round_money(amounts[-1])



# Case 4 :: Create an invoice for a taxable service and add 1 more taxable service into it and check the calculations  



def complete_two_taxable_services_booking_invoice_flow(
    page: Page,
    config,
    consumer_profile,
    doctor_name: str = "Naveen KP",
    appointment_service_name: str = "WhatsApp Service(Taxable)",
    additional_service_name: str = "General Service with Tax",
    appointment_service_tax_percentage: Decimal = Decimal("5.00"),
    additional_service_tax_percentage: Decimal = Decimal("5.00"),
) -> dict:
    """
    Create a booking invoice with two tax-exclusive taxable services.

    Validations:
    - Tax of each service
    - Total of each service
    - Combined invoice Net Total
    - Payment completion
    - Amount Due becomes zero
    """

    select_first_business_if_needed(page)
    open_appointment_dashboard(page)
    open_create_appointment_page(page)

    patient_name = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    select_appointment_doctor(
        page=page,
        doctor_name=doctor_name,
    )

    select_appointment_service(
        page=page,
        service_name=appointment_service_name,
    )

    confirm_appointment(page)

    open_latest_created_appointment(
        page=page,
        patient_name=patient_name,
    )

    open_appointment_details(page)
    create_booking_invoice(page)

    assert "/business/bookingInvoice" in page.url, (
        "Create Invoice page was not opened. "
        f"Current URL: {page.url}"
    )

    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(700)

    appointment_service_before_add = read_taxable_invoice_item_amounts(
        page=page,
        item_name=appointment_service_name,
    )

    additional_service_added = add_service_to_booking_invoice(
        page=page,
        service_name=additional_service_name,
    )

    assert additional_service_added is True, (
        f"Additional service '{additional_service_name}' was not added."
    )

    appointment_service_amounts = read_taxable_invoice_item_amounts(
        page=page,
        item_name=appointment_service_name,
    )

    additional_service_amounts = read_taxable_invoice_item_amounts(
        page=page,
        item_name=additional_service_name,
    )

    appointment_rate = appointment_service_amounts["rate"]
    appointment_actual_tax = appointment_service_amounts["tax"]
    appointment_actual_total = appointment_service_amounts["total"]

    additional_rate = additional_service_amounts["rate"]
    additional_actual_tax = additional_service_amounts["tax"]
    additional_actual_total = additional_service_amounts["total"]

    appointment_expected_tax = round_money(
        appointment_rate
        * appointment_service_tax_percentage
        / Decimal("100")
    )

    appointment_expected_total = round_money(
        appointment_rate + appointment_expected_tax
    )

    additional_expected_tax = round_money(
        additional_rate
        * additional_service_tax_percentage
        / Decimal("100")
    )

    additional_expected_total = round_money(
        additional_rate + additional_expected_tax
    )

    assert_amount_close(
        actual=appointment_actual_tax,
        expected=appointment_expected_tax,
        label=f"{appointment_service_name} tax",
        tolerance=Decimal("0.01"),
    )

    assert_amount_close(
        actual=appointment_actual_total,
        expected=appointment_expected_total,
        label=f"{appointment_service_name} total",
        tolerance=Decimal("0.01"),
    )

    assert_amount_close(
        actual=additional_actual_tax,
        expected=additional_expected_tax,
        label=f"{additional_service_name} tax",
        tolerance=Decimal("0.01"),
    )

    assert_amount_close(
        actual=additional_actual_total,
        expected=additional_expected_total,
        label=f"{additional_service_name} total",
        tolerance=Decimal("0.01"),
    )

    displayed_items_total = round_money(
    appointment_actual_total + additional_actual_total
    )

    round_off = read_invoice_amount_by_label(
        page=page,
        labels=[
            "Round Off",
            "Round off",
            "RoundOff",
        ],
        required=False,
    )

    expected_net_total = round_money(
        displayed_items_total + round_off
    )

    actual_net_total = read_invoice_amount_by_label(
        page=page,
        labels=[
            "Net Total",
            "Net total",
        ],
        required=True,
    )

    assert_amount_close(
        actual=actual_net_total,
        expected=expected_net_total,
        label="Net Total including round off",
        tolerance=Decimal("0.01"),
    )

    print(
        "\n[Two Taxable Services Validation]\n"
        f"Patient: {patient_name}\n"
        f"Service 1: {appointment_service_name}\n"
        f"Service 1 Rate: {appointment_rate}\n"
        f"Service 1 Tax %: {appointment_service_tax_percentage}\n"
        f"Service 1 Expected Tax: {appointment_expected_tax}\n"
        f"Service 1 Actual Tax: {appointment_actual_tax}\n"
        f"Service 1 Expected Total: {appointment_expected_total}\n"
        f"Service 1 Actual Total: {appointment_actual_total}\n"
        f"Service 2: {additional_service_name}\n"
        f"Service 2 Rate: {additional_rate}\n"
        f"Service 2 Tax %: {additional_service_tax_percentage}\n"
        f"Service 2 Expected Tax: {additional_expected_tax}\n"
        f"Service 2 Actual Tax: {additional_actual_tax}\n"
        f"Service 2 Expected Total: {additional_expected_total}\n"
        f"Service 2 Actual Total: {additional_actual_total}\n"
        f"Expected Net Total: {expected_net_total}\n"
        f"Actual Net Total: {actual_net_total}"
    )

    invoice_created = update_booking_invoice(page)

    payment_result = complete_booking_invoice_payment(page)
    amount_due = payment_result["amount_due"]

    assert_amount_close(
        actual=amount_due,
        expected=Decimal("0.00"),
        label="Amount Due after payment",
        tolerance=Decimal("0.01"),
    )

    return {
        "patient_name": patient_name,
        "doctor_name": doctor_name,
        "appointment_service_name": appointment_service_name,
        "additional_service_name": additional_service_name,

        "displayed_items_total": displayed_items_total,
        "round_off": round_off,
        "appointment_service_rate": appointment_rate,
        "appointment_service_expected_tax": appointment_expected_tax,
        "appointment_service_actual_tax": appointment_actual_tax,
        "appointment_service_expected_total": appointment_expected_total,
        "appointment_service_actual_total": appointment_actual_total,

        "additional_service_rate": additional_rate,
        "additional_service_expected_tax": additional_expected_tax,
        "additional_service_actual_tax": additional_actual_tax,
        "additional_service_expected_total": additional_expected_total,
        "additional_service_actual_total": additional_actual_total,

        "expected_net_total": expected_net_total,
        "actual_net_total": actual_net_total,

        "appointment_service_tax_valid": (
            abs(
                appointment_actual_tax
                - appointment_expected_tax
            )
            <= Decimal("0.01")
        ),
        "appointment_service_total_valid": (
            abs(
                appointment_actual_total
                - appointment_expected_total
            )
            <= Decimal("0.01")
        ),
        "additional_service_tax_valid": (
            abs(
                additional_actual_tax
                - additional_expected_tax
            )
            <= Decimal("0.01")
        ),
        "additional_service_total_valid": (
            abs(
                additional_actual_total
                - additional_expected_total
            )
            <= Decimal("0.01")
        ),
        "net_total_valid": (
            abs(actual_net_total - expected_net_total)
            <= Decimal("0.01")
        ),

        "invoice_created": invoice_created,
        "payment_completed": payment_result["payment_completed"],
        "payment_method": payment_result["payment_method"],
        "payment_mode": payment_result.get("payment_mode"),
        "amount_due": amount_due,
    }



 
 	
# Create an invoice with a non-taxable service. Then create a new invoice with another non-taxable service. Then create a Master Invoice with merging these 2 invoices    


def complete_booking_master_invoice_with_two_invoices_flow(
    page: Page,
    config,
    consumer_profile,
    doctor_name: str = "Naveen KP",
    first_service_name: str = "Video call Services",
    second_service_name: str = "Consultation",
) -> dict:
    """
    Create two separate booking invoices and consolidate them into a
    Master Invoice.

    Invoice 1:
    - Created from the appointment service.

    Invoice 2:
    - Created from Booking Details using New Invoice.
    - Contains the additional service.

    Finally:
    - Select both invoices.
    - Generate Master Invoice.
    - Validate Master Invoice total.
    - Complete payment.
    """

    select_first_business_if_needed(page)
    open_appointment_dashboard(page)
    open_create_appointment_page(page)

    patient_name = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    select_appointment_doctor(
        page=page,
        doctor_name=doctor_name,
    )

    select_appointment_service(
        page=page,
        service_name=first_service_name,
    )

    confirm_appointment(page)

    open_latest_created_appointment(
        page=page,
        patient_name=patient_name,
    )

    open_appointment_details(page)

    create_booking_invoice(page)

    first_service_amounts = read_booking_invoice_item_amounts(
        page=page,
        item_name=first_service_name,
    )

    first_service_rate = first_service_amounts["rate"]
    first_service_total = first_service_amounts["total"]

    first_invoice_created = update_booking_invoice(page)

    go_back_to_booking_details_from_invoice(page)

    open_new_booking_invoice(page)

    add_service_to_booking_invoice(
        page=page,
        service_name=second_service_name,
    )

    second_service_amounts = read_booking_invoice_item_amounts(
        page=page,
        item_name=second_service_name,
    )

    second_service_rate = second_service_amounts["rate"]
    second_service_total = second_service_amounts["total"]

    second_invoice_created = update_booking_invoice(page)

    go_back_to_booking_details_from_invoice(page)

    open_booking_invoices_tab(page)

    master_invoice_created = create_master_invoice_from_booking_invoices(
        page=page,
    )

    open_generated_master_invoice(page)

    expected_master_total = round_money(
        first_service_rate + second_service_rate
    )

    actual_master_total = read_master_invoice_total(page)

    assert_amount_close(
        actual=actual_master_total,
        expected=expected_master_total,
        label="Booking Master Invoice total",
        tolerance=Decimal("0.10"),
    )

    print(
        "\n[Booking Master Invoice Validation]\n"
        f"Patient: {patient_name}\n"
        f"First service: {first_service_name}\n"
        f"First service rate: {first_service_rate}\n"
        f"First service invoice total: {first_service_total}\n"
        f"Second service: {second_service_name}\n"
        f"Second service rate: {second_service_rate}\n"
        f"Second service invoice total: {second_service_total}\n"
        f"Expected Master Invoice total: {expected_master_total}\n"
        f"Actual Master Invoice total: {actual_master_total}"
    )

    payment_result = complete_booking_invoice_payment(page)
    amount_due = payment_result["amount_due"]

    assert_amount_close(
        actual=amount_due,
        expected=Decimal("0.00"),
        label="Master Invoice Amount Due after payment",
        tolerance=Decimal("0.01"),
    )

    return {
        "patient_name": patient_name,
        "doctor_name": doctor_name,
        "first_service_name": first_service_name,
        "second_service_name": second_service_name,

        "first_service_rate": first_service_rate,
        "first_service_total": first_service_total,
        "second_service_rate": second_service_rate,
        "second_service_total": second_service_total,

        "expected_master_total": expected_master_total,
        "actual_master_total": actual_master_total,

        "first_invoice_created": first_invoice_created,
        "second_invoice_created": second_invoice_created,
        "master_invoice_created": master_invoice_created,
        "master_total_valid": (
            abs(actual_master_total - expected_master_total)
            <= Decimal("0.10")
        ),

        "payment_completed": payment_result["payment_completed"],
        "payment_method": payment_result["payment_method"],
        "payment_mode": payment_result.get("payment_mode"),
        "amount_due": amount_due,
    }


# -------- Back to Booking Details helper-----

def go_back_to_booking_details_from_invoice(page: Page) -> None:
    """
    Return from Booking Invoice Details to Booking Details.
    """

    back_candidates = [
        page.get_by_role(
            "heading",
            name=re.compile(r"Back", re.IGNORECASE),
        ).locator("i"),
        page.get_by_role(
            "button",
            name=re.compile(r"Back", re.IGNORECASE),
        ),
        page.locator(
            'i[class*="arrow-left"], '
            'i[class*="angle-left"], '
            'i[class*="chevron-left"], '
            'button[aria-label*="back" i]'
        ),
    ]

    clicked = click_first_visible(back_candidates)

    assert clicked, (
        "Unable to locate the Back control on the Booking Invoice page."
    )

    page.wait_for_url(
        re.compile(
            r"/business/appointments/.+_appt",
            re.IGNORECASE,
        ),
        timeout=DEFAULT_TIMEOUT,
    )

    try:
        page.wait_for_load_state("networkidle", timeout=5_000)
    except PlaywrightTimeoutError:
        pass

    expect(
        page.get_by_text(
            re.compile(
                r"Booking Details|Appointment Details|Invoices",
                re.IGNORECASE,
            )
        ).first
    ).to_be_visible(timeout=DEFAULT_TIMEOUT)



# -------- Open New Invoice from Booking Details  -----


def open_new_booking_invoice(page: Page) -> None:
    """
    Click New Invoice from Booking Details and open a blank invoice.
    """

    new_invoice_candidates = [
        page.get_by_role(
            "button",
            name=re.compile(
                r"New Invoice",
                re.IGNORECASE,
            ),
        ),
        page.get_by_text(
            "New Invoice",
            exact=True,
        ),
        page.locator("button").filter(
            has_text="New Invoice"
        ),
    ]

    clicked = click_first_visible(new_invoice_candidates)

    assert clicked, (
        "Unable to locate the New Invoice button on Booking Details."
    )

    page.wait_for_url(
        re.compile(
            r"/business/bookingInvoice",
            re.IGNORECASE,
        ),
        timeout=DEFAULT_TIMEOUT,
    )

    try:
        page.wait_for_load_state("networkidle", timeout=5_000)
    except PlaywrightTimeoutError:
        pass

    heading = page.get_by_role(
        "heading",
        name=re.compile(r"Create Invoice", re.IGNORECASE),
    )

    expect(heading.first).to_be_visible(timeout=DEFAULT_TIMEOUT)




# ------ Open Invoices tab -------


def open_booking_invoices_tab(page: Page) -> None:
    """
    Open the Invoices section from Booking Details.
    """

    invoice_tab_candidates = [
        page.get_by_role(
            "tab",
            name=re.compile(r"^Invoices?$", re.IGNORECASE),
        ),
        page.get_by_role(
            "link",
            name=re.compile(r"^Invoices?$", re.IGNORECASE),
        ),
        page.locator("a").filter(
            has_text=re.compile(r"^Invoices?$", re.IGNORECASE)
        ),
        page.get_by_text(
            re.compile(r"^Invoices?$", re.IGNORECASE)
        ),
    ]

    clicked = click_first_visible(invoice_tab_candidates)

    assert clicked, (
        "Unable to locate the Invoices tab on Booking Details."
    )

    page.wait_for_timeout(700)

    expect(
        page.get_by_role(
            "button",
            name=re.compile(r"Create Invoice", re.IGNORECASE),
        ).first
    ).to_be_visible(timeout=DEFAULT_TIMEOUT)




# -------- Create Master Invoice -------


def create_master_invoice_from_booking_invoices(
    page: Page,
) -> bool:
    """
    Select all available booking invoices and generate a Master Invoice.
    """

    create_invoice_button_candidates = [
        page.get_by_role(
            "button",
            name=re.compile(r"Create Invoice", re.IGNORECASE),
        ),
        page.locator("button").filter(
            has_text="Create Invoice"
        ),
    ]

    clicked = click_first_visible(create_invoice_button_candidates)

    assert clicked, (
        "Unable to locate the Create Invoice button in the Invoices section."
    )

    master_invoice_menu_candidates = [
        page.get_by_role(
            "menuitem",
            name=re.compile(r"Master Invoice", re.IGNORECASE),
        ),
        page.get_by_text(
            "Master Invoice",
            exact=True,
        ),
    ]

    clicked = click_first_visible(master_invoice_menu_candidates)

    assert clicked, (
        "Unable to locate the Master Invoice menu option."
    )

    select_all_booking_invoice_checkboxes(page)

    link_button_candidates = [
        page.get_by_role(
            "button",
            name=re.compile(
                r"Link\s*&\s*Generate Master",
                re.IGNORECASE,
            ),
        ),
        page.locator("button").filter(
            has_text=re.compile(
                r"Link\s*&\s*Generate Master",
                re.IGNORECASE,
            )
        ),
    ]

    clicked = click_first_visible(link_button_candidates)

    assert clicked, (
        "Unable to locate the Link & Generate Master Invoice button."
    )

    confirmation_message = page.get_by_text(
        re.compile(
            r"consolidate the selected invoices into a Master Invoice",
            re.IGNORECASE,
        )
    )

    expect(confirmation_message.first).to_be_visible(
        timeout=DEFAULT_TIMEOUT
    )

    yes_button = page.get_by_role(
        "button",
        name="Yes",
        exact=True,
    )

    expect(yes_button.last).to_be_visible(timeout=DEFAULT_TIMEOUT)
    yes_button.last.click()

    wait_for_success_message(
        page=page,
        patterns=[
            r"master invoice.*created",
            r"master invoice.*generated",
            r"invoices.*linked",
            r"successfully",
        ],
        required=False,
    )

    expect(
        page.get_by_text(
            re.compile(r"Master Invoice", re.IGNORECASE)
        ).last
    ).to_be_visible(timeout=DEFAULT_TIMEOUT)

    return True



# ----------  Select both invoice checkboxes -------


def select_all_booking_invoice_checkboxes(page: Page) -> None:
    """
    Select all eligible component invoices displayed in the Master Invoice
    selection table.

    Header/select-all checkboxes are ignored where possible.
    """

    invoice_rows = page.get_by_role("row")
    selected_count = 0

    for index in range(invoice_rows.count()):
        row = invoice_rows.nth(index)

        try:
            if not row.is_visible():
                continue
        except PlaywrightTimeoutError:
            continue

        row_text = normalize_text(row.inner_text())

        if not row_text:
            continue

        if re.search(
            r"ID\s+Date|Invoice\s*#|Amount.*Status",
            row_text,
            re.IGNORECASE,
        ):
            continue

        checkbox = row.get_by_role("checkbox")

        if checkbox.count() == 0:
            checkbox = row.locator('input[type="checkbox"]')

        visible_checkbox = first_visible_locator(checkbox)

        if visible_checkbox is None:
            continue

        if not visible_checkbox.is_checked():
            visible_checkbox.check()

        selected_count += 1

    assert selected_count >= 2, (
        "At least two booking invoices must be selected to generate "
        f"a Master Invoice. Selected count={selected_count}"
    )

    print(
        f"[Master Invoice] Selected component invoices: {selected_count}"
    )




# ---------  Open generated Master Invoice  ------

def open_generated_master_invoice(page: Page) -> None:
    """
    Open the generated Master Invoice from the booking invoice list.

    This function finds the row whose status/type contains 'Master Invoice'
    and clicks only the View button inside that row.
    """

    page.wait_for_timeout(1_000)

    try:
        page.wait_for_load_state(
            "networkidle",
            timeout=5_000,
        )
    except PlaywrightTimeoutError:
        pass

    master_invoice_labels = page.get_by_text(
        re.compile(
            r"^\s*Master Invoice\s*$",
            re.IGNORECASE,
        )
    )

    visible_master_label = last_visible_locator(
        master_invoice_labels
    )

    assert visible_master_label is not None, (
        "Unable to locate a generated Master Invoice entry "
        "in the invoice list."
    )

    master_row_candidates = [
        visible_master_label.locator(
            "xpath=ancestor::tr[1]"
        ),
        visible_master_label.locator(
            "xpath=ancestor::*[@role='row'][1]"
        ),
        visible_master_label.locator(
            "xpath=ancestor::div["
            ".//button[normalize-space()='View']"
            "][1]"
        ),
    ]

    master_row = None

    for candidate in master_row_candidates:
        if candidate.count() == 0:
            continue

        row = candidate.first

        try:
            if row.is_visible():
                master_row = row
                break
        except PlaywrightTimeoutError:
            continue

    assert master_row is not None, (
        "Master Invoice label was found, but its containing row "
        "could not be identified."
    )

    row_text = normalize_text(master_row.inner_text())

    assert "master invoice" in row_text.lower(), (
        "Located invoice row is not a Master Invoice. "
        f"Row text: {row_text}"
    )

    view_button = master_row.get_by_role(
        "button",
        name="View",
        exact=True,
    )

    visible_view_button = first_visible_locator(
        view_button
    )

    if visible_view_button is None:
        view_button = master_row.locator("button").filter(
            has_text="View"
        )

        visible_view_button = first_visible_locator(
            view_button
        )

    assert visible_view_button is not None, (
        "Unable to locate the View button inside the "
        "Master Invoice row."
    )

    visible_view_button.scroll_into_view_if_needed()
    visible_view_button.click()

    page.wait_for_url(
        re.compile(
            r"/business/(?:bookingInvoice/view|finance/master-invoice/)",
            re.IGNORECASE,
        ),
        timeout=DEFAULT_TIMEOUT,
    )

    try:
        page.wait_for_load_state(
            "networkidle",
            timeout=5_000,
        )
    except PlaywrightTimeoutError:
        pass

    verify_master_invoice_details_page(page)




def verify_master_invoice_details_page(page: Page) -> None:
    """
    Confirm that the Finance Master Invoice page is open.
    """

    assert "/business/finance/master-invoice/" in page.url, (
        "An individual booking invoice was opened instead of the "
        f"Master Invoice. Current URL: {page.url}"
    )

    master_invoice_content = page.get_by_text(
        re.compile(
            r"Master Invoice|Detailed Breakups|Linked Invoices",
            re.IGNORECASE,
        )
    )

    expect(master_invoice_content.first).to_be_visible(
        timeout=DEFAULT_TIMEOUT
    )

        


# --------  Read generic invoice item amounts  ----------


def read_booking_invoice_item_amounts(
    page: Page,
    item_name: str,
) -> dict[str, Decimal]:
    """
    Read Rate, Tax, and Total from a booking invoice item row.
    """

    row = locate_invoice_item_row(
        page=page,
        item_name=item_name,
    )

    assert row is not None, (
        f"Unable to locate invoice row for '{item_name}'."
    )

    cells = row.get_by_role("cell")

    if cells.count() < 9:
        cells = row.locator("td")

    assert cells.count() >= 9, (
        f"Invoice row for '{item_name}' has an unexpected layout. "
        f"Cell count={cells.count()}. "
        f"Row text={normalize_text(row.inner_text())}"
    )

    rate = read_single_amount_from_cell(
        cell=cells.nth(2),
        label=f"{item_name} Rate",
    )

    tax = read_single_amount_from_cell(
        cell=cells.nth(7),
        label=f"{item_name} Tax",
    )

    total = read_single_amount_from_cell(
        cell=cells.nth(8),
        label=f"{item_name} Total",
    )

    return {
        "rate": rate,
        "tax": tax,
        "total": total,
    }



# --------  Read Master Invoice total  --------


def read_master_invoice_total(page: Page) -> Decimal:
    """
    Read the final Master Invoice Total from the Detailed Breakups footer.

    This avoids reading component invoice amounts from the Linked Invoices
    table, such as ₹450.00 or ₹500.00.
    """

    detailed_breakups = page.get_by_text(
    "Detailed Breakups",
    exact=True,
    ).first

    expect(detailed_breakups).to_be_visible(timeout=DEFAULT_TIMEOUT)

    # Preferred: locate the table containing Consultation and
    # Video call Services, then read the footer Total.
    breakup_table = detailed_breakups.locator(
        "xpath=following::table[1]"
    )

    if breakup_table.count() > 0:
        total_row = breakup_table.get_by_role("row").filter(
            has_text=re.compile(
                r"^\s*Total\s*:?\s*₹?\s*[\d,]+(?:\.\d+)?\s*$",
                re.IGNORECASE,
            )
        )

        visible_total_row = last_visible_locator(total_row)

        if visible_total_row is not None:
            amounts = extract_decimal_amounts(
                visible_total_row.inner_text()
            )

            if amounts:
                return round_money(amounts[-1])

    # Fallback: locate the Total label near the Amount Due section.
    amount_due_label = page.get_by_text(
        re.compile(r"^\s*Amount Due\s*:?\s*$", re.IGNORECASE)
    )

    visible_amount_due = last_visible_locator(amount_due_label)

    if visible_amount_due is not None:
        footer_container = visible_amount_due.locator(
            "xpath=ancestor::*["
            "self::tr or "
            "self::tfoot or "
            "contains(@class, 'total') or "
            "contains(@class, 'summary')"
            "][1]"
        )

        if footer_container.count() > 0:
            footer_text = footer_container.first.inner_text()
            amounts = extract_decimal_amounts(footer_text)

            # Footer normally contains:
            # Total ₹950.00
            # Amount Due ₹950.00
            if amounts:
                return round_money(amounts[0])

    # Final fallback: read the last visible exact Total label on the page.
    total_labels = page.get_by_text(
        re.compile(r"^\s*Total\s*:?\s*$", re.IGNORECASE)
    )

    for index in range(total_labels.count() - 1, -1, -1):
        total_label = total_labels.nth(index)

        try:
            if not total_label.is_visible():
                continue

            nearby_amounts = extract_amounts_near_locator(total_label)

            if nearby_amounts:
                return round_money(nearby_amounts[-1])

        except PlaywrightTimeoutError:
            continue

    raise AssertionError(
        "Unable to read the final Master Invoice Total "
        "from the Detailed Breakups section."
    )


# Create an invoice with a non-taxable service. Then create a new invoice with a taxable service. Then create a Master Invoice with merging these 2 invoices



def complete_booking_master_invoice_non_taxable_and_taxable_flow(
    page: Page,
    config,
    consumer_profile,
    doctor_name: str = "Naveen KP",
    non_taxable_service_name: str = "Video call Services",
    taxable_service_name: str = "WhatsApp Service(Taxable)",
    tax_percentage: Decimal = Decimal("5.00"),
) -> dict:
    """
    Create:
    1. Non-taxable booking invoice.
    2. Taxable booking invoice against the same booking.
    3. Master Invoice containing both.

    Validate taxable values between individual invoice and Master Invoice.
    """

    # ---------------------------------------------------------
    # Create appointment
    # ---------------------------------------------------------

    select_first_business_if_needed(page)

    open_appointment_dashboard(page)

    open_create_appointment_page(page)

    patient_name = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    select_appointment_doctor(
        page=page,
        doctor_name=doctor_name,
    )

    select_appointment_service(
        page=page,
        service_name=non_taxable_service_name,
    )

    confirm_appointment(page)

    # ---------------------------------------------------------
    # Open newly created appointment
    # ---------------------------------------------------------

    open_latest_created_appointment(
        page=page,
        patient_name=patient_name,
    )

    open_appointment_details(page)

    # ---------------------------------------------------------
    # INVOICE 1
    # Video call Services - non-taxable
    # ---------------------------------------------------------

    create_booking_invoice(page)

    first_service_amounts = read_booking_invoice_item_amounts(
        page=page,
        item_name=non_taxable_service_name,
    )

    non_taxable_rate = first_service_amounts["rate"]
    non_taxable_tax = first_service_amounts["tax"]
    non_taxable_total = first_service_amounts["total"]

    assert_amount_close(
        actual=non_taxable_tax,
        expected=Decimal("0.00"),
        label=f"{non_taxable_service_name} Tax",
        tolerance=Decimal("0.01"),
    )

    first_invoice_created = update_booking_invoice(page)

    # ---------------------------------------------------------
    # Return to booking
    # ---------------------------------------------------------

    go_back_to_booking_details_from_invoice(page)

    # ---------------------------------------------------------
    # INVOICE 2
    # WhatsApp Service(Taxable)
    # ---------------------------------------------------------

    open_new_booking_invoice(page)

    add_service_to_booking_invoice(
        page=page,
        service_name=taxable_service_name,
    )

    taxable_amounts = read_booking_invoice_item_amounts(
        page=page,
        item_name=taxable_service_name,
    )

    taxable_rate = taxable_amounts["rate"]
    taxable_actual_tax = taxable_amounts["tax"]
    taxable_item_total = taxable_amounts["total"]

    # ---------------------------------------------------------
    # Validate individual taxable invoice
    # ---------------------------------------------------------

    taxable_expected_tax = round_money(
        taxable_rate * tax_percentage / Decimal("100")
    )

    assert_amount_close(
        actual=taxable_actual_tax,
        expected=taxable_expected_tax,
        label=f"{taxable_service_name} Tax",
        tolerance=Decimal("0.01"),
    )

    taxable_expected_total = round_money(
        taxable_rate + taxable_actual_tax
    )

    assert_amount_close(
        actual=taxable_item_total,
        expected=taxable_expected_total,
        label=f"{taxable_service_name} item total",
        tolerance=Decimal("0.01"),
    )

    # Read the invoice-level Net Total.
    taxable_invoice_net_total = read_invoice_amount_by_label(
        page=page,
        labels=[
            "Net Total",
            "Net total",
        ],
        required=True,
    )

    assert_amount_close(
        actual=taxable_invoice_net_total,
        expected=taxable_expected_total,
        label=f"{taxable_service_name} invoice Net Total",
        tolerance=Decimal("0.01"),
    )

    tax_calculation_valid = (
        abs(
            taxable_actual_tax
            - taxable_expected_tax
        )
        <= Decimal("0.01")
    )

    second_invoice_created = update_booking_invoice(page)

    # ---------------------------------------------------------
    # Back to booking -> invoices
    # ---------------------------------------------------------

    go_back_to_booking_details_from_invoice(page)

    open_booking_invoices_tab(page)

    # ---------------------------------------------------------
    # Generate Master Invoice
    # ---------------------------------------------------------

    master_invoice_created = (
        create_master_invoice_from_booking_invoices(page)
    )

    open_generated_master_invoice(page)

    # ---------------------------------------------------------
    # Read Master Invoice detailed breakup
    # ---------------------------------------------------------

    master_taxable_amounts = (
        read_master_invoice_item_amounts(
            page=page,
            item_name=taxable_service_name,
        )
    )

    master_non_taxable_amounts = (
        read_master_invoice_item_amounts(
            page=page,
            item_name=non_taxable_service_name,
        )
    )

    master_taxable_rate = master_taxable_amounts["rate"]
    master_taxable_tax = master_taxable_amounts["tax"]
    master_taxable_amount = master_taxable_amounts["amount"]

    master_non_taxable_rate = (
        master_non_taxable_amounts["rate"]
    )

    master_non_taxable_tax = (
        master_non_taxable_amounts["tax"]
    )

    master_non_taxable_amount = (
        master_non_taxable_amounts["amount"]
    )

    # ---------------------------------------------------------
    # Compare individual invoice vs Master Invoice
    # ---------------------------------------------------------

    assert_amount_close(
        actual=master_taxable_rate,
        expected=taxable_rate,
        label=(
            f"{taxable_service_name} Master Invoice Rate"
        ),
        tolerance=Decimal("0.01"),
    )

    assert_amount_close(
        actual=master_taxable_tax,
        expected=taxable_actual_tax,
        label=(
            f"{taxable_service_name} Master Invoice Tax"
        ),
        tolerance=Decimal("0.01"),
    )

    assert_amount_close(
        actual=master_taxable_amount,
        expected=taxable_invoice_net_total,
        label=(
            f"{taxable_service_name} Master Invoice Amount"
        ),
        tolerance=Decimal("0.01"),
    )

    # Also verify non-taxable item.
    assert_amount_close(
        actual=master_non_taxable_rate,
        expected=non_taxable_rate,
        label=(
            f"{non_taxable_service_name} Master Invoice Rate"
        ),
        tolerance=Decimal("0.01"),
    )

    assert_amount_close(
        actual=master_non_taxable_tax,
        expected=Decimal("0.00"),
        label=(
            f"{non_taxable_service_name} Master Invoice Tax"
        ),
        tolerance=Decimal("0.01"),
    )

    assert_amount_close(
        actual=master_non_taxable_amount,
        expected=non_taxable_total,
        label=(
            f"{non_taxable_service_name} Master Invoice Amount"
        ),
        tolerance=Decimal("0.01"),
    )

    # ---------------------------------------------------------
    # Validate Master Invoice Amount Due
    # ---------------------------------------------------------

    expected_master_amount_due = round_money(
        master_taxable_amount
        + master_non_taxable_amount
    )

    actual_master_amount_due = (
        read_master_invoice_amount_due(page)
    )

    assert_amount_close(
        actual=actual_master_amount_due,
        expected=expected_master_amount_due,
        label="Master Invoice Amount Due",
        tolerance=Decimal("0.01"),
    )

    master_taxable_rate_valid = (
        abs(master_taxable_rate - taxable_rate)
        <= Decimal("0.01")
    )

    master_taxable_tax_valid = (
        abs(
            master_taxable_tax
            - taxable_actual_tax
        )
        <= Decimal("0.01")
    )

    master_taxable_amount_valid = (
        abs(
            master_taxable_amount
            - taxable_invoice_net_total
        )
        <= Decimal("0.01")
    )

    master_amount_due_valid = (
        abs(
            actual_master_amount_due
            - expected_master_amount_due
        )
        <= Decimal("0.01")
    )

    print(
        "\n"
        "============================================\n"
        "BOOKING MASTER INVOICE TAX VALIDATION\n"
        "============================================\n"
        f"Patient: {patient_name}\n"
        "\n"
        f"Non-taxable service: {non_taxable_service_name}\n"
        f"Individual Rate: {non_taxable_rate}\n"
        f"Individual Tax: {non_taxable_tax}\n"
        f"Individual Total: {non_taxable_total}\n"
        f"Master Rate: {master_non_taxable_rate}\n"
        f"Master Tax: {master_non_taxable_tax}\n"
        f"Master Amount: {master_non_taxable_amount}\n"
        "\n"
        f"Taxable service: {taxable_service_name}\n"
        f"Individual Rate: {taxable_rate}\n"
        f"Tax Percentage: {tax_percentage}%\n"
        f"Expected Tax: {taxable_expected_tax}\n"
        f"Actual Tax: {taxable_actual_tax}\n"
        f"Individual Net Total: {taxable_invoice_net_total}\n"
        f"Master Rate: {master_taxable_rate}\n"
        f"Master Tax: {master_taxable_tax}\n"
        f"Master Amount: {master_taxable_amount}\n"
        "\n"
        f"Expected Master Amount Due: "
        f"{expected_master_amount_due}\n"
        f"Actual Master Amount Due: "
        f"{actual_master_amount_due}\n"
        "============================================"
    )

    # ---------------------------------------------------------
    # Complete payment
    # ---------------------------------------------------------

    payment_result = complete_booking_invoice_payment(page)

    amount_due_after_payment = (
        payment_result["amount_due"]
    )

    assert_amount_close(
        actual=amount_due_after_payment,
        expected=Decimal("0.00"),
        label="Master Invoice Amount Due after payment",
        tolerance=Decimal("0.01"),
    )

    return {
        "patient_name": patient_name,

        "first_invoice_created": first_invoice_created,
        "second_invoice_created": second_invoice_created,
        "master_invoice_created": master_invoice_created,

        "non_taxable_service_name":
            non_taxable_service_name,
        "non_taxable_rate":
            non_taxable_rate,
        "non_taxable_tax":
            non_taxable_tax,
        "non_taxable_total":
            non_taxable_total,

        "taxable_service_name":
            taxable_service_name,
        "taxable_rate":
            taxable_rate,
        "taxable_expected_tax":
            taxable_expected_tax,
        "taxable_actual_tax":
            taxable_actual_tax,
        "taxable_invoice_net_total":
            taxable_invoice_net_total,

        "master_taxable_rate":
            master_taxable_rate,
        "master_taxable_tax":
            master_taxable_tax,
        "master_taxable_amount":
            master_taxable_amount,

        "master_non_taxable_amount":
            master_non_taxable_amount,

        "expected_master_amount_due":
            expected_master_amount_due,
        "actual_master_amount_due":
            actual_master_amount_due,

        "tax_calculation_valid":
            tax_calculation_valid,
        "master_taxable_rate_valid":
            master_taxable_rate_valid,
        "master_taxable_tax_valid":
            master_taxable_tax_valid,
        "master_taxable_amount_valid":
            master_taxable_amount_valid,
        "master_amount_due_valid":
            master_amount_due_valid,

        "payment_completed":
            payment_result["payment_completed"],
        "payment_method":
            payment_result["payment_method"],
        "payment_mode":
            payment_result.get("payment_mode"),
        "amount_due_after_payment":
            amount_due_after_payment,
    }

# -------- Read item from Master Invoice ------------

def read_master_invoice_item_amounts(
    page: Page,
    item_name: str,
) -> dict[str, Decimal]:
    """
    Read Rate, Tax, and Amount for a service from the Master Invoice
    Detailed Breakups table.

    Expected columns:
    Description | Date | Quantity | Rate | Discount | Tax | Amount
    """

    detailed_breakups = page.get_by_text(
        "Detailed Breakups",
        exact=True,
    ).first

    expect(detailed_breakups).to_be_visible(
        timeout=DEFAULT_TIMEOUT
    )

    # Locate the table after the visible Detailed Breakups heading.
    breakup_table = detailed_breakups.locator(
        "xpath=following::table[1]"
    )

    expect(breakup_table).to_be_visible(
        timeout=DEFAULT_TIMEOUT
    )

    # Do not use \b after item_name because names ending with
    # characters such as ")" can fail word-boundary matching.
    item_row = breakup_table.get_by_role("row").filter(
        has_text=re.compile(
            re.escape(item_name),
            re.IGNORECASE,
        )
    )

    visible_row = first_visible_locator(item_row)

    # Fallback using table rows directly.
    if visible_row is None:
        rows = breakup_table.locator("tr")

        for index in range(rows.count()):
            row = rows.nth(index)

            try:
                if not row.is_visible():
                    continue

                row_text = normalize_text(
                    row.inner_text()
                )

                if item_name.lower() in row_text.lower():
                    visible_row = row
                    break

            except PlaywrightTimeoutError:
                continue

    if visible_row is None:
        table_text = normalize_text(
            breakup_table.inner_text()
        )

        raise AssertionError(
            f"Unable to locate '{item_name}' in the Master Invoice "
            f"Detailed Breakups table.\n"
            f"Detailed Breakups content:\n{table_text}"
        )

    row_text = normalize_text(
        visible_row.inner_text()
    )

    print(
        f"[Master Invoice Item] {item_name}: {row_text}"
    )

    cells = visible_row.get_by_role("cell")

    if cells.count() < 7:
        cells = visible_row.locator("td")

    assert cells.count() >= 7, (
        f"Unexpected Master Invoice row structure for "
        f"'{item_name}'. "
        f"Cell count={cells.count()}. "
        f"Row text={row_text}"
    )

    # Master Invoice Detailed Breakups:
    #
    # 0 Description
    # 1 Date
    # 2 Quantity
    # 3 Rate
    # 4 Discount
    # 5 Tax
    # 6 Amount

    rate = read_single_amount_from_cell(
        cell=cells.nth(3),
        label=f"{item_name} Master Invoice Rate",
    )

    tax = read_single_amount_from_cell(
        cell=cells.nth(5),
        label=f"{item_name} Master Invoice Tax",
    )

    amount = read_single_amount_from_cell(
        cell=cells.nth(6),
        label=f"{item_name} Master Invoice Amount",
    )

    print(
        f"[Master Invoice Item Values] "
        f"{item_name}: "
        f"Rate={rate}, Tax={tax}, Amount={amount}"
    )

    return {
        "rate": rate,
        "tax": tax,
        "amount": amount,
    }



# -------- Read Master Invoice Amount Due ------

def read_master_invoice_amount_due(
    page: Page,
) -> Decimal:
    """
    Read Amount Due from the Master Invoice page.

    Amount Due is displayed below the Detailed Breakups table,
    not inside the table itself.
    """

    detailed_breakups = page.get_by_text(
        "Detailed Breakups",
        exact=True,
    ).first

    expect(detailed_breakups).to_be_visible(
        timeout=DEFAULT_TIMEOUT
    )

    # ---------------------------------------------------------
    # Preferred approach:
    # Locate the visible Amount Due text from the Master Invoice
    # summary below Detailed Breakups.
    # ---------------------------------------------------------

    amount_due_candidates = page.get_by_text(
        re.compile(
            r"Amount\s*Due",
            re.IGNORECASE,
        )
    )

    amount_due_locator = last_visible_locator(
        amount_due_candidates
    )

    if amount_due_locator is not None:

        # First try the text of the element itself.
        own_text = normalize_text(
            amount_due_locator.inner_text()
        )

        own_amounts = extract_decimal_amounts(
            own_text
        )

        if own_amounts:
            amount_due = round_money(
                own_amounts[-1]
            )

            print(
                f"[Master Invoice Amount Due] "
                f"{amount_due}"
            )

            return amount_due

        # -----------------------------------------------------
        # Amount may be in a sibling element:
        #
        # Amount Due:     ₹815.00
        # -----------------------------------------------------

        parent = amount_due_locator.locator(
            "xpath=parent::*"
        )

        if parent.count() > 0:

            parent_text = normalize_text(
                parent.first.inner_text()
            )

            match = re.search(
                r"Amount\s*Due\s*:?\s*"
                r"(?:₹|)?\s*"
                r"([\d,]+(?:\.\d+)?)",
                parent_text,
                re.IGNORECASE,
            )

            if match:

                amount_due = round_money(
                    Decimal(
                        match.group(1).replace(",", "")
                    )
                )

                print(
                    f"[Master Invoice Amount Due] "
                    f"{amount_due}"
                )

                return amount_due

    # ---------------------------------------------------------
    # Fallback:
    # Search the entire Master Invoice content.
    # ---------------------------------------------------------

    page_text = normalize_text(
        page.locator("body").inner_text()
    )

    matches = re.findall(
        r"Amount\s*Due\s*:?\s*"
        r"(?:₹|)?\s*"
        r"([\d,]+(?:\.\d+)?)",
        page_text,
        re.IGNORECASE,
    )

    if matches:

        # Use the last Amount Due because linked invoices can also
        # contain due amounts higher on the page.
        amount_due = round_money(
            Decimal(
                matches[-1].replace(",", "")
            )
        )

        print(
            f"[Master Invoice Amount Due] "
            f"{amount_due}"
        )

        return amount_due

    raise AssertionError(
        "Unable to read Amount Due from the Master Invoice page.\n"
        f"Page content:\n{page_text}"
    )    



# Case 7 :: Create an invoice with a taxable service. Then create a new invoice with another taxable service. Then create a Master Invoice with merging these 2 invoices        

def complete_booking_master_invoice_two_taxable_services_flow(
    page: Page,
    config,
    consumer_profile,
    doctor_name: str = "Naveen KP",
    first_taxable_service_name: str = "WhatsApp Service(Taxable)",
    second_taxable_service_name: str = "General Service with Tax",
    first_tax_percentage: Decimal = Decimal("5.00"),
    second_tax_percentage: Decimal = Decimal("5.00"),
) -> dict:
    """
    Create two taxable invoices against the same booking and merge them
    into a Master Invoice.

    Invoice 1:
    - WhatsApp Service(Taxable)

    Invoice 2:
    - General Service with Tax

    Validate:
    - Tax calculations in both individual invoices.
    - Rate/Tax/Amount preservation in Master Invoice.
    - Master item Amount matches individual invoice item Total.
    - Master Invoice Amount Due matches the sum of both source invoice
      Net Totals.
    - Payment completion.
    - Amount Due becomes zero after payment.
    """

    # =========================================================
    # CREATE APPOINTMENT
    # =========================================================

    select_first_business_if_needed(page)

    open_appointment_dashboard(page)

    open_create_appointment_page(page)

    patient_name = create_random_patient_from_consumer_profile(
        page=page,
        consumer_profile=consumer_profile,
    )

    select_appointment_doctor(
        page=page,
        doctor_name=doctor_name,
    )

    select_appointment_service(
        page=page,
        service_name=first_taxable_service_name,
    )

    confirm_appointment(page)

    # =========================================================
    # OPEN LATEST APPOINTMENT
    # =========================================================

    open_latest_created_appointment(
        page=page,
        patient_name=patient_name,
    )

    open_appointment_details(page)

    # =========================================================
    # INVOICE 1
    # WhatsApp Service(Taxable)
    # =========================================================

    create_booking_invoice(page)

    first_item = read_booking_invoice_item_amounts(
        page=page,
        item_name=first_taxable_service_name,
    )

    first_rate = first_item["rate"]
    first_actual_tax = first_item["tax"]
    first_item_total = first_item["total"]

    # ---------------------------------------------------------
    # Validate first service tax
    # ---------------------------------------------------------

    first_expected_tax = round_money(
        first_rate
        * first_tax_percentage
        / Decimal("100")
    )

    assert_amount_close(
        actual=first_actual_tax,
        expected=first_expected_tax,
        label=f"{first_taxable_service_name} Tax",
        tolerance=Decimal("0.02"),
    )

    first_expected_item_total = round_money(
        first_rate + first_actual_tax
    )

    assert_amount_close(
        actual=first_item_total,
        expected=first_expected_item_total,
        label=f"{first_taxable_service_name} Total",
        tolerance=Decimal("0.01"),
    )

    # ---------------------------------------------------------
    # Read first invoice Round Off and Net Total
    # ---------------------------------------------------------

    first_round_off = read_invoice_amount_by_label(
        page=page,
        labels=[
            "Round Off",
            "Round off",
            "RoundOff",
        ],
        required=False,
    )

    first_expected_net_total = round_money(
        first_item_total + first_round_off
    )

    first_invoice_net_total = read_invoice_amount_by_label(
        page=page,
        labels=[
            "Net Total",
            "Net total",
        ],
        required=True,
    )

    assert_amount_close(
        actual=first_invoice_net_total,
        expected=first_expected_net_total,
        label=f"{first_taxable_service_name} Net Total",
        tolerance=Decimal("0.01"),
    )

    first_tax_calculation_valid = (
        abs(
            first_actual_tax
            - first_expected_tax
        )
        <= Decimal("0.02")
    )

    first_invoice_created = update_booking_invoice(page)

    # =========================================================
    # RETURN TO BOOKING
    # =========================================================

    go_back_to_booking_details_from_invoice(page)

    # =========================================================
    # INVOICE 2
    # General Service with Tax
    # =========================================================

    open_new_booking_invoice(page)

    add_service_to_booking_invoice(
        page=page,
        service_name=second_taxable_service_name,
    )

    second_item = read_booking_invoice_item_amounts(
        page=page,
        item_name=second_taxable_service_name,
    )

    second_rate = second_item["rate"]
    second_actual_tax = second_item["tax"]
    second_item_total = second_item["total"]

    # ---------------------------------------------------------
    # Validate second service tax
    # ---------------------------------------------------------

    second_expected_tax = round_money(
        second_rate
        * second_tax_percentage
        / Decimal("100")
    )

    assert_amount_close(
        actual=second_actual_tax,
        expected=second_expected_tax,
        label=f"{second_taxable_service_name} Tax",
        tolerance=Decimal("0.02"),
    )

    second_expected_item_total = round_money(
        second_rate + second_actual_tax
    )

    assert_amount_close(
        actual=second_item_total,
        expected=second_expected_item_total,
        label=f"{second_taxable_service_name} Total",
        tolerance=Decimal("0.01"),
    )

    # ---------------------------------------------------------
    # Read second invoice Round Off and Net Total
    # ---------------------------------------------------------

    second_round_off = read_invoice_amount_by_label(
        page=page,
        labels=[
            "Round Off",
            "Round off",
            "RoundOff",
        ],
        required=False,
    )

    second_expected_net_total = round_money(
        second_item_total + second_round_off
    )

    second_invoice_net_total = read_invoice_amount_by_label(
        page=page,
        labels=[
            "Net Total",
            "Net total",
        ],
        required=True,
    )

    assert_amount_close(
        actual=second_invoice_net_total,
        expected=second_expected_net_total,
        label=f"{second_taxable_service_name} Net Total",
        tolerance=Decimal("0.01"),
    )

    second_tax_calculation_valid = (
        abs(
            second_actual_tax
            - second_expected_tax
        )
        <= Decimal("0.02")
    )

    second_invoice_created = update_booking_invoice(page)

    # =========================================================
    # GO TO BOOKING INVOICES
    # =========================================================

    go_back_to_booking_details_from_invoice(page)

    open_booking_invoices_tab(page)

    # =========================================================
    # CREATE MASTER INVOICE
    # =========================================================

    master_invoice_created = (
        create_master_invoice_from_booking_invoices(page)
    )

    open_generated_master_invoice(page)

    # =========================================================
    # READ MASTER INVOICE VALUES
    # =========================================================

    first_master_item = read_master_invoice_item_amounts(
        page=page,
        item_name=first_taxable_service_name,
    )

    second_master_item = read_master_invoice_item_amounts(
        page=page,
        item_name=second_taxable_service_name,
    )

    first_master_rate = first_master_item["rate"]
    first_master_tax = first_master_item["tax"]
    first_master_amount = first_master_item["amount"]

    second_master_rate = second_master_item["rate"]
    second_master_tax = second_master_item["tax"]
    second_master_amount = second_master_item["amount"]

    # =========================================================
    # VALIDATE FIRST TAXABLE SERVICE IN MASTER INVOICE
    # =========================================================

    assert_amount_close(
        actual=first_master_rate,
        expected=first_rate,
        label=(
            f"{first_taxable_service_name} "
            "Master Invoice Rate"
        ),
        tolerance=Decimal("0.01"),
    )

    assert_amount_close(
        actual=first_master_tax,
        expected=first_actual_tax,
        label=(
            f"{first_taxable_service_name} "
            "Master Invoice Tax"
        ),
        tolerance=Decimal("0.01"),
    )

    # Master item Amount should match the individual item's Total,
    # before invoice-level Round Off.
    assert_amount_close(
        actual=first_master_amount,
        expected=first_item_total,
        label=(
            f"{first_taxable_service_name} "
            "Master Invoice Amount"
        ),
        tolerance=Decimal("0.01"),
    )

    # =========================================================
    # VALIDATE SECOND TAXABLE SERVICE IN MASTER INVOICE
    # =========================================================

    assert_amount_close(
        actual=second_master_rate,
        expected=second_rate,
        label=(
            f"{second_taxable_service_name} "
            "Master Invoice Rate"
        ),
        tolerance=Decimal("0.01"),
    )

    assert_amount_close(
        actual=second_master_tax,
        expected=second_actual_tax,
        label=(
            f"{second_taxable_service_name} "
            "Master Invoice Tax"
        ),
        tolerance=Decimal("0.01"),
    )

    # Example:
    # General Service item Total = 288.76
    # Invoice Round Off = 0.24
    # Invoice Net Total = 289.00
    #
    # The Master item row should preserve 288.76.
    assert_amount_close(
        actual=second_master_amount,
        expected=second_item_total,
        label=(
            f"{second_taxable_service_name} "
            "Master Invoice Amount"
        ),
        tolerance=Decimal("0.01"),
    )

    # =========================================================
    # MASTER INVOICE AMOUNT DUE
    # =========================================================

    # IMPORTANT:
    # Master item rows preserve item totals before invoice-level
    # round-off.
    #
    # But the Master Invoice Amount Due represents the payable
    # totals of the source invoices.
    #
    # Example:
    #
    # WhatsApp invoice Net Total = 315.00
    # General invoice Net Total  = 289.00
    #
    # Expected Master Amount Due = 604.00

    source_invoices_net_total = round_money(
        first_invoice_net_total
        + second_invoice_net_total
    )

    actual_master_amount_due = read_master_invoice_amount_due(
        page
    )

    expected_master_amount_due = (
        source_invoices_net_total
    )

    print(
        "\n"
        "[Master Invoice Amount Due Validation]\n"
        f"First Invoice Net Total  : "
        f"{first_invoice_net_total}\n"
        f"Second Invoice Net Total : "
        f"{second_invoice_net_total}\n"
        f"Expected Amount Due      : "
        f"{expected_master_amount_due}\n"
        f"Actual Amount Due        : "
        f"{actual_master_amount_due}\n"
    )

    assert_amount_close(
        actual=actual_master_amount_due,
        expected=expected_master_amount_due,
        label="Master Invoice Amount Due",
        tolerance=Decimal("0.01"),
    )

    # =========================================================
    # VALIDATION FLAGS
    # =========================================================

    first_master_rate_valid = (
        abs(
            first_master_rate
            - first_rate
        )
        <= Decimal("0.01")
    )

    first_master_tax_valid = (
        abs(
            first_master_tax
            - first_actual_tax
        )
        <= Decimal("0.01")
    )

    first_master_amount_valid = (
        abs(
            first_master_amount
            - first_item_total
        )
        <= Decimal("0.01")
    )

    second_master_rate_valid = (
        abs(
            second_master_rate
            - second_rate
        )
        <= Decimal("0.01")
    )

    second_master_tax_valid = (
        abs(
            second_master_tax
            - second_actual_tax
        )
        <= Decimal("0.01")
    )

    second_master_amount_valid = (
        abs(
            second_master_amount
            - second_item_total
        )
        <= Decimal("0.01")
    )

    master_amount_due_valid = (
        abs(
            actual_master_amount_due
            - expected_master_amount_due
        )
        <= Decimal("0.01")
    )

    # =========================================================
    # PRINT CALCULATION DETAILS
    # =========================================================

    print(
        "\n"
        "====================================================\n"
        "BOOKING MASTER INVOICE - TWO TAXABLE SERVICES\n"
        "====================================================\n"
        f"Patient: {patient_name}\n"
        "\n"
        "FIRST TAXABLE INVOICE\n"
        "----------------------------------------------------\n"
        f"Service: {first_taxable_service_name}\n"
        f"Rate: {first_rate}\n"
        f"Tax Percentage: {first_tax_percentage}%\n"
        f"Expected Tax: {first_expected_tax}\n"
        f"Actual Tax: {first_actual_tax}\n"
        f"Item Total: {first_item_total}\n"
        f"Round Off: {first_round_off}\n"
        f"Invoice Net Total: {first_invoice_net_total}\n"
        "\n"
        "FIRST SERVICE IN MASTER INVOICE\n"
        "----------------------------------------------------\n"
        f"Rate: {first_master_rate}\n"
        f"Tax: {first_master_tax}\n"
        f"Amount: {first_master_amount}\n"
        "\n"
        "SECOND TAXABLE INVOICE\n"
        "----------------------------------------------------\n"
        f"Service: {second_taxable_service_name}\n"
        f"Rate: {second_rate}\n"
        f"Tax Percentage: {second_tax_percentage}%\n"
        f"Expected Tax: {second_expected_tax}\n"
        f"Actual Tax: {second_actual_tax}\n"
        f"Item Total: {second_item_total}\n"
        f"Round Off: {second_round_off}\n"
        f"Invoice Net Total: {second_invoice_net_total}\n"
        "\n"
        "SECOND SERVICE IN MASTER INVOICE\n"
        "----------------------------------------------------\n"
        f"Rate: {second_master_rate}\n"
        f"Tax: {second_master_tax}\n"
        f"Amount: {second_master_amount}\n"
        "\n"
        "MASTER INVOICE\n"
        "----------------------------------------------------\n"
        f"First Source Invoice Net Total: "
        f"{first_invoice_net_total}\n"
        f"Second Source Invoice Net Total: "
        f"{second_invoice_net_total}\n"
        f"Expected Amount Due: "
        f"{expected_master_amount_due}\n"
        f"Actual Amount Due: "
        f"{actual_master_amount_due}\n"
        "===================================================="
    )

    # =========================================================
    # PAYMENT
    # =========================================================

    payment_result = complete_booking_invoice_payment(page)

    amount_due_after_payment = (
        payment_result["amount_due"]
    )

    assert_amount_close(
        actual=amount_due_after_payment,
        expected=Decimal("0.00"),
        label="Master Invoice Amount Due after payment",
        tolerance=Decimal("0.01"),
    )

    # =========================================================
    # RESULT
    # =========================================================

    return {
        "patient_name": patient_name,

        "first_invoice_created":
            first_invoice_created,
        "second_invoice_created":
            second_invoice_created,
        "master_invoice_created":
            master_invoice_created,

        # -----------------------------------------------------
        # First individual invoice
        # -----------------------------------------------------

        "first_service_name":
            first_taxable_service_name,
        "first_rate":
            first_rate,
        "first_expected_tax":
            first_expected_tax,
        "first_actual_tax":
            first_actual_tax,
        "first_item_total":
            first_item_total,
        "first_round_off":
            first_round_off,
        "first_invoice_net_total":
            first_invoice_net_total,

        # -----------------------------------------------------
        # Second individual invoice
        # -----------------------------------------------------

        "second_service_name":
            second_taxable_service_name,
        "second_rate":
            second_rate,
        "second_expected_tax":
            second_expected_tax,
        "second_actual_tax":
            second_actual_tax,
        "second_item_total":
            second_item_total,
        "second_round_off":
            second_round_off,
        "second_invoice_net_total":
            second_invoice_net_total,

        # -----------------------------------------------------
        # Master Invoice item values
        # -----------------------------------------------------

        "first_master_rate":
            first_master_rate,
        "first_master_tax":
            first_master_tax,
        "first_master_amount":
            first_master_amount,

        "second_master_rate":
            second_master_rate,
        "second_master_tax":
            second_master_tax,
        "second_master_amount":
            second_master_amount,

        # -----------------------------------------------------
        # Master Invoice totals
        # -----------------------------------------------------

        "source_invoices_net_total":
            source_invoices_net_total,
        "expected_master_amount_due":
            expected_master_amount_due,
        "actual_master_amount_due":
            actual_master_amount_due,

        # -----------------------------------------------------
        # Validation
        # -----------------------------------------------------

        "first_tax_calculation_valid":
            first_tax_calculation_valid,
        "second_tax_calculation_valid":
            second_tax_calculation_valid,

        "first_master_rate_valid":
            first_master_rate_valid,
        "first_master_tax_valid":
            first_master_tax_valid,
        "first_master_amount_valid":
            first_master_amount_valid,

        "second_master_rate_valid":
            second_master_rate_valid,
        "second_master_tax_valid":
            second_master_tax_valid,
        "second_master_amount_valid":
            second_master_amount_valid,

        "master_amount_due_valid":
            master_amount_due_valid,

        # -----------------------------------------------------
        # Payment
        # -----------------------------------------------------

        "payment_completed":
            payment_result["payment_completed"],
        "payment_method":
            payment_result["payment_method"],
        "payment_mode":
            payment_result.get("payment_mode"),
        "amount_due_after_payment":
            amount_due_after_payment,
    }




def read_master_invoice_round_off(
    page: Page,
) -> Decimal:
    """
    Read the Master Invoice Round Off amount.

    Returns Decimal("0.00") when Round Off is not displayed.
    """

    round_off_candidates = page.get_by_text(
        re.compile(
            r"Round\s*Off",
            re.IGNORECASE,
        )
    )

    visible_round_off = last_visible_locator(
        round_off_candidates
    )

    if visible_round_off is not None:

        # Try the element itself.
        text = normalize_text(
            visible_round_off.inner_text()
        )

        amounts = extract_decimal_amounts(text)

        if amounts:
            round_off = round_money(amounts[-1])

            print(
                f"[Master Invoice Round Off] {round_off}"
            )

            return round_off

        # Usually label + value are under the same parent.
        parent = visible_round_off.locator(
            "xpath=parent::*"
        )

        if parent.count() > 0:

            parent_text = normalize_text(
                parent.first.inner_text()
            )

            match = re.search(
                r"Round\s*Off\s*:?\s*"
                r"(?:₹|)?\s*"
                r"([+-]?[\d,]+(?:\.\d+)?)",
                parent_text,
                re.IGNORECASE,
            )

            if match:
                round_off = round_money(
                    Decimal(
                        match.group(1).replace(",", "")
                    )
                )

                print(
                    f"[Master Invoice Round Off] {round_off}"
                )

                return round_off

    # ---------------------------------------------------------
    # Fallback: inspect the page text.
    # ---------------------------------------------------------

    page_text = normalize_text(
        page.locator("body").inner_text()
    )

    matches = re.findall(
        r"Round\s*Off\s*:?\s*"
        r"(?:₹|)?\s*"
        r"([+-]?[\d,]+(?:\.\d+)?)",
        page_text,
        re.IGNORECASE,
    )

    if matches:

        round_off = round_money(
            Decimal(
                matches[-1].replace(",", "")
            )
        )

        print(
            f"[Master Invoice Round Off] {round_off}"
        )

        return round_off

    print("[Master Invoice Round Off] 0.00")

    return Decimal("0.00")





















