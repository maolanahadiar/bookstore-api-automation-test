from faker import Faker
import random
import string

fake = Faker()

class DataGenerator:

    @staticmethod
    def username():
        return f"{fake.user_name()}{random.randint(100000,999999)}"

    @staticmethod
    def password(length=12):
        special = "!@#$%^&*"

        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(special),
        ]

        remaining = length - len(password)

        password += random.choices(
            string.ascii_letters + string.digits + special,
            k=remaining,
        )

        random.shuffle(password)

        return "".join(password)