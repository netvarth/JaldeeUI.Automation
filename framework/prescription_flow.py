import os
import random
import re
from typing import Any

from dotenv import load_dotenv
from playwright.sync_api import Page, expect


load_dotenv()

DOCTOR_NAME = "Naveen KP"
SERVICE_NAME = "Video call Services"
PHARMACY_NAME = "Swathy Pharmacy"
ORDER_ITEM_NAME = "Item4"


FREQUENCIES = [
    "QD (0-0-1)",
    "BD (1-0-1)",
    "TID (1-1-1)",
    "Weekly Once",
]


MEDICINES = [
    {
        "search": "pa",
        "name": "Paracetamol",
        "instruction_search": "af",
        "instruction": "AFTER FOOD",
    },
    {
        "search": "ib",
        "name": "Ibuprofen",
        "instruction_search": "be",
        "instruction": "BEFORE FOOD",
    },
    {
        "search": "amox",
        "name": "Amoxicillin",
        "instruction_search": "be",
        "instruction": "BEFOR OR AFTER FOOD",
    },
]


# ============================================================
# COMMON
# ============================================================

def wait_for_success_message(
    page: Page,
    expected_text: str | None = None,
) -> None:
    """
    Wait for a success toast/message.

    If the exact message is known, expected_text can be supplied.
    Otherwise this checks for a generic success notification.
    """

    success_message = page.locator(
        ".p-toast-message-success:visible, "
        ".mat-mdc-snack-bar-container:visible, "
        ".alert-success:visible"
    )

    expect(success_message.last).to_be_visible(timeout=15000)

    if expected_text:
        expect(success_message.last).to_contain_text(
            re.compile(expected_text, re.IGNORECASE),
            timeout=15000,
        )


# ============================================================
# APPOINTMENT
# ============================================================

def open_appointment_dashboard(page: Page) -> None:
    """
    Open Appointments dashboard from left side panel.
    """

    appointment_link = page.locator(
        'a[href*="/business/appointments"]'
    )

    expect(
        appointment_link
    ).to_be_visible(timeout=15000)

    appointment_link.click()

    expect(
        page.get_by_text(
            "Welcome to your Appointments",
            exact=True,
        )
    ).to_be_visible(timeout=15000)



def open_create_appointment_page(page: Page) -> None:
    """
    From Appointment Dashboard:
        Click Appointment card
        -> Open Create Appointment page
        -> Verify Create New Patient is available
    """

    appointment_card = page.locator("p-card").filter(
        has_text=re.compile(r"^Appointment$", re.IGNORECASE)
    )

    expect(
        appointment_card
    ).to_be_visible(timeout=15000)

    appointment_card.click()

    expect(
        page.get_by_text(
            "Create New Patient",
            exact=True,
        )
    ).to_be_visible(timeout=15000)


def select_appointment_doctor(
    page: Page,
    doctor_name: str,
) -> None:

    doctor_field = page.locator(
        ".p-dropdown"
    ).filter(
        has_text="Hari Kumar"
    )

    expect(
        doctor_field
    ).to_be_visible(timeout=15000)

    doctor_field.click()

    doctor_option = page.get_by_text(
        doctor_name,
        exact=True,
    )

    expect(
        doctor_option.last
    ).to_be_visible(timeout=15000)

    doctor_option.last.click()

    print(f"Selected doctor: {doctor_name}")



def select_appointment_service(
    page: Page,
    service_name: str,
) -> None:

    service_dropdown = page.get_by_text(
        "service",
        exact=True,
    )

    if service_dropdown.count() == 0:
        service_dropdown = page.get_by_text(
            re.compile(
                r"Select Service",
                re.IGNORECASE,
            )
        )

    expect(service_dropdown.first).to_be_visible(timeout=10000)
    service_dropdown.first.click()

    service_option = page.get_by_role(
        "option",
        name=service_name,
    )

    expect(service_option).to_be_visible(timeout=10000)
    service_option.click()


def create_appointment(
    page: Page,
    consumer_profile,
) -> str:
    """
    From Create Appointment page:
        -> Click Create New Patient
        -> Create random patient
        -> Save patient
        -> Select doctor
        -> Select service
        -> Confirm appointment
    """

    first_name = f"Test{random.randint(1000, 9999)}"
    last_name = f"Patient{random.randint(1000, 9999)}"
    phone = f"555{random.randint(1000000, 9999999)}"

    email = (
        f"{first_name.lower()}."
        f"{last_name.lower()}@jaldee.com"
    )

    patient_name = f"{first_name} {last_name}"

    # ========================================================
    # CLICK CREATE NEW PATIENT
    # ========================================================

    create_new_patient = page.get_by_text(
        "Create New Patient",
        exact=True,
    )

    expect(
        create_new_patient
    ).to_be_visible(timeout=15000)

    create_new_patient.click()

    # ========================================================
    # WAIT FOR PATIENT CREATION PAGE
    # ========================================================

    first_name_input = page.get_by_role(
        "textbox",
        name="First Name",
    )

    expect(
        first_name_input
    ).to_be_visible(timeout=15000)

    # ========================================================
    # ENTER PATIENT DETAILS
    # ========================================================

    first_name_input.fill(first_name)

    page.get_by_role(
        "textbox",
        name="Last Name",
    ).fill(last_name)

    email_input = page.get_by_role(
        "textbox",
        name="Email(user@xyz.com)",
    )

    if email_input.count() > 0:
        email_input.fill(email)

    phone_input = page.get_by_role(
        "textbox",
        name="10123",
    ).first

    expect(
        phone_input
    ).to_be_visible(timeout=10000)

    phone_input.fill(phone)

    # ========================================================
    # GENDER
    # ========================================================

    female_radio = page.get_by_role(
        "radio",
        name="Female",
    )

    if female_radio.count() > 0:
        female_radio.check()

    # ========================================================
    # SAVE PATIENT
    # ========================================================

    save_button = page.get_by_role(
        "button",
        name="Save",
        exact=True,
    )

    expect(
        save_button
    ).to_be_enabled(timeout=10000)

    save_button.click()

    # Some environments show Yes confirmation.
    yes_button = page.get_by_role(
        "button",
        name=re.compile(r"^Yes$", re.IGNORECASE),
    )

    if yes_button.count() > 0:
        if yes_button.last.is_visible():
            yes_button.last.click()

    # ========================================================
    # WAIT TO RETURN TO CREATE APPOINTMENT PAGE
    # ========================================================

    page.wait_for_timeout(1000)

    doctor_locator = page.get_by_text(
        re.compile(r"Select Doctor", re.IGNORECASE)
    )

    expect(
        doctor_locator
    ).to_be_visible(timeout=15000)

    # ========================================================
    # SELECT DOCTOR
    # ========================================================

    select_appointment_doctor(
        page=page,
        doctor_name=DOCTOR_NAME,
    )

    # ========================================================
    # SELECT SERVICE
    # ========================================================

    select_appointment_service(
        page=page,
        service_name=SERVICE_NAME,
    )

    # ========================================================
    # CONFIRM APPOINTMENT
    # ========================================================

    confirm_button = page.get_by_role(
        "button",
        name="Confirm",
        exact=True,
    )

    expect(
        confirm_button
    ).to_be_enabled(timeout=10000)

    confirm_button.click()

    wait_for_success_message(page)

    print(f"Created patient: {patient_name}")

    return patient_name


# ============================================================
# APPOINTMENT DASHBOARD / LATEST APPOINTMENT
# ============================================================

def go_to_last_appointment_page(page: Page) -> None:
    """
    Continue clicking Next until the last appointment page.

    If there is only one page, no action is performed.
    """

    for _ in range(50):

        next_button = page.locator(
            ".p-paginator-next"
        )

        if next_button.count() == 0:
            next_button = page.locator(
                'button[aria-label="Next Page"]'
            )

        if next_button.count() == 0:
            break

        next_button = next_button.first

        class_name = next_button.get_attribute("class") or ""
        aria_disabled = next_button.get_attribute("aria-disabled")

        if (
            next_button.is_disabled()
            or "p-disabled" in class_name
            or aria_disabled == "true"
        ):
            break

        next_button.click()
        page.wait_for_timeout(500)


def open_latest_appointment(
    page: Page,
    patient_name: str,
) -> None:
    """
    Navigate to last page and open newly created appointment.
    """

    page.wait_for_timeout(1000)

    go_to_last_appointment_page(page)

    patient = page.get_by_text(
        re.compile(
            re.escape(patient_name),
            re.IGNORECASE,
        )
    )

    if patient.count() > 0:
        patient.last.click()

    else:
        # Fallback: use last appointment tab/accordion.
        appointment_tabs = page.get_by_role("tab")

        expect(
            appointment_tabs.last
        ).to_be_visible(timeout=15000)

        appointment_tabs.last.click()

    view_details = page.get_by_role(
        "button",
        name=re.compile(
            r"View Details",
            re.IGNORECASE,
        ),
    )

    expect(view_details.last).to_be_visible(timeout=10000)
    view_details.last.click()

    page.wait_for_load_state("domcontentloaded")


# ============================================================
# PRESCRIPTION
# ============================================================

def open_prescription_section(page: Page) -> None:

    prescriptions = page.locator("a").filter(
        has_text=re.compile(
            "Prescriptions",
            re.IGNORECASE,
        )
    )

    expect(
        prescriptions.first
    ).to_be_visible(timeout=15000)

    prescriptions.first.click()

    expect(
        page.get_by_role(
            "button",
            name="+ Add Medicine",
            exact=True,
        )
    ).to_be_visible(timeout=15000)


def select_prescription_doctor(
    page: Page,
    doctor_name: str,
) -> None:

    doctor_dropdown = page.get_by_text(
        re.compile(
            r"Select Doctor",
            re.IGNORECASE,
        )
    )

    expect(
        doctor_dropdown.last
    ).to_be_visible(timeout=10000)

    doctor_dropdown.last.click()

    doctor = page.get_by_text(
        doctor_name,
        exact=True,
    )

    expect(doctor.last).to_be_visible(timeout=10000)
    doctor.last.click()


def add_medicine(
    page: Page,
    medicine_index: int,
    medicine_name: str,
    medicine_search: str,
    instruction: str,
    instruction_search: str,
) -> dict[str, Any]:

    # ========================================================
    # ADD ROW
    # ========================================================

    page.get_by_role(
        "button",
        name="+ Add Medicine",
        exact=True,
    ).click()

    page.wait_for_timeout(300)

    # ========================================================
    # MEDICINE NAME
    # ========================================================

    search_boxes = page.get_by_role("searchbox")

    medicine_input = search_boxes.last
    medicine_input.fill(medicine_search)

    medicine_option = page.get_by_text(
        medicine_name,
        exact=True,
    )

    expect(
        medicine_option.last
    ).to_be_visible(timeout=10000)

    medicine_option.last.click()

    page.wait_for_timeout(300)

    # ========================================================
    # FIND CURRENT MEDICINE ROW
    # ========================================================

    medicine_row = page.get_by_role("row").filter(
        has_text=re.compile(
            re.escape(medicine_name),
            re.IGNORECASE,
        )
    ).last

    expect(medicine_row).to_be_visible(timeout=10000)

    # ========================================================
    # UNIT
    # ========================================================

    dropdowns = medicine_row.locator(".p-dropdown")

    # First dropdown = Unit
    unit_dropdown = dropdowns.nth(0)

    expect(
        unit_dropdown
    ).to_be_visible(timeout=10000)

    unit_dropdown.click()

    # In this case only "Numbers" is available
    unit_option = page.get_by_role(
        "option",
        name="Numbers",
        exact=True,
    )

    if unit_option.count() > 0:
        expect(
            unit_option.last
        ).to_be_visible(timeout=10000)

        unit_option.last.click()

    else:
        # Fallback for PrimeNG dropdown option text
        numbers_option = page.get_by_text(
            "Numbers",
            exact=True,
        )

        expect(
            numbers_option.last
        ).to_be_visible(timeout=10000)

        numbers_option.last.click()

    print(f"Selected unit for {medicine_name}: Numbers")


    # ========================================================
    # FREQUENCY
    # ========================================================

    frequency = random.choice(FREQUENCIES)

    # Second dropdown = Frequency
    dropdowns = medicine_row.locator(".p-dropdown")

    frequency_dropdown = dropdowns.nth(1)

    expect(
        frequency_dropdown
    ).to_be_visible(timeout=10000)

    frequency_dropdown.click()

    page.wait_for_timeout(200)

    frequency_option = page.get_by_role(
        "option",
        name=frequency,
        exact=True,
    )

    if frequency_option.count() > 0:

        expect(
            frequency_option.last
        ).to_be_visible(timeout=10000)

        frequency_option.last.click()

    else:

        frequency_text = page.get_by_text(
            frequency,
            exact=True,
        )

        expect(
            frequency_text.last
        ).to_be_visible(timeout=10000)

        frequency_text.last.click()

    print(
        f"Selected frequency for {medicine_name}: {frequency}"
    )

    # ========================================================
    # DURATION
    # ========================================================

    duration = random.randint(2, 10)

    spinbuttons = medicine_row.get_by_role("spinbutton")

    if spinbuttons.count() > 0:

        duration_input = spinbuttons.first

    else:
        # Fallback based on recorded UI.
        all_spinbuttons = page.get_by_role("spinbutton")

        duration_input = all_spinbuttons.nth(
            medicine_index * 2
        )

    expect(duration_input).to_be_visible(timeout=10000)

    duration_input.click()
    duration_input.fill(str(duration))
    duration_input.press("Tab")

    page.wait_for_timeout(300)

    # ========================================================
    # NOTES / INSTRUCTIONS
    # ========================================================

    table_cells = medicine_row.locator("td")

    if table_cells.count() >= 7:
        table_cells.nth(6).click()
    else:
        medicine_row.get_by_text(
            re.compile(
                r"Notes|Instructions",
                re.IGNORECASE,
            )
        ).click()

    page.wait_for_timeout(200)

    instruction_input = medicine_row.get_by_role(
        "searchbox"
    )

    expect(
        instruction_input
    ).to_be_visible(timeout=10000)

    # First try Lucene/autocomplete search
    instruction_input.fill(
        instruction_search
    )

    page.wait_for_timeout(800)

    instruction_option = page.get_by_text(
        instruction,
        exact=True,
    )

    # ========================================================
    # LUCENE RESULT AVAILABLE
    # ========================================================

    if (
        instruction_option.count() > 0
        and instruction_option.last.is_visible()
    ):

        instruction_option.last.click()

        print(
            f"Selected instruction from Lucene for "
            f"{medicine_name}: {instruction}"
        )

    # ========================================================
    # LUCENE RESULT NOT AVAILABLE
    # ========================================================

    else:

        instruction_input.fill("")

        instruction_input.fill(
            instruction
        )

        instruction_input.press("Tab")

        print(
            f"Lucene result not available. "
            f"Typed instruction manually for "
            f"{medicine_name}: {instruction}"
        )


    # ========================================================
    # RETURN MEDICINE DATA
    # ========================================================

    return {
        "medicine": medicine_name,
        "unit": "Numbers",
        "frequency": frequency,
        "duration": duration,
        "instruction": instruction,
    }


def create_prescription(
    page: Page
) -> list[dict[str, Any]]:

    select_prescription_doctor(
        page=page,
        doctor_name=DOCTOR_NAME,
    )

    medicines_created = []

    for index, medicine in enumerate(MEDICINES):

        result = add_medicine(
            page=page,
            medicine_index=index,
            medicine_name=medicine["name"],
            medicine_search=medicine["search"],
            instruction=medicine["instruction"],
            instruction_search=medicine[
                "instruction_search"
            ],
        )

        if result is None:
            raise AssertionError(
                f"add_medicine() returned None "
                f"for {medicine['name']}"
            )

        medicines_created.append(result)

    # ========================================================
    # CREATE PRESCRIPTION
    # ========================================================

    create_prescription_button = page.get_by_role(
        "button",
        name="Create Prescription",
        exact=True,
    )

    create_prescription_button.scroll_into_view_if_needed()

    expect(
        create_prescription_button
    ).to_be_enabled(timeout=10000)

    create_prescription_button.click()

    wait_for_success_message(page)

    return medicines_created


# ============================================================
# PUSH RX
# ============================================================

def push_rx_to_pharmacy(page: Page) -> None:

    # ========================================================
    # PUSH RX
    # ========================================================

    push_rx_button = page.get_by_role(
        "button",
        name=re.compile(
            r"Push RX",
            re.IGNORECASE,
        ),
    )

    expect(
        push_rx_button
    ).to_be_visible(timeout=15000)

    push_rx_button.scroll_into_view_if_needed()

    push_rx_button.click()

    # ========================================================
    # SELECT PHARMACY
    # ========================================================

    pharmacy = page.get_by_text(
        PHARMACY_NAME,
        exact=True,
    )

    expect(
        pharmacy
    ).to_be_visible(timeout=10000)

    pharmacy.click()

    # ========================================================
    # PUSH
    # ========================================================

    push_button = page.get_by_role(
        "button",
        name="Push",
        exact=True,
    )

    expect(
        push_button
    ).to_be_enabled(timeout=10000)

    push_button.click()

    wait_for_success_message(page)


# ============================================================
# SALES ORDER
# ============================================================

def open_sales_order_dashboard(page: Page) -> None:

    # Try to identify Sales Order menu using text first.
    sales_order = page.get_by_text(
        re.compile(
            r"Sales Order",
            re.IGNORECASE,
        )
    )

    if sales_order.count() > 0:
        sales_order.first.click()

    else:
        # Existing recorder fallback.
        page.get_by_role("link").nth(3).click()

    page.wait_for_load_state("domcontentloaded")


def open_first_rx_request_and_confirm_order(
    page: Page,
) -> None:

    requests_tab = page.get_by_text(
        "Requests",
        exact=True,
    )

    expect(
        requests_tab.first
    ).to_be_visible(timeout=15000)

    requests_tab.first.click()

    page.wait_for_timeout(1000)

    view_buttons = page.locator(
        "#btnACPTOrd_ORD_RQTORD"
    )

    expect(
        view_buttons.first
    ).to_be_visible(timeout=15000)

    # First/latest request.
    view_buttons.first.click()

    confirm_order = page.get_by_role(
        "button",
        name="Confirm Order",
        exact=True,
    )

    expect(
        confirm_order
    ).to_be_visible(timeout=10000)

    confirm_order.click()

    wait_for_success_message(page)

    page.wait_for_load_state("domcontentloaded")


# ============================================================
# EDIT ORDER
# ============================================================

def edit_order_and_add_item(
    page: Page,
    item_name: str,
) -> int:

    # ========================================================
    # EDIT ORDER
    # ========================================================

    edit_order = page.get_by_role(
        "button",
        name="Edit Order",
        exact=True,
    )

    expect(
        edit_order
    ).to_be_visible(timeout=15000)

    edit_order.click()

    # ========================================================
    # CONFIRM EDIT
    # ========================================================

    warning_message = page.get_by_text(
        re.compile(
            r"Editing this order will change its status to draft",
            re.IGNORECASE,
        )
    )

    expect(
        warning_message
    ).to_be_visible(timeout=10000)

    page.get_by_role(
        "button",
        name=re.compile(
            r"^Yes$",
            re.IGNORECASE,
        ),
    ).last.click()

    # Give the UI time to switch into edit mode
    page.wait_for_timeout(1000)

    # ========================================================
    # ADD ITEM
    # ========================================================

    add_item_button = page.get_by_role(
        "button",
        name=re.compile(
            r"Add Item",
            re.IGNORECASE,
        ),
    )

    expect(
        add_item_button
    ).to_be_visible(timeout=15000)

    add_item_button.click()

    # ========================================================
    # SELECT ITEM
    # ========================================================

    select_items_dialog = page.get_by_role("dialog")

    expect(
        select_items_dialog
    ).to_be_visible(timeout=10000)

    item_row = select_items_dialog.get_by_role("row").filter(
        has_text=re.compile(
            rf"\b{re.escape(item_name)}\b",
            re.IGNORECASE,
        )
    )

    expect(
        item_row.first
    ).to_be_visible(timeout=10000)

    checkbox = item_row.first.get_by_role("checkbox")

    if checkbox.count() > 0:
        checkbox.first.check()
    else:
        item_row.first.locator(
            "#actionSltSts_ORD_ItemSelect-input"
        ).check()

    # ========================================================
    # DONE
    # ========================================================

    done_button = page.get_by_role(
        "button",
        name="Done",
        exact=True,
    )

    if done_button.count() > 0:
        done_button.first.click()
    else:
        page.locator(
            "#btnSltDn_ORD_ItemSelectTop"
        ).click()

    page.wait_for_timeout(500)

    # ========================================================
    # VERIFY ITEM AND UPDATE QUANTITY
    # ========================================================

    added_item_row = page.get_by_role("row").filter(
        has_text=re.compile(
            re.escape(item_name),
            re.IGNORECASE,
        )
    )

    expect(
        added_item_row.last
    ).to_be_visible(timeout=10000)

    quantity = random.randint(2, 10)

    quantity_input = added_item_row.last.locator(
        "#inputQty_ORD_CrtItem"
    )

    if quantity_input.count() == 0:
        quantity_input = added_item_row.last.get_by_role(
            "spinbutton"
        )

    expect(
        quantity_input.first
    ).to_be_visible(timeout=10000)

    quantity_input.first.click()

    quantity_input.first.fill(
        str(quantity)
    )

    quantity_input.first.press("Tab")

    expect(
        quantity_input.first
    ).to_have_value(str(quantity))

    # ========================================================
    # UPDATE ORDER
    # ========================================================

    update_order = page.get_by_role(
        "button",
        name="Update Order",
        exact=True,
    )

    update_order.scroll_into_view_if_needed()

    expect(
        update_order
    ).to_be_enabled(timeout=10000)

    update_order.click()

    # ========================================================
    # CONFIRM UPDATE
    # ========================================================

    confirm_update_message = page.get_by_text(
        re.compile(
            r"Are you sure you want to update order",
            re.IGNORECASE,
        )
    )

    expect(
        confirm_update_message
    ).to_be_visible(timeout=10000)

    page.get_by_role(
        "button",
        name=re.compile(
            r"^Yes$",
            re.IGNORECASE,
        ),
    ).last.click()

    wait_for_success_message(page)

    return quantity



def confirm_updated_order(page: Page) -> None:

    confirm_order = page.get_by_role(
        "button",
        name="Confirm Order",
        exact=True,
    )

    confirm_order.scroll_into_view_if_needed()

    expect(
        confirm_order
    ).to_be_enabled(timeout=10000)

    confirm_order.click()

    wait_for_success_message(page)


# ============================================================
# INVOICE
# ============================================================

def create_invoice(page: Page) -> None:

    create_invoice_button = page.get_by_role(
        "button",
        name=re.compile(
            r"Create Invoice",
            re.IGNORECASE,
        ),
    )

    create_invoice_button.scroll_into_view_if_needed()

    expect(
        create_invoice_button
    ).to_be_enabled(timeout=15000)

    create_invoice_button.click()

    wait_for_success_message(page)

    view_invoice = page.get_by_role(
        "button",
        name="View Invoice",
        exact=True,
    )

    expect(
        view_invoice
    ).to_be_visible(timeout=15000)

    view_invoice.click()

    page.wait_for_load_state("domcontentloaded")


# ============================================================
# PAYMENT
# ============================================================

def pay_invoice_by_cash(page: Page) -> None:

    # Scroll to payment area.
    page.mouse.wheel(0, 3000)

    page.wait_for_timeout(500)

    # First try actual Get Payment button.
    get_payment = page.get_by_role(
        "button",
        name=re.compile(
            r"Get Payment",
            re.IGNORECASE,
        ),
    )

    if get_payment.count() > 0:

        get_payment.first.scroll_into_view_if_needed()
        get_payment.first.click()

    else:
        # Current recorded selector.
        dropdown_button = page.get_by_role(
            "button",
            name="dropdown trigger",
        )

        expect(
            dropdown_button
        ).to_be_visible(timeout=15000)

        dropdown_button.click()

    # ========================================================
    # PAY BY CASH
    # ========================================================

    pay_by_cash = page.get_by_text(
        "Pay by Cash",
        exact=True,
    )

    expect(
        pay_by_cash
    ).to_be_visible(timeout=10000)

    pay_by_cash.click()

    pay_button = page.get_by_role(
        "button",
        name="Pay",
        exact=True,
    )

    expect(
        pay_button
    ).to_be_enabled(timeout=10000)

    pay_button.click()

    # ========================================================
    # PROCEED WITH PAYMENT
    # ========================================================

    confirmation = page.get_by_text(
        re.compile(
            r"Proceed with payment",
            re.IGNORECASE,
        )
    )

    expect(
        confirmation
    ).to_be_visible(timeout=10000)

    page.get_by_role(
        "button",
        name=re.compile(
            r"^Yes$",
            re.IGNORECASE,
        ),
    ).last.click()

    wait_for_success_message(page)


# ============================================================
# BACK TO ORDER
# ============================================================

def back_to_order_details(page: Page) -> None:

    # ========================================================
    # FIND BACK CONTROL
    # ========================================================

    back_text = page.get_by_text(
        "Back",
        exact=True,
    )

    expect(
        back_text
    ).to_be_attached(timeout=15000)

    # Scroll the actual Back control into view
    back_text.scroll_into_view_if_needed()

    page.wait_for_timeout(300)

    # ========================================================
    # CLICK BACK
    # ========================================================

    expect(
        back_text
    ).to_be_visible(timeout=15000)

    back_text.click()

    # ========================================================
    # VERIFY ORDER DETAILS PAGE
    # ========================================================

    expect(
        page.get_by_role(
            "button",
            name="Complete Order",
            exact=True,
        )
    ).to_be_visible(timeout=15000)

    print("Returned to order details page")


# ============================================================
# COMPLETE ORDER
# ============================================================

def complete_order(page: Page) -> None:

    complete_order_button = page.get_by_role(
        "button",
        name="Complete Order",
        exact=True,
    )

    complete_order_button.scroll_into_view_if_needed()

    expect(
        complete_order_button
    ).to_be_enabled(timeout=15000)

    complete_order_button.click()

    page.wait_for_timeout(300)

    # If confirmation popup appears.
    yes_button = page.get_by_role(
        "button",
        name=re.compile(
            r"^Yes$",
            re.IGNORECASE,
        ),
    )

    if yes_button.count() > 0:
        if yes_button.last.is_visible():
            yes_button.last.click()

    wait_for_success_message(page)

# ============================================================
# LOGIN TO PROVIDER
# ============================================================

def login_to_provider(page: Page) -> None:
    provider_url = os.getenv("SCALE_PROVIDER_URL")
    login_id = os.getenv("SCALE_BOOKING_LOGIN_ID")
    password = os.getenv("SCALE_BOOKING_PASSWORD")

    if not provider_url:
        raise ValueError("SCALE_PROVIDER_URL is missing from .env")

    if not login_id:
        raise ValueError("SCALE_BOOKING_LOGIN_ID is missing from .env")

    if not password:
        raise ValueError("SCALE_BOOKING_PASSWORD is missing from .env")

    page.goto(provider_url)

    page.get_by_role(
        "textbox",
        name="Enter Login ID"
    ).fill(login_id)

    page.get_by_role(
        "textbox",
        name="Enter password"
    ).fill(password)

    page.get_by_role(
        "button",
        name="Sign In"
    ).click()

    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(2000)

    if "business/login" in page.url:
        raise AssertionError(
            f"Provider login failed. Current URL: {page.url}"
        )    


# ============================================================
# COMPLETE PRESCRIPTION BUSINESS FLOW
# ============================================================

def complete_prescription_push_rx_sales_order_flow(
    page: Page,
    config,
    consumer_profile,
) -> dict[str, Any]:
    """
    Complete E2E Prescription flow.

    Flow:
        Login
        -> Appointment Dashboard
        -> Create Appointment
        -> Create Random Patient
        -> Doctor: Naveen KP
        -> Service: Video call Services
        -> Confirm Appointment
        -> Open Appointment Details
        -> Prescriptions
        -> Add Paracetamol
        -> Add Ibuprofen
        -> Add Amoxicillin
        -> Create Prescription
        -> Push RX to Swathy Pharmacy
        -> Sales Order
        -> Requests
        -> Convert Request to Order
        -> Edit Order
        -> Add Item 4
        -> Random Quantity
        -> Update Order
        -> Confirm Order
        -> Create Invoice
        -> Cash Payment
        -> Complete Order
    """

    # ========================================================
    # LOGIN
    # ========================================================

    login_to_provider(page)

    # Optional debug check
    print(f"Current URL after login: {page.url}")

    # ========================================================
    # APPOINTMENT
    # ========================================================

    open_appointment_dashboard(page)

    open_create_appointment_page(page)

    patient_name = create_appointment(
        page=page,
        consumer_profile=consumer_profile,
    )

    print(f"Created patient: {patient_name}")

    # ========================================================
    # OPEN CREATED APPOINTMENT
    # ========================================================

    open_latest_appointment(
        page=page,
        patient_name=patient_name,
    )

    # ========================================================
    # PRESCRIPTION
    # ========================================================

    open_prescription_section(page)

    prescription_data = create_prescription(page)

    print("\nPrescription created:")

    for medicine in prescription_data:
        print(
            f"Medicine={medicine['medicine']}, "
            f"Frequency={medicine['frequency']}, "
            f"Duration={medicine['duration']}, "
            f"Instruction={medicine['instruction']}"
        )

    # ========================================================
    # PUSH RX
    # ========================================================

    push_rx_to_pharmacy(page)

    # ========================================================
    # SALES ORDER
    # ========================================================

    open_sales_order_dashboard(page)

    open_first_rx_request_and_confirm_order(page)

    # ========================================================
    # EDIT ORDER
    # ========================================================

    quantity = edit_order_and_add_item(
        page=page,
        item_name=ORDER_ITEM_NAME,
    )

    print(
        f"{ORDER_ITEM_NAME} random quantity: {quantity}"
    )

    # ========================================================
    # CONFIRM UPDATED ORDER
    # ========================================================

    confirm_updated_order(page)

    # ========================================================
    # CREATE INVOICE
    # ========================================================

    create_invoice(page)

    # ========================================================
    # CASH PAYMENT
    # ========================================================

    pay_invoice_by_cash(page)

    # ========================================================
    # BACK TO ORDER
    # ========================================================

    back_to_order_details(page)

    # ========================================================
    # COMPLETE ORDER
    # ========================================================

    complete_order(page)

    return {
        "patient_name": patient_name,
        "doctor": DOCTOR_NAME,
        "service": SERVICE_NAME,
        "pharmacy": PHARMACY_NAME,
        "medicines": prescription_data,
        "order_item": ORDER_ITEM_NAME,
        "order_item_quantity": quantity,
    }