import allure
from data import MessageData
from methods.login_method import LoginMethods


class TestUserLogin:
    @allure.title('Test Successful login')
    @allure.description('Тут создаем тестовые данные для регистрации, регистрируемся на сайте, входим на сайт,'
                        'проверяем код и тело ответа')
    def test_user_login(self,generate_registration_data):
        with allure.step("Создаем пользователя"):
            #print(generate_registration_data)
            LoginMethods.register_new_user_and_return_login_password(generate_registration_data)
            #print(body.json())
        with allure.step("Логин под пользователем"):
            #print(generate_registration_data)
            body = LoginMethods.login_in_system(generate_registration_data['email'], generate_registration_data['password'])
            #print(body.json())
        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert body.status_code == 200
            assert body.json()["accessToken"] != 0
            assert body.json()["refreshToken"] != 0
            assert body.json()["success"] == True
            assert body.json()["user"]["email"] == generate_registration_data['email']
            assert body.json()["user"]["name"] == generate_registration_data['name']