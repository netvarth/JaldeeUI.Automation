import pytest
from playwright.sync_api import expect

from framework.auth import (
    login,
    logout,
    assert_login_page_visible,
    login_with_invalid_credentials,
)

from framework.appointment_actions import (
    select_first_business_card,
    open_first_booking_from_dashboard,
    open_booking_by_patient_name_from_dashboard,
    assert_appointment_details_opened,
    go_back_from_appointment_details,
    assert_patient_not_visible_on_dashboard,
)


@pytest.mark.smoke
@pytest.mark.appointment
def test_view_first_appointment_details_from_dashboard(page, config):
    """
    Happy path test.

    Flow:
    1. Login
    2. Select first business card
    3. Click the first booking View button from dashboard
    4. Verify appointment details page opened
    5. Go back
    """

    login(page, config)

    select_first_business_card(page)

    open_first_booking_from_dashboard(page)

    assert_appointment_details_opened(page)

    go_back_from_appointment_details(page)


@pytest.mark.smoke
@pytest.mark.appointment
def test_view_known_patient_appointment_details_from_dashboard(page, config, appointment_data):
    """
    Opens a known patient's appointment from the dashboard.
    """

    known_patient = appointment_data["dashboard"]["known_dashboard_patient"]

    login(page, config)

    select_first_business_card(page)

    open_booking_by_patient_name_from_dashboard(page, known_patient)

    assert_appointment_details_opened(page)

    go_back_from_appointment_details(page)


@pytest.mark.appointment
def test_invalid_patient_appointment_should_not_be_visible(page, config, appointment_data):
    """
    Edge case test.

    Verifies that a non-existing patient is not shown on dashboard.
    """

    invalid_patient = appointment_data["dashboard"]["invalid_patient"]

    login(page, config)

    select_first_business_card(page)

    assert_patient_not_visible_on_dashboard(page, invalid_patient)


@pytest.mark.auth
def test_user_can_logout_successfully(page, config):
    """
    Logout test.

    Verifies user can login and logout successfully.
    """

    login(page, config)

    logout(page, fail_if_not_logged_out=True)

    assert_login_page_visible(page)


@pytest.mark.auth
def test_invalid_login_should_not_allow_user_inside(page, config):
    """
    Error scenario.

    Invalid credentials should not login successfully.
    """

    login_with_invalid_credentials(
        page,
        config,
        login_id="invalid_user",
        password="invalid_password",
    )

    expect(page.get_by_role("button", name="Sign In")).to_be_visible()