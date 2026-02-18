import time

from pages.home_page import HomePage
from pages.login_page import Login_Page

def test_home_page(page, config):
    login = Login_Page(page, config["base_url"])
    login.open()
    homepage = HomePage(page, config["base_url"])
    homepage.click_about_us()
    time.sleep(2)
    homepage.click_on_services()
    print("test is success")