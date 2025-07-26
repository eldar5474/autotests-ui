from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        # Локаторы Email
        self.email_div = page.get_by_test_id('registration-form-email-input')
        self.email_input = self.email_div.locator('input')
        self.email_label = self.email_div.locator('label')

        # Локаторы Username
        self.username_div = page.get_by_test_id(
            'registration-form-username-input')
        self.username_input = self.username_div.locator('input')
        self.username_label = self.username_div.locator('label')

        # Локаторы Password
        self.password_div = page.get_by_test_id(
            'registration-form-password-input')
        self.password_input = self.password_div.locator('input')
        self.password_label = self.password_div.locator('label')

        self.registration_button = page.get_by_test_id(
            'registration-page-registration-button')

    def fill_registration_username_input(self, username: str):
        expect(self.username_input).to_be_visible()
        expect(self.username_label).to_have_text('Username')
        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

    def fill_registration_email_input(self, email: str):
        expect(self.email_input).to_be_visible()
        expect(self.email_label).to_have_text('Email')
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

    def fill_registration_password_input(self, password: str):
        expect(self.password_input).to_be_visible()
        expect(self.password_label).to_have_text('Password')
        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_registration_button(self):
        self.registration_button.click()
