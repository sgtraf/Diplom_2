import allure
from data import MessageData
from methods.login_method import LoginMethods


class TestRegistration:
    @allure.title('Test Successful registration')
    @allure.description('Тут создаем тестовые данные для регистрации, регистрируемся на сайте, проверяем код '
                        'и тело ответа')
    def test_user_registration(self,generate_registration_data):
        with allure.step("Создаем пользователя"):
            #print(generate_registration_data)
            body = LoginMethods.register_new_user_and_return_login_password(generate_registration_data)
            #print(body.json())
        with allure.step("Проверяем, что код ответа и тело соответствует документации"):
            assert body.status_code == 200 and body.json()["accessToken"] != 0
            assert body.json()["refreshToken"] != 0