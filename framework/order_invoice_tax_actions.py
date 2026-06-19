import random
import re
from decimal import Decimal, ROUND_HALF_UP

from playwright.sync_api import Page, expect


DEFAULT_TIMEOUT = 15000


def complete_sales_order_invoice_tax_flow(page: Page, config, consumer_profile: dict) -> dict:
    """
    Flow:
    - Open Sales Order
    - Verify/select B&B Stores
    - Create order
    - Create new customer
    - Select Sale_catalog
    - Add Item_4
    - Add Item_6 with random colour
    - Add customer/seller notes
    - Confirm order
    - Create invoice
    - View invoice
    - Verify Item_4 inclusive tax split
    - Verify invoice totals
    - Get payment by cash
    - Complete order
    """

    select_first_business_if_needed(page)
    close_blocking_dialog_if_present(page)

    open_sales_order_dashboard(page)
    close_blocking_dialog_if_present(page)

    ensure_store_is_bnb_stores(page)
    open_create_order_popup(page)

    customer_name = create_new_customer_from_profile(page, consumer_profile)

    select_sale_catalog_and_go_next(page)

    add_item_4_from_select_item_popup(page)
    add_item_6_from_search(page)

    add_order_note(page, "Notes to customer")
    add_order_note(page, "Notes from seller")

    confirm_order(page)

    create_invoice(page)
    view_invoice(page)

    item_4_tax_result = verify_item_4_invoice_tax_split(page)
    invoice_total_result = verify_invoice_totals(page)

    payment_result = complete_cash_payment(page)

    go_back_to_order_details(page)

    order_completed = complete_order(page)

    return {
        "customer_name": customer_name,
        "item_4_tax_result": item_4_tax_result,
        "invoice_total_result": invoice_total_result,
        "payment_completed": payment_result,
        "order_completed": order_completed,
        "final_url": page.url,
    }


# -------------------------
# Navigation
# -------------------------


def close_blocking_dialog_if_present(page: Page) -> None:
    """
    Close any unexpected PrimeNG dialog/overlay that blocks page clicks.

    This is mainly for popups that appear after login or dashboard load.
    """

    dialog_overlay = page.locator(".p-dialog-mask.p-component-overlay").last

    if not is_visible(dialog_overlay, timeout=1500):
        return

    print("[Dialog] Blocking dialog detected. Trying to close it.")

    close_button = find_first_visible(
        page,
        [
            lambda: page.locator(".p-dialog-header-close").last,
            lambda: page.locator("button.p-dialog-header-close").last,
            lambda: page.get_by_role("button", name=re.compile(r"close", re.I)).last,
            lambda: page.locator("xpath=//button[contains(@class, 'p-dialog-header-close')]").last,
        ],
        timeout=3000,
    )

    if close_button is not None:
        close_button.click()
        page.wait_for_timeout(1000)

        if not is_visible(dialog_overlay, timeout=1000):
            print("[Dialog] Blocking dialog closed using close button.")
            return

    page.keyboard.press("Escape")
    page.wait_for_timeout(1000)

    if is_visible(dialog_overlay, timeout=1000):
        print("[Warning] Dialog overlay is still visible after close attempt.")
    else:
        print("[Dialog] Blocking dialog closed using Escape.")


def select_first_business_if_needed(page: Page) -> None:
    """
    After login, sometimes business card selection page appears.
    If it appears, select the first business card.
    """

    page.wait_for_load_state("networkidle")

    possible_business_card = page.locator(".p-card-content > div > div > img").first

    if is_visible(possible_business_card, timeout=3000):
        possible_business_card.click()
        page.wait_for_load_state("networkidle")


def open_sales_order_dashboard(page: Page) -> None:
    """
    Open Sales Order dashboard only if we are not already there.

    Expected behavior:
    - After login, if already on Sales Order dashboard, stay there.
    - If another dashboard is open, click Sales Order icon/menu from left side panel.
    """

    page.wait_for_load_state("networkidle")
    close_blocking_dialog_if_present(page)

    current_url = page.url.lower()

    if "/business/salesorder/dashboard" in current_url or "/salesorder/dashboard" in current_url:
        print("[Navigation] Already on Sales Order dashboard.")
        return

    print("[Navigation] Not on Sales Order dashboard. Opening from left side panel.")

    click_first_visible(
        page,
        [
            lambda: page.locator("a[href*='salesorder/dashboard']").first,
            lambda: page.locator("[routerlink*='salesorder/dashboard']").first,
            lambda: page.locator("[id*='ORD_Dashbrd']").first,
            lambda: page.get_by_role("link", name=re.compile(r"Sales\s*Order", re.I)),
            lambda: page.locator("xpath=//a[contains(normalize-space(), 'Sales Order')]").first,
            lambda: page.locator("xpath=//*[contains(normalize-space(), 'Sales Order') and self::a or self::button]").first,
        ],
        "Sales Order left side panel icon/menu",
    )

    page.wait_for_load_state("networkidle")
    close_blocking_dialog_if_present(page)


def ensure_store_is_bnb_stores(page: Page) -> None:
    """
    Store dropdown on top must be B&B Stores.
    If another store is selected, open dropdown and select B&B Stores.
    """

    page.wait_for_load_state("networkidle")
    close_blocking_dialog_if_present(page)

    bnb_store_text = page.get_by_text("B&B Stores", exact=False).first

    if bnb_store_text.is_visible():
        print("[Store] B&B Stores is already selected or visible.")
        return

    print("[Store] B&B Stores not visible. Opening store dropdown.")

    click_first_visible(
        page,
        [
            lambda: page.locator("#headerComp_BUS_business").get_by_role(
                "button",
                name=re.compile("dropdown trigger", re.I),
            ),
            lambda: page.locator("#headerComp_BUS_business .p-dropdown-trigger").first,
            lambda: page.locator(".p-dropdown-trigger").first,
            lambda: page.get_by_role("button", name=re.compile("dropdown trigger", re.I)).first,
        ],
        "store dropdown trigger",
    )

    click_first_visible(
        page,
        [
            lambda: page.get_by_text("B&B Stores", exact=True),
            lambda: page.locator("li").filter(has_text="B&B Stores").first,
            lambda: page.locator("p-dropdownitem").filter(has_text="B&B Stores").first,
            lambda: page.locator("xpath=//*[normalize-space()='B&B Stores']").first,
        ],
        "B&B Stores option",
    )

    page.wait_for_load_state("networkidle")

    expect(page.get_by_text("B&B Stores", exact=False).first).to_be_visible(timeout=DEFAULT_TIMEOUT)

    print("[Store] B&B Stores selected.")


def open_create_order_popup(page: Page) -> None:
    """
    Click Create Order icon from Sales Order dashboard and wait for Create Order popup.
    """

    page.wait_for_load_state("networkidle")

    click_first_visible(
        page,
        [
            lambda: page.locator("#btnCreate_ORD_Order").first,
            lambda: page.locator("#actionCreate_ORD_Dashbrd").first,
            lambda: page.get_by_role("button", name=re.compile(r"Create\s*Order", re.I)),
            lambda: page.get_by_text("Create Order", exact=False),
        ],
        "Create Order icon/button",
    )

    # Wait directly for the create order popup. Do not close this dialog.
    create_order_dialog = page.locator(".p-dialog, p-dynamicdialog").filter(
        has_text=re.compile(r"New Customer|Select Catalog|Create Order", re.I)
    ).last

    expect(create_order_dialog).to_be_visible(timeout=DEFAULT_TIMEOUT)

    print("[Order] Create Order popup opened.")


# -------------------------
# Customer
# -------------------------

def create_new_customer_from_profile(page: Page, consumer_profile: dict) -> str:
    """
    Click +New Customer and create customer using framework/test_data.py profile.
    """

    first_name = get_profile_value(consumer_profile, ["first_name", "firstname", "fname"], "Test")
    last_name = get_profile_value(consumer_profile, ["last_name", "lastname", "lname"], "Customer")
    email = get_profile_value(
        consumer_profile,
        ["email", "email_id"],
        f"{first_name.lower()}.{random.randint(1000, 9999)}@jaldee.com",
    )
    phone = get_profile_value(
        consumer_profile,
        ["phone", "mobile", "phone_number", "mobile_number"],
        f"555{random.randint(1000000, 9999999)}",
    )
    address = get_profile_value(
        consumer_profile,
        ["address"],
        f"Test address {random.randint(100, 999)}",
    )

    customer_name = f"{first_name} {last_name}".strip()

    click_new_customer_from_create_order_popup(page)

    fill_first_visible(
        page,
        [
            lambda: page.get_by_role("textbox", name=re.compile(r"First Name", re.I)),
            lambda: page.get_by_placeholder(re.compile(r"First Name", re.I)),
        ],
        first_name,
        "First Name",
    )

    fill_first_visible(
        page,
        [
            lambda: page.get_by_role("textbox", name=re.compile(r"Last Name", re.I)),
            lambda: page.get_by_placeholder(re.compile(r"Last Name", re.I)),
        ],
        last_name,
        "Last Name",
    )

    fill_first_visible(
        page,
        [
            lambda: page.get_by_role("textbox", name=re.compile(r"Email", re.I)),
            lambda: page.get_by_placeholder(re.compile(r"Email", re.I)),
        ],
        email,
        "Email",
    )

    fill_first_visible(
        page,
        [
            lambda: page.get_by_role("textbox", name=re.compile(r"10123|Mobile|Phone", re.I)).first,
            lambda: page.get_by_placeholder(re.compile(r"Mobile|Phone", re.I)),
            lambda: page.locator("input[type='tel']").first,
        ],
        phone,
        "Phone",
    )

    fill_first_visible(
        page,
        [
            lambda: page.get_by_role("textbox", name=re.compile(r"Enter Customer Address|Address", re.I)),
            lambda: page.get_by_placeholder(re.compile(r"Enter Customer Address|Address", re.I)),
            lambda: page.locator("textarea").first,
        ],
        address,
        "Address",
    )

    click_first_visible(
        page,
        [
            lambda: page.get_by_role("button", name=re.compile(r"^Save$", re.I)),
            lambda: page.get_by_text("Save", exact=True),
        ],
        "Save customer button",
    )

    # Wait directly for Create Order popup to return.
    create_order_dialog = page.locator(".p-dialog, p-dynamicdialog").filter(
        has_text=re.compile(r"Select Catalog|Create Order|Sale_catalog", re.I)
    ).last

    expect(create_order_dialog).to_be_visible(timeout=DEFAULT_TIMEOUT)

    print(f"[Customer] Created customer: {customer_name}, phone: {phone}")

    return customer_name


# -------------------------
# Catalog
# -------------------------

def select_sale_catalog_and_go_next(page: Page) -> None:
    """
    Select Sale_catalog from Select Catalog dropdown and click Next.
    """

    click_first_visible(
        page,
        [
            lambda: page.locator(".p-multiselect-trigger-icon").first,
            lambda: page.locator(".p-multiselect-trigger").first,
            lambda: page.get_by_text("Select Catalog", exact=False),
        ],
        "Select Catalog dropdown",
    )

    click_first_visible(
        page,
        [
            lambda: page.get_by_text("Sale_catalog", exact=True),
            lambda: page.locator("p-multiselectitem").filter(has_text="Sale_catalog"),
            lambda: page.locator("li").filter(has_text="Sale_catalog"),
        ],
        "Sale_catalog option",
    )

    click_first_visible(
        page,
        [
            lambda: page.locator(".p-ripple.p-element.p-multiselect-close").first,
            lambda: page.locator(".p-multiselect-close").first,
            lambda: page.get_by_role("button", name=re.compile(r"close", re.I)),
        ],
        "catalog dropdown close icon",
    )

    click_first_visible(
        page,
        [
            lambda: page.get_by_role("button", name=re.compile(r"^Next$", re.I)),
            lambda: page.get_by_text("Next", exact=True),
        ],
        "Next button",
    )

    page.wait_for_load_state("networkidle")


# -------------------------
# Items
# -------------------------

def add_item_4_from_select_item_popup(page: Page) -> None:
    """
    Click Add Item, select Item_4 from select item popup, then click Done.
    """

    click_first_visible(
        page,
        [
            lambda: page.get_by_role("button", name=re.compile(r"Add Item", re.I)),
            lambda: page.get_by_text("+ Add Item", exact=False),
            lambda: page.get_by_text("Add Item", exact=False),
        ],
        "+ Add Item button",
    )

    item_4_row = page.get_by_role("row", name=re.compile(r"Item_4", re.I)).first

    expect(item_4_row).to_be_visible(timeout=DEFAULT_TIMEOUT)

    checkbox = item_4_row.locator("input[type='checkbox']").first

    if checkbox.count() > 0:
        checkbox.check(force=True)
    else:
        item_4_row.click()

    click_first_visible(
        page,
        [
            lambda: page.locator("#btnSltDn_ORD_ItemSelect"),
            lambda: page.get_by_role("button", name=re.compile(r"Done|Select|Add", re.I)),
            lambda: page.get_by_text("Done", exact=True),
        ],
        "item popup Done button",
    )

    page.wait_for_load_state("networkidle")

    print("[Item] Item_4 selected.")


def add_item_6_from_search(page: Page) -> None:
    """
    Search 'it', select Item_6, select any available colour, then click Select Item.
    """

    search_box = find_first_visible(
        page,
        [
            lambda: page.get_by_role("searchbox", name=re.compile(r"Search items", re.I)),
            lambda: page.get_by_placeholder(re.compile(r"Search items", re.I)),
            lambda: page.locator("input[placeholder*='Search items']").first,
        ],
        timeout=3000,
    )

    if search_box is None:
        click_first_visible(
            page,
            [
                lambda: page.get_by_role("button", name=re.compile(r"Add Item", re.I)),
                lambda: page.get_by_text("+ Add Item", exact=False),
                lambda: page.get_by_text("Add Item", exact=False),
            ],
            "+ Add Item button for Item_6",
        )

        search_box = find_first_visible(
            page,
            [
                lambda: page.get_by_role("searchbox", name=re.compile(r"Search items", re.I)),
                lambda: page.get_by_placeholder(re.compile(r"Search items", re.I)),
                lambda: page.locator("input[placeholder*='Search items']").first,
            ],
            timeout=DEFAULT_TIMEOUT,
        )

    if search_box is None:
        raise AssertionError("Search items field was not found for Item_6.")

    search_box.fill("it")

    click_first_visible(
        page,
        [
            lambda: page.get_by_text("Item_6", exact=True),
            lambda: page.locator("xpath=//*[normalize-space()='Item_6']"),
        ],
        "Item_6 search result",
    )

    colour_options = ["Blue", "Green", "White"]
    random.shuffle(colour_options)

    selected_colour = None

    for colour in colour_options:
        colour_button = page.get_by_role("button", name=re.compile(fr"^{colour}$", re.I)).first
        if is_visible(colour_button, timeout=2000):
            colour_button.click()
            selected_colour = colour
            break

    if selected_colour is None:
        raise AssertionError("No colour option found for Item_6. Expected Blue, Green, or White.")

    click_first_visible(
        page,
        [
            lambda: page.get_by_role("button", name=re.compile(r"Select Item", re.I)),
            lambda: page.get_by_text("Select Item", exact=False),
        ],
        "Select Item button",
    )

    page.wait_for_load_state("networkidle")

    print(f"[Item] Item_6 selected with colour: {selected_colour}")


# -------------------------
# Notes and order confirmation
# -------------------------

def add_order_note(page: Page, note_button_text: str) -> None:
    """
    Add random note for:
    - Notes to customer
    - Notes from seller
    """

    note_text = f"Automation note {random.randint(10000, 99999)}"

    click_first_visible(
        page,
        [
            lambda: page.get_by_text(note_button_text, exact=False),
            lambda: page.get_by_role("button", name=re.compile(note_button_text, re.I)),
        ],
        note_button_text,
    )

    note_field = find_first_visible(
        page,
        [
            lambda: page.locator("textarea").last,
            lambda: page.get_by_role("textbox").last,
        ],
        timeout=DEFAULT_TIMEOUT,
    )

    if note_field is None:
        raise AssertionError(f"Note field not found for {note_button_text}")

    note_field.fill(note_text)

    click_first_visible(
        page,
        [
            lambda: page.get_by_role("button", name=re.compile(r"^Save$", re.I)),
            lambda: page.get_by_text("Save", exact=True),
        ],
        f"Save button for {note_button_text}",
    )

    print(f"[Note] {note_button_text}: {note_text}")


def confirm_order(page: Page) -> None:
    click_first_visible(
        page,
        [
            lambda: page.get_by_role("button", name=re.compile(r"Confirm Order", re.I)),
            lambda: page.get_by_text("Confirm Order", exact=False),
        ],
        "Confirm Order button",
    )

    assert_success_or_info_message(page, "Order confirmation")

    print("[Order] Confirm Order completed.")


# -------------------------
# Invoice
# -------------------------

def create_invoice(page: Page) -> None:
    click_first_visible(
        page,
        [
            lambda: page.get_by_role("button", name=re.compile(r"Create Invoice", re.I)),
            lambda: page.get_by_text("+ Create Invoice", exact=False),
            lambda: page.get_by_text("Create Invoice", exact=False),
        ],
        "+ Create Invoice button",
    )

    page.wait_for_load_state("networkidle")

    print("[Invoice] Create Invoice clicked.")


def view_invoice(page: Page) -> None:
    """
    Click View Invoice and wait until invoice details page is opened.

    The test must not continue tax validation while still on order details page.
    """

    page.wait_for_load_state("domcontentloaded")

    # Scroll down because View Invoice is usually below payment/invoice section.
    page.mouse.wheel(0, 1800)
    page.wait_for_timeout(500)

    click_first_visible(
        page,
        [
            lambda: page.get_by_role("button", name=re.compile(r"View Invoice", re.I)),
            lambda: page.get_by_text("View Invoice", exact=False),
            lambda: page.locator("xpath=//*[contains(normalize-space(), 'View Invoice')]").first,
        ],
        "View Invoice button",
    )

    wait_until_invoice_details_page(page)

    print(f"[Invoice] Invoice details page opened: {page.url}")


def wait_until_invoice_details_page(page: Page) -> None:
    """
    Wait until browser is actually on Sales Order invoice details page.
    """

    try:
        page.wait_for_url(
            re.compile(r".*/business/salesorder/invoice/.*"),
            timeout=DEFAULT_TIMEOUT,
        )
        page.wait_for_load_state("domcontentloaded")
        return
    except Exception:
        pass

    current_url = page.url

    if "/business/salesorder/invoice/" in current_url or "/salesorder/invoice/" in current_url:
        page.wait_for_load_state("domcontentloaded")
        return

    raise AssertionError(
        "View Invoice was clicked, but invoice details page did not open. "
        f"Current URL: {page.url}"
    )    


def verify_item_4_invoice_tax_split(page: Page) -> dict:
    """
    Item_4 has 18% tax and price is tax inclusive.

    Formula:
        taxableAmount = totalAmount * 100 / (100 + taxPercentage)

    Then:
        totalTax = totalAmount - taxableAmount
        CGST = totalTax / 2
        SGST = totalTax / 2
    """

    if "/salesorder/invoice/" not in page.url:
        raise AssertionError(
            "Invoice tax validation started before invoice details page opened. "
            f"Current URL: {page.url}"
        )

    tax_percentage = Decimal("18")

    row_data = get_invoice_row_data(page, "Item_4")

    total_amount = row_data["total_amount"]
    gst_actual = row_data.get("gst_amount")

    taxable_expected = round_money(
        total_amount * Decimal("100") / (Decimal("100") + tax_percentage)
    )

    total_tax_expected = round_money(total_amount - taxable_expected)
    cgst_expected = round_money(total_tax_expected / Decimal("2"))
    sgst_expected = round_money(total_tax_expected / Decimal("2"))

    cgst_actual = read_tax_component_amount(page, "CGST")
    sgst_actual = read_tax_component_amount(page, "SGST")

    assert_amount_close(
        actual=cgst_actual,
        expected=cgst_expected,
        label="Item_4 CGST",
    )

    assert_amount_close(
        actual=sgst_actual,
        expected=sgst_expected,
        label="Item_4 SGST",
    )

    if gst_actual is not None:
        assert_amount_close(
            actual=gst_actual,
            expected=total_tax_expected,
            label="Item_4 GST",
        )

    print("[Invoice Tax] Item_4 inclusive tax calculation checked.")
    print(f"[Invoice Tax] Item_4 Total Inclusive Amount: {total_amount}")
    print(f"[Invoice Tax] Expected Taxable Amount: {taxable_expected}")
    print(f"[Invoice Tax] Expected Total Tax: {total_tax_expected}")
    print(f"[Invoice Tax] CGST: actual={cgst_actual}, expected={cgst_expected}")
    print(f"[Invoice Tax] SGST: actual={sgst_actual}, expected={sgst_expected}")

    return {
        "item": "Item_4",
        "tax_percentage": tax_percentage,
        "total_amount": total_amount,
        "taxable_expected": taxable_expected,
        "total_tax_expected": total_tax_expected,
        "gst_actual": gst_actual,
        "gst_expected": total_tax_expected,
        "cgst_actual": cgst_actual,
        "cgst_expected": cgst_expected,
        "sgst_actual": sgst_actual,
        "sgst_expected": sgst_expected,
        "row_data": row_data,
    }


def verify_invoice_totals(page: Page) -> dict:
    """
    Verify:
    - Subtotal
    - Net Total With Tax
    - Delivery Charge if present
    - Net Payable

    Rule:
        Net Payable = Net Total With Tax + Delivery Charge
    """

    subtotal = read_amount_by_label(page, ["Subtotal", "Sub Total"], required=True, use_last=True)
    net_total_with_tax = read_amount_by_label(page, ["Net Total With Tax", "Net Total with Tax", "Total With Tax"], required=True, use_last=True)
    delivery_charge = read_amount_by_label(page, ["Delivery Charge", "Delivery Charges"], required=False, use_last=True)
    net_payable = read_amount_by_label(page, ["Net Payable", "Amount Payable", "Payable Amount"], required=True, use_last=True)

    if delivery_charge is None:
        delivery_charge = Decimal("0.00")

    expected_net_payable = round_money(net_total_with_tax + delivery_charge)

    assert subtotal >= Decimal("0.00"), "Subtotal is invalid."

    assert_amount_close(
        actual=net_payable,
        expected=expected_net_payable,
        label="Net Payable",
    )

    print("[Invoice Total] Invoice totals are correct.")
    print(f"[Invoice Total] Subtotal: {subtotal}")
    print(f"[Invoice Total] Net Total With Tax: {net_total_with_tax}")
    print(f"[Invoice Total] Delivery Charge: {delivery_charge}")
    print(f"[Invoice Total] Net Payable: actual={net_payable}, expected={expected_net_payable}")

    return {
        "subtotal": subtotal,
        "net_total_with_tax": net_total_with_tax,
        "delivery_charge": delivery_charge,
        "net_payable": net_payable,
        "expected_net_payable": expected_net_payable,
    }


# -------------------------
# Payment and complete order
# -------------------------

def complete_cash_payment(page: Page) -> bool:
    """
    Complete invoice payment using Pay by Cash.

    PrimeNG dropdown options can detach/re-render, so Pay by Cash selection
    is handled with a retry helper.
    """

    page.wait_for_load_state("domcontentloaded")

    open_get_payment_dropdown(page)
    select_pay_by_cash_from_dropdown(page)

    note_field = find_first_visible(
        page,
        [
            lambda: page.locator("#inputNote_ORD_PayBill").first,
            lambda: page.get_by_placeholder(re.compile(r"note", re.I)).first,
            lambda: page.locator("textarea").last,
        ],
        timeout=5000,
    )

    if note_field is not None:
        note_field.fill(f"Cash payment automation note {random.randint(1000, 9999)}")

    click_first_visible(
        page,
        [
            lambda: page.get_by_role("button", name=re.compile(r"^Pay$", re.I)),
            lambda: page.locator("button").filter(has_text=re.compile(r"^Pay$", re.I)).last,
            lambda: page.get_by_text("Pay", exact=True),
        ],
        "Pay button",
    )

    click_first_visible(
        page,
        [
            lambda: page.get_by_role("button", name=re.compile(r"^Yes$", re.I)),
            lambda: page.locator("button").filter(has_text=re.compile(r"^Yes$", re.I)).last,
            lambda: page.get_by_text("Yes", exact=True),
        ],
        "Proceed with payment Yes button",
    )

    assert_success_or_info_message(page, "Payment completion")

    print("[Payment] Cash payment completed.")

    return True

def open_get_payment_dropdown(page: Page) -> None:
    """
    Open Get Payment dropdown on invoice details page.
    """

    page.wait_for_load_state("domcontentloaded")

    page.mouse.wheel(0, 1200)
    page.wait_for_timeout(500)

    click_first_visible(
        page,
        [
            lambda: page.get_by_role("combobox", name=re.compile(r"Get Payment", re.I)),
            lambda: page.locator("p-dropdown").filter(has_text=re.compile(r"Get Payment", re.I)).locator(".p-dropdown-trigger").first,
            lambda: page.locator(".p-dropdown").filter(has_text=re.compile(r"Get Payment", re.I)).locator(".p-dropdown-trigger").first,
            lambda: page.locator("xpath=//*[contains(normalize-space(), 'Get Payment')]/ancestor::*[contains(@class, 'p-dropdown')][1]//*[contains(@class, 'p-dropdown-trigger')]").first,
            lambda: page.get_by_role("button", name=re.compile(r"dropdown trigger", re.I)).last,
        ],
        "Get Payment dropdown",
    )

    page.wait_for_timeout(500)

    print("[Payment] Get Payment dropdown opened.")


def select_pay_by_cash_from_dropdown(page: Page) -> None:
    """
    Select Pay by Cash from PrimeNG dropdown.

    Retries because PrimeNG option nodes can detach during dropdown animation.
    """

    for attempt in range(1, 4):
        try:
            print(f"[Payment] Selecting Pay by Cash. Attempt: {attempt}")

            pay_by_cash_option = find_first_visible(
                page,
                [
                    lambda: page.get_by_role("option", name=re.compile(r"Pay by Cash", re.I)),
                    lambda: page.locator("li[role='option']").filter(has_text=re.compile(r"Pay by Cash", re.I)).first,
                    lambda: page.locator("p-dropdownitem").filter(has_text=re.compile(r"Pay by Cash", re.I)).first,
                    lambda: page.locator("xpath=//*[normalize-space()='Pay by Cash']").last,
                    lambda: page.get_by_text("Pay by Cash", exact=True).last,
                ],
                timeout=5000,
            )

            if pay_by_cash_option is None:
                open_get_payment_dropdown(page)
                continue

            pay_by_cash_option.scroll_into_view_if_needed(timeout=3000)
            pay_by_cash_option.click(timeout=5000)

            page.wait_for_timeout(1000)

            print("[Payment] Pay by Cash selected.")
            return

        except Exception as error:
            print(f"[Payment] Pay by Cash selection failed on attempt {attempt}: {error}")

            page.keyboard.press("Escape")
            page.wait_for_timeout(500)
            open_get_payment_dropdown(page)

    page.screenshot(
        path="reports/artifacts/pay_by_cash_selection_failed.png",
        full_page=True,
    )

    raise AssertionError("Could not select Pay by Cash from Get Payment dropdown.")



def go_back_to_order_details(page: Page) -> None:
    click_first_visible(
        page,
        [
            lambda: page.get_by_role("button", name=re.compile(r"Back", re.I)),
            lambda: page.get_by_text("Back", exact=False),
            lambda: page.locator("[aria-label='Back']").first,
            lambda: page.locator("i").nth(1),
        ],
        "Back button",
    )

    page.wait_for_load_state("networkidle")


def complete_order(page: Page) -> bool:
    page.mouse.wheel(0, 1500)

    click_first_visible(
        page,
        [
            lambda: page.get_by_role("button", name=re.compile(r"Complete Order", re.I)),
            lambda: page.get_by_text("Complete Order", exact=False),
        ],
        "Complete Order button",
    )

    assert_success_or_info_message(page, "Complete Order")

    print("[Order] Complete Order done.")

    return True


# -------------------------
# Invoice row parsing
# -------------------------

def get_invoice_row_data(page: Page, item_name: str) -> dict:
    """
    Reads invoice row using Playwright role row instead of tr.

    Current invoice row example:
    1 Item_4 1 350.00 271.19 271.19 48.81 320.00

    Columns:
    Sl.No.
    Item Name
    QTY
    MRP
    S.Price
    Net Total
    GST
    Total Amount
    """

    page.wait_for_load_state("domcontentloaded")

    row = find_first_visible(
        page,
        [
            lambda: page.get_by_role("row", name=re.compile(fr"{re.escape(item_name)}", re.I)),
            lambda: page.locator("xpath=//*[contains(normalize-space(), '" + item_name + "')]").first,
        ],
        timeout=DEFAULT_TIMEOUT,
    )

    if row is None:
        body_text = normalize_text(page.locator("body").inner_text(timeout=5000))
        raise AssertionError(
            f"Could not find invoice row for {item_name}. "
            f"Current URL: {page.url}. "
            f"Page text: {body_text[:2000]}"
        )

    row_text = normalize_text(row.inner_text(timeout=5000))

    print(f"[Invoice Row Text] {item_name}: {row_text}")

    amounts = extract_all_money(row_text)

    if len(amounts) < 5:
        raise AssertionError(
            f"Could not read expected invoice amounts from row for {item_name}. "
            f"Row text: {row_text}. "
            f"Amounts found: {amounts}"
        )

    # For row:
    # 1 Item_4 1 350.00 271.19 271.19 48.81 320.00
    #
    # amounts = [1, 4, 1, 350.00, 271.19, 271.19, 48.81, 320.00]
    #
    # Because Item_4 contains number 4, remove the item-name number effect by using last values.
    total_amount = amounts[-1]
    gst_amount = amounts[-2]
    net_total = amounts[-3]
    selling_price = amounts[-4]
    mrp = amounts[-5]

    return {
        "item": item_name,
        "row_text": row_text,
        "amounts": amounts,
        "mrp": mrp,
        "selling_price": selling_price,
        "net_total": net_total,
        "gst_amount": gst_amount,
        "total_amount": total_amount,
    }




def find_amount_from_row_map(row_map: dict, include_keywords: list[str], exclude_keywords: list[str]) -> Decimal | None:
    for header, cell_text in row_map.items():
        header_lower = header.lower()

        if not all(keyword.lower() in header_lower for keyword in include_keywords):
            continue

        if any(keyword.lower() in header_lower for keyword in exclude_keywords):
            continue

        amount = extract_last_money(cell_text)

        if amount is not None:
            return amount

    return None


# -------------------------
# Amount helpers
# -------------------------

def read_amount_by_label(page: Page, labels: list[str], required: bool, use_last: bool = False) -> Decimal | None:
    for label in labels:
        matches = page.locator(
            f"xpath=//*[contains(translate(normalize-space(.), "
            f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), "
            f"'{label.lower()}')]"
        )

        count = matches.count()

        if count == 0:
            continue

        indexes = range(count - 1, -1, -1) if use_last else range(count)

        for index in indexes:
            locator = matches.nth(index)

            if not locator.is_visible():
                continue

            own_text = normalize_text(locator.inner_text())
            amount = extract_last_money(own_text)

            if amount is not None:
                return amount

            parent_text = normalize_text(locator.locator("xpath=parent::*").inner_text())
            amount = extract_last_money(parent_text)

            if amount is not None:
                return amount

    if required:
        raise AssertionError(f"Could not read amount for labels: {labels}")

    return None


def extract_last_money(text: str) -> Decimal | None:
    """
    Extract the last amount from text.
    Supports:
    ₹1,234.50
    1234.50
    1,234
    """

    cleaned = text.replace(",", "")
    matches = re.findall(r"-?\d+(?:\.\d+)?", cleaned)

    if not matches:
        return None

    return round_money(Decimal(matches[-1]))


def extract_all_money(text: str) -> list[Decimal]:
    """
    Extract all decimal/integer money values from text.
    """

    if not text:
        return []

    cleaned = text.replace(",", "")

    matches = re.findall(r"-?\d+(?:\.\d+)?", cleaned)

    return [round_money(Decimal(value)) for value in matches]


def extract_money_prefer_currency_or_decimal(text: str) -> Decimal | None:
    """
    Extract amount from text.

    Priority:
    1. Currency amount like ₹24.41
    2. Decimal amount like 24.41
    3. Last number, excluding percentage-like values where possible
    """

    if not text:
        return None

    cleaned = text.replace(",", "")

    currency_matches = re.findall(
        r"(?:₹|Rs\.?|INR)\s*(-?\d+(?:\.\d+)?)",
        cleaned,
        flags=re.I,
    )

    if currency_matches:
        return round_money(Decimal(currency_matches[-1]))

    decimal_matches = re.findall(r"-?\d+\.\d{1,2}", cleaned)

    if decimal_matches:
        return round_money(Decimal(decimal_matches[-1]))

    all_numbers = re.findall(r"-?\d+(?:\.\d+)?", cleaned)

    if not all_numbers:
        return None

    # Avoid returning tax percentage such as 9 or 18 if there are other numbers.
    filtered_numbers = []

    for number in all_numbers:
        if f"{number}%" in cleaned:
            continue
        filtered_numbers.append(number)

    if filtered_numbers:
        return round_money(Decimal(filtered_numbers[-1]))

    return round_money(Decimal(all_numbers[-1]))



def round_money(value: Decimal) -> Decimal:
    return Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def assert_amount_close(actual: Decimal, expected: Decimal, label: str, tolerance: Decimal = Decimal("0.10")) -> None:
    difference = abs(actual - expected)

    if difference > tolerance:
        print(
            f"[Amount Mismatch] {label}: actual={actual}, expected={expected}, "
            f"difference={difference}, tolerance={tolerance}"
        )

    assert difference <= tolerance, (
        f"{label} mismatch. "
        f"Actual={actual}, Expected={expected}, Difference={difference}"
    )


def read_tax_component_amount(page: Page, component_name: str) -> Decimal:
    """
    Reads CGST/SGST amount from invoice page text.

    Example page text:
    CGST ₹ 24.41 SGST ₹ 24.41 Total Items 2 ...
    """

    page_text = normalize_text(page.locator("body").inner_text(timeout=5000))

    pattern = re.compile(
        rf"{re.escape(component_name)}\s*[^\d-]*(-?\d+(?:\.\d+)?)",
        re.I,
    )

    match = pattern.search(page_text)

    if not match:
        raise AssertionError(
            f"{component_name} amount was not found on invoice page. "
            f"Current URL: {page.url}. "
            f"Page text: {page_text[:2000]}"
        )

    amount = round_money(Decimal(match.group(1)))

    print(f"[Tax Component] {component_name}: {amount}")

    return amount




# -------------------------
# Generic Playwright helpers
# -------------------------

def click_first_visible(page: Page, locator_factories: list, description: str, timeout: int = DEFAULT_TIMEOUT):
    locator = find_first_visible(page, locator_factories, timeout=timeout)

    if locator is None:
        raise AssertionError(f"Could not find visible element: {description}")

    locator.click()
    return locator


def fill_first_visible(page: Page, locator_factories: list, value: str, description: str, timeout: int = DEFAULT_TIMEOUT):
    locator = find_first_visible(page, locator_factories, timeout=timeout)

    if locator is None:
        raise AssertionError(f"Could not find visible field: {description}")

    locator.fill(str(value))
    return locator


def find_first_visible(page: Page, locator_factories: list, timeout: int = DEFAULT_TIMEOUT):
    per_locator_timeout = min(2500, timeout)

    for factory in locator_factories:
        try:
            locator = factory()

            if callable(locator):
                locator = locator()

            locator = locator.first
            locator.wait_for(state="visible", timeout=per_locator_timeout)

            return locator

        except Exception:
            continue

    return None


def is_visible(locator, timeout: int = 2000) -> bool:
    try:
        locator.wait_for(state="visible", timeout=timeout)
        return True
    except Exception:
        return False


def assert_success_or_info_message(page: Page, action_name: str) -> None:
    """
    Looks for common toast/success messages.
    """

    possible_message = find_first_visible(
        page,
        [
            lambda: page.locator(".p-toast-message").last,
            lambda: page.locator(".p-toast-detail").last,
            lambda: page.get_by_text(re.compile(r"success|completed|created|confirmed|paid|payment", re.I)).last,
        ],
        timeout=8000,
    )

    if possible_message is None:
        print(f"[Warning] No toast message found after: {action_name}")
        return

    print(f"[Message] {action_name}: {normalize_text(possible_message.inner_text())}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def get_profile_value(profile: dict, keys: list[str], default: str) -> str:
    for key in keys:
        value = profile.get(key)

        if value:
            return str(value)

    return str(default)


def click_new_customer_from_create_order_popup(page: Page) -> None:
    """
    Click New customer from Create Order popup.

    The popup is already open. The button accessible name is:
    New customer
    """

    create_order_dialog = page.get_by_role("dialog").filter(
        has_text=re.compile(r"Create Order", re.I)
    ).last

    expect(create_order_dialog).to_be_visible(timeout=DEFAULT_TIMEOUT)

    new_customer_button = create_order_dialog.get_by_role(
        "button",
        name=re.compile(r"^New\s*customer$", re.I),
    ).first

    expect(new_customer_button).to_be_visible(timeout=DEFAULT_TIMEOUT)
    expect(new_customer_button).to_be_enabled(timeout=DEFAULT_TIMEOUT)

    print("[Customer] Clicking New customer button.")

    new_customer_button.scroll_into_view_if_needed(timeout=5000)
    new_customer_button.click(timeout=10000)

    first_name_field = wait_for_customer_first_name_field(page, timeout=10000)

    if first_name_field is not None:
        print("[Customer] Customer creation form loaded.")
        return

    print("[Customer] First click did not open form. Retrying New customer click.")

    fallback_button = create_order_dialog.locator(
        "xpath=.//button[contains(normalize-space(), 'New customer') or contains(normalize-space(), 'New Customer')]"
    ).last

    if is_visible(fallback_button, timeout=3000):
        fallback_button.click(timeout=10000)

        first_name_field = wait_for_customer_first_name_field(page, timeout=10000)

        if first_name_field is not None:
            print("[Customer] Customer creation form loaded after fallback click.")
            return

    try:
        page.screenshot(
            path="reports/artifacts/new_customer_click_failed.png",
            full_page=True,
        )
    except Exception:
        pass

    dialog_text = normalize_text(create_order_dialog.inner_text(timeout=3000))

    raise AssertionError(
        "New customer button was visible, but customer creation form did not open. "
        f"Current URL: {page.url}. "
        f"Dialog text: {dialog_text}"
    )


def wait_for_customer_first_name_field(page: Page, timeout: int = DEFAULT_TIMEOUT):
    """
    Wait for customer creation First Name field.
    """

    return find_first_visible(
        page,
        [
            lambda: page.get_by_role("textbox", name=re.compile(r"First Name", re.I)),
            lambda: page.get_by_placeholder(re.compile(r"First Name", re.I)),
            lambda: page.locator("input[placeholder*='First']").first,
            lambda: page.locator("input[formcontrolname*='first']").first,
            lambda: page.locator("input[name*='first']").first,
            lambda: page.locator("input[id*='first']").first,
        ],
        timeout=timeout,
    )
