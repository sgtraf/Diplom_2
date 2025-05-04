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
        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert body.status_code == 200
            assert body.json()["accessToken"] != 0
            assert body.json()["refreshToken"] != 0
            assert body.json()["success"] == True
            assert body.json()["user"]["email"] == generate_registration_data['email']
            assert body.json()["user"]["name"] == generate_registration_data['name']

    def test_second_user_registration_with_same_data(self,generate_registration_data):
        with allure.step("Создаем пользователя"):
            LoginMethods.register_new_user_and_return_login_password(generate_registration_data)
        with allure.step("Создаем повторно пользователя с теми же данными"):
            body = LoginMethods.register_new_user_and_return_login_password(generate_registration_data)
        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert body.status_code == 403
            assert body.json()["message"] == MessageData.MESSEGE_TEXT_403
            assert body.json()["success"] == False

    def test_registration_without_email(self,generate_registration_data_without_delete_method):
        generate_registration_data_without_delete_method["email"] = ''
        with allure.step("Пытаемся создать пользователя без почты"):
            body = LoginMethods.register_new_user_and_return_login_password(generate_registration_data_without_delete_method)

        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert body.status_code == 403
            assert body.json()["message"] == MessageData.MESSEGE_TEXT_403_WITHOUT_ONE
            assert body.json()["success"] == False

    def test_registration_without_password(self,generate_registration_data_without_delete_method):
        generate_registration_data_without_delete_method["password"] = ''
        with allure.step("Пытаемся создать пользователя без пароля"):
            body = LoginMethods.register_new_user_and_return_login_password(generate_registration_data_without_delete_method)

        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert body.status_code == 403
            assert body.json()["message"] == MessageData.MESSEGE_TEXT_403_WITHOUT_ONE
            assert body.json()["success"] == False

    def test_registration_without_name(self,generate_registration_data_without_delete_method):
        generate_registration_data_without_delete_method["name"] = ''
        with allure.step("Пытаемся создать пользователя без имени"):
            body = LoginMethods.register_new_user_and_return_login_password(generate_registration_data_without_delete_method)

        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert body.status_code == 403
            assert body.json()["message"] == MessageData.MESSEGE_TEXT_403_WITHOUT_ONE
            assert body.json()["success"] == False
