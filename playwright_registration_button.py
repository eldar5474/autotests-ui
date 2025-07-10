from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwight:

    chromium = playwight.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    #Проверяем, что кнопка "Registration" находится в состоянии disabled
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    #Заполняем поле Email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.focus()
    expect(email_input).to_be_focused()
    for i in 'user.name@gmail.com':
        page.keyboard.type(i, delay=100)

    #Заполняем поле Username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.focus()
    expect(username_input).to_be_focused()
    for i in 'username':
        page.keyboard.type(i, delay=100)
    
    #Заполняем поле Password
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.focus()
    expect(password_input).to_be_focused()
    for i in 'password':
        page.keyboard.type(i, delay=100)

     #Проверяем, что кнопка "Registration" находится в состоянии enable
    expect(registration_button).to_be_enabled()

    registration_button.hover()
    

    