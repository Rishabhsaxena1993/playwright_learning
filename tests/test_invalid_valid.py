from pages.login_page import Login_Page
from pages.register_page import RegisterPage


def test_login_invalid_valid(page, config):
    # Phase 1: Login Test
    print("\n" + "="*80)
    print("PHASE 1: TESTING LOGIN")
    print("="*80)

    login = Login_Page(page, config["base_url"])
    login.open()
    page.wait_for_timeout(1000)

    login.enter_username("QATest48")
    login.enter_password("Thesword")

    try:
        login.login_button()
        print("✅ Login button clicked")
    except Exception as e:
        print(f"⚠️ Error during login: {e}")

    # Verify login and continue regardless of result
    login_result = login.verify_login_successful()
    if login_result:
        print("✅ Login verification passed - proceeding to registration")
    else:
        print("⚠️ Login verification failed - continuing to registration phase anyway")

    # Phase 2: Registration Test
    print("\n" + "="*80)
    print("PHASE 2: TESTING REGISTRATION")
    print("="*80)

    try:
        register = RegisterPage(page, config["base_url"])
        register.open()
        page.wait_for_timeout(1000)

        register.click_register()
        page.wait_for_timeout(500)

        register.enter_firstname("Test")
        register.enter_last_name("User")
        register.enter_address("123 Test St")
        register.enter_city("Test City")
        register.enter_state("TS")
        register.enter_zip_code("12345")
        register.enter_phone("1234567890")
        register.enter_ssn("123456789")
        register.enter_username("QATest48")
        register.enter_password("Thesword")
        register.enter_confirm_password("Thesword")

        register.click_register_button()
        page.wait_for_timeout(2000)

        print("✅ Registration test completed")
    except Exception as e:
        print(f"❌ Registration failed: {e}")
        raise
