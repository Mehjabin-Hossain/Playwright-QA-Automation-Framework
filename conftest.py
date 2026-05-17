import pytest

from qa_config import get_settings


@pytest.fixture(autouse=True)
def configure_page(page):
    page.set_default_timeout(get_settings().default_timeout)
