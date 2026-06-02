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
    open_appointment_by_patient_name,
    click_view_details_or_assign_myself,
    assert_appointment_details_opened,
    go_back_from_appointment_details,
    assert_appointment_not_visible,
)


@pytest.mark.smoke
@pytest.mark.appointment
def test_view_appointment_details_happy_path(page, config):
    """
    Happy path test.

    Flow:
    1. Login
    2. Select first business card
    3. Open appointment for John Miller
    4. Click View Details / Assign Myself View Details
    5. Verify details page opened
    6. Go back
    """

    login(page, config)

    select_first_business_card(page)

    open_appointment_by_patient_name(page, "John Miller")

    click_view_details_or_assign_myself(page)

    assert_appointment_details_opened(page)

    go_back_from_appointment_details(page)


@pytest.mark.appointment
def test_invalid_patient_appointment_should_not_be_visible(page, config):
    """
    Edge case test.

    Verifies that a non-existing appointment is not shown.
    """

    login(page, config)

    select_first_business_card(page)

    assert_appointment_not_visible(page, "Patient Name That Should Not Exist")


@pytest.mark.auth
def test_user_can_logout_successfully(page, config):
    """
    Logout test.

    Verifies user can login and logout successfully.
    """

    login(page, config)

    logout(page)

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
        password="invalid_password"
    )

    expect(page.get_by_role("button", name="Sign In")).to_be_visible()