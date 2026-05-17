"""Simple runner for the login/logout smoke flow.

For day-to-day QA work, prefer running the pytest suite:
    pytest
"""

from playwright.sync_api import sync_playwright

from pages.auth_page import AuthPage
from qa_config import get_settings


def run() -> None:
    settings = get_settings()
    email, password = settings.require_credentials()

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=settings.headless,
            slow_mo=settings.slow_mo,
        )
        page = browser.new_page()
        page.set_default_timeout(settings.default_timeout)

        auth_page = AuthPage(page, settings.base_url)
        auth_page.open()
        auth_page.login(email, password)
        auth_page.expect_logged_in()
        auth_page.logout()
        auth_page.expect_logged_out()

        browser.close()


if __name__ == "__main__":
    run()
