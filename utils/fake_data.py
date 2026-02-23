from faker import Faker

fake = Faker()


def get_fake_user():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "address": fake.address(),
        "username": fake.user_name(),
        "password": "Test@123"
    }
