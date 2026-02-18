from playwright.sync_api import sync_playwright
from pages.register_page import RegisterPage

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://parabank.parasoft.com/")
    page.wait_for_timeout(1000)

    register = RegisterPage(page, "")
    register.click_register()
    register.enter_firstname("QA")
    register.enter_last_name("Test")
    register.enter_address("ADADADA")
    register.enter_city("Crewe")
    register.enter_state("UP")
    register.enter_zip_code("12121")
    register.enter_phone("1234567890")
    register.enter_ssn("12345")
    register.enter_username("QATest44")
    register.enter_password("Thesword")
    register.enter_confirm_password("Thesword")
    register.click_register_button()
    page.wait_for_timeout(3000)

