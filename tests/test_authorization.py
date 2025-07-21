from playwright.sync_api import sync_playwright, expect, Playwright, Page
import pytest

case = {
    "Verify user cannot login with invalid email and password": ("user.name@gmail.com", "password"),
    "Verify user cannot login with invalid email and empty password": ("user.name@gmail.com", "  "),
    "Verify user cannot login with empty email and invalid password": ("  ", "password")
}


@pytest.mark.parametrize("email, password", list(case.values()), ids=[f"{name} (email: '{email}', password: '{password}')" for name, (email, password) in case.items()])
def test_wrong_email_or_password_authorization(playwright: Playwright, page: Page, email: str, password: str):

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.get_by_test_id(
        'login-form-email-input').locator('input')
    email_input.fill(email)

    password_input = page.get_by_test_id(
        'login-form-password-input').locator('input')
    password_input.fill(password)

    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = page.get_by_test_id(
        'login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text(
        "Wrong email or password")
