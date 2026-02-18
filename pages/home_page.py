from pages.base_page import BasePage

class HomePage(BasePage):

    ABOUT_US_LINK = "//ul[@class='leftmenu']//a[normalize-space()='About Us']"
    SERVICES = "//ul[@class='leftmenu']//a[normalize-space()='Services']"
    def click_about_us(self):
        self.page.click(self.ABOUT_US_LINK)

    def click_on_services(self):
        self.page.click(self.SERVICES)
