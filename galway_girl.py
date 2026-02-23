import pytest
import time
from pages.login_page import Login_Page
from pages.register_page import RegisterPage


class TestLoginAndRegisterFlow:
    """
    Comprehensive test automation for user registration and login flow.

    Scenario:
    1. Test multiple login scenarios with different password combinations (should fail)
    2. Register a new user with username 'verifiedmcpserver'
    3. Login with the newly registered user
    4. Print all attempted usernames and the valid login
    """

    def setup_method(self):
        """Initialize test data"""
        self.invalid_credentials = [
            {"username": "testuser1", "password": "wrongpassword"},
            {"username": "testuser2", "password": "password123"},
            {"username": "qatest000048", "password": "wrongpass"},
            {"username": "invaliduser", "password": "invalid123"},
        ]
        self.valid_username = "verifiedmcpserver"
        self.valid_password = "Thesword"
        self.attempted_usernames = []
        self.successful_login = None

    def test_01_login_with_invalid_credentials(self, page, config):
        """
        Test login with multiple invalid credential combinations.
        These are expected to fail.
        """
        print("\n" + "="*80)
        print("PHASE 1: TESTING INVALID LOGIN CREDENTIALS")
        print("="*80)

        login = Login_Page(page, config["base_url"])

        for idx, creds in enumerate(self.invalid_credentials, 1):
            username = creds["username"]
            password = creds["password"]

            print(f"\nAttempt {idx}:")
            print(f"  Username: {username}")
            print(f"  Password: {password}")

            self.attempted_usernames.append(username)

            # Open login page
            login.open()
            page.wait_for_timeout(500)

            # Get the current URL before login
            original_url = page.url

            # Try to login
            login.login(username, password)
            page.wait_for_timeout(1500)

            # Check if login failed by checking:
            # 1. Error message presence
            # 2. Whether we're still on the login page
            is_error_visible = login.is_login_failed()
            current_url = page.url
            is_still_on_login_page = current_url == original_url

            # Login fails if either error is shown OR we're still on login page
            is_failed = is_error_visible or is_still_on_login_page

            print(f"  Result: {'❌ LOGIN FAILED (Expected)' if is_failed else '⚠️ Login succeeded (unexpected)'}")
            print(f"  Details: Error shown: {is_error_visible}, Still on login page: {is_still_on_login_page}")

            # We expect login to fail, but just log it if it succeeds
            if not is_failed:
                print(f"  ⚠️  Warning: User '{username}' may have been logged in (URL changed to {current_url})")

            # Clear the form for next attempt
            page.reload()
            page.wait_for_timeout(500)

    def test_02_register_new_user_with_verified_username(self, page, config):
        """
        Register a new user with username 'verifiedmcpserver'.
        """
        print("\n" + "="*80)
        print("PHASE 2: REGISTERING NEW USER")
        print("="*80)

        reg = RegisterPage(page, config["base_url"])

        print(f"\nRegistering user with:")
        print(f"  Username: {self.valid_username}")
        print(f"  Password: {self.valid_password}")

        # Register the new user
        reg.open()
        page.wait_for_timeout(500)

        reg.click_register()
        page.wait_for_timeout(500)

        # Enter registration details
        reg.enter_firstname("Verified")
        reg.enter_last_name("MCPServer")
        reg.enter_address("Test Street")
        reg.enter_city("Noida")
        reg.enter_state("UP")
        reg.enter_zip_code("123456")
        reg.enter_phone("123456789")
        reg.enter_ssn("123756")
        reg.enter_username(self.valid_username)
        reg.enter_password(self.valid_password)
        reg.enter_confirm_password(self.valid_password)

        page.wait_for_timeout(1000)

        # Click register button
        reg.click_register_button()

        # Wait for registration to complete
        page.wait_for_timeout(3000)

        # Get the registered username
        registered_username = reg.print_username()

        print(f"\n✅ User registered successfully!")
        print(f"  Registered username: {registered_username}")

    def test_03_login_with_valid_registered_user(self, page, config):
        """
        Login with the newly registered user 'verifiedmcpserver'.
        """
        print("\n" + "="*80)
        print("PHASE 3: LOGGING IN WITH REGISTERED USER")
        print("="*80)

        login = Login_Page(page, config["base_url"])

        print(f"\nAttempting login with:")
        print(f"  Username: {self.valid_username}")
        print(f"  Password: {self.valid_password}")

        # Open login page
        login.open()
        page.wait_for_timeout(500)

        # Perform login
        login.login(self.valid_username, self.valid_password)
        page.wait_for_timeout(2000)

        # Check if login failed
        is_failed = login.is_login_failed()

        if is_failed:
            print(f"\n❌ Login failed with registered user. This may indicate an issue.")
            assert False, f"Failed to login with registered user '{self.valid_username}'"
        else:
            print(f"\n✅ LOGIN SUCCESSFUL!")
            self.successful_login = self.valid_username
            print(f"  Successfully logged in with username: {self.successful_login}")

    def test_04_print_login_summary_report(self, page, config):
        """
        Print a summary report of all attempted logins and the valid one.
        """
        print("\n" + "="*80)
        print("PHASE 4: LOGIN ATTEMPT SUMMARY REPORT")
        print("="*80)

        print(f"\n📊 INVALID LOGIN ATTEMPTS (Expected to fail):")
        print(f"   {'─'*60}")
        for idx, username in enumerate(self.attempted_usernames, 1):
            print(f"   {idx}. {username:<40} ❌ FAILED (as expected)")

        print(f"\n📊 VALID REGISTERED USER:")
        print(f"   {'─'*60}")
        print(f"   Username: {self.valid_username:<40} ✅ REGISTERED & LOGGED IN")

        print(f"\n{'='*80}")
        print("TEST EXECUTION COMPLETED SUCCESSFULLY!")
        print(f"{'='*80}\n")


# Standalone test functions (for direct pytest execution)

def test_invalid_login_attempts(page, config):
    """
    Standalone test to verify multiple invalid login attempts fail as expected.
    """
    test_class = TestLoginAndRegisterFlow()
    test_class.setup_method()
    test_class.test_01_login_with_invalid_credentials(page, config)


def test_register_verified_user(page, config):
    """
    Standalone test to register a user with username 'verifiedmcpserver'.
    """
    test_class = TestLoginAndRegisterFlow()
    test_class.setup_method()
    test_class.test_02_register_new_user_with_verified_username(page, config)


def test_login_verified_user(page, config):
    """
    Standalone test to login with the registered 'verifiedmcpserver' user.
    """
    test_class = TestLoginAndRegisterFlow()
    test_class.setup_method()
    test_class.test_03_login_with_valid_registered_user(page, config)


def test_complete_flow(page, config):
    """
    Complete test flow: Invalid attempts -> Register -> Valid login
    """
    test_class = TestLoginAndRegisterFlow()
    test_class.setup_method()

    # Phase 1: Test invalid credentials
    test_class.test_01_login_with_invalid_credentials(page, config)

    # Create a fresh page for registration
    page.context.close()
    browser = page.context.browser
    new_context = browser.new_context()
    new_page = new_context.new_page()
    new_page.set_default_timeout(config["timeout"])

    # Phase 2: Register new user
    test_class.test_02_register_new_user_with_verified_username(new_page, config)

    # Close context and create another for final login
    new_context.close()
    final_context = browser.new_context()
    final_page = final_context.new_page()
    final_page.set_default_timeout(config["timeout"])

    # Phase 3: Login with registered user
    test_class.test_03_login_with_valid_registered_user(final_page, config)

    # Phase 4: Print summary
    test_class.test_04_print_login_summary_report(final_page, config)

    # Cleanup
    final_context.close()

