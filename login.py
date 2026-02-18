from playwright.sync_api import sync_playwright
from pages.login_page import Login_Page
from pages.open_new_account import Open_New_Account

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=['--start-maximized'])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    page.goto("https://parabank.parasoft.com/")
    page.wait_for_timeout(3000)

    login = Login_Page(page, "")
    login.enter_username("QATest44")
    login.enter_password("Thesword")
    login.login_button()

    open_new_account = Open_New_Account(page, "")
    open_new_account.click_open_new_account()
    page.wait_for_timeout(2000)


    def select_account_type(value):
        page.select_option("#type", value=value)


    # sirf ek baar print
    options = page.locator("#type option").all_text_contents()
    for opt in options:
        print(opt)

    select_account_type("1")
    # select_account_type("0")
    page.wait_for_timeout(2000)

    open_new_account.click_open_account_button()
    open_new_account.verify_congratulation_message()
    open_new_account.click_newly_added_account_number()
    open_new_account.verify_printed_account_number()
    open_new_account.verify_balance()
