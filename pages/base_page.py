class BasePage:
    def __init__(self, page, base_url=None):
        self.page = page
        self.base_url = base_url

    def click(self, locator):
        """Waits for element and clicks"""
        self.page.wait_for_selector(locator)
        self.page.click(locator)

    def type(self, locator, text):
        """Waits and fills text into input"""
        self.page.wait_for_selector(locator)
        self.page.fill(locator, text)

    def wait_for(self, locator, timeout=5000):
        """Explicit wait"""
        self.page.wait_for_selector(locator, timeout=timeout)

    def get_text(self, locator):
        """Returns text of an element"""
        self.page.wait_for_selector(locator)
        return self.page.inner_text(locator)

    def is_visible(self, locator):
        """Returns boolean instead of throwing error"""
        try:
            return self.page.is_visible(locator)
        except:
            return False

    def assert_text(self, locator, expected):
        """Assertion helper"""
        actual = self.get_text(locator)
        assert actual == expected, f"❌ Expected: {expected}, Got: {actual}"
