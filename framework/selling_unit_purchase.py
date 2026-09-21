import os
import random
import re
import string
from datetime import datetime
from typing import Optional

from playwright.sync_api import Page, expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from framework.test_data import generate_consumer_profile


# Run all tests :- python -m pytest .\tests\test_selling_unit_purchase.py -v -s

# Run Only Purchase :- python -m pytest .\tests\test_selling_unit_purchase.py::test_01_create_and_approve_purchase -v -s
# Run Only Catalog Update :- python -m pytest .\tests\test_selling_unit_purchase.py::test_02_add_purchased_items_to_sales_order_catalog -v -s
# Run Only Order Creation :- python -m pytest .\tests\test_selling_unit_purchase.py::test_03_create_order_for_new_customer -v -s

class SellingUnitPurchaseFlow:

    STORE_NAME = "TT Store"
    VENDOR_NAME = "Madhurai Sweets"
    INVENTORY_CATALOG = "TT Inventory"

    def __init__(self, page: Page):
        self.page = page
        self.selected_item_names = set()
        self.selected_order_items = set()

    def find_parent_item_name(
        self,
        purchased_item_name: str
    ) -> str:

        words = purchased_item_name.strip().split()

        # Try:
        # "Soan Papdi Elaichi"
        # "Soan Papdi"
        # "Soan"
        #
        # For "Gulab Jamun", exact "Gulab Jamun" will be found
        # and therefore it will NOT incorrectly become "Gulab".

        for end_index in range(
            len(words),
            0,
            -1
        ):

            candidate = " ".join(
                words[:end_index]
            )

            row = self.page.get_by_role(
                "row"
            ).filter(
                has_text=re.compile(
                    re.escape(candidate),
                    re.I
                )
            ).first

            if row.count() > 0:

                print(
                    f"Purchased item: "
                    f"{purchased_item_name} | "
                    f"Catalog parent: {candidate}"
                )

                return candidate

        raise AssertionError(
            f"Could not determine catalog parent "
            f"for purchased item "
            f"'{purchased_item_name}'"
        )

    # ============================================================
    # RANDOM DATA
    # ============================================================

    @staticmethod
    def random_bill_number() -> str:
        return str(random.randint(1000, 9999))

    @staticmethod
    def random_quantity() -> int:
        return random.randint(1, 10)

    @staticmethod
    def random_mrp() -> int:
        return random.randint(100, 500)

    @staticmethod
    def random_purchase_price(mrp: int) -> int:
        return random.randint(max(1, int(mrp * 0.60)), mrp - 1)

    @staticmethod
    def random_batch_number() -> str:
        letters = "".join(random.choices(string.ascii_uppercase, k=3))
        numbers = random.randint(100, 999)
        return f"{letters}{numbers}"

    # ============================================================
    # LOGIN
    # ============================================================

    def login(self) -> None:

        provider_url = os.getenv(
            "SCALE_PROVIDER_URL",
            "https://scale.jaldee.com/business/login"
        )

        login_id = os.getenv(
            "SCALE_SALESORDER_LOGIN_ID"
        )

        password = os.getenv(
            "SCALE_SALESORDER_PASSWORD"
        )

        assert login_id, (
            "SCALE_SALESORDER_LOGIN_ID "
            "is missing from .env"
        )

        assert password, (
            "SCALE_SALESORDER_PASSWORD "
            "is missing from .env"
        )

        print(
            f"Opening provider application: "
            f"{provider_url}"
        )

        self.page.goto(
            provider_url
        )

        self.page.wait_for_load_state(
            "domcontentloaded"
        )

        self.page.wait_for_timeout(
            500
        )

        print(
            f"Current URL after navigation: "
            f"{self.page.url}"
        )

        # ---------------------------------------------------------
        # CHECK IF USER IS ALREADY LOGGED IN
        #
        # When an authenticated browser opens /business/login,
        # the application redirects directly to the business app.
        # ---------------------------------------------------------

        sales_order_sidebar = self.page.locator(
            'a[href*="/business/salesorder/dashboard"]'
        )

        inventory_sidebar = self.page.locator(
            'a[href*="/business/salesorder/inventory"]'
        )

        welcome_text = self.page.get_by_text(
            re.compile(
                r"Welcome back",
                re.I
            )
        )

        already_logged_in = (
            sales_order_sidebar.count() > 0
            or inventory_sidebar.count() > 0
            or welcome_text.count() > 0
        )

        if already_logged_in:

            print(
                "Existing authenticated session found. "
                "Login not required."
            )

            return

        # ---------------------------------------------------------
        # LOGIN FORM
        # ---------------------------------------------------------

        login_input = self.page.get_by_role(
            "textbox",
            name="Enter Login ID"
        )

        expect(
            login_input
        ).to_be_visible(
            timeout=20_000
        )

        print(
            "Login page opened. "
            "Entering credentials."
        )

        login_input.fill(
            login_id
        )

        password_input = self.page.get_by_role(
            "textbox",
            name="Enter password"
        )

        expect(
            password_input
        ).to_be_visible(
            timeout=10_000
        )

        password_input.fill(
            password
        )

        sign_in = self.page.get_by_role(
            "button",
            name="Sign In"
        )

        expect(
            sign_in
        ).to_be_visible(
            timeout=10_000
        )

        expect(
            sign_in
        ).to_be_enabled()

        sign_in.click()

        # ---------------------------------------------------------
        # VERIFY AUTHENTICATED APPLICATION
        # ---------------------------------------------------------

        self.page.wait_for_load_state(
            "domcontentloaded"
        )

        sales_order_sidebar = self.page.locator(
            'a[href*="/business/salesorder/dashboard"]'
        )

        expect(
            sales_order_sidebar.first
        ).to_be_visible(
            timeout=30_000
        )

        print(
            "Login completed successfully"
        )

        print(
            f"Authenticated URL: "
            f"{self.page.url}"
        )


    # ============================================================
    # INVENTORY NAVIGATION
    # ============================================================

    def open_inventory_management(self) -> None:

        print(
            f"Current page before Inventory Management: "
            f"{self.page.url}"
            )

        print("Opening Inventory Management from side panel")

        # ---------------------------------------------------------
        # BEST LOCATOR:
        # Inventory Management sidebar link
        # ---------------------------------------------------------

        inventory_link = self.page.locator(
            'a[href*="/business/salesorder/inventory"]'
        )

        expect(
            inventory_link.first
        ).to_be_visible(
            timeout=20_000
        )

        inventory_link.first.click()

        # ---------------------------------------------------------
        # VERIFY INVENTORY DASHBOARD
        # ---------------------------------------------------------

        expect(
            self.page
        ).to_have_url(
            re.compile(
                r"/business/salesorder/inventory"
            ),
            timeout=20_000
        )

        print(
            f"Opened Inventory Management dashboard: "
            f"{self.page.url}"
        )



    def open_purchase_tab(self) -> None:

        purchase = self.page.get_by_text(
            "Purchase",
            exact=True
        )

        expect(purchase.first).to_be_visible(timeout=20_000)
        purchase.first.click()

        expect(
            self.page.get_by_role(
                "button",
                name=re.compile(r"Create", re.I)
            ).last
        ).to_be_visible(timeout=20_000)

    def click_create_purchase(self) -> None:

        create_button = self.page.get_by_role(
            "button",
            name=re.compile(r"Create", re.I)
        )

        expect(create_button.last).to_be_visible()
        create_button.last.click()

        expect(
            self.page.get_by_text(
                re.compile(r"Create Purchase", re.I)
            ).first
        ).to_be_visible(timeout=20_000)

    # ============================================================
    # PURCHASE HEADER
    # ============================================================

    def select_store(self) -> None:

        # Store may already be selected if only one store exists.
        store_dropdown = self.page.get_by_text(
            "Select Store",
            exact=True
        )

        if store_dropdown.count() == 0:
            return

        try:
            store_dropdown.first.click()

            option = self.page.get_by_role(
                "option",
                name=self.STORE_NAME
            )

            if option.count() > 0:
                option.first.click()

        except Exception:
            # Store may already be automatically populated.
            pass

    def select_vendor(self) -> None:

        vendor_dropdown = self.page.get_by_text(
            re.compile(r"Select Vendor")
        )

        expect(vendor_dropdown.first).to_be_visible()
        vendor_dropdown.first.click()

        vendor = self.page.get_by_text(
            self.VENDOR_NAME,
            exact=True
        )

        expect(vendor.last).to_be_visible()
        vendor.last.click()

    def select_inventory_catalog(self) -> None:

        catalog_dropdown = self.page.get_by_text(
            re.compile(r"Select Inventory Catalog|Select Catalog")
        )

        expect(catalog_dropdown.last).to_be_visible()
        catalog_dropdown.last.click()

        catalog_option = self.page.get_by_role(
            "option",
            name=self.INVENTORY_CATALOG
        )

        if catalog_option.count() > 0:
            catalog_option.first.click()
        else:
            self.page.get_by_text(
                self.INVENTORY_CATALOG,
                exact=True
            ).last.click()

    def enter_purchase_bill_number(self) -> str:

        bill_number = self.random_bill_number()

        bill_input = self.page.get_by_role(
            "textbox",
            name=re.compile(r"Enter Purchase Bill")
        )

        expect(bill_input).to_be_visible()
        bill_input.fill(bill_number)

        return bill_number

    def select_today_as_bill_date(self) -> None:

        calendar = self.page.locator("#selectCal_ORD_PurchsCrt")

        expect(calendar).to_be_visible()

        calendar.get_by_role("textbox").click()

        today = str(datetime.now().day)

        today_element = self.page.locator(
            ".p-datepicker-today"
        ).get_by_text(today, exact=True)

        if today_element.count() > 0:
            today_element.first.click()
        else:
            self.page.locator(
                ".p-datepicker-calendar"
            ).get_by_text(
                today,
                exact=True
            ).first.click()


    # ============================================================
    # ITEM SELECTION
    # ============================================================

    def open_add_items_popup(self) -> None:

        button = self.page.get_by_role(
            "button",
            name=re.compile(r"Add Items", re.I)
        )

        expect(button).to_be_visible()
        button.click()



    def select_random_item(self) -> str:

        # Open Select Items popup
        self.open_add_items_popup()

        # Wait for popup
        popup = self.page.get_by_role("dialog").filter(
            has_text="Select Items"
        )

        expect(popup).to_be_visible(
            timeout=15_000
        )

        # Wait until at least one item row is available
        expect(
            popup.get_by_role("row").nth(1)
        ).to_be_visible(
            timeout=15_000
        )

        rows = popup.get_by_role("row")

        available_items = []

        # Skip first row because it is table header
        for index in range(1, rows.count()):

            row = rows.nth(index)

            cells = row.get_by_role("cell")

            if cells.count() < 2:
                continue

            # second cell contains Item Name
            item_name = cells.nth(1).inner_text().strip()

            if not item_name:
                continue

            # Do not choose previously selected item
            if item_name in self.selected_item_names:
                continue

            available_items.append(
                {
                    "item_name": item_name,
                    "row": row,
                }
            )

        if not available_items:
            raise AssertionError(
                "No different item available for second purchase item. "
                f"Already selected: {self.selected_item_names}"
            )

        # Select random different item
        selected_item = random.choice(
            available_items
        )

        item_name = selected_item["item_name"]
        row = selected_item["row"]

        print(
            f"Selecting purchase item: {item_name}"
        )

        # ---------------------------------------------------------
        # Click radio button in selected row
        # ---------------------------------------------------------

        radio = row.get_by_role("radio")

        expect(radio).to_be_visible(
            timeout=10_000
        )

        radio.click()

        expect(radio).to_be_checked()

        # ---------------------------------------------------------
        # Click Done
        # ---------------------------------------------------------

        done_button = popup.get_by_role(
            "button",
            name=re.compile(r"Done", re.I)
        )

        expect(done_button).to_be_visible()
        expect(done_button).to_be_enabled()

        done_button.click()

        # Handle attribute popup if applicable
        self.handle_attribute_popup_if_present()

        # Store selected item
        self.selected_item_names.add(
            item_name
        )

        print(
            f"Selected purchase item: {item_name}"
        )

        return item_name


    def handle_attribute_popup_if_present(self) -> None:
        """
        Some inventory items have attributes.

        Example:
            Item
              -> attribute popup
              -> choose one variant
              -> Done

        If no attribute popup appears, this method simply returns.
        """

        self.page.wait_for_timeout(500)

        dialogs = self.page.locator(
            ".p-dialog:visible"
        )

        if dialogs.count() == 0:
            return

        dialog = dialogs.last

        dialog_text = dialog.inner_text().lower()

        if (
            "attribute" not in dialog_text
            and "select item" not in dialog_text
        ):
            return

        controls = dialog.locator(
            'input[type="radio"]:visible, '
            'input[type="checkbox"]:visible'
        )

        if controls.count() == 0:
            return

        index = random.randint(
            0,
            controls.count() - 1
        )

        controls.nth(index).check()

        done = dialog.get_by_role(
            "button",
            name=re.compile(r"Done", re.I)
        )

        if done.count() > 0:
            done.click()

    # ============================================================
    # PURCHASE ITEM DETAILS
    # ============================================================

    def fill_batch_if_present(self) -> str | None:

        batch_input = self.page.locator(
            "#inputBatch_ORD_PurchsCrt"
        )

        if batch_input.count() == 0:
            return None

        if not batch_input.is_visible():
            return None

        batch_number = self.random_batch_number()

        batch_input.fill(batch_number)

        return batch_number
    

    def fill_quantity(self) -> int:

        quantity = self.random_quantity()

        quantity_input = self.page.locator(
            "#inputNumber_ORD_PurchsCrt"
        )

        expect(quantity_input).to_be_visible()

        quantity_input.fill(str(quantity))

        return quantity

    def select_future_expiry_date_if_present(
        self,
        has_batch: bool
    ) -> None:

        if not has_batch:
            return

        calendar_inputs = self.page.locator(
            ".p-calendar:visible input:visible"
        )

        if calendar_inputs.count() == 0:
            raise AssertionError(
                "Batch item found, but expiry date field is not available"
            )

        expiry_input = calendar_inputs.last
        expiry_input.click()

        datepicker = self.page.locator(
            ".p-datepicker:visible"
        )

        expect(datepicker).to_be_visible()

        purchase_date = datetime.now()

        target_month = purchase_date.month + 2
        target_year = purchase_date.year

        if target_month > 12:
            target_month -= 12
            target_year += 1

        expected_month = datetime(
            target_year,
            target_month,
            1
        ).strftime("%B")

        expected_year = str(target_year)

        print(
            f"Purchase month: {purchase_date.strftime('%B %Y')} | "
            f"Expiry month: {expected_month} {expected_year}"
        )

        next_button = datepicker.locator(
            ".p-datepicker-next"
        )

        for _ in range(2):
            next_button.click()
            self.page.wait_for_timeout(300)

        month_text = datepicker.locator(
            ".p-datepicker-month"
        )

        year_text = datepicker.locator(
            ".p-datepicker-year"
        )

        if month_text.count() > 0:
            expect(month_text).to_have_text(
                re.compile(expected_month, re.I)
            )

        if year_text.count() > 0:
            expect(year_text).to_have_text(
                expected_year
            )

        # Select an actual clickable date cell
        valid_date_cells = datepicker.locator(
            "td:not(.p-datepicker-other-month)"
        ).filter(
            has=self.page.locator(
                "span:not(.p-disabled)"
            )
        )

        count = valid_date_cells.count()

        if count == 0:
            raise AssertionError(
                f"No enabled expiry date found in "
                f"{expected_month} {expected_year}"
            )

        random_index = random.randint(
            0,
            count - 1
        )

        valid_date_cells.nth(
            random_index
        ).click()


    def fill_prices(self) -> tuple[int, int]:

        mrp = self.random_mrp()

        purchase_price = self.random_purchase_price(
            mrp
        )

        mrp_input = self.page.locator(
            "#inputMrp_ORD_PurchsCrt"
        )

        purchase_input = self.page.locator(
            "#inputPrice_ORD_PurchsCrt"
        )

        expect(mrp_input).to_be_visible()
        expect(purchase_input).to_be_visible()

        mrp_input.fill(str(mrp))
        purchase_input.fill(str(purchase_price))

        return mrp, purchase_price

    def add_current_item(self) -> None:

        add_button = self.page.get_by_role(
            "button",
            name="Add",
            exact=True
        )

        expect(add_button).to_be_enabled()

        add_button.click()

        self.page.wait_for_timeout(500)

    # ============================================================
    # COMPLETE ONE ITEM
    # ============================================================

    def add_random_purchase_item(self) -> dict:

        item_name = self.select_random_item()

        batch = self.fill_batch_if_present()

        quantity = self.fill_quantity()

        self.select_future_expiry_date_if_present(
            has_batch=batch is not None
        )

        mrp, purchase_price = self.fill_prices()

        self.add_current_item()

        return {
            "item_name": item_name,
            "batch": batch,
            "quantity": quantity,
            "mrp": mrp,
            "purchase_price": purchase_price,
        }
    # ============================================================
    # TOAST ASSERTION
    # ============================================================

    def assert_success_message(
        self,
        expected_pattern: str = r"success|created|saved|approved"
    ) -> str:

        toast = self.page.locator(
            ".p-toast-message:visible"
        ).last

        expect(toast).to_be_visible(
            timeout=15_000
        )

        message = toast.inner_text()

        assert re.search(
            expected_pattern,
            message,
            re.I
        ), (
            f"Unexpected message received: {message}"
        )

        return message

    # ============================================================
    # CREATE PURCHASE
    # ============================================================

    def create_purchase(self) -> None:

        create_button = self.page.get_by_role(
            "button",
            name="Create Purchase",
            exact=True
        )

        expect(create_button).to_be_visible()
        expect(create_button).to_be_enabled()

        create_button.click()

        messages = self.assert_and_wait_for_success_messages(
            expected_messages=[
                "Purchase created successfully"
            ]
        )

        print(
            f"Create purchase messages: {messages}"
        )

    # ============================================================
    # SEND TO REVIEW
    # ============================================================

    def send_to_review(self) -> None:

        send_to_review_button = self.page.get_by_role(
            "button",
            name=re.compile(
                r"Send.*Review",
                re.I
            )
        )

        expect(
            send_to_review_button
        ).to_be_visible(
            timeout=20_000
        )

        expect(
            send_to_review_button
        ).to_be_enabled()

        send_to_review_button.click()

        messages = self.assert_and_wait_for_success_messages(
            expected_messages=[
                "Purchase status changed successfully"
            ]
        )

        print(
            f"Send to review messages: {messages}"
        )

        # Wait until the Purchases grid page is loaded
        expect(
            self.page.get_by_text(
                re.compile(
                    r"Purchases \(\d+\)",
                    re.I
                )
            )
        ).to_be_visible(
            timeout=20_000
        )

    def assert_and_wait_for_success_messages(
        self,
        expected_messages: list[str] | None = None,
        timeout_ms: int = 20_000,
    ) -> list[str]:

        collected_messages = []

        # Give the toast time to appear
        self.page.wait_for_timeout(300)

        elapsed = 0
        interval = 250
        no_toast_time = 0

        while elapsed < timeout_ms:

            # evaluate_all() takes a snapshot of currently matching elements.
            # It does not keep waiting on an element that disappeared.
            messages = self.page.locator(
                ".p-toast-message:visible"
            ).evaluate_all(
                """
                elements => elements
                    .map(el => el.innerText.trim())
                    .filter(text => text.length > 0)
                """
            )

            if messages:

                no_toast_time = 0

                for message in messages:

                    if message not in collected_messages:
                        collected_messages.append(message)

                        print(
                            f"Success message: {message}"
                        )

            else:

                no_toast_time += interval

                # No toast for 1 second means the toast sequence
                # has most likely completed.
                if (
                    collected_messages
                    and no_toast_time >= 1000
                ):
                    break

            self.page.wait_for_timeout(interval)

            elapsed += interval

        # ---------------------------------------------------------
        # Assert expected messages, if supplied
        # ---------------------------------------------------------

        if expected_messages:

            combined_messages = " | ".join(
                collected_messages
            )

            for expected_message in expected_messages:

                assert expected_message.lower() in combined_messages.lower(), (
                    f"Expected success message "
                    f"'{expected_message}' was not found. "
                    f"Actual messages: {collected_messages}"
                )

        return collected_messages


    # ============================================================
    # APPROVE PURCHASE
    # ============================================================

    def approve_latest_purchase_from_grid(self) -> None:

        # ---------------------------------------------------------
        # Wait until Purchases grid is fully loaded
        # ---------------------------------------------------------

        expect(
            self.page.get_by_text(
                re.compile(r"Purchases \(\d+\)", re.I)
            )
        ).to_be_visible(
            timeout=20_000
        )

        # Make sure no success toast is blocking the grid
        self.assert_and_wait_for_success_messages()

        # ---------------------------------------------------------
        # First tbody row = latest purchase
        # ---------------------------------------------------------

        latest_purchase_row = self.page.locator(
            "table tbody tr"
        ).first

        expect(
            latest_purchase_row
        ).to_be_visible(
            timeout=20_000
        )

        row_text = latest_purchase_row.inner_text()

        print("Latest purchase:")
        print(row_text)

        # ---------------------------------------------------------
        # Latest purchase must be IN REVIEW
        # ---------------------------------------------------------

        expect(
            latest_purchase_row.get_by_text(
                "IN REVIEW",
                exact=True
            )
        ).to_be_visible()

        # ---------------------------------------------------------
        # Click blue Approve button
        # ---------------------------------------------------------

        approve_button = latest_purchase_row.get_by_role(
            "button",
            name=re.compile(r"Approve", re.I)
        )

        expect(
            approve_button
        ).to_be_visible()

        expect(
            approve_button
        ).to_be_enabled()

        print(
            "Clicking blue Approve button "
            "for latest purchase"
        )

        approve_button.click()

        # ---------------------------------------------------------
        # Verify navigation away from purchase grid
        # ---------------------------------------------------------

        expect(
            approve_button
        ).not_to_be_visible(
            timeout=20_000
        )

        # Give details page time to render
        self.page.wait_for_load_state(
            "domcontentloaded"
        )

        # ---------------------------------------------------------
        # Find final green Approve button
        # ---------------------------------------------------------

        final_approve_button = self.page.get_by_role(
            "button",
            name="Approve",
            exact=True
        )

        expect(
            final_approve_button.last
        ).to_be_visible(
            timeout=20_000
        )

        expect(
            final_approve_button.last
        ).to_be_enabled()

        print(
            "Clicking final green Approve button"
        )

        final_approve_button.last.click()

        # ---------------------------------------------------------
        # Assert approval success messages
        # ---------------------------------------------------------

        messages = self.assert_and_wait_for_success_messages()

        print(
            f"Purchase approval messages: {messages}"
        )

        # ---------------------------------------------------------
        # Purchase grid should appear again
        # ---------------------------------------------------------

        expect(
            self.page.get_by_text(
                re.compile(r"Purchases \(\d+\)", re.I)
            )
        ).to_be_visible(
            timeout=20_000
        )



    # ============================================================
    # TEST FLOW 1
    # CREATE + APPROVE PURCHASE
    # ============================================================   

    def create_and_approve_purchase(
        self,
        number_of_items: int = 2,
    ) -> dict:
        """
        Create and approve a purchase.

        Returns:
            {
                "bill_number": ...,
                "items": [...]
            }
        """

        self.selected_item_names.clear()

        self.login()

        self.open_inventory_management()

        self.open_purchase_tab()

        self.click_create_purchase()

        self.select_store()

        self.select_vendor()

        self.select_inventory_catalog()

        bill_number = self.enter_purchase_bill_number()

        self.select_today_as_bill_date()

        purchased_items = []

        for _ in range(number_of_items):
            item_data = self.add_random_purchase_item()
            purchased_items.append(item_data)

        self.create_purchase()

        self.send_to_review()

        self.approve_latest_purchase_from_grid()

        print("\n============================================")
        print("PURCHASE TEST COMPLETED")
        print("============================================")

        print(
            f"Bill Number      : {bill_number}"
        )

        for item in purchased_items:
            print(
                f"Purchased Item   : {item['item_name']} | "
                f"Qty: {item['quantity']} | "
                f"Batch: {item['batch']} | "
                f"MRP: {item['mrp']} | "
                f"Purchase Price: {item['purchase_price']}"
            )

        return {
            "bill_number": bill_number,
            "items": purchased_items,
        }



    def add_purchased_items_to_sales_order_catalog(
        self,
        purchase_result: dict,
        ) -> dict:

        purchased_items = purchase_result["items"]

        if not purchased_items:
            raise AssertionError(
                "No purchased items were supplied."
            )

        self.update_purchased_items_in_sales_catalog(
            purchased_items
        )

        return {
            "bill_number": purchase_result["bill_number"],
            "items": purchased_items,
            "catalog_updated": True,
        }
    

    def add_latest_purchase_items_to_sales_order_catalog(
        self
    ) -> dict:

        print(
            "Getting latest purchased items "
            "from Purchase Details"
        )

        # ---------------------------------------------------------
        # LOGIN
        # ---------------------------------------------------------

        self.login()

        # ---------------------------------------------------------
        # INVENTORY MANAGEMENT
        # ---------------------------------------------------------

        self.open_inventory_management_dashboard()

        # ---------------------------------------------------------
        # PURCHASE CARD
        # ---------------------------------------------------------

        self.open_purchase_from_inventory_dashboard()

        # ---------------------------------------------------------
        # LATEST PURCHASE
        # ---------------------------------------------------------

        self.open_latest_purchase_details()

        # ---------------------------------------------------------
        # CAPTURE PURCHASED ITEMS
        # ---------------------------------------------------------

        purchased_items = (
            self.capture_items_from_latest_purchase()
        )

        if not purchased_items:
            raise AssertionError(
                "No purchased items found "
                "in latest purchase."
            )

        print(
            f"Latest purchased items: "
            f"{purchased_items}"
        )

        # ---------------------------------------------------------
        # SALES ORDER DASHBOARD
        # ---------------------------------------------------------

        self.open_sales_order_dashboard()

        # ---------------------------------------------------------
        # SALES ORDER CATALOG
        # ---------------------------------------------------------

        self.open_sales_order_catalog()

        self.open_first_sales_order_catalog()

        # ---------------------------------------------------------
        # UPDATE EACH PURCHASED ITEM
        # ---------------------------------------------------------

        for item in purchased_items:

            print(
                f"Updating Sales Order Catalog item: "
                f"{item['item_name']}"
            )

            self.update_purchased_item_in_sales_catalog(
                item
            )

        print(
            "Finished updating latest purchased "
            "items in Sales Order Catalog"
        )

        return {
            "catalog_updated": True,
            "items": purchased_items,
        }


    def create_order_for_new_customer(
        self,
        catalog_result: dict,
    ) -> dict:
        

        # ---------------------------------------------------------
        # LOGIN FIRST
        # Test 3 starts with a fresh browser/page
        # ---------------------------------------------------------

        self.login()

        purchased_items = catalog_result["items"]

        if not purchased_items:
            raise AssertionError(
                "No purchased items were supplied."
            )

        if not catalog_result.get(
            "catalog_updated",
            False,
        ):
            raise AssertionError(
                "Purchased items are not updated "
                "in Sales Order Catalog."
            )

        order_result = (
            self.create_and_complete_order_for_purchased_items(
                purchased_items
            )
        )

        return {
            "bill_number": catalog_result.get("bill_number"),
            "items": purchased_items,
            "customer": order_result["customer"],
            "order_items": order_result["order_items"],
            "stock_before": order_result["stock_before"],
            "stock_after": order_result["stock_after"],
        }


    # ============================================================
    # COMPLETE PURCHASE SETUP
    # ============================================================

    def prepare_stock_for_selling_unit_test(
        self,
        number_of_items: int = 2,
    ) -> dict:

        purchase_result = self.create_and_approve_purchase(
            number_of_items=number_of_items
        )

        catalog_result = (
            self.add_purchased_items_to_sales_order_catalog(
                purchase_result
            )
        )

        order_result = self.create_order_for_new_customer(
            catalog_result
        )

        return {
            "bill_number": purchase_result["bill_number"],
            "items": purchase_result["items"],
            "order": order_result,
        }
    # ============================================================
    # OPEN SALES ORDER DASHBOARD
    # ============================================================

    def open_sales_order_dashboard(self) -> None:

            # Side-panel Sales Order icon/link
            sales_order_link = self.page.locator(
                'a[href*="/business/salesorder/dashboard"]'
            ).first

            expect(
                sales_order_link
            ).to_be_visible(timeout=20_000)

            sales_order_link.click()

            self.page.wait_for_load_state(
                "domcontentloaded"
            )

            print("Opened Sales Order dashboard")



    # ============================================================
    # OPEN CATALOG TAB
    # ============================================================

    def open_sales_order_catalog(self) -> None:

            catalogs_text = self.page.get_by_text(
                "Catalogs",
                exact=True
            )

            expect(
                catalogs_text
            ).to_be_visible(
                timeout=20_000
            )

            catalogs_card = catalogs_text.locator(
                "xpath=ancestor::div[contains(@class,'p-card') or contains(@class,'card')][1]"
            )

            if catalogs_card.count() > 0:
                print("Clicking Catalogs card")
                catalogs_card.click()
            else:
                print("Clicking Catalogs text")
                catalogs_text.click()

            self.page.wait_for_load_state(
                "domcontentloaded"
            )


    # ============================================================
    # OPEN SALES ORDER CATALOG
    # ============================================================
    def open_first_sales_order_catalog(self) -> None:

            # Wait for catalog grid
            catalog_rows = self.page.locator(
                "table tbody tr"
            )

            expect(
                catalog_rows.first
            ).to_be_visible(timeout=20_000)

            first_catalog_row = catalog_rows.first

            print(
                "Opening Sales Order Catalog:",
                first_catalog_row.inner_text()
            )

            # Usually catalog name is a clickable link/text
            clickable_catalog = first_catalog_row.locator(
                "a"
            ).first

            if clickable_catalog.count() > 0:
                clickable_catalog.click()
            else:
                # fallback: click first meaningful cell
                first_catalog_row.get_by_role(
                    "cell"
                ).nth(0).click()

            self.page.wait_for_load_state(
                "domcontentloaded"
            )


    # ============================================================
    # Open Edit Details for a purchased item
    # ============================================================

    def open_item_edit_details(
            self,
            purchased_item_name: str
        ) -> str:

            print(
                f"Searching Catalog Details for: "
                f"{purchased_item_name}"
            )

            words = purchased_item_name.strip().split()

            max_scroll_attempts = 10

            for attempt in range(
                max_scroll_attempts
            ):

                # Try full name first, then progressively shorter names.
                for end_index in range(
                    len(words),
                    0,
                    -1
                ):

                    candidate = " ".join(
                        words[:end_index]
                    )

                    item_row = self.page.get_by_role(
                        "row"
                    ).filter(
                        has_text=re.compile(
                            re.escape(candidate),
                            re.I
                        )
                    ).first

                    if item_row.count() == 0:
                        continue

                    try:

                        if not item_row.is_visible():
                            continue

                        item_row.scroll_into_view_if_needed()

                        edit_button = item_row.get_by_role(
                            "button",
                            name="Edit Details",
                            exact=True
                        )

                        if edit_button.count() == 0:
                            continue

                        print(
                            f"Purchased item: "
                            f"{purchased_item_name}"
                        )

                        print(
                            f"Parent catalog item: "
                            f"{candidate}"
                        )

                        edit_button.click()

                        self.page.wait_for_load_state(
                            "domcontentloaded"
                        )

                        print(
                            f"Opened Edit Details for: "
                            f"{candidate}"
                        )

                        # Return actual parent name found
                        return candidate

                    except Exception:
                        continue

                print(
                    f"Item not visible yet. "
                    f"Scrolling Catalog Details... "
                    f"Attempt {attempt + 1}"
                )

                self.page.mouse.wheel(
                    0,
                    700
                )

                self.page.wait_for_timeout(
                    500
                )

            raise AssertionError(
                f"Purchased item "
                f"'{purchased_item_name}' "
                f"or its parent was not found "
                f"in Catalog Details"
            )

    # ============================================================
    # Open the 3-dot menu and Inventory Management
    # ============================================================
    def open_inventory_management_popup_for_row(
            self,
            row
        ) -> None:

            row.scroll_into_view_if_needed()

            # ---------------------------------------------------------
            # Click 3-dot button from the last cell
            # ---------------------------------------------------------

            cells = row.get_by_role("cell")

            if cells.count() == 0:
                raise AssertionError(
                    "No cells found in selling-unit row"
                )

            action_cell = cells.last

            three_dot_button = action_cell.get_by_role(
                "button"
            )

            expect(
                three_dot_button
            ).to_be_visible(
                timeout=10_000
            )

            expect(
                three_dot_button
            ).to_be_enabled()

            print(
                "Clicking 3-dot menu for selling-unit row"
            )

            three_dot_button.click()

            # ---------------------------------------------------------
            # Click Inventory management
            #
            # Batch item:
            #   Inventory management
            #
            # Non-batch item:
            #   Inventory management
            #   Generate Barcode
            #
            # Always choose Inventory management
            # ---------------------------------------------------------

            inventory_management = self.page.get_by_role(
                "button",
                name=re.compile(
                    r"Inventory management",
                    re.I
                )
            )

            expect(
                inventory_management
            ).to_be_visible(
                timeout=10_000
            )

            print(
                "Clicking Inventory management"
            )

            inventory_management.click()

            # ---------------------------------------------------------
            # Wait for Edit Item Details popup
            # ---------------------------------------------------------

            popup = self.page.get_by_role(
                "dialog"
            ).filter(
                has_text=re.compile(
                    r"Edit Item Details",
                    re.I
                )
            )

            expect(
                popup
            ).to_be_visible(
                timeout=15_000
            )

            print(
                "Edit Item Details popup opened"
            )



    # ============================================================
    # Handle batch item
    # ============================================================

    def add_latest_batch_to_catalog_item(
            self,
            purchased_batch: str
        ) -> None:

            popup = self.page.get_by_role(
                "dialog"
            ).filter(
                has_text=re.compile(
                    r"Edit Item Details",
                    re.I
                )
            )

            expect(
                popup
            ).to_be_visible(
                timeout=15_000
            )

            # =========================================================
            # BATCH TABLE
            # =========================================================

            batch_table = popup.locator(
                "table"
            )

            expect(
                batch_table
            ).to_be_visible(
                timeout=10_000
            )

            existing_rows = batch_table.locator(
                "tbody tr"
            )

            existing_count = existing_rows.count()

            if existing_count == 0:
                raise AssertionError(
                    "No existing batch rows found. "
                    "Cannot copy previous MRP and Sales Price."
                )

            # =========================================================
            # READ MRP AND SALES PRICE FROM PREVIOUS BATCH
            # =========================================================

            previous_row = existing_rows.last

            previous_row.scroll_into_view_if_needed()

            previous_mrp_input = previous_row.get_by_role(
                "textbox",
                name="Enter MRP"
            )

            previous_sales_price_input = previous_row.get_by_role(
                "textbox",
                name="Enter Batch Price"
            )

            expect(
                previous_mrp_input
            ).to_be_visible()

            expect(
                previous_sales_price_input
            ).to_be_visible()

            previous_mrp = (
                previous_mrp_input.input_value().strip()
            )

            previous_sales_price = (
                previous_sales_price_input.input_value().strip()
            )

            if not previous_mrp:
                raise AssertionError(
                    "Previous batch MRP is empty"
                )

            if not previous_sales_price:
                raise AssertionError(
                    "Previous batch Sales Price is empty"
                )

            print(
                f"Previous batch MRP: {previous_mrp}"
            )

            print(
                f"Previous batch Sales Price: "
                f"{previous_sales_price}"
            )

            # =========================================================
            # CLICK ADD
            # =========================================================

            add_button = popup.get_by_role(
                "button",
                name="Add",
                exact=True
            )

            expect(add_button).to_be_visible()
            expect(add_button).to_be_enabled()

            add_button.click()

            # Wait until new row appears
            expect(
                batch_table.locator(
                    "tbody tr"
                )
            ).to_have_count(
                existing_count + 1,
                timeout=10_000
            )

            # =========================================================
            # SCROLL POPUP TO BOTTOM
            # =========================================================

            popup.evaluate(
                """
                element => {
                    const scrollable =
                        element.querySelector('.p-dialog-content') ||
                        element.querySelector('[class*="dialog-content"]') ||
                        element;

                    scrollable.scrollTop = scrollable.scrollHeight;
                }
                """
            )

            self.page.wait_for_timeout(
                500
            )

            # =========================================================
            # GET NEW LAST ROW
            # =========================================================

            batch_rows = batch_table.locator(
                "tbody tr"
            )

            new_row = batch_rows.last

            new_row.scroll_into_view_if_needed()

            self.page.wait_for_timeout(
                300
            )

            # =========================================================
            # OPEN SELECT BATCH DROPDOWN
            # =========================================================

            batch_name_cell = new_row.get_by_role(
                "cell"
            ).first

            # First try the visible dropdown trigger button
            dropdown_trigger = batch_name_cell.get_by_role(
                "button",
                name=re.compile(r"dropdown trigger", re.I)
            )

            if dropdown_trigger.count() > 0:

                expect(
                    dropdown_trigger.first
                ).to_be_visible(
                    timeout=10_000
                )

                expect(
                    dropdown_trigger.first
                ).to_be_enabled()

                print(
                    "Opening Select Batch dropdown"
                )

                dropdown_trigger.first.click()

            else:

                # Fallback: click the visible dropdown container/cell
                print(
                    "Dropdown trigger button not found. "
                    "Clicking Batch Name cell."
                )

                expect(
                    batch_name_cell
                ).to_be_visible(
                    timeout=10_000
                )

                batch_name_cell.click()

            # =========================================================
            # WAIT FOR BATCH LIST
            # =========================================================

            listbox = self.page.get_by_role(
                "listbox"
            )

            expect(
                listbox
            ).to_be_visible(
                timeout=10_000
            )

            # =========================================================
            # SCROLL BATCH LIST TO BOTTOM
            # =========================================================

            listbox.evaluate(
                """
                element => {
                    element.scrollTop = element.scrollHeight;
                }
                """
            )

            self.page.wait_for_timeout(
                500
            )

            # =========================================================
            # SELECT PURCHASED BATCH
            # =========================================================

            purchased_batch_option = listbox.get_by_role(
                "option",
                name=purchased_batch,
                exact=True
            )

            selected_batch = None

            if purchased_batch_option.count() > 0:

                purchased_batch_option.scroll_into_view_if_needed()

                expect(
                    purchased_batch_option
                ).to_be_visible(
                    timeout=10_000
                )

                print(
                    f"Selecting purchased batch: "
                    f"{purchased_batch}"
                )

                purchased_batch_option.click()

                selected_batch = purchased_batch

            else:

                # -----------------------------------------------------
                # Fallback:
                # select the final batch from the dropdown
                # -----------------------------------------------------

                batch_options = listbox.get_by_role(
                    "option"
                )

                option_count = batch_options.count()

                if option_count == 0:
                    raise AssertionError(
                        "No batch options found in "
                        "Select Batch dropdown"
                    )

                latest_option = batch_options.last

                latest_option.scroll_into_view_if_needed()

                expect(
                    latest_option
                ).to_be_visible(
                    timeout=10_000
                )

                selected_batch = (
                    latest_option.inner_text().strip()
                )

                print(
                    f"Purchased batch "
                    f"'{purchased_batch}' not found. "
                    f"Selecting latest batch: "
                    f"{selected_batch}"
                )

                latest_option.click()

            # =========================================================
            # SCROLL NEW ROW INTO VIEW AGAIN
            # =========================================================

            new_row.scroll_into_view_if_needed()

            self.page.wait_for_timeout(
                300
            )

            # =========================================================
            # ENTER SAME MRP AS PREVIOUS BATCH
            # =========================================================

            new_mrp_input = new_row.get_by_role(
                "textbox",
                name="Enter MRP"
            )

            expect(
                new_mrp_input
            ).to_be_visible(
                timeout=10_000
            )

            new_mrp_input.fill(
                previous_mrp
            )

            # =========================================================
            # ENTER SAME SALES PRICE AS PREVIOUS BATCH
            # =========================================================

            new_sales_price_input = new_row.get_by_role(
                "textbox",
                name="Enter Batch Price"
            )

            expect(
                new_sales_price_input
            ).to_be_visible(
                timeout=10_000
            )

            new_sales_price_input.fill(
                previous_sales_price
            )

            # =========================================================
            # VERIFY VALUES
            # =========================================================

            expect(
                new_mrp_input
            ).to_have_value(
                previous_mrp
            )

            expect(
                new_sales_price_input
            ).to_have_value(
                previous_sales_price
            )

            print(
                f"New batch {selected_batch} -> "
                f"MRP: {previous_mrp}, "
                f"Sales Price: {previous_sales_price}"
            )

            # =========================================================
            # SAVE
            # =========================================================

            save_button = popup.get_by_role(
                "button",
                name="Save",
                exact=True
            )

            save_button.scroll_into_view_if_needed()

            expect(
                save_button
            ).to_be_visible()

            expect(
                save_button
            ).to_be_enabled()

            save_button.click()

            # =========================================================
            # WAIT FOR SUCCESS
            # =========================================================

            messages = (
                self.assert_and_wait_for_success_messages()
            )

            print(
                f"Batch update messages: "
                f"{messages}"
            )



    # ============================================================
    # Handle item without batch
    # ============================================================

    def close_non_batch_inventory_popup(
            self
        ) -> None:

            popup = self.page.get_by_role(
                "dialog"
            ).filter(
                has_text=re.compile(
                    r"Edit Item Details",
                    re.I
                )
            )

            expect(
                popup
            ).to_be_visible(
                timeout=15_000
            )

            print(
                "Non-batch item: closing "
                "Edit Item Details popup"
            )

            # Prefer Save if available
            save_button = popup.get_by_role(
                "button",
                name="Save",
                exact=True
            )

            if save_button.count() > 0:

                expect(
                    save_button
                ).to_be_visible(
                    timeout=10_000
                )

                expect(
                    save_button
                ).to_be_enabled()

                save_button.click()

            else:

                cancel_button = popup.get_by_role(
                    "button",
                    name="Cancel",
                    exact=True
                )

                expect(
                    cancel_button
                ).to_be_visible(
                    timeout=10_000
                )

                cancel_button.click()

            # ---------------------------------------------------------
            # IMPORTANT:
            # Wait until popup is fully closed
            # ---------------------------------------------------------

            expect(
                popup
            ).not_to_be_visible(
                timeout=15_000
            )

            print(
                "Returned to Item Details page"
            )


    # ============================================================
    # Save the complete item-details page
    # ============================================================

    def save_catalog_item_details_page(
            self
        ) -> None:

            print(
                "Saving Sales Order Catalog item details"
            )

            # ---------------------------------------------------------
            # MAKE SURE INVENTORY MANAGEMENT POPUP IS CLOSED
            # ---------------------------------------------------------

            visible_dialogs = self.page.get_by_role(
                "dialog"
            )

            for index in range(
                visible_dialogs.count()
            ):

                dialog = visible_dialogs.nth(
                    index
                )

                if dialog.is_visible():
                    raise AssertionError(
                        "Edit Item Details popup is still open "
                        "before final item-details Save"
                    )

            # ---------------------------------------------------------
            # SCROLL TO BOTTOM OF ITEM DETAILS PAGE
            # ---------------------------------------------------------

            self.page.evaluate(
                """
                window.scrollTo(
                    0,
                    document.body.scrollHeight
                );
                """
            )

            self.page.wait_for_timeout(
                500
            )

            # ---------------------------------------------------------
            # FIND VISIBLE PAGE-LEVEL SAVE BUTTON
            # ---------------------------------------------------------

            save_buttons = self.page.get_by_role(
                "button",
                name="Save",
                exact=True
            )

            visible_save_button = None

            for index in range(
                save_buttons.count()
            ):

                button = save_buttons.nth(
                    index
                )

                try:
                    if button.is_visible():

                        # Ignore Save buttons inside dialogs.
                        inside_dialog = button.locator(
                            "xpath=ancestor::*[@role='dialog']"
                        )

                        if inside_dialog.count() == 0:

                            visible_save_button = button
                            break

                except Exception:
                    continue

            if visible_save_button is None:
                raise AssertionError(
                    "Visible page-level Save button not found "
                    "on Sales Order item details page"
                )

            visible_save_button.scroll_into_view_if_needed()

            expect(
                visible_save_button
            ).to_be_visible(
                timeout=10_000
            )

            expect(
                visible_save_button
            ).to_be_enabled()

            print(
                "Clicking bottom Save button "
                "on item details page"
            )

            # ---------------------------------------------------------
            # CLICK SAVE
            # ---------------------------------------------------------

            visible_save_button.click()

            # ---------------------------------------------------------
            # WAIT FOR SUCCESS MESSAGE IF IT APPEARS
            # ---------------------------------------------------------

            self.page.wait_for_timeout(
                300
            )

            toast = self.page.locator(
                ".p-toast-message:visible"
            )

            if toast.count() > 0:

                messages = (
                    self.assert_and_wait_for_success_messages()
                )

                print(
                    f"Catalog item save messages: "
                    f"{messages}"
                )

            # ---------------------------------------------------------
            # VERY IMPORTANT:
            # VERIFY NAVIGATION BACK TO CATALOG DETAILS
            # ---------------------------------------------------------

            self.page.wait_for_url(
                re.compile(
                    r"/business/salesorder/catalogs/details/"
                ),
                timeout=20_000
            )

            self.page.wait_for_load_state(
                "domcontentloaded"
            )

            # ---------------------------------------------------------
            # VERIFY CATALOG DETAILS PAGE
            # ---------------------------------------------------------

            catalog_details = self.page.get_by_text(
                "Catalog Details",
                exact=True
            )

            expect(
                catalog_details
            ).to_be_visible(
                timeout=20_000
            )

            print(
                f"Saved Sales Order Catalog item. "
                f"Returned to Catalog Details: "
                f"{self.page.url}"
            )



    def get_item_detail_rows(
            self,
            purchased_item_name: str,
            parent_item_name: str
        ):

            all_rows = self.page.locator(
                "table tbody tr"
            )

            matched_rows = []

            attribute_part = purchased_item_name[
                len(parent_item_name):
            ].strip()

            print(
                f"Searching item detail rows | "
                f"Parent: {parent_item_name} | "
                f"Attribute: {attribute_part}"
            )

            for index in range(
                all_rows.count()
            ):

                row = all_rows.nth(index)

                try:
                    row_text = (
                        row.inner_text()
                        .strip()
                    )
                except Exception:
                    continue

                if not row_text:
                    continue

                if (
                    parent_item_name.lower()
                    not in row_text.lower()
                ):
                    continue

                if attribute_part:

                    if (
                        attribute_part.lower()
                        not in row_text.lower()
                    ):
                        continue

                matched_rows.append(
                    row
                )

                print(
                    f"Matched selling-unit row: "
                    f"{row_text}"
                )

            return matched_rows



    # ============================================================
    # Complete processing of one purchased item
    # ============================================================
    def update_purchased_item_in_sales_catalog(
            self,
            purchase_item: dict
        ) -> None:

            purchased_item_name = purchase_item[
                "item_name"
            ]

            batch = purchase_item.get(
                "batch"
            )

            print(
                f"\nUpdating purchased item: "
                f"{purchased_item_name}"
            )

            print(
                f"Purchased batch: {batch}"
            )

            # ---------------------------------------------------------
            # Open parent item from Catalog Details
            # This method should return the actual parent item name.
            #
            # Example:
            # Soan Papdi Elaichi -> Soan Papdi
            # Jalebi Yellow      -> Jalebi
            # Gulab Jamun        -> Gulab Jamun
            # ---------------------------------------------------------

            parent_item_name = self.open_item_edit_details(
                purchased_item_name
            )

            # ---------------------------------------------------------
            # Find rows belonging to the purchased attribute
            # across all selling units
            # ---------------------------------------------------------

            # Wait for Angular/UI to finish rendering all selling-unit rows
            self.page.wait_for_timeout(700)

            item_rows = self.get_item_detail_rows(
                purchased_item_name,
                parent_item_name
            )

            row_count = len(item_rows)

            if row_count == 0:
                raise AssertionError(
                    f"No matching selling-unit rows found for "
                    f"'{purchased_item_name}' "
                    f"under parent '{parent_item_name}'"
                )

            print(
                f"{purchased_item_name} has "
                f"{row_count} selling-unit combinations"
            )

            # =========================================================
            # BATCH ITEM
            # =========================================================

            if batch is not None:

                for index in range(
                    row_count
                ):

                    # Re-fetch rows each time because Angular may
                    # re-render the table after popup save.
                    item_rows = self.get_item_detail_rows(
                        purchased_item_name,
                        parent_item_name
                    )

                    row = item_rows[
                        index
                    ]

                    row.scroll_into_view_if_needed()

                    print(
                        f"Updating "
                        f"{purchased_item_name}: "
                        f"{index + 1}/{row_count}"
                    )

                    self.open_inventory_management_popup_for_row(
                        row
                    )

                    self.add_latest_batch_to_catalog_item(
                        purchased_batch=batch
                    )
            # =========================================================
            # NON-BATCH ITEM
            # =========================================================

            else:

                # For non-batch items, only open Inventory Management
                # for the first matching selling-unit row.
                # No need to process the remaining selling units.

                row = item_rows[0]

                row.scroll_into_view_if_needed()

                print(
                    f"Non-batch item: processing only first "
                    f"selling-unit row for {purchased_item_name}"
                )

                self.open_inventory_management_popup_for_row(
                    row
                )

                self.close_non_batch_inventory_popup()

            # =========================================================
            # SAVE ITEM DETAILS PAGE
            # =========================================================

            self.save_catalog_item_details_page()



    # ============================================================
    # PROCESS BOTH PURCHASED ITEMS
    # ============================================================

    def update_purchased_items_in_sales_catalog(
            self,
            purchased_items: list[dict]
        ) -> None:

            self.open_sales_order_dashboard()

            self.open_sales_order_catalog()

            self.open_first_sales_order_catalog()

            for purchase_item in purchased_items:

                self.update_purchased_item_in_sales_catalog(
                    purchase_item
                )

            print(
                "Finished updating all purchased items "
                "in Sales Order Catalog"
            )


    # ============================================================
    # OPEN INVENTORY MANAGEMENT DASHBOARD
    # ============================================================

    def open_inventory_management_dashboard(
        self
    ) -> None:

        print(
            f"Current URL before Inventory Management: "
            f"{self.page.url}"
        )

        # ---------------------------------------------------------
        # WAIT FOR INVENTORY SIDEBAR LINK
        # ---------------------------------------------------------

        inventory_link = self.page.locator(
            'a[href*="/business/salesorder/inventory"]'
        ).first

        expect(
            inventory_link
        ).to_be_visible(
            timeout=20_000
        )

        # Give Angular/sidebar rendering a moment to settle
        self.page.wait_for_timeout(
            500
        )

        # Re-locate after possible Angular re-render
        inventory_link = self.page.locator(
            'a[href*="/business/salesorder/inventory"]'
        ).first

        href = inventory_link.get_attribute(
            "href"
        )

        if not href:
            raise AssertionError(
                "Inventory Management sidebar href "
                "was not found."
            )

        print(
            f"Inventory sidebar href: "
            f"{href}"
        )

        # ---------------------------------------------------------
        # BUILD ABSOLUTE URL
        # ---------------------------------------------------------

        if href.startswith("/"):

            origin_match = re.match(
                r"^(https?://[^/]+)",
                self.page.url
            )

            if not origin_match:
                raise AssertionError(
                    f"Unable to determine application origin "
                    f"from URL: {self.page.url}"
                )

            inventory_url = (
                origin_match.group(1)
                + href
            )

        else:
            inventory_url = href

        print(
            f"Opening Inventory Management: "
            f"{inventory_url}"
        )

        # ---------------------------------------------------------
        # NAVIGATE DIRECTLY
        #
        # This avoids Angular sidebar re-render causing:
        # "Element is not attached to the DOM"
        # ---------------------------------------------------------

        self.page.goto(
            inventory_url
        )

        self.page.wait_for_load_state(
            "domcontentloaded"
        )

        # ---------------------------------------------------------
        # VERIFY URL
        # ---------------------------------------------------------

        expect(
            self.page
        ).to_have_url(
            re.compile(
                r"/business/salesorder/inventory"
            ),
            timeout=20_000
        )

        # ---------------------------------------------------------
        # VERIFY REAL INVENTORY HEADING
        # Avoid tooltip duplicate.
        # ---------------------------------------------------------

        inventory_heading = (
            self.page.locator("#kt_header")
            .get_by_text(
                "Inventory Management",
                exact=True
            )
        )

        expect(
            inventory_heading
        ).to_be_visible(
            timeout=20_000
        )

        print(
            f"Opened Inventory Management dashboard: "
            f"{self.page.url}"
        )


    # ============================================================
    # OPEN STOCKS PAGE
    # ============================================================
    def open_stocks_page(self) -> None:

            # ---------------------------------------------------------
            # CONFIRM INVENTORY MANAGEMENT DASHBOARD
            # ---------------------------------------------------------

            inventory_heading = self.page.get_by_text(
                "Inventory Management",
                exact=True
            )

            expect(
                inventory_heading
            ).to_be_visible(
                timeout=20_000
            )

            print(
                f"Inventory dashboard URL: "
                f"{self.page.url}"
            )

            # ---------------------------------------------------------
            # WAIT FOR DASHBOARD OVERLAY
            # ---------------------------------------------------------

            overlay = self.page.locator(
                ".overlay:visible"
            )

            if overlay.count() > 0:

                print(
                    "Waiting for Inventory dashboard "
                    "overlay to disappear"
                )

                expect(
                    overlay
                ).to_have_count(
                    0,
                    timeout=30_000
                )

            self.page.wait_for_timeout(
                500
            )

            # ---------------------------------------------------------
            # LOCATE EXACT STOCKS CARD
            #
            # Important:
            # There are multiple p-card-content elements on this page.
            # Match the one whose complete text is only "Stocks"
            # and which contains stock.svg.
            # ---------------------------------------------------------

            stocks_card_content = (
                self.page.locator(
                    ".p-card-content"
                )
                .filter(
                    has_text=re.compile(
                        r"^\s*Stocks\s*$",
                        re.I
                    )
                )
                .filter(
                    has=self.page.locator(
                        'img[src="assets/images/rx-order/'
                        'inventory-dashboard/stock.svg"]'
                    )
                )
            )

            expect(
                stocks_card_content
            ).to_have_count(
                1,
                timeout=20_000
            )

            # ---------------------------------------------------------
            # SCROLL EXACT STOCKS CARD INTO VIEW
            # ---------------------------------------------------------

            print(
                "Scrolling exact Stocks card into view"
            )

            stocks_card_content.scroll_into_view_if_needed()

            self.page.wait_for_timeout(
                700
            )

            expect(
                stocks_card_content
            ).to_be_visible(
                timeout=10_000
            )

            # ---------------------------------------------------------
            # CLICK STOCKS CARD
            # ---------------------------------------------------------

            print(
                "Clicking exact Stocks card"
            )

            stocks_card_content.click()

            # ---------------------------------------------------------
            # VERIFY NAVIGATION
            # ---------------------------------------------------------

            self.page.wait_for_timeout(
                500
            )

            check_stock = self.page.get_by_role(
                "button",
                name="Check Stock",
                exact=True
            )

            expect(
                check_stock
            ).to_be_visible(
                timeout=20_000
            )

            print(
                f"Opened Stocks page: "
                f"{self.page.url}"
            )

    # ============================================================
    # SELECT STORE IF NEEDED
    # ============================================================

    def select_stock_store_if_needed(self) -> None:

                select_store = self.page.get_by_text(
                    "Select Store",
                    exact=True
                )

                if select_store.count() == 0:
                    print(
                        f"Store already selected: {self.STORE_NAME}"
                    )
                    return

                select_store.first.click()

                store_option = self.page.get_by_role(
                    "option",
                    name=self.STORE_NAME
                )

                expect(
                    store_option
                ).to_be_visible(
                    timeout=10_000
                )

                store_option.click()


    # ============================================================
    # SELECT INVENTORY CATALOG IF NEEDED
    # ============================================================

    def select_stock_catalog_if_needed(self) -> None:

                select_catalog = self.page.get_by_text(
                    re.compile(
                        r"Select Inventory Catalog",
                        re.I
                    )
                )

                if select_catalog.count() == 0:
                    print(
                        f"Inventory Catalog already selected: "
                        f"{self.INVENTORY_CATALOG}"
                    )
                    return

                select_catalog.last.click()

                option = self.page.get_by_role(
                    "option",
                    name=self.INVENTORY_CATALOG
                )

                expect(
                    option
                ).to_be_visible(
                    timeout=10_000
                )

                option.click()



    # ============================================================
    # CHECK STOCK
    # ============================================================

    def click_check_stock(self) -> None:

            overlay = self.page.locator(
                ".overlay:visible"
            )

            if overlay.count() > 0:

                print(
                    "Waiting for Stocks page "
                    "overlay to disappear"
                )

                expect(
                    overlay
                ).to_have_count(
                    0,
                    timeout=20_000
                )

            check_stock = self.page.get_by_role(
                "button",
                name="Check Stock",
                exact=True
            )

            expect(
                check_stock
            ).to_be_visible(
                timeout=20_000
            )

            expect(
                check_stock
            ).to_be_enabled()

            check_stock.scroll_into_view_if_needed()

            print("Clicking Check Stock")

            check_stock.click()

            # Wait for stock results loading
            self.page.wait_for_timeout(
                300
            )

            overlay = self.page.locator(
                ".overlay:visible"
            )

            if overlay.count() > 0:

                expect(
                    overlay
                ).to_have_count(
                    0,
                    timeout=20_000
                )

            print("Stock loaded")



    # ============================================================
    # CAPTURE INHAND STOCK FOR PURCHASED ITEMS
    # ============================================================

    def capture_inhand_stock(
                self,
                purchased_items: list[dict]
            ) -> dict[str, float]:

                stock_values = {}

                # Scroll down so stock rows are rendered/visible
                self.page.mouse.wheel(
                    0,
                    1000
                )

                self.page.wait_for_timeout(
                    500
                )

                for purchase_item in purchased_items:

                    item_name = purchase_item[
                        "item_name"
                    ]

                    print(
                        f"Checking stock for: {item_name}"
                    )

                    stock_row = self.page.get_by_role(
                        "row"
                    ).filter(
                        has_text=re.compile(
                            re.escape(item_name),
                            re.I
                        )
                    ).first

                    if stock_row.count() == 0:

                        # Some stock grids may show parent/base item name
                        words = item_name.split()

                        for end_index in range(
                            len(words) - 1,
                            0,
                            -1
                        ):

                            candidate = " ".join(
                                words[:end_index]
                            )

                            stock_row = self.page.get_by_role(
                                "row"
                            ).filter(
                                has_text=re.compile(
                                    re.escape(candidate),
                                    re.I
                                )
                            ).first

                            if stock_row.count() > 0:
                                break

                    expect(
                        stock_row
                    ).to_be_visible(
                        timeout=15_000
                    )

                    stock_row.scroll_into_view_if_needed()

                    row_text = stock_row.inner_text()

                    print(
                        f"Stock row for {item_name}: "
                        f"{row_text}"
                    )

                    # -----------------------------------------------------
                    # Locate Inhand column
                    # -----------------------------------------------------

                    headers = self.page.get_by_role(
                        "columnheader"
                    )

                    inhand_index = None

                    for index in range(
                        headers.count()
                    ):

                        header_text = (
                            headers.nth(index)
                            .inner_text()
                            .strip()
                            .lower()
                        )

                        if "inhand" in header_text.replace(" ", ""):
                            inhand_index = index
                            break

                    if inhand_index is None:
                        raise AssertionError(
                            "Inhand column not found in Stocks grid"
                        )

                    cells = stock_row.get_by_role(
                        "cell"
                    )

                    inhand_text = (
                        cells.nth(inhand_index)
                        .inner_text()
                        .strip()
                    )

                    number_match = re.search(
                        r"-?\d+(?:\.\d+)?",
                        inhand_text
                    )

                    if not number_match:
                        raise AssertionError(
                            f"Could not read Inhand quantity for "
                            f"{item_name}: {inhand_text}"
                        )

                    inhand_qty = float(
                        number_match.group()
                    )

                    stock_values[
                        item_name
                    ] = inhand_qty

                    print(
                        f"{item_name} Inhand stock: "
                        f"{inhand_qty}"
                    )

                return stock_values



    def get_purchased_items_stock(
            self,
            purchased_items: list[dict]
        ) -> dict[str, float]:

            self.open_inventory_management_dashboard()

            self.open_stocks_page()

            self.select_stock_store_if_needed()

            self.select_stock_catalog_if_needed()

            self.click_check_stock()

            return self.capture_inhand_stock(
                purchased_items
            )



    # ============================================================
    # CLICK CREATE ORDER
    # ============================================================

    def open_create_order_popup(self) -> None:

            create_order = self.page.get_by_text(
                "Create Order",
                exact=True
            )

            expect(
                create_order
            ).to_be_visible(
                timeout=20_000
            )

            create_order.click()

            popup = self.page.get_by_role(
                "dialog"
            )

            expect(
                popup
            ).to_be_visible(
                timeout=15_000
            )

            print("Create Order popup opened")


    # ============================================================
    # CREATE NEW CUSTOMER
    # ============================================================

    def create_new_order_customer(
            self
        ) -> dict:

            # ---------------------------------------------------------
            # GENERATE CUSTOMER USING COMMON TEST DATA GENERATOR
            # ---------------------------------------------------------

            customer = generate_consumer_profile()

            first_name = customer["first_name"]
            last_name = customer["last_name"]
            phone = customer["phone"]
            email = customer["email"]
            gender = customer["gender"]

            customer_name = customer.get(
                "full_name",
                f"{first_name} {last_name}"
            )

            print(
                f"Creating customer: {customer_name}"
            )

            print(
                f"Phone: {phone} | "
                f"Email: {email} | "
                f"Gender: {gender}"
            )

            # ---------------------------------------------------------
            # CLICK NEW CUSTOMER
            # ---------------------------------------------------------

            new_customer = self.page.get_by_text(
                re.compile(
                    r"New Customer",
                    re.I
                )
            )

            expect(
                new_customer
            ).to_be_visible(
                timeout=15_000
            )

            new_customer.click()

            # ---------------------------------------------------------
            # FIRST NAME
            # ---------------------------------------------------------

            first_name_input = self.page.get_by_role(
                "textbox",
                name="First Name"
            )

            expect(
                first_name_input
            ).to_be_visible(
                timeout=15_000
            )

            first_name_input.fill(
                first_name
            )

            # ---------------------------------------------------------
            # LAST NAME
            # ---------------------------------------------------------

            last_name_input = self.page.get_by_role(
                "textbox",
                name="Last Name"
            )

            expect(
                last_name_input
            ).to_be_visible(
                timeout=10_000
            )

            last_name_input.fill(
                last_name
            )

            # ---------------------------------------------------------
            # PHONE
            # ---------------------------------------------------------

            phone_input = self.page.get_by_role(
                "textbox",
                name="10123"
            ).first

            if phone_input.count() == 0:
                phone_input = self.page.locator(
                    'input[type="tel"]'
                ).first

            expect(
                phone_input
            ).to_be_visible(
                timeout=10_000
            )

            phone_input.fill(
                phone
            )

            # ---------------------------------------------------------
            # EMAIL
            # ---------------------------------------------------------

            email_input = self.page.get_by_role(
                "textbox",
                name="Email(user@xyz.com)"
            )

            if email_input.count() == 0:
                email_input = self.page.locator(
                    'input[type="email"]'
                )

            if email_input.count() > 0:

                expect(
                    email_input.first
                ).to_be_visible(
                    timeout=10_000
                )

                email_input.first.fill(
                    email
                )

            # ---------------------------------------------------------
            # GENDER
            # ---------------------------------------------------------

            gender_radio = self.page.get_by_role(
                "radio",
                name=gender,
                exact=True
            )

            if gender_radio.count() > 0:

                expect(
                    gender_radio
                ).to_be_visible(
                    timeout=10_000
                )

                gender_radio.check()

            # ---------------------------------------------------------
            # SAVE
            # ---------------------------------------------------------

            save_button = self.page.get_by_role(
                "button",
                name="Save",
                exact=True
            )

            expect(
                save_button
            ).to_be_enabled(
                timeout=10_000
            )

            save_button.click()

            self.page.wait_for_timeout(
                1000
            )

            print(
                f"Created customer: "
                f"{customer_name}"
            )

            return customer


    # ============================================================
    # CONTINUE CREATE ORDER
    # ============================================================

    def continue_create_order(self) -> None:

            popup = self.page.get_by_role(
                "dialog"
            )

            expect(
                popup
            ).to_be_visible(
                timeout=20_000
            )

            # Store/catalog may already be defaulted.

            next_button = popup.get_by_role(
                "button",
                name="Next",
                exact=True
            )

            expect(
                next_button
            ).to_be_enabled()

            next_button.click()

            self.page.wait_for_load_state(
                "domcontentloaded"
            )

            print("Opened order creation page")



    # ============================================================
    # SEARCH AND ADD ONE OF THE PURCHASED ITEMS TO ORDER
    # ============================================================

    def search_and_add_order_item(
            self,
            purchase_item: dict
        ) -> dict:

            item_name = purchase_item[
                "item_name"
            ]

            print(
                f"Adding purchased item to order: "
                f"{item_name}"
            )

            # ---------------------------------------------------------
            # DETERMINE PARENT + ATTRIBUTE
            # ---------------------------------------------------------

            parent_item_name = item_name
            attribute_name = ""

            known_attributes = [
                "Orange",
                "Yellow",
                "Kesar",
                "Elaichi",
            ]

            for attribute in known_attributes:

                suffix = f" {attribute}"

                if item_name.endswith(
                    suffix
                ):

                    parent_item_name = item_name[
                        :-len(suffix)
                    ]

                    attribute_name = attribute

                    break

            print(
                f"Parent item: "
                f"{parent_item_name}"
            )

            if attribute_name:

                print(
                    f"Purchased attribute: "
                    f"{attribute_name}"
                )

            # ---------------------------------------------------------
            # MAIN ORDER PAGE SEARCH
            # ---------------------------------------------------------

            search_box = self.page.get_by_role(
                "searchbox",
                name="Search items",
                exact=True
            )

            expect(
                search_box
            ).to_be_visible(
                timeout=20_000
            )

            search_text = (
                parent_item_name[:3]
            )

            print(
                f"Searching order item using: "
                f"{search_text}"
            )

            search_box.fill(
                search_text
            )

            self.page.wait_for_timeout(
                700
            )

            # ---------------------------------------------------------
            # WAIT FOR SEARCH DROPDOWN
            # ---------------------------------------------------------

            listbox = self.page.get_by_role(
                "listbox"
            )

            expect(
                listbox
            ).to_be_visible(
                timeout=15_000
            )

            options = listbox.get_by_role(
                "option"
            )

            expect(
                options.first
            ).to_be_visible(
                timeout=15_000
            )

            # ---------------------------------------------------------
            # FIND EXACT PARENT ITEM RESULT
            # ---------------------------------------------------------

            matched_option = None

            for index in range(
                options.count()
            ):

                option = options.nth(
                    index
                )

                if not option.is_visible():
                    continue

                option_text = (
                    option.inner_text()
                    .strip()
                )

                print(
                    f"Order search option: "
                    f"{option_text}"
                )

                if option_text.lower().startswith(
                    parent_item_name.lower()
                ):

                    matched_option = option
                    break

            if matched_option is None:

                raise AssertionError(
                    f"Could not find "
                    f"'{parent_item_name}' "
                    f"in order search results"
                )

            # ---------------------------------------------------------
            # THIS CLICK IS IMPORTANT
            #
            # Jal
            #   ↓
            # Jalebi ₹100 TT Sales Catalog
            #   ↓ CLICK HERE
            # Select Item popup opens
            # ---------------------------------------------------------

            print(
                f"Clicking searched item: "
                f"{parent_item_name}"
            )

            matched_option.click()

            self.page.wait_for_timeout(
                500
            )

            # ---------------------------------------------------------
            # HANDLE SELECT ITEM POPUP
            # ---------------------------------------------------------

            selection = (
                self.select_order_item_combination(
                    purchased_item_name=item_name,
                    parent_item_name=parent_item_name,
                    attribute_name=attribute_name
                )
            )

            return {
                "item_name": item_name,
                "parent_item_name": parent_item_name,
                **selection
            }
        
        
    # ============================================================
    # SELECT ATTRIBUTE AND SELLING UNIT FOR ORDER ITEM
    # ============================================================

    def select_order_item_combination(
            self,
            purchased_item_name: str,
            parent_item_name: str,
            attribute_name: str = ""
        ) -> dict:

            self.page.wait_for_timeout(300)

            # ---------------------------------------------------------
            # FIND SELECT ITEM DIALOG
            # ---------------------------------------------------------

            dialogs = self.page.get_by_role("dialog")

            select_dialog = None

            for index in range(dialogs.count()):

                dialog = dialogs.nth(index)

                if not dialog.is_visible():
                    continue

                select_button = dialog.get_by_role(
                    "button",
                    name=re.compile(r"Select Item", re.I)
                )

                if (
                    select_button.count() > 0
                    and select_button.first.is_visible()
                ):
                    select_dialog = dialog
                    break

            # ---------------------------------------------------------
            # NO POPUP = SINGLE CONFIGURATION ITEM
            # ---------------------------------------------------------

            if select_dialog is None:

                print(
                    f"No Select Item popup for "
                    f"{purchased_item_name}"
                )

                return {
                    "attribute": None,
                    "selling_unit": None
                }

            dialog = select_dialog

            print(
                f"Select Item popup opened for: "
                f"{parent_item_name}"
            )

            selected_attribute = None
            selected_unit = None

            # ---------------------------------------------------------
            # ATTRIBUTE / VARIANT
            # ---------------------------------------------------------

            if attribute_name:

                attribute_button = dialog.get_by_role(
                    "button",
                    name=attribute_name,
                    exact=True
                )

                if (
                    attribute_button.count() > 0
                    and attribute_button.first.is_visible()
                ):

                    print(
                        f"Selecting attribute: "
                        f"{attribute_name}"
                    )

                    attribute_button.first.click()

                    selected_attribute = attribute_name

                    self.page.wait_for_timeout(300)

            # ---------------------------------------------------------
            # SELLING UNITS
            # ---------------------------------------------------------

            known_units = {
                "kg",
                "g",
                "mg",
                "gram",
                "kilogram",
                "milligram",
                "box",
                "numbers",
                "number",
                "can",
                "strip",
                "packet",
                "pack",
                "litre",
                "liter",
                "ml",
                "cl",
                "tablet",
                "bottle",
            }

            unit_candidates = []

            buttons = dialog.get_by_role("button")

            for index in range(buttons.count()):

                button = buttons.nth(index)

                if not button.is_visible():
                    continue

                try:
                    button_text = button.inner_text().strip()
                except Exception:
                    continue

                if not button_text:
                    continue

                normalized = button_text.lower()

                if normalized in known_units:

                    unit_candidates.append(
                        (
                            button,
                            button_text
                        )
                    )

            # ---------------------------------------------------------
            # RANDOMLY SELECT SELLING UNIT
            # ---------------------------------------------------------

            if unit_candidates:

                unit_button, selected_unit = random.choice(
                    unit_candidates
                )

                print(
                    f"Selecting selling unit: "
                    f"{selected_unit}"
                )

                unit_button.click()

                self.page.wait_for_timeout(300)

            # ---------------------------------------------------------
            # CLICK SELECT ITEM
            # ---------------------------------------------------------

            select_item_button = dialog.get_by_role(
                "button",
                name=re.compile(
                    r"Select Item",
                    re.I
                )
            ).last

            expect(
                select_item_button
            ).to_be_visible(
                timeout=10_000
            )

            expect(
                select_item_button
            ).to_be_enabled(
                timeout=10_000
            )

            print(
                f"Clicking Select Item | "
                f"Attribute: {selected_attribute} | "
                f"Unit: {selected_unit}"
            )

            select_item_button.click()

            # ---------------------------------------------------------
            # WAIT UNTIL POPUP CLOSES
            # ---------------------------------------------------------

            expect(
                dialog
            ).not_to_be_visible(
                timeout=15_000
            )

            print(
                f"Added {purchased_item_name} "
                f"to Sales Order"
            )

            return {
                "attribute": selected_attribute,
                "selling_unit": selected_unit
            }


    # ============================================================
    # RANDOM ATTRIBUTE AND SELLING UNIT SELECTION
    # ============================================================

    def randomize_item_attribute_and_unit(
            self,
            dialog,
            purchase_item: dict,
            selection: dict
        ) -> None:

            # ---------------------------------------------------------
            # Attribute radio buttons
            # ---------------------------------------------------------

            radios = dialog.get_by_role(
                "radio"
            )

            if radios.count() > 1:

                random_attribute_index = random.randint(
                    0,
                    radios.count() - 1
                )

                radios.nth(
                    random_attribute_index
                ).check()

                print(
                    f"Selected random attribute index: "
                    f"{random_attribute_index}"
                )

            # ---------------------------------------------------------
            # Selling unit controls
            # ---------------------------------------------------------

            # Depending on UI these may also be radio buttons.
            # Re-read after attribute change.
            self.page.wait_for_timeout(
                300
            )

            unit_controls = dialog.locator(
                '[role="radio"]:visible'
            )

            if unit_controls.count() > 1:

                random_unit_index = random.randint(
                    0,
                    unit_controls.count() - 1
                )

                unit_controls.nth(
                    random_unit_index
                ).check()

                print(
                    f"Selected random unit index: "
                    f"{random_unit_index}"
                )



    # ============================================================
    # CONFIRM SALES ORDER
    # ============================================================
    def confirm_sales_order(self) -> None:

            confirm_button = self.page.get_by_role(
                "button",
                name=re.compile(
                    r"Confirm Order",
                    re.I
                )
            )

            expect(
                confirm_button
            ).to_be_visible(
                timeout=15_000
            )

            confirm_button.click()

            self.page.wait_for_timeout(
                700
            )

            # Check whether insufficient-stock error appeared
            stock_error = self.page.get_by_text(
                re.compile(
                    r"Required quantity is not available",
                    re.I
                )
            )

            if stock_error.count() > 0:

                error_text = (
                    stock_error.first
                    .inner_text()
                    .strip()
                )

                print(
                    f"Stock error: {error_text}"
                )

                self.handle_order_stock_error(
                    error_text
                )

                # Try confirmation again
                confirm_button = self.page.get_by_role(
                    "button",
                    name=re.compile(
                        r"Confirm Order",
                        re.I
                    )
                )

                confirm_button.click()

            messages = (
                self.assert_and_wait_for_success_messages()
            )

            print(
                f"Order confirmation messages: "
                f"{messages}"
            )


    # ============================================================
    # HANDLE INSUFFICIENT STOCK ERROR
    # ============================================================  

    def handle_order_stock_error(
            self,
            error_text: str
        ) -> None:

            match = re.search(
                r"item\s+(.+?)\.\s*Available Quantity",
                error_text,
                re.I
            )

            if not match:
                raise AssertionError(
                    f"Could not determine item from "
                    f"stock error: {error_text}"
                )

            item_name = (
                match.group(1)
                .strip()
            )

            print(
                f"Adjusting batch for: {item_name}"
            )

            item_row = self.page.get_by_role(
                "row"
            ).filter(
                has_text=re.compile(
                    re.escape(item_name),
                    re.I
                )
            ).first

            expect(
                item_row
            ).to_be_visible(
                timeout=10_000
            )

            batch_dropdown = item_row.get_by_text(
                re.compile(
                    r"Select Batch|Batch",
                    re.I
                )
            )

            if batch_dropdown.count() == 0:

                # Reduce quantity as fallback
                quantity_input = item_row.get_by_role(
                    "spinbutton"
                )

                if quantity_input.count() == 0:
                    quantity_input = (
                        item_row.locator(
                            'input[type="number"]'
                        )
                    )

                if quantity_input.count() == 0:
                    raise AssertionError(
                        f"Unable to adjust quantity for "
                        f"{item_name}"
                    )

                quantity_input.first.fill("1")

                return

            batch_dropdown.first.click()

            batch_options = self.page.get_by_role(
                "option"
            )

            if batch_options.count() == 0:
                raise AssertionError(
                    f"No available batch found for "
                    f"{item_name}"
                )

            # Choose the last available batch.
            batch_options.last.click()   



    # ============================================================
    # CREATE INVOICE FOR ORDER
    # ============================================================ 

    def create_invoice_for_order(self) -> None:

            create_invoice = self.page.get_by_role(
                "button",
                name=re.compile(
                    r"Create Invoice",
                    re.I
                )
            )

            expect(
                create_invoice
            ).to_be_visible(
                timeout=20_000
            )

            create_invoice.click()

            self.assert_and_wait_for_success_messages()

            expect(
                self.page.get_by_role(
                    "button",
                    name=re.compile(
                        r"View Invoice",
                        re.I
                    )
                )
            ).to_be_visible(
                timeout=20_000
            )  


    # ============================================================
    # OPEN INVOICE
    # ============================================================  

    def open_invoice(self) -> None:

            view_invoice = self.page.get_by_role(
                "button",
                name=re.compile(
                    r"View Invoice",
                    re.I
                )
            )

            expect(
                view_invoice
            ).to_be_visible()

            view_invoice.click()

            self.page.wait_for_load_state(
                "domcontentloaded"
            )



    # ============================================================
    # SHARE INVOICE
    # ============================================================ 

    def share_invoice(self) -> None:

            share_invoice = self.page.get_by_role(
                "button",
                name=re.compile(
                    r"Share Invoice",
                    re.I
                )
            )

            expect(
                share_invoice
            ).to_be_visible(
                timeout=20_000
            )

            share_invoice.click()

            dialog = self.page.get_by_role(
                "dialog"
            )

            expect(
                dialog
            ).to_be_visible()

            share_button = dialog.get_by_role(
                "button",
                name=re.compile(
                    r"SHARE",
                    re.I
                )
            )

            expect(
                share_button
            ).to_be_enabled()

            share_button.click()

            messages = (
                self.assert_and_wait_for_success_messages()
            )

            print(
                f"Share Invoice messages: {messages}"
            )


    # ============================================================
    # PAY INVOICE BY CASH
    # ============================================================ 

    def pay_invoice_by_cash(self) -> None:

            print("Starting invoice payment")

            # ---------------------------------------------------------
            # GET PAYMENT DROPDOWN
            # PrimeNG keeps a hidden combobox input.
            # Click the visible dropdown container/trigger instead.
            # ---------------------------------------------------------

            print("Opening Get Payment dropdown")

            get_payment_input = self.page.locator(
                'input[role="combobox"][placeholder="Get Payment"]'
            )

            if get_payment_input.count() == 0:
                raise AssertionError(
                    "Get Payment dropdown was not found "
                    "on Invoice Details page."
                )

            # Find the PrimeNG dropdown containing the input
            get_payment_dropdown = get_payment_input.first.locator(
                "xpath=ancestor::*[contains(@class,'p-dropdown') "
                "or contains(@class,'p-select')][1]"
            )

            if (
                get_payment_dropdown.count() > 0
                and get_payment_dropdown.is_visible()
            ):

                get_payment_dropdown.click()

            else:

                # Fallback: visible dropdown-trigger button near Get Payment
                dropdown_triggers = self.page.get_by_role(
                    "button",
                    name=re.compile(
                        r"dropdown trigger",
                        re.I
                    )
                )

                visible_trigger = None

                for index in range(
                    dropdown_triggers.count()
                ):

                    trigger = dropdown_triggers.nth(index)

                    if not trigger.is_visible():
                        continue

                    # Get the surrounding dropdown and check that
                    # it belongs to Get Payment.
                    parent = trigger.locator(
                        "xpath=ancestor::*[contains(@class,'p-dropdown') "
                        "or contains(@class,'p-select')][1]"
                    )

                    if parent.count() == 0:
                        continue

                    parent_text = (
                        parent.inner_text()
                        .strip()
                        .lower()
                    )

                    parent_html = (
                        parent.evaluate(
                            "el => el.outerHTML"
                        )
                        .lower()
                    )

                    if (
                        "get payment" in parent_text
                        or "get payment" in parent_html
                    ):
                        visible_trigger = trigger
                        break

                if visible_trigger is None:
                    raise AssertionError(
                        "Visible Get Payment dropdown trigger "
                        "was not found."
                    )

                visible_trigger.click()

            self.page.wait_for_timeout(300)

            # ---------------------------------------------------------
            # SELECT PAY BY CASH
            # ---------------------------------------------------------

            cash_option = self.page.get_by_role(
                "option",
                name=re.compile(
                    r"Pay\s*by\s*Cash|Cash",
                    re.I
                )
            )

            if cash_option.count() == 0:

                cash_option = self.page.get_by_text(
                    re.compile(
                        r"Pay\s*by\s*Cash",
                        re.I
                    )
                )

            expect(
                cash_option.first
            ).to_be_visible(
                timeout=10_000
            )

            print("Selecting Pay by Cash")

            cash_option.first.click()

            self.page.wait_for_timeout(500)

            # ---------------------------------------------------------
            # PAYMENT POPUP
            # ---------------------------------------------------------

            dialogs = self.page.get_by_role("dialog")

            payment_dialog = None

            for index in range(dialogs.count()):

                dialog = dialogs.nth(index)

                if not dialog.is_visible():
                    continue

                pay_button = dialog.get_by_role(
                    "button",
                    name="Pay",
                    exact=True
                )

                if (
                    pay_button.count() > 0
                    and pay_button.first.is_visible()
                ):
                    payment_dialog = dialog
                    break

            # ---------------------------------------------------------
            # CLICK PAY
            # ---------------------------------------------------------

            if payment_dialog is not None:

                pay_button = payment_dialog.get_by_role(
                    "button",
                    name="Pay",
                    exact=True
                )

            else:

                pay_button = self.page.get_by_role(
                    "button",
                    name="Pay",
                    exact=True
                ).last

            expect(
                pay_button
            ).to_be_visible(
                timeout=15_000
            )

            expect(
                pay_button
            ).to_be_enabled(
                timeout=10_000
            )

            print("Clicking Pay")

            pay_button.click()

            self.page.wait_for_timeout(300)

            # ---------------------------------------------------------
            # CONFIRMATION:
            # Proceed with payment ?
            # ---------------------------------------------------------

            confirmation_text = self.page.get_by_text(
                re.compile(
                    r"Proceed\s+with\s+payment",
                    re.I
                )
            )

            if confirmation_text.count() > 0:

                expect(
                    confirmation_text.first
                ).to_be_visible(
                    timeout=10_000
                )

                print(
                    "Payment confirmation popup opened"
                )

            # ---------------------------------------------------------
            # CLICK YES
            # ---------------------------------------------------------

            yes_button = self.page.get_by_role(
                "button",
                name=re.compile(
                    r"^Yes$",
                    re.I
                )
            )

            expect(
                yes_button.last
            ).to_be_visible(
                timeout=10_000
            )

            print(
                "Confirming payment"
            )

            yes_button.last.click()

            # ---------------------------------------------------------
            # ASSERT PAYMENT SUCCESS
            # ---------------------------------------------------------

            self.page.wait_for_timeout(300)

            messages = (
                self.assert_and_wait_for_success_messages()
            )

            print(
                f"Payment messages: "
                f"{messages}"
            )

            print(
                "Invoice payment completed successfully"
            )

    # ============================================================
    # GO BACK TO ORDER DETAILS
    # ============================================================ 

    def go_back_to_order_details(self) -> None:

            back = self.page.get_by_text(
                "Back",
                exact=True
            )

            if back.count() > 0:

                back.first.click()

            else:

                self.page.go_back()

            self.page.wait_for_load_state(
                "domcontentloaded"
            )



    # ============================================================
    # COMPLETE SALES ORDER
    # ============================================================ 

    def complete_sales_order(self) -> None:

            self.page.mouse.wheel(
                0,
                1500
            )

            complete_order = self.page.get_by_role(
                "button",
                name=re.compile(
                    r"Complete Order",
                    re.I
                )
            )

            complete_order.scroll_into_view_if_needed()

            expect(
                complete_order
            ).to_be_visible(
                timeout=20_000
            )

            expect(
                complete_order
            ).to_be_enabled()

            complete_order.click()

            messages = (
                self.assert_and_wait_for_success_messages()
            )

            print(
                f"Complete Order messages: "
                f"{messages}"
            )



    def create_and_complete_order_for_purchased_items(
            self,
            purchased_items: list[dict]
        ) -> dict:

            # =========================================================
            # STOCK BEFORE ORDER
            # =========================================================

            stock_before = self.get_purchased_items_stock(
                purchased_items
            )

            print(
                f"Stock before order: {stock_before}"
            )

            # =========================================================
            # CREATE ORDER
            # =========================================================

            self.open_sales_order_dashboard()

            self.open_create_order_popup()

            customer = self.create_new_order_customer()

            self.continue_create_order()

            order_items = []

            for purchase_item in purchased_items:

                selected_item = self.search_and_add_order_item(
                    purchase_item
                )

                order_items.append(
                    selected_item
                )

            self.confirm_sales_order()

            # =========================================================
            # INVOICE
            # =========================================================

            self.create_invoice_for_order()

            self.open_invoice()

            self.share_invoice()

            self.pay_invoice_by_cash()

            # =========================================================
            # COMPLETE ORDER
            # =========================================================

            self.go_back_to_order_details()

            self.complete_sales_order()

            # =========================================================
            # STOCK AFTER ORDER
            # =========================================================

            stock_after = self.get_purchased_items_stock(
                purchased_items
            )

            print(
                f"Stock after order: {stock_after}"
            )

            return {
                "customer": customer,
                "order_items": order_items,
                "stock_before": stock_before,
                "stock_after": stock_after,
            }


    def open_purchase_from_inventory_dashboard(
        self
    ) -> None:

        inventory_heading = (
            self.page.locator("#kt_header")
            .get_by_text(
                "Inventory Management",
                exact=True
            )
        )

        expect(
            inventory_heading
        ).to_be_visible(
            timeout=20_000
        )

        overlay = self.page.locator(
            ".overlay:visible"
        )

        if overlay.count() > 0:

            expect(
                overlay
            ).to_have_count(
                0,
                timeout=30_000
            )

        # ---------------------------------------------------------
        # PURCHASE CARD
        # ---------------------------------------------------------

        purchase_card = (
            self.page.locator(
                ".p-card-content"
            )
            .filter(
                has_text=re.compile(
                    r"^\s*Purchase\s*$",
                    re.I
                )
            )
        )

        expect(
            purchase_card
        ).to_have_count(
            1,
            timeout=20_000
        )

        purchase_card.scroll_into_view_if_needed()

        print(
            "Clicking Purchase card"
        )

        purchase_card.click()

        self.page.wait_for_load_state(
            "domcontentloaded"
        )

        # ---------------------------------------------------------
        # VERIFY PURCHASE GRID
        # ---------------------------------------------------------

        purchase_rows = self.page.locator(
            "table tbody tr"
        )

        expect(
            purchase_rows.first
        ).to_be_visible(
            timeout=20_000
        )

        print(
            f"Opened Purchase grid: "
            f"{self.page.url}"
        )



    def open_latest_purchase_details(
            self
        ) -> None:

            rows = self.page.locator(
                "table tbody tr"
            )

            expect(
                rows.first
            ).to_be_visible(
                timeout=20_000
            )

            latest_row = rows.first

            print(
                "Latest purchase row:"
            )

            print(
                latest_row.inner_text()
            )

            # ---------------------------------------------------------
            # VIEW BUTTON
            # ---------------------------------------------------------

            view_button = latest_row.get_by_role(
                "button",
                name=re.compile(
                    r"View",
                    re.I
                )
            )

            if view_button.count() == 0:

                view_button = latest_row.get_by_text(
                    "View",
                    exact=True
                )

            expect(
                view_button.first
            ).to_be_visible(
                timeout=15_000
            )

            print(
                "Clicking View for latest purchase"
            )

            view_button.first.click()

            self.page.wait_for_timeout(
                500
            )

            print(
                f"Opened latest Purchase Details: "
                f"{self.page.url}"
            )




    def capture_items_from_latest_purchase(
            self
        ) -> list[dict]:

            print(
                "Reading items from latest "
                "Purchase Details"
            )

            # Slight scroll because item table is lower
            self.page.mouse.wheel(
                0,
                500
            )

            self.page.wait_for_timeout(
                500
            )

            tables = self.page.locator(
                "table"
            )

            item_table = None

            # ---------------------------------------------------------
            # FIND ITEM TABLE
            # ---------------------------------------------------------

            for index in range(
                tables.count()
            ):

                table = tables.nth(index)

                if not table.is_visible():
                    continue

                table_text = (
                    table.inner_text()
                    .lower()
                )

                if (
                    "item" in table_text
                    and (
                        "quantity" in table_text
                        or "qty" in table_text
                    )
                ):

                    item_table = table
                    break

            if item_table is None:

                raise AssertionError(
                    "Purchase item table not found "
                    "on Purchase Details page."
                )

            rows = item_table.locator(
                "tbody tr"
            )

            expect(
                rows.first
            ).to_be_visible(
                timeout=15_000
            )

            purchased_items = []

            # ---------------------------------------------------------
            # READ EACH ITEM ROW
            # ---------------------------------------------------------

            for index in range(
                rows.count()
            ):

                row = rows.nth(index)

                if not row.is_visible():
                    continue

                cells = row.get_by_role(
                    "cell"
                )

                if cells.count() == 0:
                    continue

                row_text = row.inner_text().strip()

                print(
                    f"Purchase item row: "
                    f"{row_text}"
                )

                # Usually item name is first meaningful cell.
                item_name = (
                    cells.nth(0)
                    .inner_text()
                    .strip()
                )

                if not item_name:
                    continue

                # -----------------------------------------------------
                # TRY TO GET BATCH
                # -----------------------------------------------------

                batch = None

                # Look for a cell containing a likely batch value
                # if Batch column exists.
                headers = item_table.locator(
                    "thead th"
                )

                batch_column_index = None

                for header_index in range(
                    headers.count()
                ):

                    header_text = (
                        headers.nth(header_index)
                        .inner_text()
                        .strip()
                        .lower()
                    )

                    if "batch" in header_text:

                        batch_column_index = (
                            header_index
                        )

                        break

                if (
                    batch_column_index is not None
                    and batch_column_index
                    < cells.count()
                ):

                    batch_text = (
                        cells.nth(
                            batch_column_index
                        )
                        .inner_text()
                        .strip()
                    )

                    if (
                        batch_text
                        and batch_text != "-"
                    ):
                        batch = batch_text

                purchased_items.append(
                    {
                        "item_name": item_name,
                        "batch": batch,
                    }
                )

                print(
                    f"Captured purchased item: "
                    f"{item_name} | "
                    f"Batch: {batch}"
                )

            if not purchased_items:

                raise AssertionError(
                    "No item rows could be read from "
                    "Purchase Details."
                )

            return purchased_items

# ----------------------------------------------------------------------------

    def create_random_sales_order_for_new_customer(
        self,
        number_of_items: int = 2,
    ) -> dict:

        # ---------------------------------------------------------
        # LOGIN
        # ---------------------------------------------------------

        self.login()

        # ---------------------------------------------------------
        # SALES ORDER
        # ---------------------------------------------------------

        self.open_sales_order_dashboard()

        self.open_create_order_popup()

        customer = self.create_new_order_customer()

        self.continue_create_order()

        # ---------------------------------------------------------
        # ADD RANDOM ITEMS
        # ---------------------------------------------------------

        order_items = []

        for _ in range(number_of_items):

            selected_item = (
                self.add_random_item_to_sales_order()
            )

            order_items.append(
                selected_item
            )

        # ---------------------------------------------------------
        # CONFIRM ORDER
        # ---------------------------------------------------------

        self.confirm_sales_order()

        # ---------------------------------------------------------
        # INVOICE
        # ---------------------------------------------------------

        self.create_invoice_for_order()

        self.open_invoice()

        self.share_invoice()

        self.pay_invoice_by_cash()

        # ---------------------------------------------------------
        # COMPLETE ORDER
        # ---------------------------------------------------------

        self.go_back_to_order_details()

        self.complete_sales_order()

        return {
            "customer": customer,
            "order_items": order_items,
        }   


    def add_random_item_to_sales_order(
        self
    ) -> dict:

        print("Adding random item to Sales Order")

        # ---------------------------------------------------------
        # CLICK + ADD ITEM
        # ---------------------------------------------------------

        add_item = self.page.get_by_role(
            "button",
            name="Add Item",
            exact=True
        )

        expect(
            add_item
        ).to_be_visible(
            timeout=15_000
        )

        add_item.click()

        # ---------------------------------------------------------
        # OUTER SELECT ITEMS POPUP
        # ---------------------------------------------------------

        select_items_dialog = (
            self.page.get_by_role("dialog")
            .filter(
                has_text=re.compile(
                    r"Select Items",
                    re.I
                )
            )
            .first
        )

        expect(
            select_items_dialog
        ).to_be_visible(
            timeout=15_000
        )

        self.page.wait_for_timeout(500)

        print("Select Items popup opened")

        # ---------------------------------------------------------
        # ITEM ROWS
        # ---------------------------------------------------------

        rows = select_items_dialog.locator(
            "tbody tr"
        )

        expect(
            rows.first
        ).to_be_visible(
            timeout=15_000
        )

        available_items = []

        for index in range(
            rows.count()
        ):

            row = rows.nth(index)

            if not row.is_visible():
                continue

            cells = row.get_by_role(
                "cell"
            )

            if cells.count() < 2:
                continue

            checkbox = row.get_by_role(
                "checkbox"
            )

            if checkbox.count() == 0:
                continue

            # Based on current popup:
            # column 0 = checkbox
            # column 1 = Item Name
            item_name = (
                cells.nth(1)
                .inner_text()
                .strip()
            )

            if not item_name:
                continue

            # Avoid same item twice
            if (
                hasattr(
                    self,
                    "selected_order_items"
                )
                and item_name
                in self.selected_order_items
            ):
                continue

            available_items.append(
                {
                    "item_name": item_name,
                    "checkbox": checkbox.first,
                }
            )

        if not available_items:

            raise AssertionError(
                "No Sales Order items available "
                "in Select Items popup."
            )

        print(
            "Available Sales Order items: "
            + ", ".join(
                item["item_name"]
                for item in available_items
            )
        )

        # ---------------------------------------------------------
        # RANDOM ITEM
        # ---------------------------------------------------------

        selected = random.choice(
            available_items
        )

        item_name = selected[
            "item_name"
        ]

        checkbox = selected[
            "checkbox"
        ]

        print(
            f"Random Sales Order item selected: "
            f"{item_name}"
        )

        # ---------------------------------------------------------
        # SELECT CHECKBOX
        # ---------------------------------------------------------

        expect(
            checkbox
        ).to_be_visible(
            timeout=10_000
        )

        checkbox.check()

        expect(
            checkbox
        ).to_be_checked()

        self.page.wait_for_timeout(
            500
        )

        # ---------------------------------------------------------
        # IMPORTANT:
        # CONFIGURABLE ITEM MAY IMMEDIATELY OPEN
        # SELECT ITEM POPUP
        # ---------------------------------------------------------

        combination = (
            self.select_random_order_item_combination(
                item_name
            )
        )

        # ---------------------------------------------------------
        # AFTER INNER POPUP IS HANDLED,
        # CLICK DONE ON OUTER SELECT ITEMS POPUP
        # ---------------------------------------------------------

        expect(
            select_items_dialog
        ).to_be_visible(
            timeout=10_000
        )

        done_button = (
            select_items_dialog.get_by_role(
                "button",
                name=re.compile(
                    r"\bDone\b",
                    re.I
                )
            )
            .last
        )

        expect(
            done_button
        ).to_be_visible(
            timeout=10_000
        )

        expect(
            done_button
        ).to_be_enabled(
            timeout=10_000
        )

        print(
            "Clicking Done on Select Items popup"
        )

        done_button.click()

        expect(
            select_items_dialog
        ).not_to_be_visible(
            timeout=15_000
        )

        # ---------------------------------------------------------
        # STORE SELECTED ITEM
        # ---------------------------------------------------------

        if not hasattr(
            self,
            "selected_order_items"
        ):
            self.selected_order_items = set()

        self.selected_order_items.add(
            item_name
        )

        print(
            f"Added Sales Order item: "
            f"{item_name}"
        )

        return {
            "item_name": item_name,
            **combination,
        }

                                            


    def select_random_order_item_combination(
        self,
        item_name: str,
    ) -> dict:

        self.page.wait_for_timeout(
            300
        )

        dialogs = self.page.get_by_role(
            "dialog"
        )

        select_dialog = None

        # ---------------------------------------------------------
        # FIND INNER "SELECT ITEM" POPUP
        # ---------------------------------------------------------

        for index in range(
            dialogs.count()
        ):

            dialog = dialogs.nth(index)

            if not dialog.is_visible():
                continue

            select_item_button = (
                dialog.get_by_role(
                    "button",
                    name=re.compile(
                        r"Select Item",
                        re.I
                    )
                )
            )

            if (
                select_item_button.count() > 0
                and select_item_button.last.is_visible()
            ):

                select_dialog = dialog
                break

        # ---------------------------------------------------------
        # NO POPUP:
        # SIMPLE ITEM
        # ---------------------------------------------------------

        if select_dialog is None:

            print(
                f"No Select Item popup for "
                f"{item_name}"
            )

            return {
                "attribute": None,
                "selling_unit": None,
            }

        dialog = select_dialog

        print(
            f"Select Item popup opened for "
            f"{item_name}"
        )

        selected_attribute = None
        selected_unit = None

        # ---------------------------------------------------------
        # KNOWN SELLING UNITS
        # ---------------------------------------------------------

        known_units = {
            "kg",
            "g",
            "mg",
            "gram",
            "kilogram",
            "milligram",
            "box",
            "nos",
            "numbers",
            "number",
            "can",
            "strip",
            "packet",
            "pack",
            "litre",
            "liter",
            "ml",
            "cl",
            "tablet",
            "bottle",
        }

        ignored_buttons = {
            "cancel",
            "select item",
        }

        buttons = dialog.get_by_role(
            "button"
        )

        attribute_candidates = []
        unit_candidates = []

        for index in range(
            buttons.count()
        ):

            button = buttons.nth(index)

            if not button.is_visible():
                continue

            try:
                text = (
                    button.inner_text()
                    .strip()
                )
            except Exception:
                continue

            if not text:
                continue

            normalized = (
                text.lower()
            )

            if normalized in ignored_buttons:
                continue

            if normalized in known_units:

                unit_candidates.append(
                    (
                        button,
                        text
                    )
                )

            else:

                attribute_candidates.append(
                    (
                        button,
                        text
                    )
                )

        # ---------------------------------------------------------
        # RANDOM ATTRIBUTE
        # Example:
        # Kesar / Elaichi
        # ---------------------------------------------------------

        if attribute_candidates:

            (
                attribute_button,
                selected_attribute
            ) = random.choice(
                attribute_candidates
            )

            print(
                f"Selecting random attribute: "
                f"{selected_attribute}"
            )

            attribute_button.click()

            self.page.wait_for_timeout(
                300
            )

        # ---------------------------------------------------------
        # RE-READ UNIT BUTTONS AFTER ATTRIBUTE CHANGE
        # ---------------------------------------------------------

        unit_candidates = []

        buttons = dialog.get_by_role(
            "button"
        )

        for index in range(
            buttons.count()
        ):

            button = buttons.nth(index)

            if not button.is_visible():
                continue

            try:
                text = (
                    button.inner_text()
                    .strip()
                )
            except Exception:
                continue

            normalized = (
                text.lower()
            )

            if normalized in known_units:

                unit_candidates.append(
                    (
                        button,
                        text
                    )
                )

        # ---------------------------------------------------------
        # RANDOM SELLING UNIT
        # Example:
        # nos / box
        # ---------------------------------------------------------

        if unit_candidates:

            (
                unit_button,
                selected_unit
            ) = random.choice(
                unit_candidates
            )

            print(
                f"Selecting random selling unit: "
                f"{selected_unit}"
            )

            unit_button.click()

            self.page.wait_for_timeout(
                300
            )

        # ---------------------------------------------------------
        # SELECT ITEM
        # ---------------------------------------------------------

        select_item_button = (
            dialog.get_by_role(
                "button",
                name=re.compile(
                    r"Select Item",
                    re.I
                )
            )
            .last
        )

        expect(
            select_item_button
        ).to_be_visible(
            timeout=10_000
        )

        expect(
            select_item_button
        ).to_be_enabled(
            timeout=10_000
        )

        print(
            f"Clicking Select Item | "
            f"Item: {item_name} | "
            f"Attribute: {selected_attribute} | "
            f"Unit: {selected_unit}"
        )

        select_item_button.click()

        expect(
            dialog
        ).not_to_be_visible(
            timeout=15_000
        )

        return {
            "attribute": selected_attribute,
            "selling_unit": selected_unit,
        }

    # ============================================================
    # CREATE ORDER FOR EXISTING CUSTOMER
    # ============================================================

    def select_existing_order_customer(
        self,
        search_text: str = "8281"
    ) -> dict:

        print(
            f"Searching existing customer using: "
            f"{search_text}"
        )

        dialog = self.page.get_by_role(
            "dialog"
        ).filter(
            has_text=re.compile(
                r"Create Order",
                re.I
            )
        )

        expect(
            dialog
        ).to_be_visible(
            timeout=15_000
        )

        # ---------------------------------------------------------
        # CUSTOMER SEARCH
        # ---------------------------------------------------------

        customer_search = dialog.get_by_role(
            "searchbox",
            name=re.compile(
                r"Select customer",
                re.I
            )
        )

        expect(
            customer_search
        ).to_be_visible(
            timeout=10_000
        )

        customer_search.fill(
            search_text
        )

        self.page.wait_for_timeout(
            700
        )

        # ---------------------------------------------------------
        # CUSTOMER SEARCH RESULTS
        # ---------------------------------------------------------

        listbox = dialog.get_by_role(
            "listbox"
        ).first

        expect(
            listbox
        ).to_be_visible(
            timeout=15_000
        )

        customer_option = listbox.get_by_role(
                "option"
            ).filter(
                has_text=re.compile(
                    r"Jisha\s+Rajan.*8281276241",
                    re.I | re.S
                )
            )

        expect(
            customer_option.first
        ).to_be_visible(
            timeout=15_000
        )

        print(
            "Existing customer result found:"
        )

        print(
            customer_option.first.inner_text()
        )

        # ---------------------------------------------------------
        # CLICK SEARCH RESULT
        # ---------------------------------------------------------

        customer_option.first.click()

        self.page.wait_for_timeout(
            500
        )

        print(
            "Clicked existing customer search result"
        )

        # ---------------------------------------------------------
        # VERIFY RESULT DROPDOWN CLOSED / CUSTOMER SELECTED
        # ---------------------------------------------------------

        expect(
            listbox
        ).not_to_be_visible(
            timeout=10_000
        )

        print(
            "Existing customer selected successfully"
        )

        return {
            "full_name": "Jisha Rajan",
            "search_text": search_text,
        }



    def create_random_sales_order_for_existing_customer(
        self,
        number_of_items: int = 2,
    ) -> dict:

        print("\n============================================")
        print("CREATING SALES ORDER FOR EXISTING CUSTOMER")
        print("============================================")

        # ---------------------------------------------------------
        # LOGIN
        # ---------------------------------------------------------

        self.login()

        # Reset only Test 4 random item tracking
        if hasattr(
            self,
            "selected_order_items"
        ):
            self.selected_order_items.clear()

        # ---------------------------------------------------------
        # SALES ORDER DASHBOARD
        # ---------------------------------------------------------

        self.open_sales_order_dashboard()

        # ---------------------------------------------------------
        # CREATE ORDER POPUP
        # ---------------------------------------------------------

        self.open_create_order_popup()

        # ---------------------------------------------------------
        # EXISTING CUSTOMER
        # ---------------------------------------------------------

        customer = (
            self.select_existing_order_customer(
                search_text="8281"
            )
        )

        # ---------------------------------------------------------
        # SAME WORKING FUNCTION USED BY TEST 3
        #
        # Store and TT Sales Catalog should already be selected.
        # Click Next.
        # ---------------------------------------------------------

        self.continue_create_order()

        # ---------------------------------------------------------
        # ADD RANDOM ITEMS
        # SAME WORKING TEST 3 FUNCTION
        # ---------------------------------------------------------

        order_items = []

        for _ in range(
            number_of_items
        ):

            selected_item = (
                self.add_random_item_to_sales_order()
            )

            order_items.append(
                selected_item
            )

        # ---------------------------------------------------------
        # CONFIRM ORDER
        # ---------------------------------------------------------

        self.confirm_sales_order()

        # ---------------------------------------------------------
        # CREATE INVOICE
        # ---------------------------------------------------------

        self.create_invoice_for_order()

        # ---------------------------------------------------------
        # OPEN INVOICE
        # ---------------------------------------------------------

        self.open_invoice()

        # ---------------------------------------------------------
        # SHARE INVOICE
        # ---------------------------------------------------------

        self.share_invoice()

        # ---------------------------------------------------------
        # PAYMENT
        # ---------------------------------------------------------

        self.pay_invoice_by_cash()

        # ---------------------------------------------------------
        # BACK TO ORDER
        # ---------------------------------------------------------

        self.go_back_to_order_details()

        # ---------------------------------------------------------
        # COMPLETE ORDER
        # ---------------------------------------------------------

        self.complete_sales_order()

        print("\n============================================")
        print("EXISTING CUSTOMER SALES ORDER COMPLETED")
        print("============================================")

        return {
            "customer": customer,
            "order_items": order_items,
        }



    