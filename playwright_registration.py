from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:

    chromium = playwright.chromium.launch(headless=False)

    page = chromium.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    ui_course_title = page.get_by_test_id('authentication-ui-course-title-text')
    expect(ui_course_title).to_have_text('UI Course')

    #Локаторы Email
    email_div = page.get_by_test_id('registration-form-email-input')
    email_input = email_div.locator('input')
    email_label = email_div.locator('label')

    #Проверки Email
    expect(email_input).to_be_visible
    expect(email_label).to_have_text('Email')
    email_input.fill('user.name@gmail.com')

    #Локаторы Username
    username_div = page.get_by_test_id('registration-form-username-input')
    username_input = username_div.locator('input')
    username_label = username_div.locator('label')

    #Проверки Username
    expect(username_input).to_be_visible
    expect(username_label).to_have_text('Username')
    username_input.fill('username')

    #Локаторы Password
    password_div = page.get_by_test_id('registration-form-password-input')
    password_input = password_div.locator('input')
    password_label = password_div.locator('label')

    #Проверки Password
    expect(password_input).to_be_visible
    expect(password_label).to_have_text('Password')
    password_input.fill('password')

    #Переход на дашборд
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()
    page.wait_for_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    #Проверка заголовка
    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_have_text('Dashboard')
