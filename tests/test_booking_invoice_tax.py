from decimal import Decimal

import pytest
from playwright.sync_api import Page

from framework.auth import login
from framework.booking_invoice_tax_actions import (
    complete_single_service_booking_invoice_flow,
    complete_taxable_booking_service_invoice_flow,
    complete_two_taxable_services_booking_invoice_flow,
    complete_booking_master_invoice_with_two_invoices_flow,
)
from framework.test_data import generate_consumer_profile


# Case 1 :: Create an invoice and do the payment

@pytest.mark.booking
@pytest.mark.invoice
def test_create_booking_invoice_for_single_service(
    page: Page,
    config,
) -> None:
    """
    Case:
    Create a booking invoice for a single service and complete payment.

    Expected:
    - A random patient is created.
    - An appointment is created for Naveen KP.
    - A single service is selected.
    - The latest appointment is opened.
    - An invoice is generated successfully.
    - Payment is completed using Cash or Pay by Others.
    - Invoice Amount Due becomes zero.
    """

    consumer_profile = generate_consumer_profile()

    login(page, config)

    result = complete_single_service_booking_invoice_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
        doctor_name="Naveen KP",
        service_name="Video call Services",
    )

    assert result["invoice_created"] is True
    assert result["payment_completed"] is True
    assert result["amount_due"] == 0



# Case 2 :: Create an invoice and add 1 more service into it and do the payment    


import pytest
from playwright.sync_api import Page

from framework.auth import login
from framework.booking_invoice_tax_actions import (
    complete_booking_invoice_with_additional_service_flow,
)
from framework.test_data import generate_consumer_profile


@pytest.mark.booking
@pytest.mark.invoice
def test_create_booking_invoice_add_one_more_service_and_complete_payment(
    page: Page,
    config,
) -> None:
    """
    Case:
    Create a booking invoice with one appointment service, add one more
    service to the invoice, and complete payment.

    Expected:
    - A random patient is created.
    - An appointment is created for Naveen KP.
    - Video call Services is selected for the appointment.
    - Booking invoice is opened.
    - Consultation is added as an additional invoice item.
    - Net Total equals the total of both invoice items.
    - Invoice is updated successfully.
    - Payment is completed.
    - Amount Due becomes zero.
    """

    consumer_profile = generate_consumer_profile()

    login(page, config)

    result = complete_booking_invoice_with_additional_service_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
        doctor_name="Naveen KP",
        appointment_service_name="Video call Services",
        additional_service_name="Consultation",
    )

    assert result["invoice_created"] is True
    assert result["additional_service_added"] is True
    assert result["payment_completed"] is True
    assert result["amount_due"] == 0


# Case 3 :: Create invoice for a taxable service and check the calculations are correct


@pytest.mark.booking
@pytest.mark.invoice
@pytest.mark.invoice_tax
def test_create_invoice_for_taxable_service_and_verify_calculations(
    page: Page,
    config,
) -> None:
    """
    Case:
    Create an invoice for a taxable booking service and verify the tax
    calculations before completing payment.

    Expected:
    - WhatsApp Service(Taxable) is booked for Naveen KP.
    - The displayed service rate is tax-exclusive.
    - Tax equals Rate * 5 / 100.
    - Total equals Rate + Tax.
    - Net Total equals the taxable service total.
    - Invoice is updated successfully.
    - Payment completes successfully.
    - Amount Due becomes zero.
    """

    consumer_profile = generate_consumer_profile()

    login(page, config)

    result = complete_taxable_booking_service_invoice_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
        doctor_name="Naveen KP",
        service_name="WhatsApp Service(Taxable)",
        tax_percentage=Decimal("5.00"),
    )

    assert result["invoice_created"] is True
    assert result["tax_calculation_valid"] is True
    assert result["total_calculation_valid"] is True
    assert result["payment_completed"] is True
    assert result["amount_due"] == Decimal("0.00")


# Case 4 :: Create an invoice for a taxable service and add 1 more taxable service into it and check the calculations  



@pytest.mark.booking
@pytest.mark.invoice
@pytest.mark.invoice_tax
def test_create_invoice_with_two_taxable_services_and_verify_calculations(
    page: Page,
    config,
) -> None:
    """
    Case:
    Create a booking invoice for one taxable service, add another taxable
    service, validate both service tax calculations and the invoice Net Total,
    and complete payment.

    Expected:
    - WhatsApp Service(Taxable) is booked for Naveen KP.
    - General Service with Tax is added to the invoice.
    - Both services have 5% tax.
    - Each service tax equals Rate * 5 / 100.
    - Each service total equals Rate + Tax.
    - Net Total equals the sum of both service totals.
    - Payment completes successfully.
    - Amount Due becomes zero.
    """

    consumer_profile = generate_consumer_profile()

    login(page, config)

    result = complete_two_taxable_services_booking_invoice_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
        doctor_name="Naveen KP",
        appointment_service_name="WhatsApp Service(Taxable)",
        additional_service_name="General Service with Tax",
        appointment_service_tax_percentage=Decimal("5.00"),
        additional_service_tax_percentage=Decimal("5.00"),
    )

    assert result["appointment_service_tax_valid"] is True
    assert result["appointment_service_total_valid"] is True
    assert result["additional_service_tax_valid"] is True
    assert result["additional_service_total_valid"] is True
    assert result["net_total_valid"] is True
    assert result["invoice_created"] is True
    assert result["payment_completed"] is True
    assert result["amount_due"] == Decimal("0.00")


 
 	
# Case 5 :: Create an invoice with a non-taxable service. Then create a new invoice with another non-taxable service. Then create a Master Invoice with merging these 2 invoices    


@pytest.mark.booking
@pytest.mark.invoice
@pytest.mark.master_invoice
def test_create_master_invoice_from_two_booking_invoices_and_complete_payment(
    page: Page,
    config,
    ) -> None:
    """
    Case:
    Create two invoices against one booking, consolidate them into a
    Master Invoice, validate the combined total, and complete payment.

    Invoice 1:
    - Video call Services

    Invoice 2:
    - Consultation

    Expected:
    - Both invoices are created successfully.
    - Both invoices are linked to a Master Invoice.
    - Master Invoice total equals:
      Video call Services rate + Consultation rate.
    - Payment completes successfully.
    - Master Invoice Amount Due becomes zero.
    """

    consumer_profile = generate_consumer_profile()

    login(page, config)

    result = complete_booking_master_invoice_with_two_invoices_flow(
        page=page,
        config=config,
        consumer_profile=consumer_profile,
        doctor_name="Naveen KP",
        first_service_name="Video call Services",
        second_service_name="Consultation",
    )

    assert result["first_invoice_created"] is True
    assert result["second_invoice_created"] is True
    assert result["master_invoice_created"] is True
    assert result["master_total_valid"] is True
    assert result["payment_completed"] is True
    assert result["amount_due"] == Decimal("0.00")

# Case 6 :: Create an invoice with a non-taxable service. Then create a new invoice with another taxable service. Then create a Master Invoice with merging these 2 invoices




