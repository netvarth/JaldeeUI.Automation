from decimal import Decimal

from playwright.sync_api import Page

from framework.test_data import generate_consumer_profile
from framework.ip_invoice_tax_actions import (
    complete_ip_master_invoice_discount_tax_flow,
    assert_amount_close,
    complete_ip_master_invoice_exempt_discount_tax_flow,
    round_money,
    complete_ip_invoice_taxable_bed_exempt_service_flow,
    complete_ip_invoice_exempt_bed_taxable_service_flow,
    complete_ip_invoice_taxable_bed_taxable_service_flow,
    complete_ip_invoice_exempt_bed_exempt_service_flow,
    complete_ip_invoice_taxable_bed_multiple_days_flow,
    complete_master_invoice_taxable_order_item_and_ip_invoice_flow,
)


# Apply a line item discount to a taxable order item in the Master Invoice and verify that the discount is calculated.

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



# Apply a line item discount to a tax exempt order item in the Master Invoice and verify that the discount is calculated.

def test_ip_invoice_tax_exempt_item_line_discount_full_flow(page: Page, config) -> None:
    """
    Case:
    Line item discount applied on tax-exempt order item; amount reduces without GST calculation.

    Flow:
    Create an IP order with tax-exempt item Med_3 or Med_5, generate the order invoice,
    service invoice, and Master Invoice. Apply and remove a line item discount, and verify
    that the discount is applied on Rate * Quantity while GST and CESS remain zero.
    """

    consumer_profile = generate_consumer_profile()

    result = complete_ip_master_invoice_exempt_discount_tax_flow(
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

    assert result["selected_item_name"] in ["Med_3", "Med_5"]
    assert result["selected_item_is_exempt"] is True
    assert result["selected_quantity"] >= 1
    assert result["master_invoice_type"] == "Master Invoice"

    order_invoice_tax_result = result["order_invoice_tax_result"]

    assert order_invoice_tax_result["taxable_actual"] > Decimal("0")
    assert order_invoice_tax_result["gst_expected"] == Decimal("0")
    assert order_invoice_tax_result["cess_expected"] == Decimal("0")
    assert order_invoice_tax_result["cgst_expected"] == Decimal("0")
    assert order_invoice_tax_result["sgst_expected"] == Decimal("0")
    assert order_invoice_tax_result["gst_actual"] == Decimal("0")
    assert order_invoice_tax_result["cess_actual"] == Decimal("0")
    assert order_invoice_tax_result["summary_cgst_actual"] == Decimal("0")
    assert order_invoice_tax_result["summary_sgst_actual"] == Decimal("0")
    assert order_invoice_tax_result["summary_cess_actual"] == Decimal("0")
    assert order_invoice_tax_result["subtotal_actual"] > Decimal("0")
    assert order_invoice_tax_result["net_total_with_tax_actual"] > Decimal("0")

    before_discount = result["before_discount_tax_result"]
    after_discount = result["after_discount_tax_result"]

    assert result["discount_applied"] is True
    assert result["discount_amount"] > Decimal("0")

    expected_amount_before_discount = round_money(
        before_discount["pharmacy_rate_actual"] * Decimal(str(result["selected_quantity"]))
    )

    assert_amount_close(
        before_discount["pharmacy_amount_before_discount_actual"],
        expected_amount_before_discount,
        "Before discount exempt item amount should be Rate * Quantity.",
    )

    assert_amount_close(
        after_discount["pharmacy_amount_before_discount_actual"],
        expected_amount_before_discount,
        "After discount exempt item base amount should remain Rate * Quantity.",
    )

    expected_taxable_after_discount = round_money(
        expected_amount_before_discount - result["discount_amount"]
    )

    if expected_taxable_after_discount < Decimal("0"):
        expected_taxable_after_discount = Decimal("0")

    assert after_discount["pharmacy_discount_actual"] == result["discount_amount"]

    assert_amount_close(
        after_discount["pharmacy_taxable_actual"],
        expected_taxable_after_discount,
        "After discount exempt item amount should be Rate * Quantity - Discount.",
    )

    assert after_discount["pharmacy_taxable_actual"] < before_discount["pharmacy_taxable_actual"]

    assert after_discount["pharmacy_gst_actual"] == Decimal("0")
    assert after_discount["pharmacy_cess_actual"] == Decimal("0")
    assert after_discount["summary_cgst_actual"] == Decimal("0")
    assert after_discount["summary_sgst_actual"] == Decimal("0")
    assert after_discount["summary_cess_actual"] == Decimal("0")

    assert result["discount_removed"] is True

    after_remove_discount = result["after_remove_discount_tax_result"]

    assert after_remove_discount["pharmacy_discount_actual"] == Decimal("0")

    assert_amount_close(
        after_remove_discount["pharmacy_taxable_actual"],
        before_discount["pharmacy_taxable_actual"],
        "After removing discount exempt item amount should return to original Rate * Quantity amount.",
    )

    assert after_remove_discount["pharmacy_gst_actual"] == Decimal("0")
    assert after_remove_discount["pharmacy_cess_actual"] == Decimal("0")
    assert after_remove_discount["summary_cgst_actual"] == Decimal("0")
    assert after_remove_discount["summary_sgst_actual"] == Decimal("0")
    assert after_remove_discount["summary_cess_actual"] == Decimal("0")

    assert result["final_url"]  

# ***** IP invoice with taxable bed and exempt service; GST applies only on bed charge *****

def test_ip_invoice_taxable_bed_exempt_service_tax_only_on_bed_flow(page: Page, config) -> None:
    """
    Case:
    IP invoice with taxable bed and exempt service; GST applies only on bed charge.

    Expected:
    - Bed has 5% GST.
    - Bed rate shown in invoice is tax excluded.
    - Bed tax = Bed Rate * 5 / 100.
    - Bed total = Bed Rate + Bed Tax.
    - Doc Visit service has no tax.
    - Net Total = Room/Bed Charges Amount + Services Amount.
    """

    consumer_profile = generate_consumer_profile()

    result = complete_ip_invoice_taxable_bed_exempt_service_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
    )

    assert result["patient_created"] is True
    assert result["admission_created"] is True
    assert result["service_added"] is True
    assert result["discharged"] is True
    assert result["invoice_created"] is True
    assert result["invoice_paid"] is True
    assert result["returned_to_ip_details"] is True
    assert result["checked_out"] is True

    tax_result = result["tax_result"]

    assert tax_result["bed_tax_percentage"] == Decimal("5")
    assert tax_result["bed_tax_actual"] == tax_result["bed_tax_expected"]
    assert tax_result["bed_total_actual"] == tax_result["bed_total_expected"]

    assert tax_result["service_tax_actual"] == Decimal("0")
    assert tax_result["net_total_actual"] == tax_result["net_total_expected"]

    assert result["final_url"]

    print("Amounts are correct")   


# ***** IP invoice with exempt bed and taxable service; GST applies only on service *****

def test_ip_invoice_exempt_bed_taxable_service_tax_only_on_service_flow(page: Page, config) -> None:
    """
    Case:
    IP invoice with exempt bed and taxable service; GST applies only on service.

    Expected:
    - Bed has no tax.
    - Nursing Service has 5% GST.
    - Service rate shown in invoice is tax excluded.
    - Service tax = Service Rate * 5 / 100.
    - Service amount = Service Rate + Service Tax.
    - Net Total = Room/Bed Charges Amount + Services Amount.
    """

    consumer_profile = generate_consumer_profile()

    result = complete_ip_invoice_exempt_bed_taxable_service_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
    )

    assert result["patient_created"] is True
    assert result["admission_created"] is True
    assert result["service_added"] is True
    assert result["discharged"] is True
    assert result["invoice_created"] is True

    tax_result = result["tax_result"]

    assert tax_result["bed_tax_actual"] == Decimal("0")
    assert tax_result["service_tax_percentage"] == Decimal("5")
    assert tax_result["service_tax_actual"] == tax_result["service_tax_expected"]
    assert tax_result["service_total_actual"] == tax_result["service_total_expected"]
    assert tax_result["summary_tax_actual"] == tax_result["service_tax_expected"]
    assert tax_result["net_total_actual"] == tax_result["net_total_expected"]

    assert result["final_url"]

    print("Amounts are correct")  




# ----- IP invoice with both bed and services taxable; GST calculated correctly -----


def test_ip_invoice_taxable_bed_taxable_service_gst_calculated_correctly_flow(
    page: Page,
    config,
) -> None:
    """
    Case:
    IP invoice with both bed and services taxable; GST calculated correctly.

    Expected:
    - Bed has 5% GST.
    - Nursing Service has 5% GST.
    - Bed tax = Bed Rate * 5 / 100.
    - Bed total = Bed Rate + Bed Tax.
    - Service tax = Service Rate * 5 / 100.
    - Service total = Service Rate + Service Tax.
    - Net Total = Bed Total + Service Total.
    - If calculations are correct, invoice is paid by Cash.
    - Patient is checked out after payment.
    """

    consumer_profile = generate_consumer_profile()

    result = complete_ip_invoice_taxable_bed_taxable_service_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
    )

    assert result["patient_created"] is True
    assert result["admission_created"] is True
    assert result["service_added"] is True
    assert result["discharged"] is True
    assert result["invoice_created"] is True

    tax_result = result["tax_result"]

    assert tax_result["bed_tax_percentage"] == Decimal("5")
    assert tax_result["service_tax_percentage"] == Decimal("5")

    assert tax_result["bed_tax_actual"] == tax_result["bed_tax_expected"]
    assert tax_result["bed_total_actual"] == tax_result["bed_total_expected"]

    assert tax_result["service_tax_actual"] == tax_result["service_tax_expected"]
    assert tax_result["service_total_actual"] == tax_result["service_total_expected"]

    assert tax_result["summary_tax_actual"] == tax_result["summary_tax_expected"]
    assert tax_result["net_total_actual"] == tax_result["net_total_expected"]

    assert result["invoice_paid"] is True
    assert result["returned_to_ip_details"] is True
    assert result["checked_out"] is True

    assert result["final_url"]

    print("Amounts are correct")



# ------ IP invoice with both bed and services exempt; no GST applied -----    


def test_ip_invoice_exempt_bed_exempt_service_no_gst_applied_flow(
    page: Page,
    config,
) -> None:
    """
    Case:
    IP invoice with both bed and services exempt; no GST applied.

    Expected:
    - Bed has no tax.
    - Doc Visit service has no tax.
    - Net Total = Room/Bed Charges Amount + Services Amount.
    """

    consumer_profile = generate_consumer_profile()

    result = complete_ip_invoice_exempt_bed_exempt_service_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
    )

    assert result["patient_created"] is True
    assert result["admission_created"] is True
    assert result["service_added"] is True
    assert result["discharged"] is True
    assert result["invoice_created"] is True

    tax_result = result["tax_result"]

    assert tax_result["bed_tax_actual"] == Decimal("0")
    assert tax_result["service_tax_actual"] == Decimal("0")
    assert tax_result["net_total_actual"] == tax_result["net_total_expected"]

    assert result["final_url"]

    print("Amounts are correct")




# IP bed charges calculated for multiple days; tax and total match bed days



def test_ip_bed_charges_multiple_days_tax_total_match_bed_days_flow(
    page: Page,
    config,
) -> None:
    """
    Case:
    IP bed charges calculated for multiple days; tax and total match bed days.

    Expected:
    - Taxable bed is selected: Bed with Tax.
    - Checkin date is a past date.
    - Expected Checkout Date is today.
    - Quantity equals number of bed days including checkin date and today.
    - Bed charge = Bed Rate * Quantity.
    - Bed tax = Bed charge * 5 / 100.
    - Bed total = Bed charge + Bed tax.
    - Net Total = Bed total.
    - If calculations are correct, invoice is paid by Cash.
    - Patient is checked out after payment.
    """

    consumer_profile = generate_consumer_profile()

    result = complete_ip_invoice_taxable_bed_multiple_days_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
    )

    assert result["patient_created"] is True
    assert result["admission_created"] is True
    assert result["discharged"] is True
    assert result["invoice_created"] is True

    tax_result = result["tax_result"]

    assert tax_result["bed_tax_percentage"] == Decimal("5")
    assert tax_result["bed_quantity_actual"] == tax_result["bed_quantity_expected"]
    assert tax_result["bed_charge_actual"] == tax_result["bed_charge_expected"]
    assert tax_result["bed_tax_actual"] == tax_result["bed_tax_expected"]
    assert tax_result["bed_total_actual"] == tax_result["bed_total_expected"]
    assert tax_result["net_total_actual"] == tax_result["net_total_expected"]

    assert result["invoice_paid"] is True
    assert result["returned_to_ip_details"] is True
    assert result["checked_out"] is True

    assert result["final_url"]

    print("Amounts are correct")




# Master invoice created with order with taxable item and IP with non-taxable service; totals match individual invoices 



def test_master_invoice_one_taxable_order_item_and_one_ip_invoice_totals_match_flow(
    page: Page,
    config,
) -> None:
    """
    Case:
    Master invoice created with one order item with tax and one IP invoice;
    totals match individual invoices.

    Expected:
    - IP patient is created and admitted.
    - Doc Visit service is added.
    - Order request is created from IP service.
    - One taxable medicine item is selected from Med_1, Med_2, Med_4.
    - Sales order is confirmed.
    - Sales order invoice tax split is validated and captured.
    - IP invoice is generated.
    - Master invoice is generated by linking order invoice + IP invoice.
    - Master invoice pharmacy tax equals captured GST + CESS from order invoice.
    - Master invoice Net Total equals individual invoice totals.
    """

    consumer_profile = generate_consumer_profile()

    result = complete_master_invoice_taxable_order_item_and_ip_invoice_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
    )

    assert result["patient_created"] is True
    assert result["admission_created"] is True
    assert result["service_added"] is True
    assert result["order_requested"] is True
    assert result["sales_order_confirmed"] is True
    assert result["sales_order_invoice_created"] is True
    assert result["sales_order_completed"] is True
    assert result["ip_invoice_created"] is True
    assert result["master_invoice_created"] is True

    order_tax_result = result["order_invoice_tax_result"]
    master_tax_result = result["master_invoice_tax_result"]

    assert order_tax_result["tax_actual"] == order_tax_result["tax_expected"]
    assert master_tax_result["master_pharmacy_tax_actual"] == master_tax_result["master_pharmacy_tax_expected"]
    assert master_tax_result["master_net_total_actual"] == master_tax_result["master_net_total_expected"]

    assert result["final_url"]

    print("Both master invoice and individual invoice amounts are correct")



# Master invoice created with order with non-taxable item and IP with taxable service; totals match individual invoices    



    