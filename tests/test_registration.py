from playwright.sync_api import sync_playwright, expect, Playwright, Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashBoardPage


def test_successful_registration(playwright: Playwright, registration_page: RegistrationPage, dashboard_page: DashBoardPage):

    registration_page.visit(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_username_input('username')
    registration_page.fill_registration_email_input('user.name@gmail.com')
    registration_page.fill_registration_password_input('password')
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title()
