from decimal import Decimal

from playwright.sync_api import Page

from framework.test_data import generate_consumer_profile
from framework.ip_invoice_tax_actions import (
    complete_ip_master_invoice_discount_tax_flow,
)


def test_ip_invoice_tax_calculation_full_flow(page: Page, config) -> None:
    """
    Case:
    IP invoice tax calculation full flow.

    Steps:
    1. Login with IP account.
    2. Open IP dashboard.
    3. Create new IP admission with random patient.
    4. Add Doc Visit service.
    5. Request pharmacy order from service.
    6. Select one random medicine:
       - Med_1: GST 5% + CESS 1%
       - Med_2: GST 5% + CESS 1%
       - Med_4: GST 5%
    7. Confirm sales order request.
    8. Create sales order invoice.
    9. Validate pharmacy order invoice tax-inclusive split.
    10. Create IP service invoice.
    11. Link service invoice + pharmacy invoice into Master Invoice.
    12. Validate Master Invoice tax-exclusive breakup.
    13. Apply On Demand Discount to pharmacy item.
    14. Validate tax and totals after discount.
    15. Remove discount.
    16. Validate tax and totals after discount removal.
    """

    consumer_profile = generate_consumer_profile()

    result = complete_ip_master_invoice_discount_tax_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
    )

    assert result["patient_created"] is True
    assert result["admission_created"] is True
    assert result["service_added"] is True
    assert result["order_requested"] is True
    assert result["order_confirmed"] is True
    assert result["order_invoice_created"] is True
    assert result["ip_service_invoice_created"] is True
    assert result["master_invoice_created"] is True

    assert result["selected_item_name"] in ["Med_1", "Med_2", "Med_4"]
    assert result["selected_quantity"] >= 1
    assert result["master_invoice_type"] == "Master Invoice"

    order_invoice_tax_result = result["order_invoice_tax_result"]

    assert order_invoice_tax_result["taxable_expected"] > Decimal("0")
    assert order_invoice_tax_result["gst_expected"] > Decimal("0")
    assert order_invoice_tax_result["cgst_expected"] > Decimal("0")
    assert order_invoice_tax_result["sgst_expected"] > Decimal("0")
    assert order_invoice_tax_result["summary_cgst_actual"] > Decimal("0")
    assert order_invoice_tax_result["summary_sgst_actual"] > Decimal("0")
    assert order_invoice_tax_result["subtotal_actual"] > Decimal("0")
    assert order_invoice_tax_result["net_total_with_tax_actual"] > Decimal("0")

    if result["selected_item_name"] in ["Med_1", "Med_2"]:
        assert order_invoice_tax_result["cess_expected"] > Decimal("0")
        assert order_invoice_tax_result["cess_actual"] > Decimal("0")
        assert order_invoice_tax_result["summary_cess_actual"] > Decimal("0")

    if result["selected_item_name"] == "Med_4":
        assert order_invoice_tax_result["cess_expected"] == Decimal("0")
        assert order_invoice_tax_result["cess_actual"] == Decimal("0")

    master_invoice_tax_result = result["master_invoice_tax_result"]

    assert master_invoice_tax_result["service_amount_actual"] > Decimal("0")
    assert master_invoice_tax_result["pharmacy_taxable_actual"] > Decimal("0")
    assert master_invoice_tax_result["pharmacy_gst_actual"] >= Decimal("0")
    assert master_invoice_tax_result["summary_cgst_actual"] >= Decimal("0")
    assert master_invoice_tax_result["summary_sgst_actual"] >= Decimal("0")
    assert master_invoice_tax_result["subtotal_actual"] > Decimal("0")
    assert master_invoice_tax_result["net_total_actual"] > Decimal("0")

    if result["selected_item_name"] in ["Med_1", "Med_2"]:
        assert master_invoice_tax_result["pharmacy_cess_actual"] >= Decimal("0")

    if result["selected_item_name"] == "Med_4":
        assert master_invoice_tax_result["pharmacy_cess_actual"] == Decimal("0")

    assert result["discount_applied"] is True
    assert result["discount_amount"] > Decimal("0")

    before_discount = result["before_discount_tax_result"]
    after_discount = result["after_discount_tax_result"]

    assert before_discount["net_total_actual"] > Decimal("0")
    assert after_discount["net_total_actual"] > Decimal("0")
    assert after_discount["net_total_actual"] < before_discount["net_total_actual"]

    assert after_discount["pharmacy_discount_actual"] == result["discount_amount"]

    assert after_discount["pharmacy_amount_before_discount_actual"] == before_discount["pharmacy_amount_before_discount_actual"]
    assert after_discount["pharmacy_taxable_actual"] < before_discount["pharmacy_taxable_actual"]
    assert after_discount["pharmacy_total_expected"] < before_discount["pharmacy_total_expected"]

    expected_taxable_after_discount = (
        before_discount["pharmacy_amount_before_discount_actual"] - result["discount_amount"]
    )

    assert after_discount["pharmacy_taxable_actual"] == expected_taxable_after_discount
    assert after_discount["pharmacy_gst_actual"] >= Decimal("0")
    assert after_discount["summary_cgst_actual"] >= Decimal("0")
    assert after_discount["summary_sgst_actual"] >= Decimal("0")


    if result["selected_item_name"] in ["Med_1", "Med_2"]:
        assert after_discount["pharmacy_cess_actual"] >= Decimal("0")

    if result["selected_item_name"] == "Med_4":
        assert after_discount["pharmacy_cess_actual"] == Decimal("0")

    assert result["discount_removed"] is True

    after_remove_discount = result["after_remove_discount_tax_result"]

    assert after_remove_discount["pharmacy_discount_actual"] == Decimal("0")
    assert after_remove_discount["pharmacy_taxable_actual"] >= after_discount["pharmacy_taxable_actual"]
    assert after_remove_discount["net_total_actual"] >= after_discount["net_total_actual"]

    assert result["final_url"]