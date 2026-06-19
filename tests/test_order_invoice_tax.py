import pytest

from framework.auth import login
from framework.test_data import generate_consumer_profile
from framework.order_invoice_tax_actions import complete_sales_order_invoice_tax_flow


@pytest.mark.order
@pytest.mark.invoice_tax
def test_order_invoice_tax_split_and_payment_flow(page, config):
    """
    Order invoice tax validation.

    Validates:
    - Customer creation using random consumer profile
    - Sale_catalog selection
    - Item_4 and Item_6 order creation
    - Item_4 inclusive tax split
    - CGST and SGST calculation
    - Invoice subtotal/net payable calculation
    - Cash payment
    - Complete order
    """

    consumer_profile = generate_consumer_profile()

    login(page, config)

    result = complete_sales_order_invoice_tax_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
    )

    assert result["customer_name"]
    assert result["item_4_tax_result"]["taxable_expected"] > 0
    assert result["item_4_tax_result"]["cgst_actual"] == result["item_4_tax_result"]["cgst_expected"]
    assert result["item_4_tax_result"]["sgst_actual"] == result["item_4_tax_result"]["sgst_expected"]
    assert result["payment_completed"] is True
    assert result["order_completed"] is True
    assert result["final_url"]