import os
import sys
import allure
import pytest

# Run with: pytest tests/test_selling_unit_purchase.py

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from framework.selling_unit_purchase import SellingUnitPurchaseFlow


@allure.feature("Sales Order")
@allure.story("Selling Unit")
@allure.title(
    "Purchase inventory items and update them "
    "in Sales Order Catalog"
)
@pytest.mark.selling_unit
@pytest.mark.sales_order
def test_prepare_items_for_selling_unit_sales_order(page):

    purchase_flow = SellingUnitPurchaseFlow(page)

    result = purchase_flow.prepare_stock_for_selling_unit_test(
        number_of_items=2
    )

    # Purchase bill number should be generated
    assert result["bill_number"]

    # Exactly 2 items should be purchased
    assert len(result["items"]) == 2

    # Ensure both purchased items are different
    item_names = [
        item["item_name"]
        for item in result["items"]
    ]

    assert len(set(item_names)) == 2, (
        f"Duplicate items selected: {item_names}"
    )

    # Validate purchase data
    for item in result["items"]:

        assert item["item_name"]

        assert item["quantity"] > 0

        assert item["mrp"] > 0

        assert item["purchase_price"] > 0

        assert item["mrp"] > item["purchase_price"]