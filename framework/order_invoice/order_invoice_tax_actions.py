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



def complete_exempt_items_order_invoice_flow(page: Page, config) -> dict:
    """
    Order created with only exempt items; no GST applied and total equals item sum.

    Flow:
    - Open Sales Order dashboard
    - Open Create Order popup
    - Select existing consumer Jisha using 8281
    - Select Sale_catalog
    - Add Item_2 with random colour Black/Blue
    - Add Item_6 with random colour Blue/Green/White
    - Confirm order
    - Create invoice
    - View invoice
    - Verify no CGST/SGST and no GST calculated
    - Pay by Others with random payment mode
    - Complete order
    """

    select_first_business_if_needed(page)
    close_blocking_dialog_if_present(page)

    open_sales_order_dashboard(page)
    # close_blocking_dialog_if_present(page)

    ensure_store_is_bnb_stores(page)
    open_create_order_popup(page)

    consumer_selected = select_existing_order_consumer(
        page=page,
        search_text="8281",
        consumer_text="Jisha Sreejith",
    )

    select_sale_catalog_and_go_next(page)

    add_item_2_with_random_colour(page)
    add_item_6_from_search(page)

    confirm_order(page)

    create_invoice(page)
    view_invoice(page)

    exempt_tax_result = verify_exempt_invoice_no_gst(page)

    payment_result = complete_other_payment(page)

    go_back_to_order_details(page)

    order_completed = complete_order(page)

    return {
        "consumer_selected": consumer_selected,
        "exempt_tax_result": exempt_tax_result,
        "payment_completed": payment_result,
        "order_completed": order_completed,
        "final_url": page.url,
    }


def select_existing_order_consumer(page: Page, search_text: str, consumer_text: str) -> bool:
    """
    Select existing consumer from Create Order popup.

    Example:
    search_text = "8281"
    consumer_text = "Jisha Sreejith"

    This waits for the Create Order popup to become stable before typing.
    """

    wait_for_create_order_popup_ready(page)

    create_order_dialog = page.get_by_role("dialog").filter(
        has_text=re.compile(r"Create Order|Select customer", re.I)
    ).last

    expect(create_order_dialog).to_be_visible(timeout=DEFAULT_TIMEOUT)

    customer_search = create_order_dialog.get_by_role(
        "searchbox",
        name=re.compile(r"Select customer", re.I),
    ).first

    expect(customer_search).to_be_visible(timeout=DEFAULT_TIMEOUT)

    customer_search.click()
    customer_search.fill(search_text)

    consumer_text_locator = find_first_visible(
        page,
        [
            lambda: page.locator("p-autocompleteitem").filter(
                has_text=re.compile(consumer_text, re.I)
            ).first,
            lambda: page.locator("li").filter(
                has_text=re.compile(consumer_text, re.I)
            ).first,
            lambda: page.locator("[role='option']").filter(
                has_text=re.compile(consumer_text, re.I)
            ).first,
            lambda: page.get_by_text(re.compile(consumer_text, re.I)).first,
        ],
        timeout=DEFAULT_TIMEOUT,
    )

    if consumer_text_locator is None:
        raise AssertionError(
            f"Consumer matching '{consumer_text}' was not found after searching '{search_text}'."
        )

    print(f"[Consumer] Consumer option appeared for search: {search_text}")

    # First try keyboard selection. This is usually most stable for autocomplete.
    customer_search.press("ArrowDown")
    page.wait_for_timeout(300)
    customer_search.press("Enter")
    page.wait_for_timeout(1000)

    if is_consumer_selected_in_create_order_popup(page, consumer_text):
        print(f"[Consumer] Existing consumer selected by keyboard: {consumer_text}")
        return True

    print("[Consumer] Keyboard selection did not confirm. Trying option click.")

    clickable_option = find_first_visible(
        page,
        [
            lambda: page.locator("p-autocompleteitem").filter(
                has_text=re.compile(consumer_text, re.I)
            ).first,
            lambda: page.locator("li").filter(
                has_text=re.compile(consumer_text, re.I)
            ).first,
            lambda: page.locator("[role='option']").filter(
                has_text=re.compile(consumer_text, re.I)
            ).first,
        ],
        timeout=5000,
    )

    if clickable_option is not None:
        try:
            clickable_option.click(timeout=5000)
            page.wait_for_timeout(1000)

            if is_consumer_selected_in_create_order_popup(page, consumer_text):
                print(f"[Consumer] Existing consumer selected by option click: {consumer_text}")
                return True

        except Exception as error:
            print(f"[Consumer] Normal option click failed: {error}")

        try:
            clickable_option.dispatch_event("click")
            page.wait_for_timeout(1000)

            if is_consumer_selected_in_create_order_popup(page, consumer_text):
                print(f"[Consumer] Existing consumer selected by dispatch click: {consumer_text}")
                return True

        except Exception as error:
            print(f"[Consumer] Dispatch click failed: {error}")

    print("[Consumer] Trying text locator dispatch click fallback.")

    try:
        consumer_text_locator.dispatch_event("click")
        page.wait_for_timeout(1000)

        if is_consumer_selected_in_create_order_popup(page, consumer_text):
            print(f"[Consumer] Existing consumer selected by text dispatch click: {consumer_text}")
            return True

    except Exception as error:
        print(f"[Consumer] Text dispatch click failed: {error}")

    page.screenshot(
        path="reports/artifacts/existing_consumer_selection_failed.png",
        full_page=True,
    )

    dialog_text = normalize_text(create_order_dialog.inner_text(timeout=3000))

    raise AssertionError(
        f"Consumer '{consumer_text}' appeared but could not be selected. "
        f"Current URL: {page.url}. "
        f"Dialog text: {dialog_text}"
    )



def is_consumer_selected_in_create_order_popup(page: Page, consumer_text: str) -> bool:
    """
    Check whether the consumer is selected in the Create Order popup.
    """

    create_order_dialog = page.get_by_role("dialog").filter(
        has_text=re.compile(r"Create Order|Select customer", re.I)
    ).last

    try:
        dialog_text = normalize_text(create_order_dialog.inner_text(timeout=3000))
    except Exception:
        return False

    return consumer_text.lower() in dialog_text.lower()





# -------------------------
# Navigation
# -------------------------


def close_blocking_dialog_if_present(page: Page) -> None:
    """
    Close unexpected PrimeNG dialog/overlay that blocks page clicks.

    Important:
    Do NOT close valid business dialogs like:
    - Create Order
    - Select Items
    - payment dialogs
    - item attribute dialogs
    """

    dialog = page.get_by_role("dialog").last

    if not is_visible(dialog, timeout=1500):
        return

    try:
        dialog_text = normalize_text(dialog.inner_text(timeout=2000))
    except Exception:
        dialog_text = ""

    valid_dialog_keywords = [
        "Create Order",
        "Select customer",
        "Select Catalog",
        "Select Items",
        "Select Item",
        "Payment",
        "Get Payment",
        "Pay",
        "Select mode",
        "New customer",
        "First Name",
    ]

    for keyword in valid_dialog_keywords:
        if keyword.lower() in dialog_text.lower():
            print(f"[Dialog] Valid dialog detected, not closing it: {keyword}")
            return

    print("[Dialog] Unexpected blocking dialog detected. Trying to close it.")

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
        page.wait_for_timeout(700)
        print("[Dialog] Unexpected dialog closed using close button.")
        return

    page.keyboard.press("Escape")
    page.wait_for_timeout(700)

    print("[Dialog] Escape pressed for unexpected dialog.")



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
    Open Sales Order dashboard.

    Important:
    Do not treat URLs like this as dashboard:
    /salesorder/catalogs?from=orderDashboard

    Only this path is dashboard:
    /business/salesorder/dashboard
    """

    page.wait_for_load_state("domcontentloaded")
    close_blocking_dialog_if_present(page)

    current_url = page.url.lower()

    if re.search(r"/business/salesorder/dashboard(?:\?|$)", current_url):
        print("[Navigation] Already on Sales Order dashboard.")
        return

    print(f"[Navigation] Not on Sales Order dashboard. Current URL: {page.url}")

    # Direct navigation is more stable than clicking sidebar icons.
    dashboard_url = re.sub(
        r"/business/.*",
        "/business/salesorder/dashboard",
        page.url,
        flags=re.I,
    )

    if dashboard_url == page.url:
        dashboard_url = "https://scale.jaldee.com/business/salesorder/dashboard"

    print(f"[Navigation] Opening Sales Order dashboard directly: {dashboard_url}")

    page.goto(dashboard_url)
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(1500)

    expect(page).to_have_url(
        re.compile(r".*/business/salesorder/dashboard.*"),
        timeout=DEFAULT_TIMEOUT,
    )

    expect(page.get_by_text("Sales Order", exact=False).first).to_be_visible(
        timeout=DEFAULT_TIMEOUT
    )

    print("[Navigation] Sales Order dashboard opened.")


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
    Click Create Order from Sales Order dashboard and wait for Create Order popup.
    """

    page.wait_for_load_state("domcontentloaded")

    if not re.search(r"/business/salesorder/dashboard(?:\?|$)", page.url.lower()):
        print(f"[Order] Not on dashboard before Create Order click. Current URL: {page.url}")
        open_sales_order_dashboard(page)

    if is_create_order_popup_open(page, timeout=1000):
        wait_for_create_order_popup_ready(page)
        print("[Order] Create Order popup already open and ready.")
        return

    print("[Order] Trying to open Create Order popup from dashboard.")

    create_order_tile = find_first_visible(
        page,
        [
            lambda: page.locator("#actionCreate_ORD_Dashbrd").first,
            lambda: page.locator("#btnCreate_ORD_Order").first,
            lambda: page.locator("[id*='Create'][id*='ORD']").first,
            lambda: page.locator("[id*='Create'][id*='Order']").first,
            lambda: page.locator(
                "xpath=//*[normalize-space()='Create Order']/ancestor::*[contains(@class, 'p-card')][1]"
            ).first,
            lambda: page.locator(
                "xpath=//*[normalize-space()='Create Order']/ancestor::*[contains(@class, 'card')][1]"
            ).first,
            lambda: page.get_by_text("Create Order", exact=True).first,
        ],
        timeout=DEFAULT_TIMEOUT,
    )

    if create_order_tile is None:
        page.screenshot(
            path="reports/artifacts/create_order_tile_not_found.png",
            full_page=True,
        )

        body_text = normalize_text(page.locator("body").inner_text(timeout=5000))

        raise AssertionError(
            "Create Order tile was not found on Sales Order dashboard. "
            f"Current URL: {page.url}. "
            f"Page text: {body_text[:2000]}"
        )

    create_order_tile.scroll_into_view_if_needed(timeout=5000)
    create_order_tile.click(timeout=10000, force=True)

    page.wait_for_timeout(1500)

    if not is_create_order_popup_open(page, timeout=5000):
        print("[Order] Normal click did not open popup. Trying JS parent click.")

        if not click_create_order_using_js_parent(page):
            print("[Order] JS parent click did not open popup. Trying mouse coordinate click.")

            if not click_create_order_using_mouse_coordinates(page):
                page.screenshot(
                    path="reports/artifacts/create_order_click_failed.png",
                    full_page=True,
                )

                body_text = normalize_text(page.locator("body").inner_text(timeout=5000))

                raise AssertionError(
                    "Create Order was visible, but clicking it did not open the Create Order popup. "
                    f"Current URL: {page.url}. "
                    f"Page text: {body_text[:2000]}"
                )

    wait_for_create_order_popup_ready(page)

    print("[Order] Create Order popup opened and ready.")

    


def is_create_order_popup_open(page: Page, timeout: int = 1000) -> bool:
    """
    Returns True if Create Order dialog is already visible.
    """

    dialog = page.get_by_role("dialog").filter(
        has_text=re.compile(r"Create Order|Select customer|Select Catalog", re.I)
    ).last

    return is_visible(dialog, timeout=timeout)



def click_create_order_using_js_parent(page: Page) -> bool:
    """
    Click nearest useful parent of the visible 'Create Order' text.

    This is needed because Create Order appears as plain text in the accessibility tree,
    but the click handler may be attached to a parent div/card.
    """

    create_order_text = find_first_visible(
        page,
        [
            lambda: page.get_by_text("Create Order", exact=True).first,
            lambda: page.locator("xpath=//*[normalize-space()='Create Order']").first,
        ],
        timeout=5000,
    )

    if create_order_text is None:
        print("[Order] Create Order text was not found for JS parent click.")
        return False

    try:
        clicked_info = create_order_text.evaluate(
            """
            (el) => {
                let node = el;

                for (let depth = 0; depth < 10 && node; depth++) {
                    const text = (node.innerText || '').trim();
                    const rect = node.getBoundingClientRect();

                    const hasCreateOrderText = text.includes('Create Order');
                    const usefulSize =
                        rect.width >= 60 &&
                        rect.height >= 30 &&
                        rect.width <= 600 &&
                        rect.height <= 400;

                    if (hasCreateOrderText && usefulSize) {
                        node.click();

                        return {
                            clicked: true,
                            depth: depth,
                            tag: node.tagName,
                            className: node.className,
                            text: text.substring(0, 100),
                            width: rect.width,
                            height: rect.height
                        };
                    }

                    node = node.parentElement;
                }

                el.click();

                return {
                    clicked: true,
                    depth: -1,
                    tag: el.tagName,
                    className: el.className,
                    text: (el.innerText || '').substring(0, 100)
                };
            }
            """
        )

        print(f"[Order] JS Create Order click result: {clicked_info}")

        page.wait_for_timeout(1500)

        return is_create_order_popup_open(page, timeout=3000)

    except Exception as error:
        print(f"[Order] JS parent click failed: {error}")
        return False
    


def click_create_order_using_mouse_coordinates(page: Page) -> bool:
    """
    Final fallback: click around the visible Create Order text.

    Some dashboard cards attach the click handler to the icon/card area,
    not the text itself.
    """

    create_order_text = find_first_visible(
        page,
        [
            lambda: page.get_by_text("Create Order", exact=True).first,
            lambda: page.locator("xpath=//*[normalize-space()='Create Order']").first,
        ],
        timeout=5000,
    )

    if create_order_text is None:
        print("[Order] Create Order text was not found for mouse fallback.")
        return False

    try:
        create_order_text.scroll_into_view_if_needed(timeout=5000)

        box = create_order_text.bounding_box(timeout=5000)

        if box is None:
            print("[Order] Could not get Create Order bounding box.")
            return False

        x = box["x"] + box["width"] / 2
        y = box["y"] + box["height"] / 2

        click_points = [
            (x, y),
            (x, y - 35),
            (x, y - 60),
            (x, y + 35),
        ]

        for index, point in enumerate(click_points, start=1):
            print(f"[Order] Mouse clicking Create Order point {index}: {point}")

            page.mouse.click(point[0], point[1])
            page.wait_for_timeout(1500)

            if is_create_order_popup_open(page, timeout=3000):
                return True

        return False

    except Exception as error:
        print(f"[Order] Mouse coordinate click failed: {error}")
        return False    




def wait_for_sales_order_dashboard_ready(page: Page) -> None:
    """
    Wait until Sales Order dashboard is stable before clicking Create Order.

    This avoids clicking Create Order while the dashboard is still re-rendering.
    """

    if "/salesorder/dashboard" not in page.url:
        return

    expect(page.get_by_text("Sales Order", exact=False).first).to_be_visible(timeout=DEFAULT_TIMEOUT)
    expect(page.get_by_text("Create Order", exact=True).first).to_be_visible(timeout=DEFAULT_TIMEOUT)

    # Wait for common dashboard content to settle.
    find_first_visible(
        page,
        [
            lambda: page.get_by_text(re.compile(r"Orders", re.I)).first,
            lambda: page.get_by_text(re.compile(r"Stats", re.I)).first,
            lambda: page.locator("table").first,
        ],
        timeout=DEFAULT_TIMEOUT,
    )

    # Small stability wait. This is intentional to avoid Create Order popup being closed by dashboard re-render.
    page.wait_for_timeout(1500)




def wait_for_create_order_popup_ready(page: Page) -> None:
    """
    Wait for Create Order popup to be ready.

    The popup is ready only when:
    - dialog is visible
    - Select customer searchbox is visible
    - Next button is visible
    """

    last_error = None

    for attempt in range(1, 4):
        try:
            print(f"[Order] Waiting for Create Order popup. Attempt: {attempt}")

            create_order_dialog = page.get_by_role("dialog").filter(
                has_text=re.compile(r"Create Order|Select customer|Select Catalog", re.I)
            ).last

            expect(create_order_dialog).to_be_visible(timeout=DEFAULT_TIMEOUT)

            customer_search = create_order_dialog.get_by_role(
                "searchbox",
                name=re.compile(r"Select customer", re.I),
            ).first

            expect(customer_search).to_be_visible(timeout=DEFAULT_TIMEOUT)

            next_button = create_order_dialog.get_by_role(
                "button",
                name=re.compile(r"^Next$", re.I),
            ).first

            expect(next_button).to_be_visible(timeout=DEFAULT_TIMEOUT)

            page.wait_for_timeout(1000)

            expect(create_order_dialog).to_be_visible(timeout=3000)
            expect(customer_search).to_be_visible(timeout=3000)
            expect(next_button).to_be_visible(timeout=3000)

            return

        except Exception as error:
            last_error = error
            print(f"[Order] Create Order popup was not stable yet: {error}")
            page.wait_for_timeout(1000)

    raise AssertionError(
        "Create Order popup did not become stable. "
        f"Last error: {last_error}"
    )



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


def add_item_6_from_search(page: Page) -> dict:
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
        timeout=DEFAULT_TIMEOUT,
    )

    if search_box is None:
        raise AssertionError("Search items field was not found for Item_6.")

    search_box.click()
    search_box.fill("it")

    click_first_visible(
        page,
        [
            lambda: page.get_by_text("Item_6", exact=True),
            lambda: page.locator("xpath=//*[normalize-space()='Item_6']").first,
        ],
        "Item_6 search result",
    )

    selected_colour = select_random_item_colour(
        page=page,
        colours=["Blue", "Green", "White"],
        item_name="Item_6",
    )

    click_select_item_button(page)

    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(1000)

    print(f"[Item] Item_6 selected with colour: {selected_colour}")

    return {
        "item_name": "Item_6",
        "colour": selected_colour,
    }



# --------------------------------
# Notes and order confirmation
# --------------------------------

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
    Reads invoice row using Playwright role row.

    Supports:
    - Exempt rows
    - Taxable rows
    - Taxable + CESS rows
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

    money_values = extract_decimal_money_values(row_text)

    if len(money_values) < 4:
        raise AssertionError(
            f"Could not read expected invoice money values from row for {item_name}. "
            f"Row text: {row_text}. "
            f"Money values found: {money_values}"
        )

    cess_amount = Decimal("0.00")

    if len(money_values) >= 6:
        # Taxable row with CESS:
        # MRP, S.Price, Net Total, GST, CESS, Total Amount
        mrp = money_values[-6]
        selling_price = money_values[-5]
        net_total = money_values[-4]
        gst_amount = money_values[-3]
        cess_amount = money_values[-2]
        total_amount = money_values[-1]

    elif len(money_values) == 5:
        # Taxable row without CESS:
        # MRP, S.Price, Net Total, GST, Total Amount
        mrp = money_values[-5]
        selling_price = money_values[-4]
        net_total = money_values[-3]
        gst_amount = money_values[-2]
        total_amount = money_values[-1]

    else:
        # Exempt row:
        # MRP, S.Price, Net Total, Total Amount
        mrp = money_values[-4]
        selling_price = money_values[-3]
        net_total = money_values[-2]
        gst_amount = Decimal("0.00")
        total_amount = money_values[-1]

    return {
        "item": item_name,
        "row_text": row_text,
        "money_values": money_values,
        "mrp": mrp,
        "selling_price": selling_price,
        "net_total": net_total,
        "gst_amount": gst_amount,
        "cess_amount": cess_amount,
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


def extract_decimal_money_values(text: str) -> list[Decimal]:
    """
    Extract only decimal money values from text.

    This avoids picking item numbers, serial numbers, and quantity values.

    Example:
    1 Item_2 Black 1 650.00 594.00 594.00 594.00

    Returns:
    [650.00, 594.00, 594.00, 594.00]
    """

    if not text:
        return []

    cleaned = text.replace(",", "")

    matches = re.findall(r"-?\d+\.\d{1,2}", cleaned)

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
    Reads CGST/SGST/CESS amount from invoice summary area.

    Important:
    The invoice table header can contain text like CESS(₹), so we should not
    read from the table area. We isolate the summary area starting from CGST.
    """

    page_text = normalize_text(page.locator("body").inner_text(timeout=5000))

    summary_start = page_text.lower().rfind("cgst")

    if summary_start == -1:
        raise AssertionError(
            f"Could not find invoice tax summary area. "
            f"Current URL: {page.url}. "
            f"Page text: {page_text[:2000]}"
        )

    summary_text = page_text[summary_start:]

    # Stop after Get Payment / payment section if present.
    stop_keywords = ["Get Payment", "Settle Invoice", "Cancel Invoice"]

    for keyword in stop_keywords:
        stop_index = summary_text.lower().find(keyword.lower())

        if stop_index != -1:
            summary_text = summary_text[:stop_index]
            break

    print(f"[Tax Summary Text] {summary_text}")

    pattern = re.compile(
        rf"{re.escape(component_name)}\s*(?:₹|Rs\.?|INR)?\s*(-?\d+(?:\.\d+)?)",
        re.I,
    )

    match = pattern.search(summary_text)

    if not match:
        raise AssertionError(
            f"Could not read amount for {component_name} from invoice summary. "
            f"Summary text: {summary_text}. "
            f"Current URL: {page.url}"
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


def add_item_2_with_random_colour(page: Page) -> dict:
    """
    Add Item_2 from Select Items popup.

    Item_2 opens attribute popup. Select Black or Blue randomly.
    Then click Select Item.
    Then click Done from Select Items popup.
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

    item_2_row = page.get_by_role("row", name=re.compile(r"Item_2", re.I)).first

    expect(item_2_row).to_be_visible(timeout=DEFAULT_TIMEOUT)

    checkbox = item_2_row.locator("input[type='checkbox']").first

    if checkbox.count() > 0:
        checkbox.check(force=True)
    else:
        item_2_row.click()

    selected_colour = select_random_item_colour(
        page=page,
        colours=["Black", "Blue"],
        item_name="Item_2",
    )

    click_select_item_button(page)

    click_select_items_done_button(page)

    print(f"[Item] Item_2 selected with colour: {selected_colour}")

    return {
        "item_name": "Item_2",
        "colour": selected_colour,
    }



def select_random_item_colour(page: Page, colours: list[str], item_name: str) -> str:
    """
    Select a random available colour from item attribute popup.
    """

    shuffled_colours = colours[:]
    random.shuffle(shuffled_colours)

    for colour in shuffled_colours:
        colour_button = page.get_by_role(
            "button",
            name=re.compile(fr"^{colour}$", re.I),
        ).first

        if is_visible(colour_button, timeout=3000):
            colour_button.click()
            print(f"[Item] {item_name} colour selected: {colour}")
            return colour

    raise AssertionError(
        f"No expected colour option found for {item_name}. "
        f"Expected one of: {colours}"
    )


def click_select_item_button(page: Page) -> None:
    """
    Click Select Item button from item attribute popup.
    """

    click_first_visible(
        page,
        [
            lambda: page.get_by_role("button", name=re.compile(r"Select Item", re.I)),
            lambda: page.get_by_text("Select Item", exact=False),
            lambda: page.locator("button").filter(has_text=re.compile(r"Select Item", re.I)).last,
        ],
        "Select Item button",
    )

    page.wait_for_timeout(1000)


def click_select_items_done_button(page: Page) -> None:
    """
    Click Done button from Select Items popup.

    In this UI, Done can appear at top right or bottom.
    """

    click_first_visible(
        page,
        [
            lambda: page.locator("#btnSltDn_ORD_ItemSelectTop").first,
            lambda: page.locator("#btnSltDn_ORD_ItemSelect").first,
            lambda: page.get_by_role("button", name=re.compile(r"Done|Select", re.I)).last,
            lambda: page.locator("button").filter(has_text=re.compile(r"Done", re.I)).last,
        ],
        "Select Items Done button",
    )

    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(1000)



def verify_exempt_invoice_no_gst(page: Page) -> dict:
    """
    Verify exempt invoice:
    - CGST should not be visible
    - SGST should not be visible
    - Item GST amounts should be 0
    - Subtotal should equal item total amount sum
    - Net payable should equal subtotal + delivery charge, if delivery charge exists
    """

    if "/salesorder/invoice/" not in page.url:
        raise AssertionError(
            "Exempt invoice validation started before invoice details page opened. "
            f"Current URL: {page.url}"
        )

    item_2_row = get_invoice_row_data(page, "Item_2")
    item_6_row = get_invoice_row_data(page, "Item_6")

    item_2_gst = item_2_row.get("gst_amount", Decimal("0.00"))
    item_6_gst = item_6_row.get("gst_amount", Decimal("0.00"))

    total_gst_amount = round_money(item_2_gst + item_6_gst)

    if total_gst_amount != Decimal("0.00"):
        print(
            f"[Tax Error] GST was calculated for exempt invoice. "
            f"Item_2 GST={item_2_gst}, Item_6 GST={item_6_gst}, Total GST={total_gst_amount}"
        )

    assert total_gst_amount == Decimal("0.00"), (
        "GST should not be calculated for exempt items. "
        f"Actual GST={total_gst_amount}"
    )

    cgst_visible = is_invoice_tax_label_visible(page, "CGST")
    sgst_visible = is_invoice_tax_label_visible(page, "SGST")

    if cgst_visible or sgst_visible:
        print(
            f"[Tax Error] CGST/SGST is visible for exempt invoice. "
            f"CGST visible={cgst_visible}, SGST visible={sgst_visible}"
        )

    assert cgst_visible is False, "CGST should not be visible for exempt invoice."
    assert sgst_visible is False, "SGST should not be visible for exempt invoice."

    item_total_sum = round_money(item_2_row["total_amount"] + item_6_row["total_amount"])

    subtotal = read_amount_by_label(
        page,
        ["Subtotal", "Sub Total"],
        required=True,
        use_last=True,
    )

    assert_amount_close(
        actual=subtotal,
        expected=item_total_sum,
        label="Exempt Invoice Subtotal",
    )

    delivery_charge = read_amount_by_label(
        page,
        ["Delivery Charge", "Delivery Charges"],
        required=False,
        use_last=True,
    )

    if delivery_charge is None:
        delivery_charge = Decimal("0.00")

    net_payable = read_amount_by_label(
        page,
        ["Net payable", "Net Payable", "Amount Payable", "Payable Amount"],
        required=True,
        use_last=True,
    )

    expected_net_payable = round_money(subtotal + delivery_charge)

    assert_amount_close(
        actual=net_payable,
        expected=expected_net_payable,
        label="Exempt Invoice Net Payable",
    )

    print("[Exempt Invoice] No GST calculation found. Totals are correct.")
    print(f"[Exempt Invoice] Item_2 total: {item_2_row['total_amount']}")
    print(f"[Exempt Invoice] Item_6 total: {item_6_row['total_amount']}")
    print(f"[Exempt Invoice] Subtotal actual={subtotal}, expected={item_total_sum}")
    print(f"[Exempt Invoice] Delivery Charge: {delivery_charge}")
    print(f"[Exempt Invoice] Net Payable actual={net_payable}, expected={expected_net_payable}")

    return {
        "item_2_row": item_2_row,
        "item_6_row": item_6_row,
        "item_total_sum": item_total_sum,
        "subtotal": subtotal,
        "delivery_charge": delivery_charge,
        "net_payable": net_payable,
        "expected_net_payable": expected_net_payable,
        "item_2_gst": item_2_gst,
        "item_6_gst": item_6_gst,
        "total_gst_amount": total_gst_amount,
        "cgst_visible": cgst_visible,
        "sgst_visible": sgst_visible,
    }



def is_invoice_tax_label_visible(page: Page, label: str) -> bool:
    """
    Check whether CGST/SGST label is visible in invoice summary area.
    """

    locator = page.locator(
        f"xpath=//*[contains(translate(normalize-space(.), "
        f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), "
        f"'{label.lower()}')]"
    ).first

    return is_visible(locator, timeout=2000)



def complete_other_payment(page: Page) -> bool:
    """
    Complete invoice payment using Pay by Others.
    Then randomly select one payment mode.
    """

    page.wait_for_load_state("domcontentloaded")

    open_get_payment_dropdown(page)
    select_pay_by_others_from_dropdown(page)

    selected_mode = select_random_other_payment_mode(page)

    note_field = find_first_visible(
        page,
        [
            lambda: page.locator("#inputNote_ORD_PayBill").first,
            lambda: page.get_by_placeholder(re.compile(r"Leave a Payment Note|Payment Note|Note", re.I)).first,
            lambda: page.locator("textarea").last,
        ],
        timeout=5000,
    )

    if note_field is not None:
        note = f"Other payment automation note {random.randint(1000, 9999)}"
        note_field.fill(note)
        print(f"[Payment] Payment note entered: {note}")

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

    assert_success_or_info_message(page, "Other payment completion")

    print(f"[Payment] Pay by Others completed. Mode: {selected_mode}")

    return True



def select_pay_by_others_from_dropdown(page: Page) -> None:
    """
    Select Pay by Others from Get Payment dropdown.
    """

    for attempt in range(1, 4):
        try:
            print(f"[Payment] Selecting Pay by Others. Attempt: {attempt}")

            pay_by_others_option = find_first_visible(
                page,
                [
                    lambda: page.get_by_role("option", name=re.compile(r"Pay by Others", re.I)),
                    lambda: page.locator("li[role='option']").filter(has_text=re.compile(r"Pay by Others", re.I)).first,
                    lambda: page.locator("p-dropdownitem").filter(has_text=re.compile(r"Pay by Others", re.I)).first,
                    lambda: page.locator("xpath=//*[normalize-space()='Pay by Others']").last,
                    lambda: page.get_by_text("Pay by Others", exact=True).last,
                ],
                timeout=5000,
            )

            if pay_by_others_option is None:
                open_get_payment_dropdown(page)
                continue

            pay_by_others_option.scroll_into_view_if_needed(timeout=3000)
            pay_by_others_option.click(timeout=5000)

            page.wait_for_timeout(1000)

            print("[Payment] Pay by Others selected.")
            return

        except Exception as error:
            print(f"[Payment] Pay by Others selection failed on attempt {attempt}: {error}")

            page.keyboard.press("Escape")
            page.wait_for_timeout(500)
            open_get_payment_dropdown(page)

    page.screenshot(
        path="reports/artifacts/pay_by_others_selection_failed.png",
        full_page=True,
    )

    raise AssertionError("Could not select Pay by Others from Get Payment dropdown.")



def select_random_other_payment_mode(page: Page) -> str:
    """
    In Pay by Others popup, select a random payment mode from Select mode dropdown.
    """

    payment_dialog = page.get_by_role("dialog").filter(
        has_text=re.compile(r"Select mode|Payment Note|Pay", re.I)
    ).last

    expect(payment_dialog).to_be_visible(timeout=DEFAULT_TIMEOUT)

    click_first_visible(
        page,
        [
            lambda: payment_dialog.get_by_role("combobox", name=re.compile(r"Select mode", re.I)),
            lambda: payment_dialog.locator("p-dropdown").filter(has_text=re.compile(r"Select mode", re.I)).locator(".p-dropdown-trigger").first,
            lambda: payment_dialog.locator(".p-dropdown-trigger").first,
            lambda: payment_dialog.get_by_role("button", name=re.compile(r"dropdown trigger", re.I)).first,
        ],
        "Select mode dropdown",
    )

    page.wait_for_timeout(500)

    option_locators = [
        page.locator("li[role='option']").filter(
            has_text=re.compile(r"Debit Card|Credit Card|UPI|Cheque|Bank|NEFT|RTGS|IMPS|Other", re.I)
        ),
        page.locator("p-dropdownitem").filter(
            has_text=re.compile(r"Debit Card|Credit Card|UPI|Cheque|Bank|NEFT|RTGS|IMPS|Other", re.I)
        ),
    ]

    visible_options = []

    for option_group in option_locators:
        count = option_group.count()

        for index in range(count):
            option = option_group.nth(index)

            if option.is_visible():
                text = normalize_text(option.inner_text(timeout=3000))

                if text and "select" not in text.lower():
                    visible_options.append((text, option))

    if not visible_options:
        raise AssertionError("No payment mode options were visible in Select mode dropdown.")

    selected_text, selected_option = random.choice(visible_options)

    selected_option.click(timeout=5000)

    page.wait_for_timeout(500)

    print(f"[Payment] Other payment mode selected: {selected_text}")

    return selected_text


# ***** Order created with only taxable items; GST applies correctly on all items *****

def complete_taxable_items_order_invoice_flow(page: Page, config, consumer_profile: dict) -> dict:
    """
    Order created with only taxable items; GST applies correctly on all items.

    Items:
    - Item_4: GST 18%
    - Item_1: GST 5% + CESS 1%
    """

    select_first_business_if_needed(page)

    close_blocking_dialog_if_present(page)

    open_sales_order_dashboard(page)

    ensure_store_is_bnb_stores(page)
    open_create_order_popup(page)

    customer_name = create_new_customer_from_profile(page, consumer_profile)

    select_sale_catalog_and_go_next(page)

    add_item_4_from_select_item_popup(page)
    add_item_1_from_search(page)

    add_order_note(page, "Notes to customer")
    add_order_note(page, "Notes from seller")

    confirm_order(page)

    create_invoice(page)
    view_invoice(page)

    taxable_tax_result = verify_taxable_invoice_all_items(page)

    invoice_total_result = verify_invoice_totals(page)

    payment_result = complete_random_invoice_payment(page)

    go_back_to_order_details(page)

    order_completed = complete_order(page)

    return {
        "customer_name": customer_name,
        "taxable_tax_result": taxable_tax_result,
        "invoice_total_result": invoice_total_result,
        "payment_completed": payment_result,
        "order_completed": order_completed,
        "final_url": page.url,
    }

    # Item_1 helper
    
def add_item_1_from_search(page: Page) -> dict:
    """
    Search 'it', select Item_1, select any available colour, then click Select Item.

    Expected colours:
    - Red
    - Blue
    - Green
    """

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
        raise AssertionError("Search items field was not found for Item_1.")

    search_box.click()
    search_box.fill("it")

    click_first_visible(
        page,
        [
            lambda: page.get_by_text("Item_1", exact=True),
            lambda: page.locator("xpath=//*[normalize-space()='Item_1']").first,
        ],
        "Item_1 search result",
    )

    selected_colour = select_random_item_colour(
        page=page,
        colours=["Red", "Blue", "Green"],
        item_name="Item_1",
    )

    click_select_item_button(page)

    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(1000)

    print(f"[Item] Item_1 selected with colour: {selected_colour}")

    return {
        "item_name": "Item_1",
        "colour": selected_colour,
    }


    # taxable invoice verification

def verify_taxable_invoice_all_items(page: Page) -> dict:
    """
    Verify taxable invoice:

    Item_4:
    - GST 18%
    - No CESS

    Item_1:
    - GST 5%
    - CESS 1%

    Tax-inclusive formula:
    taxableAmount = totalAmount * 100 / (100 + gstPercentage + cessPercentage)
    """

    if "/salesorder/invoice/" not in page.url:
        raise AssertionError(
            "Taxable invoice validation started before invoice details page opened. "
            f"Current URL: {page.url}"
        )

    item_4_row = get_invoice_row_data(page, "Item_4")
    item_1_row = get_invoice_row_data(page, "Item_1")

    item_4_result = calculate_tax_inclusive_item_split(
        item_name="Item_4",
        row_data=item_4_row,
        gst_percentage=Decimal("18"),
        cess_percentage=Decimal("0"),
    )

    item_1_result = calculate_tax_inclusive_item_split(
        item_name="Item_1",
        row_data=item_1_row,
        gst_percentage=Decimal("5"),
        cess_percentage=Decimal("1"),
    )

    expected_total_gst = round_money(
            item_4_result["gst_expected"] + item_1_result["gst_expected"]
        )

        # Invoice summary splits total GST into CGST and SGST.
        # Do not sum already-rounded item-level CGST/SGST values.
    expected_total_cgst = round_money(expected_total_gst / Decimal("2"))
    expected_total_sgst = round_money(expected_total_gst / Decimal("2"))

    expected_total_cess = round_money(
            item_4_result["cess_expected"] + item_1_result["cess_expected"]
        )

    summary_cgst_actual = read_tax_component_amount(page, "CGST")
    summary_sgst_actual = read_tax_component_amount(page, "SGST")
    summary_cess_actual = read_tax_component_amount(page, "CESS")

    assert_amount_close(
        actual=summary_cgst_actual,
        expected=expected_total_cgst,
        label="Invoice Summary CGST",
    )

    assert_amount_close(
        actual=summary_sgst_actual,
        expected=expected_total_sgst,
        label="Invoice Summary SGST",
    )

    assert_amount_close(
        actual=summary_cess_actual,
        expected=expected_total_cess,
        label="Invoice Summary CESS",
    )

    item_total_sum = round_money(item_4_row["total_amount"] + item_1_row["total_amount"])

    net_total_with_tax = read_amount_by_label(
        page,
        ["Net Total With Tax", "Net Total with Tax", "Total With Tax"],
        required=True,
        use_last=True,
    )

    assert_amount_close(
        actual=net_total_with_tax,
        expected=item_total_sum,
        label="Taxable Invoice Net Total With Tax",
    )

    print("[Taxable Invoice] GST/CGST/SGST/CESS calculations are correct.")
    print(f"[Taxable Invoice] Item_4 result: {item_4_result}")
    print(f"[Taxable Invoice] Item_1 result: {item_1_result}")
    print(f"[Taxable Invoice] Summary CGST actual={summary_cgst_actual}, expected={expected_total_cgst}")
    print(f"[Taxable Invoice] Summary SGST actual={summary_sgst_actual}, expected={expected_total_sgst}")
    print(f"[Taxable Invoice] Summary CESS actual={summary_cess_actual}, expected={expected_total_cess}")

    return {
        "item_4_result": item_4_result,
        "item_1_result": item_1_result,
        "summary_total_gst_expected": expected_total_gst,
        "summary_cgst_actual": summary_cgst_actual,
        "summary_cgst_expected": expected_total_cgst,
        "summary_sgst_actual": summary_sgst_actual,
        "summary_sgst_expected": expected_total_sgst,
        "summary_cess_actual": summary_cess_actual,
        "summary_cess_expected": expected_total_cess,
        "net_total_with_tax": net_total_with_tax,
        "item_total_sum": item_total_sum,
    }



#   ------ inclusive tax calculation helper ------

def calculate_tax_inclusive_item_split(
    item_name: str,
    row_data: dict,
    gst_percentage: Decimal,
    cess_percentage: Decimal = Decimal("0"),
) -> dict:
    """
    Calculate inclusive tax split for one item.

    taxableAmount = totalAmount * 100 / (100 + gstPercentage + cessPercentage)

    GST amount = taxableAmount * gstPercentage / 100
    CGST = GST / 2
    SGST = GST / 2
    CESS = taxableAmount * cessPercentage / 100
    """

    total_amount = row_data["total_amount"]

    total_tax_percentage = gst_percentage + cess_percentage

    taxable_expected = round_money(
        total_amount * Decimal("100") / (Decimal("100") + gst_percentage + cess_percentage)
    )

    gst_expected = round_money(taxable_expected * gst_percentage / Decimal("100"))
    cess_expected = round_money(taxable_expected * cess_percentage / Decimal("100"))

    cgst_expected = round_money(gst_expected / Decimal("2"))
    sgst_expected = round_money(gst_expected / Decimal("2"))

    total_tax_expected = round_money(gst_expected + cess_expected)

    row_gst_actual = row_data.get("gst_amount", Decimal("0.00"))
    row_cess_actual = row_data.get("cess_amount", Decimal("0.00"))
    row_net_total_actual = row_data.get("net_total")

    assert_amount_close(
        actual=row_net_total_actual,
        expected=taxable_expected,
        label=f"{item_name} Taxable / Net Total",
    )

    assert_amount_close(
        actual=row_gst_actual,
        expected=gst_expected,
        label=f"{item_name} GST",
    )

    if cess_percentage > Decimal("0"):
        assert_amount_close(
            actual=row_cess_actual,
            expected=cess_expected,
            label=f"{item_name} CESS",
        )

    print(f"[Taxable Item] {item_name} total inclusive amount: {total_amount}")
    print(f"[Taxable Item] {item_name} taxable expected: {taxable_expected}")
    print(f"[Taxable Item] {item_name} GST actual={row_gst_actual}, expected={gst_expected}")
    print(f"[Taxable Item] {item_name} CGST expected={cgst_expected}")
    print(f"[Taxable Item] {item_name} SGST expected={sgst_expected}")
    print(f"[Taxable Item] {item_name} CESS actual={row_cess_actual}, expected={cess_expected}")

    return {
        "item": item_name,
        "total_amount": total_amount,
        "gst_percentage": gst_percentage,
        "cess_percentage": cess_percentage,
        "taxable_expected": taxable_expected,
        "gst_actual": row_gst_actual,
        "gst_expected": gst_expected,
        "cess_actual": row_cess_actual,
        "cess_expected": cess_expected,
        "cgst_expected": cgst_expected,
        "sgst_expected": sgst_expected,
        "total_tax_expected": total_tax_expected,
        "row_data": row_data,
    }


#   ------- Random payment helper ------

def complete_random_invoice_payment(page: Page) -> bool:
    """
    Randomly complete invoice payment using:
    - Pay by Cash
    - Pay by Others
    """

    payment_type = random.choice(["cash", "others"])

    print(f"[Payment] Random payment type selected: {payment_type}")

    if payment_type == "cash":
        return complete_cash_payment(page)

    return complete_other_payment(page)



def complete_mixed_taxable_exempt_order_invoice_flow(
    page: Page,
    config,
    consumer_profile: dict,
) -> dict:
    """
    Order created with taxable and exempt items; tax breakup shows correct segregation.

    Customer is selected randomly:
    - Existing customer Jisha Sreejith
    - New random customer

    Taxable:
    - Item_4: GST 18%
    - Item_1: GST 5% + CESS 1%

    Exempt:
    - Item_6: GST 5%, but exempt
    - Item_2: GST 5% + CESS 1%, but exempt
    """

    select_first_business_if_needed(page)

    close_blocking_dialog_if_present(page)

    open_sales_order_dashboard(page)

    ensure_store_is_bnb_stores(page)
    open_create_order_popup(page)

    customer_type = random.choice(["existing", "new"])

    print(f"[Customer] Random customer type selected: {customer_type}")

    if customer_type == "existing":
        customer_selected = select_existing_order_consumer(
            page=page,
            search_text="8281",
            consumer_text="Jisha Sreejith",
        )
        customer_name = "Jisha Sreejith"

    else:
        customer_name = create_new_customer_from_profile(page, consumer_profile)
        customer_selected = True

    select_sale_catalog_and_go_next(page)

    add_item_4_from_select_item_popup(page)

    add_item_1_from_search(page)

    add_item_6_from_search(page)

    add_item_2_with_random_colour(page)

    add_order_note(page, "Notes to customer")
    add_order_note(page, "Notes from seller")

    confirm_order(page)

    create_invoice(page)
    view_invoice(page)

    mixed_tax_result = verify_mixed_taxable_exempt_invoice_tax_breakup(page)

    invoice_total_result = verify_invoice_totals(page)

    payment_result = complete_random_invoice_payment(page)

    go_back_to_order_details(page)

    order_completed = complete_order(page)

    return {
        "customer_type": customer_type,
        "customer_selected": customer_selected,
        "customer_name": customer_name,
        "mixed_tax_result": mixed_tax_result,
        "invoice_total_result": invoice_total_result,
        "payment_completed": payment_result,
        "order_completed": order_completed,
        "final_url": page.url,
    }



def verify_mixed_taxable_exempt_invoice_tax_breakup(page: Page) -> dict:
    """
    Verify mixed taxable + exempt invoice.

    Taxable items:
    - Item_4: GST 18%
    - Item_1: GST 5% + CESS 1%

    Exempt items:
    - Item_6: GST should be 0
    - Item_2: GST and CESS should be 0

    Tax summary should include only taxable items.
    """

    if "/salesorder/invoice/" not in page.url:
        raise AssertionError(
            "Mixed taxable/exempt invoice validation started before invoice details page opened. "
            f"Current URL: {page.url}"
        )

    item_4_row = get_invoice_row_data(page, "Item_4")
    item_1_row = get_invoice_row_data(page, "Item_1")
    item_6_row = get_invoice_row_data(page, "Item_6")
    item_2_row = get_invoice_row_data(page, "Item_2")

    item_4_result = calculate_tax_inclusive_item_split(
        item_name="Item_4",
        row_data=item_4_row,
        gst_percentage=Decimal("18"),
        cess_percentage=Decimal("0"),
    )

    item_1_result = calculate_tax_inclusive_item_split(
        item_name="Item_1",
        row_data=item_1_row,
        gst_percentage=Decimal("5"),
        cess_percentage=Decimal("1"),
    )

    item_6_result = assert_exempt_invoice_item_has_no_tax(
        item_name="Item_6",
        row_data=item_6_row,
    )

    item_2_result = assert_exempt_invoice_item_has_no_tax(
        item_name="Item_2",
        row_data=item_2_row,
    )

    expected_total_gst = round_money(
        item_4_result["gst_expected"] + item_1_result["gst_expected"]
    )

    # Invoice summary splits total GST into CGST and SGST.
    # Do not sum already-rounded item-level CGST/SGST values.
    expected_total_cgst = round_money(expected_total_gst / Decimal("2"))
    expected_total_sgst = round_money(expected_total_gst / Decimal("2"))

    expected_total_cess = round_money(
        item_4_result["cess_expected"] + item_1_result["cess_expected"]
    )

    summary_cgst_actual = read_tax_component_amount(page, "CGST")
    summary_sgst_actual = read_tax_component_amount(page, "SGST")
    summary_cess_actual = read_tax_component_amount(page, "CESS")

    assert_amount_close(
        actual=summary_cgst_actual,
        expected=expected_total_cgst,
        label="Mixed Invoice Summary CGST",
    )

    assert_amount_close(
        actual=summary_sgst_actual,
        expected=expected_total_sgst,
        label="Mixed Invoice Summary SGST",
    )

    assert_amount_close(
        actual=summary_cess_actual,
        expected=expected_total_cess,
        label="Mixed Invoice Summary CESS",
    )

    expected_subtotal = round_money(
        item_4_row["net_total"]
        + item_1_row["net_total"]
        + item_6_row["net_total"]
        + item_2_row["net_total"]
    )

    expected_net_total_with_tax = round_money(
        item_4_row["total_amount"]
        + item_1_row["total_amount"]
        + item_6_row["total_amount"]
        + item_2_row["total_amount"]
    )

    subtotal_actual = read_amount_by_label(
        page,
        ["Subtotal", "Sub Total"],
        required=True,
        use_last=True,
    )

    net_total_with_tax_actual = read_amount_by_label(
        page,
        ["Net Total With Tax", "Net Total with Tax", "Total With Tax"],
        required=True,
        use_last=True,
    )

    assert_amount_close(
        actual=subtotal_actual,
        expected=expected_subtotal,
        label="Mixed Invoice Subtotal",
    )

    assert_amount_close(
        actual=net_total_with_tax_actual,
        expected=expected_net_total_with_tax,
        label="Mixed Invoice Net Total With Tax",
    )

    print("[Mixed Invoice] Taxable and exempt tax segregation is correct.")
    print(f"[Mixed Invoice] Item_4 taxable result: {item_4_result}")
    print(f"[Mixed Invoice] Item_1 taxable result: {item_1_result}")
    print(f"[Mixed Invoice] Item_6 exempt result: {item_6_result}")
    print(f"[Mixed Invoice] Item_2 exempt result: {item_2_result}")
    print(f"[Mixed Invoice] Summary CGST actual={summary_cgst_actual}, expected={expected_total_cgst}")
    print(f"[Mixed Invoice] Summary SGST actual={summary_sgst_actual}, expected={expected_total_sgst}")
    print(f"[Mixed Invoice] Summary CESS actual={summary_cess_actual}, expected={expected_total_cess}")
    print(f"[Mixed Invoice] Subtotal actual={subtotal_actual}, expected={expected_subtotal}")
    print(f"[Mixed Invoice] Net Total With Tax actual={net_total_with_tax_actual}, expected={expected_net_total_with_tax}")

    return {
        "item_4_result": item_4_result,
        "item_1_result": item_1_result,
        "item_6_result": item_6_result,
        "item_2_result": item_2_result,
        "summary_total_gst_expected": expected_total_gst,
        "summary_cgst_actual": summary_cgst_actual,
        "summary_cgst_expected": expected_total_cgst,
        "summary_sgst_actual": summary_sgst_actual,
        "summary_sgst_expected": expected_total_sgst,
        "summary_cess_actual": summary_cess_actual,
        "summary_cess_expected": expected_total_cess,
        "subtotal_actual": subtotal_actual,
        "subtotal_expected": expected_subtotal,
        "net_total_with_tax_actual": net_total_with_tax_actual,
        "net_total_with_tax_expected": expected_net_total_with_tax,
    }


def assert_exempt_invoice_item_has_no_tax(item_name: str, row_data: dict) -> dict:
    """
    Verify that an exempt item row has no GST and no CESS.

    This applies even if the item master has GST/CESS configured.
    If the item is exempt in the account/catalog, invoice row tax should be 0.
    """

    gst_amount = row_data.get("gst_amount", Decimal("0.00"))
    cess_amount = row_data.get("cess_amount", Decimal("0.00"))

    if gst_amount != Decimal("0.00"):
        print(
            f"[Tax Error] Exempt item {item_name} has GST. "
            f"GST actual={gst_amount}. Row={row_data}"
        )

    if cess_amount != Decimal("0.00"):
        print(
            f"[Tax Error] Exempt item {item_name} has CESS. "
            f"CESS actual={cess_amount}. Row={row_data}"
        )

    assert_amount_close(
        actual=gst_amount,
        expected=Decimal("0.00"),
        label=f"{item_name} Exempt GST",
    )

    assert_amount_close(
        actual=cess_amount,
        expected=Decimal("0.00"),
        label=f"{item_name} Exempt CESS",
    )

    print(f"[Exempt Item] {item_name} GST=0.00 and CESS=0.00 verified.")

    return {
        "item": item_name,
        "gst_amount": gst_amount,
        "cess_amount": cess_amount,
        "total_amount": row_data["total_amount"],
        "net_total": row_data["net_total"],
        "row_data": row_data,
    }


