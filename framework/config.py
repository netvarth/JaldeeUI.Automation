import os
from dotenv import load_dotenv


load_dotenv()


def get_config():
    """
    Reads test configuration from .env file.

    We are keeping this simple:
    - No classes
    - No app version
    - No business card index
    """

    return {
        "login_url": os.getenv(
            "BASE_URL",
            "https://scale.jaldee.com/business/login"
        ),

        "login_id": os.getenv("TEST_LOGIN_ID", ""),
        "password": os.getenv("TEST_PASSWORD", ""),

        "default_timeout_ms": int(os.getenv("DEFAULT_TIMEOUT_MS", "15000")),
    }