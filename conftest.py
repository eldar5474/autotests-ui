import pytest
from playwright.sync_api import sync_playwright, Page, expect, Playwright
from collections.abc import Generator

pytest_plugins = (
    "fixtures.pages" 
)


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    chromium = playwright.chromium.launch(headless=False)
    context = chromium.new_context()
    page = context.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id(
        "registration-form-email-input").locator("input")
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id(
        "registration-form-username-input").locator("input")
    username_input.fill("username")

    password_input = page.get_by_test_id(
        "registration-form-password-input").locator("input")
    password_input.fill("password")

    registration_button = page.get_by_test_id(
        "registration-page-registration-button")
    expect(registration_button).to_be_enabled()
    registration_button.click()

    page.wait_for_load_state("networkidle")
    context.storage_state(path="chromium_state.json")
    chromium.close()


@pytest.fixture(scope='function')
def chromium_page_with_state(playwright: Playwright, initialize_browser_state) -> Generator[Page, None, None]:
    chromium = playwright.chromium.launch(headless=False)
    context = chromium.new_context(storage_state="chromium_state.json")
    yield context.new_page()
    chromium.close()


@pytest.fixture
def chromium_page(playwright: Playwright) -> Generator[Page, None, None]:
    chromium = playwright.chromium.launch(headless=False)
    yield chromium.new_page()
    chromium.close()
