import time

from pages.register_page import RegisterPage
from utils.fake_data import get_fake_user


def test_register(page, config):
    user = get_fake_user()

    register = RegisterPage(page, config["base_url"])
    register.register_user_wrapper(
        user["first_name"],
        user["last_name"],
        user["username"],
        user["password"],
        user["address"]
    )
