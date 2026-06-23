import pytest

from framework.auth import login
from framework.test_data import generate_consumer_profile
from framework.order_invoice_tax_actions import complete_sales_order_invoice_tax_flow
from framework.order_invoice_tax_actions import (
    complete_sales_order_invoice_tax_flow,
    complete_exempt_items_order_invoice_flow,
    complete_taxable_items_order_invoice_flow,
    complete_mixed_taxable_exempt_order_invoice_flow,
)


# ----- Order created with one taxable item and one exempt item; GST applies only to taxable item -----

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

# ------ Order created with only exempt items; no GST applied and total equals item sum ------

@pytest.mark.order
@pytest.mark.invoice_tax
def test_order_invoice_exempt_items_no_gst_flow(page, config):
    """
    Order created with only exempt items.

    Validates:
    - Existing consumer Jisha is selected
    - Sale_catalog is selected
    - Item_2 and Item_6 are added
    - No CGST / SGST is shown in invoice
    - GST is not calculated
    - Subtotal equals item total sum
    - Net payable equals subtotal + delivery charge, if delivery charge exists
    - Payment is completed using Pay by Others
    - Order is completed
    """

    login(page, config)

    result = complete_exempt_items_order_invoice_flow(
        page=page,
        config=config,
    )

    assert result["consumer_selected"] is True
    assert result["exempt_tax_result"]["cgst_visible"] is False
    assert result["exempt_tax_result"]["sgst_visible"] is False
    assert result["exempt_tax_result"]["total_gst_amount"] == 0
    assert result["payment_completed"] is True
    assert result["order_completed"] is True
    assert result["final_url"]  



#  ------ Order created with only taxable items; GST applies correctly on all items -----

@pytest.mark.order
@pytest.mark.invoice_tax
def test_order_invoice_taxable_items_gst_applies_correctly_flow(page, config):
    """
    Order created with only taxable items.

    Validates:
    - New customer is created
    - Sale_catalog is selected
    - Item_4 and Item_1 are added
    - Item_4 GST 18% inclusive tax split is correct
    - Item_1 GST 5% + CESS 1% inclusive split is correct
    - CGST, SGST, and CESS totals are correct
    - Subtotal / Net Total With Tax / Delivery Charge / Net Payable are correct
    - Payment is completed using random Cash/Others mode
    - Order is completed
    """

    consumer_profile = generate_consumer_profile()

    login(page, config)

    result = complete_taxable_items_order_invoice_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
    )

    assert result["customer_name"]
    assert result["taxable_tax_result"]["item_4_result"]["taxable_expected"] > 0
    assert result["taxable_tax_result"]["item_1_result"]["taxable_expected"] > 0
    assert result["taxable_tax_result"]["summary_cgst_actual"] > 0
    assert result["taxable_tax_result"]["summary_sgst_actual"] > 0
    assert result["taxable_tax_result"]["summary_cess_actual"] > 0
    assert result["payment_completed"] is True
    assert result["order_completed"] is True
    assert result["final_url"]   



    #----- Order created with taxable and exempt items; tax breakup shows correct segregation -----


@pytest.mark.order
@pytest.mark.invoice_tax
def test_order_invoice_taxable_and_exempt_items_tax_breakup_flow(page, config):
    """
    Order created with taxable and exempt items; tax breakup shows correct segregation.

    Customer can be:
    - Existing customer Jisha Sreejith
    - New random customer
    """

    consumer_profile = generate_consumer_profile()

    login(page, config)

    result = complete_mixed_taxable_exempt_order_invoice_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
    )

    assert result["customer_selected"] is True
    assert result["customer_type"] in ["existing", "new"]

    assert result["mixed_tax_result"]["item_4_result"]["taxable_expected"] > 0
    assert result["mixed_tax_result"]["item_1_result"]["taxable_expected"] > 0

    assert result["mixed_tax_result"]["item_6_result"]["gst_amount"] == 0
    assert result["mixed_tax_result"]["item_6_result"]["cess_amount"] == 0

    assert result["mixed_tax_result"]["item_2_result"]["gst_amount"] == 0
    assert result["mixed_tax_result"]["item_2_result"]["cess_amount"] == 0

    assert result["mixed_tax_result"]["summary_cgst_actual"] > 0
    assert result["mixed_tax_result"]["summary_sgst_actual"] > 0
    assert result["mixed_tax_result"]["summary_cess_actual"] > 0

    assert result["payment_completed"] is True
    assert result["order_completed"] is True
    assert result["final_url"]



#    Line item discount applied on taxable order item; taxable value and GST reduce correctly       
