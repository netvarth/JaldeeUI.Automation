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
def test_view_jisha_rajan_appointment_details_from_dashboard(page, config):
    """
    Opens Jisha Rajan's appointment from the dashboard.

    Flow:
    1. Login
    2. Select first business card
    3. Find Jisha Rajan's booking on dashboard
    4. Click the related View button
    5. Verify appointment details page opened
    6. Go back
    """

    login(page, config)

    select_first_business_card(page)

    open_booking_by_patient_name_from_dashboard(page, "Jisha Rajan")

    assert_appointment_details_opened(page)

    go_back_from_appointment_details(page)


@pytest.mark.appointment
def test_invalid_patient_appointment_should_not_be_visible(page, config):
    """
    Edge case test.

    Verifies that a non-existing patient is not shown on dashboard.
    """

    login(page, config)

    select_first_business_card(page)

    assert_patient_not_visible_on_dashboard(page, "Patient Name That Should Not Exist")


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