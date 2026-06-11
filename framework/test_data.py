import json
import random
import re
from pathlib import Path

from faker import Faker


fake = Faker("en_IN")


def load_json_test_data(file_name):
    """
    Loads test data from the data folder.

    Example:
        load_json_test_data("appointment_test_data.json")
    """

    file_path = Path("data") / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Test data file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def generate_consumer_profile():
    """
    Generates random consumer/customer details.

    This can be reused across features like:
    - take appointment
    - invoice
    - orders
    - membership
    - customer/consumer flows

    Rules:
    - Email must always end with .test@jaldee.com
    - Phone number must always start with 555
    - Address should be India-based
    - Gender is random
    - DOB is random adult DOB
    """

    gender = random.choice(["Male", "Female"])

    if gender == "Female":
        first_name = fake.first_name_female()
    else:
        first_name = fake.first_name_male()

    last_name = fake.last_name()

    unique_number = random.randint(100000, 999999)

    email_first = clean_email_part(first_name)
    email_last = clean_email_part(last_name)

    email = f"{email_first}.{email_last}.{unique_number}.test@jaldee.com"

    phone_number = generate_jaldee_test_phone_number()
    pincode = generate_indian_pincode()

    dob_date = fake.date_of_birth(minimum_age=18, maximum_age=75)
    dob = dob_date.strftime("%d/%m/%Y")

    address = (
        f"{fake.street_address()}\n"
        f"{fake.city()}, Kerala\n"
        f"Pincode: {pincode}\n"
        f"India"
    )

    note = f"Automation test note {unique_number}"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": f"{first_name} {last_name}",
        "email": email,
        "phone": phone_number,
        "address": address,
        "pincode": pincode,
        "gender": gender,
        "dob": dob,
        "note": note,
    }


def clean_email_part(value):
    """
    Converts a name into a safe email part.
    """

    cleaned = re.sub(r"[^a-zA-Z0-9]", "", value).lower()

    if not cleaned:
        cleaned = "consumer"

    return cleaned


def generate_jaldee_test_phone_number():
    """
    Generates a 10-digit test phone number starting with 555.
    """

    remaining_digits = random.randint(1000000, 9999999)

    return f"555{remaining_digits}"


def generate_indian_pincode():
    """
    Generates a 6-digit Indian-style pincode.
    """

    return str(random.randint(100000, 999999))