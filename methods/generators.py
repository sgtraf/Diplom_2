from faker import Faker


class GenerateBody:
    @staticmethod
    def generate_user_data():
        fake = Faker()

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

    @staticmethod
    def generate_lonely_user_data():
        fake = Faker()

        email = fake.email(domain='efefefefefefefefefefeggg.tu')
        name = fake.first_name()
        password = fake.password()

        # собираем тело запроса
        payload_email = {
                "email": email
                }
        payload_password = {
                "password": password
                }
        payload_name = {
                "name": name
                }

        return {'email': payload_email, 'password': payload_password, 'name': payload_name}
