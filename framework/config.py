import os

from dotenv import load_dotenv

load_dotenv()


def get_env_value(key, default=None):
    value = os.getenv(key, default)

    if value is None or value == "":
        raise ValueError(f"Missing required environment variable: {key}")

    return value


def get_test_env():
    return os.getenv("TEST_ENV", "scale").lower()


def get_provider_url(test_env):
    if test_env == "scale":
        return get_env_value("SCALE_PROVIDER_URL")

    if test_env == "prod":
        return get_env_value("PROD_PROVIDER_URL")

    raise ValueError(
        f"Invalid TEST_ENV: {test_env}. Allowed values: scale, prod"
    )


def get_consumer_url(test_env):
    if test_env == "scale":
        return get_env_value("SCALE_CONSUMER_URL")

    if test_env == "prod":
        return get_env_value("PROD_CONSUMER_URL")

    raise ValueError(
        f"Invalid TEST_ENV: {test_env}. Allowed values: scale, prod"
    )


def get_provider_account(test_env, account_name):
    """
    Returns provider login credentials.

    account_name options:
    - booking
    - order
    - ip
    """

    account_name = account_name.lower()

    account_map = {
        "scale": {
            "booking": {
                "login_id": get_env_value("SCALE_BOOKING_LOGIN_ID"),
                "password": get_env_value("SCALE_BOOKING_PASSWORD"),
            },
            "order": {
                "login_id": get_env_value("SCALE_ORDER_LOGIN_ID"),
                "password": get_env_value("SCALE_ORDER_PASSWORD"),
            },
            "ip": {
                "login_id": get_env_value("SCALE_IP_LOGIN_ID"),
                "password": get_env_value("SCALE_IP_PASSWORD"),
            },
        },
        "prod": {
            "booking": {
                "login_id": get_env_value("PROD_BOOKING_LOGIN_ID"),
                "password": get_env_value("PROD_BOOKING_PASSWORD"),
            },
        },
    }

    if test_env not in account_map:
        raise ValueError(
            f"Invalid TEST_ENV: {test_env}. Allowed values: scale, prod"
        )

    if account_name not in account_map[test_env]:
        raise ValueError(
            f"Invalid account '{account_name}' for environment '{test_env}'. "
            f"Allowed accounts: {list(account_map[test_env].keys())}"
        )

    return account_map[test_env][account_name]


def get_consumer_phone(test_env):
    if test_env == "scale":
        return get_env_value("SCALE_CONSUMER_PHONE")

    if test_env == "prod":
        return get_env_value("PROD_CONSUMER_PHONE")

    raise ValueError(
        f"Invalid TEST_ENV: {test_env}. Allowed values: scale, prod"
    )


def get_config(account_name="booking"):
    """
    Returns full test config.

    Default account is booking.
    For order tests, pass account_name='order'.
    For IP tests, pass account_name='ip'.
    """

    test_env = get_test_env()
    provider_account = get_provider_account(test_env, account_name)

    return {
        "test_env": test_env,
        "account_name": account_name,

        "login_url": get_provider_url(test_env),
        "login_id": provider_account["login_id"],
        "password": provider_account["password"],

        "consumer_url": get_consumer_url(test_env),
        "consumer_phone": get_consumer_phone(test_env),

        "default_timeout_ms": int(os.getenv("DEFAULT_TIMEOUT_MS", "15000")),

        "report_output_dir": os.getenv("REPORT_OUTPUT_DIR", "reports/current"),
        "report_artifact_dir": os.getenv("REPORT_ARTIFACT_DIR", "reports/artifacts"),
    }