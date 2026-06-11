import os
from dotenv import load_dotenv


load_dotenv()


def get_config():
    """
    Reads test configuration from .env file.
    """

    return {
        "login_url": os.getenv(
            "BASE_URL",
            "https://scale.jaldee.com/business/login"
        ),

        "login_id": os.getenv("TEST_LOGIN_ID", ""),
        "password": os.getenv("TEST_PASSWORD", ""),

        "default_timeout_ms": int(os.getenv("DEFAULT_TIMEOUT_MS", "15000")),
        "test_env": os.getenv("TEST_ENV", "scale"),

        "report_output_dir": os.getenv("REPORT_OUTPUT_DIR", "reports/current"),
        "report_artifact_dir": os.getenv("REPORT_ARTIFACT_DIR", "reports/artifacts"),
    }