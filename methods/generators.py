from faker import Faker
import json


class GenerateBody:
    @staticmethod
    def generate_user_data():
        fake = Faker(locale='Ru')

        email = fake.email(domain='mail.ru')
        name = fake.first_name()
        password = fake.password()

        # собираем тело запроса
        payload = {
                "email": email,
                "password": password,
                "name": name
                }

        return payload

print(json.dumps(GenerateBody.generate_user_data()))