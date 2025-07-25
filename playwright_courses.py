from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:

    chromium = playwright.chromium.launch(headless=False)
    context = chromium.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input").locator("input")
    password_input.fill("password")

    registration_button = page.get_by_test_id("registration-page-registration-button")
    expect(registration_button).to_be_enabled()
    registration_button.click()
    
    page.wait_for_load_state("networkidle")

    context.storage_state(path="chromium_state.json")


with sync_playwright() as playwright:

    chromium = playwright.chromium.launch(headless=False)
    context = chromium.new_context(storage_state="chromium_state.json")
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    page.wait_for_load_state("networkidle")
    page.wait_for_url("**/courses")
    
    courses_page_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_page_title).to_be_visible()
    expect(courses_page_title).to_have_text("Courses")

    courses_list_title = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(courses_list_title).to_be_visible()
    expect(courses_list_title).to_have_text("There is no results")

    courses_list_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(courses_list_icon).to_be_visible()

    courses_list_description = page.get_by_test_id("courses-list-empty-view-description-text")
    expect(courses_list_description).to_be_visible()
    expect(courses_list_description).to_have_text("Results from the load test pipeline will be displayed here")
