import allure
import pytest

from framework.auth import login
from framework.test_data import generate_consumer_profile
from framework.appointment_actions import (
    select_first_business_card,
    open_take_appointment_from_dashboard_button,
    open_take_appointment_from_sidebar,
    click_create_new_patient,
    fill_new_patient_basic_details,
    select_random_appointment_options,
    add_appointment_note,
    upload_appointment_attachment,
    confirm_appointment,
    open_created_appointment_details,
    assert_appointment_details_opened,
    assert_created_patient_visible,
)


def complete_take_appointment_flow(page, config, appointment_data, open_take_appointment_action):
    """
    Common reusable flow for taking/creating an appointment.

    The opening action changes depending on the scenario:
    - dashboard Create Appointment button
    - sidebar Appointment link
    """

    consumer_profile = generate_consumer_profile()
    take_appointment_data = appointment_data["take_appointment"]

    allure.dynamic.title(
        f"Take appointment for new consumer: {consumer_profile['full_name']}"
    )

    with allure.step("Login as business user"):
        login(page, config)

    with allure.step("Select first business card"):
        select_first_business_card(page)

    with allure.step("Open take appointment flow"):
        open_take_appointment_action(page)

    with allure.step("Click Create New Patient"):
        click_create_new_patient(page)

    with allure.step(f"Fill new patient details: {consumer_profile['full_name']}"):
        fill_new_patient_basic_details(page, consumer_profile)

    with allure.step("Select appointment options"):
        selected_options = select_random_appointment_options(
            page,
            take_appointment_data,
        )

    with allure.step("Attach selected appointment options to report"):
        allure.attach(
            str(selected_options),
            name="Selected Appointment Options",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Add appointment note"):
        add_appointment_note(page, consumer_profile["note"])

    with allure.step("Upload appointment attachment"):
        upload_appointment_attachment(
            page,
            take_appointment_data["attachment_path"],
        )

    with allure.step("Confirm appointment"):
        confirm_appointment(page, consumer_profile)

    with allure.step("Open created appointment details"):
        open_created_appointment_details(page, consumer_profile)

    with allure.step("Verify appointment details page opened"):
        assert_appointment_details_opened(page)

    with allure.step("Verify created patient is visible"):
        assert_created_patient_visible(page, consumer_profile)


@allure.epic("Jaldee Business")
@allure.feature("Take Appointment")
@allure.story("Create appointment from dashboard")
@pytest.mark.smoke
@pytest.mark.appointment
def test_take_appointment_from_dashboard_create_button(page, config, appointment_data):
    """
    Happy path test.

    Opens appointment creation using the dashboard Create Appointment button.
    """

    complete_take_appointment_flow(
        page,
        config,
        appointment_data,
        open_take_appointment_from_dashboard_button,
    )


@allure.epic("Jaldee Business")
@allure.feature("Take Appointment")
@allure.story("Create appointment from sidebar")
@pytest.mark.smoke
@pytest.mark.appointment
def test_take_appointment_from_sidebar_appointment_link(page, config, appointment_data):
    """
    Happy path test.

    Opens appointment creation using the sidebar Appointment link.
    """

    complete_take_appointment_flow(
        page,
        config,
        appointment_data,
        open_take_appointment_from_sidebar,
    )