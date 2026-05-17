import pytest

from pages.auth_page import AuthPage
from qa_config import get_settings


@pytest.mark.smoke
def test_user_can_login_and_logout(page):
    settings = get_settings()
    email, password = settings.require_credentials()

    auth_page = AuthPage(page, settings.base_url)
    auth_page.open()
    auth_page.login(email, password)
    auth_page.expect_logged_in()
    auth_page.logout()
    auth_page.expect_logged_out()
