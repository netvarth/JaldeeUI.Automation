import allure
from playwright.sync_api import Page

from framework.prescription_with_sellingunit.prescription_flow import (
    complete_prescription_push_rx_sales_order_flow,
)

# To run the test case :- pytest tests\test_prescription_flow.py


@allure.feature("Prescription")
@allure.story("Create Prescription and Push RX")
@allure.title(
    "Create prescription, push RX, convert to sales order and complete order"
)
def test_create_prescription_push_rx_and_complete_sales_order(
    page: Page,
    config,
    appointment_data,
):
    """
    Test Case:
        Create Appointment
        -> Create New Random Patient
        -> Create Prescription
        -> Add Multiple Medicines
        -> Push RX to Pharmacy
        -> Convert Prescription Request to Sales Order
        -> Edit Order
        -> Add Item
        -> Update and Confirm Order
        -> Create Invoice
        -> Pay by Cash
        -> Complete Order
    """

    result = complete_prescription_push_rx_sales_order_flow(
        page=page,
        config=config,
        consumer_profile=appointment_data,
    )

    print("\n============================================")
    print("PRESCRIPTION TEST COMPLETED")
    print("============================================")

    print(
        f"Patient          : {result['patient_name']}"
    )
    print(
        f"Doctor           : {result['doctor']}"
    )
    print(
        f"Service          : {result['service']}"
    )
    print(
        f"Pharmacy         : {result['pharmacy']}"
    )
    print(
        f"Order Item       : {result['order_item']}"
    )
    print(
        f"Order Quantity   : "
        f"{result['order_item_quantity']}"
    )

    print("\nMedicines:")

    for medicine in result["medicines"]:
        print(
            f"{medicine['medicine']} | "
            f"{medicine['frequency']} | "
            f"{medicine['duration']} days | "
            f"{medicine['instruction']}"
        )

    print("============================================")