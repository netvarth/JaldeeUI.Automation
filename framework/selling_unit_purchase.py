import os
import random
import re
import string
from datetime import datetime
from typing import Optional

from playwright.sync_api import Page, expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

# The script to run this test case is ::- pytest tests/test_selling_unit_purchase.py

class SellingUnitPurchaseFlow:

    STORE_NAME = "TT Store"
    VENDOR_NAME = "Madhurai Sweets"
    INVENTORY_CATALOG = "TT Inventory"

    def __init__(self, page: Page):
        self.page = page
        self.selected_item_names = set()

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

        login_id = os.getenv("SCALE_SALESORDER_LOGIN_ID")
        password = os.getenv("SCALE_SALESORDER_PASSWORD")

        assert login_id, "SCALE_SALESORDER_LOGIN_ID is missing from .env"
        assert password, "SCALE_SALESORDER_PASSWORD is missing from .env"

        self.page.goto(provider_url)

        login_input = self.page.get_by_role(
            "textbox",
            name="Enter Login ID"
        )

        expect(login_input).to_be_visible()

        login_input.fill(login_id)

        self.page.get_by_role(
            "textbox",
            name="Enter password"
        ).fill(password)

        self.page.get_by_role(
            "button",
            name="Sign In"
        ).click()

        self.page.wait_for_load_state("domcontentloaded")

        # Give the dashboard a reliable indication that login completed.
        expect(
            self.page.get_by_text(
                re.compile(r"Welcome back", re.I)
            )
        ).to_be_visible(timeout=30_000)

    # ============================================================
    # INVENTORY NAVIGATION
    # ============================================================

    def open_inventory_management(self) -> None:

        # Prefer accessible text if the side menu is expanded.
        inventory_text = self.page.get_by_text(
            "Inventory Management",
            exact=True
        )

        if inventory_text.count() > 0:
            inventory_text.first.click()

        else:
            # Fallback for collapsed side menu.
            inventory_icon = self.page.locator(
                'img[src*="inventory" i]'
            )

            if inventory_icon.count() == 0:
                raise AssertionError(
                    "Inventory Management menu could not be located"
                )

            inventory_icon.first.click()

        self.page.wait_for_load_state("domcontentloaded")

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
    # STOCK PAGE
    # ============================================================

    # def go_back_to_inventory_dashboard(self) -> None:

    #     # On the recording there is a back arrow beside Purchases.
    #     back_button = self.page.locator(
    #         'button:has(i[class*="arrow-left"]), '
    #         'i[class*="arrow-left"]'
    #     )

    #     if back_button.count() > 0:
    #         back_button.first.click()
    #         return

    #     # Fallback
    #     self.page.go_back()

    # def open_stocks_tab(self) -> None:

    #     stock_tab = self.page.get_by_text(
    #         "Stocks",
    #         exact=True
    #     )

    #     expect(stock_tab.first).to_be_visible(
    #         timeout=20_000
    #     )

    #     stock_tab.first.click()

    # def select_stock_store_if_required(self) -> None:

    #     store = self.page.get_by_text(
    #         "Select Store",
    #         exact=True
    #     )

    #     if store.count() == 0:
    #         return

    #     try:
    #         store.first.click()

    #         option = self.page.get_by_role(
    #             "option",
    #             name=self.STORE_NAME
    #         )

    #         if option.count() > 0:
    #             option.first.click()

    #     except Exception:
    #         pass

    # def select_stock_inventory_catalog(self) -> None:

    #     catalog = self.page.get_by_text(
    #         re.compile(r"Select Inventory Catalog")
    #     )

    #     expect(catalog.last).to_be_visible()

    #     catalog.last.click()

    #     option = self.page.get_by_role(
    #         "option",
    #         name=self.INVENTORY_CATALOG
    #     )

    #     if option.count() > 0:
    #         option.first.click()
    #     else:
    #         self.page.get_by_text(
    #             self.INVENTORY_CATALOG,
    #             exact=True
    #         ).last.click()

    # def check_stock(self) -> None:

    #     check_stock = self.page.get_by_role(
    #         "button",
    #         name="Check Stock",
    #         exact=True
    #     )

    #     expect(check_stock).to_be_enabled()

    #     check_stock.click()

    #     self.page.wait_for_timeout(1000)

    # def verify_item_in_stock(
    #     self,
    #     item_name: str
    # ) -> None:

    #     if not item_name:
    #         return

    #     stock_row = self.page.get_by_role(
    #         "row"
    #     ).filter(
    #         has_text=item_name
    #     )

    #     expect(
    #         stock_row.first
    #     ).to_be_visible(timeout=15_000)

    # ============================================================
    # COMPLETE PURCHASE SETUP
    # ============================================================

    def prepare_stock_for_selling_unit_test(
        self,
        number_of_items: int = 2
    ) -> dict:

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

        # self.go_back_to_inventory_dashboard()

        # self.open_stocks_tab()

        # self.select_stock_store_if_required()

        # self.select_stock_inventory_catalog()

        # self.check_stock()

        # for item in purchased_items:
        #     self.verify_item_in_stock(
        #         item["item_name"]
        #     )

        # Update the purchased items in Sales Order Catalog
        self.update_purchased_items_in_sales_catalog(
            purchased_items
        )

        return {
            "bill_number": bill_number,
            "items": purchased_items,
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

        # Existing batch rows
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
        # READ PRICE FROM PREVIOUS/LATEST EXISTING BATCH
        # BEFORE CLICKING ADD
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

        expect(
            add_button
        ).to_be_visible()

        expect(
            add_button
        ).to_be_enabled()

        add_button.click()

        # Wait for new batch row to appear
        expect(
            batch_table.locator("tbody tr")
        ).to_have_count(
            existing_count + 1,
            timeout=10_000
        )

        # =========================================================
        # NEW ROW = LAST ROW
        # =========================================================

        batch_rows = batch_table.locator(
            "tbody tr"
        )

        new_row = batch_rows.last

        # Important:
        # scroll popup so the newly added batch row is fully visible
        new_row.scroll_into_view_if_needed()

        self.page.wait_for_timeout(300)

        # =========================================================
        # SELECT LATEST BATCH
        # =========================================================

        batch_dropdown = new_row.get_by_role(
            "combobox",
            name="Select Batch"
        )

        expect(
            batch_dropdown
        ).to_be_visible(
            timeout=10_000
        )

        batch_dropdown.click()

        batch_options = self.page.get_by_role(
            "option"
        )

        expect(
            batch_options.last
        ).to_be_visible(
            timeout=10_000
        )

        latest_batch = (
            batch_options.last.inner_text().strip()
        )

        print(
            f"Selecting latest batch: {latest_batch}"
        )

        batch_options.last.click()

        # =========================================================
        # SCROLL TO NEW ROW AGAIN AFTER DROPDOWN CLOSES
        # =========================================================

        new_row.scroll_into_view_if_needed()

        self.page.wait_for_timeout(300)

        # =========================================================
        # ENTER SAME MRP AS PREVIOUS BATCH
        # =========================================================

        new_mrp_input = new_row.get_by_role(
            "textbox",
            name="Enter MRP"
        )

        expect(
            new_mrp_input
        ).to_be_visible()

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
        ).to_be_visible()

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
            f"New batch {latest_batch} -> "
            f"MRP: {previous_mrp}, "
            f"Sales Price: {previous_sales_price}"
        )

        # =========================================================
        # SCROLL TO SAVE BUTTON
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
        # Use the safer toast handler already created
        # =========================================================

        messages = (
            self.assert_and_wait_for_success_messages()
        )

        print(
            f"Batch update messages: {messages}"
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
        ).to_be_visible(timeout=15_000)

        cancel_button = popup.get_by_role(
            "button",
            name=re.compile(
                r"Cancel|Close",
                re.I
            )
        )

        if cancel_button.count() > 0:
            cancel_button.last.click()
            return

        save_button = popup.get_by_role(
            "button",
            name="Save",
            exact=True
        )

        if save_button.count() > 0:
            save_button.last.click()


    # ============================================================
    # Save the complete item-details page
    # ============================================================

    def save_catalog_item_details_page(
        self
    ) -> None:

        save_button = self.page.get_by_role(
            "button",
            name="Save",
            exact=True
        )

        expect(
            save_button.last
        ).to_be_visible(timeout=15_000)

        expect(
            save_button.last
        ).to_be_enabled()

        save_button.last.click()

        self.page.wait_for_load_state(
            "domcontentloaded"
        )

        print(
            "Saved Sales Order Catalog item"
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

        item_rows = self.get_item_detail_rows(
            purchased_item_name,
            parent_item_name
        )

        row_count = len(
            item_rows
        )

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

                self.add_latest_batch_to_catalog_item()

        # =========================================================
        # NON-BATCH ITEM
        # =========================================================

        else:

            # For non-batch items, no need to update every
            # selling-unit combination.
            row = item_rows[0]

            row.scroll_into_view_if_needed()

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




    