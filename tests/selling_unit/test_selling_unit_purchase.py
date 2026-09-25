import os
import sys
import allure
import pytest

# Run all tests :- pytest tests/selling_unit -s -v   OR   pytest tests/selling_unit/test_selling_unit_purchase.py -s -v

# Run Only Purchase :- pytest tests/selling_unit/test_selling_unit_purchase.py::test_01_create_and_approve_purchase -v -s
# Run Only Catalog Update :- pytest tests/selling_unit/test_selling_unit_purchase.py::test_02_add_purchased_items_to_sales_order_catalog -v -s
# Run Only Order Creation for new customers :- pytest tests/selling_unit/test_selling_unit_purchase.py::test_03_create_order_for_new_customer -v -s
# Run Only Order Creation for existing customers :- pytest tests/selling_unit/test_selling_unit_purchase.py::test_04_create_order_for_existing_customer -v -s
# Run Only Item Creation :- pytest tests/selling_unit/test_selling_unit_purchase.py::test_01_create_items -s -v

# from framework.selling_unit_purchase import (
#     SellingUnitPurchaseFlow,
# )

from framework.selling_unit.selling_unit_purchase import SellingUnitPurchaseFlow



# ============================================================
# FIXTURES
# ============================================================
@pytest.fixture(scope="module")
def created_items_result(
    selling_unit_flow,
):

    return (
        selling_unit_flow
        .create_items_for_selling_unit_test()
    )


# ============================================================
# SHARED BROWSER SESSION FOR THESE 3 DEPENDENT TESTS
# ============================================================

@pytest.fixture(scope="module")
def selling_unit_flow(browser):

    context = browser.new_context()

    page = context.new_page()

    flow = SellingUnitPurchaseFlow(page)

    yield flow

    context.close()


# ============================================================
# PURCHASE DATA
# Runs once and is reused by Test 1, 2 and 3
# ============================================================

@pytest.fixture(scope="module")
def purchase_result(
    selling_unit_flow,
):

    return selling_unit_flow.create_and_approve_purchase(
        number_of_items=2
    )



# ============================================================
# CATALOG DATA
# Depends on purchase_result
# ============================================================

@pytest.fixture(scope="module")
def catalog_result(
    selling_unit_flow,
):

    return (
        selling_unit_flow
        .add_latest_purchase_items_to_sales_order_catalog()
    )



# ============================================================
# ORDER DATA
# ============================================================
@pytest.fixture(scope="module")
def order_result(
    selling_unit_flow,
):

    return (
        selling_unit_flow
        .create_random_sales_order_for_new_customer(
            number_of_items=2
        )
    )



# ============================================================
# EXISTING CUSTOMER ORDER DATA
# ============================================================
@pytest.fixture(scope="module")
def existing_customer_order_result(
    selling_unit_flow,
):

    return (
        selling_unit_flow
        .create_random_sales_order_for_existing_customer(
            number_of_items=2
        )
    )

# ============================================================
# TEST CASE 1
# PURCHASE
# ============================================================

def test_01_create_and_approve_purchase(
    purchase_result,
):

    assert purchase_result is not None

    assert purchase_result["bill_number"]

    assert purchase_result["items"]

    assert len(
        purchase_result["items"]
    ) == 2

    print("\n============================================")
    print("TEST 1 - PURCHASE PASSED")
    print("============================================")

    print(
        f"Bill Number: "
        f"{purchase_result['bill_number']}"
    )

    for item in purchase_result["items"]:

        print(
            f"Item={item['item_name']} | "
            f"Quantity={item['quantity']} | "
            f"Batch={item['batch']} | "
            f"MRP={item['mrp']} | "
            f"Purchase Price={item['purchase_price']}"
        )


# ============================================================
# TEST CASE 2
# ADD PURCHASED ITEMS TO SALES ORDER CATALOG
# ============================================================

def test_02_add_purchased_items_to_sales_order_catalog(
    catalog_result,
):

    assert catalog_result is not None

    assert catalog_result["catalog_updated"] is True

    assert catalog_result["items"]

    print("\n============================================")
    print("TEST 2 - SALES CATALOG UPDATE PASSED")
    print("============================================")

    for item in catalog_result["items"]:

        print(
            f"Catalog Item: "
            f"{item['item_name']}"
        )


# ============================================================
# TEST CASE 3
# CREATE ORDER FOR NEW CUSTOMER
# ============================================================

def test_03_create_order_for_new_customer(
    order_result,
):

    assert order_result is not None

    assert order_result["customer"]

    assert order_result["order_items"]

    print("\n============================================")
    print("TEST 3 - SALES ORDER PASSED")
    print("============================================")

    print(
        f"Customer: "
        f"{order_result['customer'].get('full_name', '')}"
    )

    for item in order_result["order_items"]:

        print(
            f"Order Item: "
            f"{item['item_name']}"
        )



# ============================================================
# TEST CASE 4
# CREATE ORDER FOR EXISTING CUSTOMER
# ============================================================

def test_04_create_order_for_existing_customer(
    existing_customer_order_result,
):

    assert (
        existing_customer_order_result
        is not None
    )

    assert (
        existing_customer_order_result[
            "customer"
        ]
    )

    assert (
        existing_customer_order_result[
            "order_items"
        ]
    )

    customer = (
        existing_customer_order_result[
            "customer"
        ]
    )

    assert (
        customer["full_name"]
        == "Jisha Rajan"
    )

    print("\n============================================")
    print(
        "TEST 4 - EXISTING CUSTOMER "
        "SALES ORDER PASSED"
    )
    print("============================================")

    print(
        f"Customer: "
        f"{customer['full_name']}"
    )

    for item in (
        existing_customer_order_result[
            "order_items"
        ]
    ):

        print(
            f"Order Item: "
            f"{item['item_name']} | "
            f"Attribute: "
            f"{item.get('attribute')} | "
            f"Selling Unit: "
            f"{item.get('selling_unit')}"
        )



def test_01_create_items(
    created_items_result,
):

    assert created_items_result is not None

    items = created_items_result["items"]

    assert len(items) == 2

    assert (
        items[0]["base_unit"]
        == "Numbers"
    )

    assert (
        items[1]["base_unit"]
        == "Box"
    )

    assert (
        items[1]["batch_applicable"]
        is True
    )

    assert (
        items[1]["unit_contains"]
        in [10, 20, 30]
    )

    assert (
        len(
            items[1]["attribute"][
                "option_values"
            ]
        )
        == 2
    )

    print("\n============================================")
    print("TEST 1 - CREATE ITEMS PASSED")
    print("============================================")

    for item in items:

        print(
            f"Created Item: "
            f"{item['item_name']}"
        )

