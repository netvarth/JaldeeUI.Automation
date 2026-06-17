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
    get_random_attachment_path_from_folder,
    perform_random_appointment_full_detail_actions,
    perform_random_appointment_reschedule,
    perform_new_mr_complete_case_flow,
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
        attachment_path = get_random_attachment_path_from_folder()

        upload_appointment_attachment(
            page,
            attachment_path,
        )

    with allure.step("Confirm appointment"):
        confirm_appointment(page, consumer_profile)

    with allure.step("Open created appointment details"):
        open_created_appointment_details(page, consumer_profile)

    with allure.step("Verify appointment details page opened"):
        assert_appointment_details_opened(page)

    with allure.step("Verify created patient is visible"):
        assert_created_patient_visible(page, consumer_profile)

    return {
        "consumer_profile": consumer_profile,
        "selected_options": selected_options,
        "attachment_path": attachment_path,
        "final_url": page.url,
    }


# @allure.epic("Jaldee Business")
# @allure.feature("Take Appointment")
# @allure.story("Create appointment from dashboard")
# @pytest.mark.smoke
# @pytest.mark.appointment
# def test_take_appointment_from_dashboard_create_button(page, config, appointment_data):
#     """
#     Happy path test.

#     Opens appointment creation using the dashboard Create Appointment button.
#     """

#     complete_take_appointment_flow(
#         page,
#         config,
#         appointment_data,
#         open_take_appointment_from_dashboard_button,
#     )


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


@allure.epic("Jaldee Business")
@allure.feature("Appointment Details")
@allure.story("Send message, send attachment, follow-up, invoice payment, and create case")
@pytest.mark.smoke
@pytest.mark.appointment
def test_random_appointment_full_detail_actions(page, config):
    """
    Appointment full detail action flow.
    """

    attachment_path = get_random_attachment_path_from_folder()

    with allure.step("Login as business user"):
        login(page, config)

    with allure.step("Select first business card"):
        select_first_business_card(page)

    with allure.step("Perform all detail actions on one random appointment"):
        action_result = perform_random_appointment_full_detail_actions(
            page,
            attachment_path,
        )

    with allure.step("Attach action result to report"):
        allure.attach(
            str(action_result),
            name="Appointment Full Detail Action Result",
            attachment_type=allure.attachment_type.TEXT,
        )



@allure.epic("Jaldee Business")
@allure.feature("Appointment Details")
@allure.story("Reschedule random appointment")
@pytest.mark.smoke
@pytest.mark.appointment
def test_random_appointment_reschedule(page, config):
    """
    Appointment reschedule flow.

    Steps:
    - Login
    - Select business
    - Open appointment dashboard from sidebar
    - Randomly select one appointment accordion/tab
    - Click View Details
    - Open More Actions
    - Click Reschedule
    - Select random future date
    - Select random time slot
    - Click Reschedule
    - Assert success message
    """

    with allure.step("Login as business user"):
        login(page, config)

    with allure.step("Select first business card"):
        select_first_business_card(page)

    with allure.step("Open random appointment and reschedule"):
        reschedule_result = perform_random_appointment_reschedule(page)

    with allure.step("Attach reschedule result to report"):
        allure.attach(
            str(reschedule_result),
            name="Appointment Reschedule Result",
            attachment_type=allure.attachment_type.TEXT,
        )



@allure.epic("Jaldee Business")
@allure.feature("New MR")
@allure.story("Enable New MR and complete case flow from random appointment")
@pytest.mark.smoke
@pytest.mark.appointment
def test_new_mr_complete_case_flow_from_random_appointment(page, config):
    """
    New MR full case flow.

    Steps:
    - Login
    - Select business
    - Enable New MR if needed
    - Randomly select appointment
    - Create case
    - Upload case file
    - New Visit
    - Add Clinical Notes
    - Add Chief Complaint
    - Add History
    - Add Medication
    - Add Vital Signs
    - Add Treatment Plan
    - Create Prescription
    - Upload Prescription
    - Share Case via Email
    """

    with allure.step("Login as business user"):
        login(page, config)

    with allure.step("Select first business card"):
        select_first_business_card(page)

    with allure.step("Perform New MR complete case flow"):
        result = perform_new_mr_complete_case_flow(page)

    with allure.step("Attach New MR result"):
        allure.attach(
            str(result),
            name="New MR Complete Case Result",
            attachment_type=allure.attachment_type.TEXT,
        )        


