import re

from playwright.sync_api import Page, expect


class AuthPage:
    """Page object for authentication flows."""

    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        self.login_link = page.locator("a.login")
        self.email_input = page.locator('input[name="email"]')
        self.password_input = page.locator('input[name="password"]')
        self.submit_button = page.locator('button[type="submit"]')
        self.profile_dropdown = page.get_by_text("Company Manager")
        self.logout_button = page.get_by_role("button", name="Log Out")

    def open(self) -> None:
        self.page.goto(self.base_url, wait_until="domcontentloaded")
        expect(self.login_link).to_be_visible()

    def login(self, email: str, password: str) -> None:
        self.login_link.click()
        expect(self.email_input).to_be_visible()
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()

    def expect_logged_in(self) -> None:
        expect(self.profile_dropdown).to_be_visible()

    def logout(self) -> None:
        self.profile_dropdown.click()
        expect(self.logout_button).to_be_visible()
        self.logout_button.click()

    def expect_logged_out(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*/login.*"))
        expect(self.email_input).to_be_visible()
