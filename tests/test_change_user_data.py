import allure
from data import MessageData
from methods.login_method import LoginMethods


class TestChangeUserData:
    @allure.title('Test Change User Data')
    @allure.description('Nen меняем данные пользователя, регистрируемся на сайте, входим на сайт, проверяем можно ли'
                        ' изменить поля сведений для пользователя' 
                        'проверяем код и тело ответа. Затем удаляем пользователя')
    def test_change_user_email(self,generate_registration_data):
        with allure.step("Создаем пользователя"):
            LoginMethods.register_new_user_and_return_login_password(generate_registration_data)
        with allure.step("Логин под пользователем"):
            body = LoginMethods.login_in_system(generate_registration_data['email'], generate_registration_data['password'])

        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert body.status_code == 200
            assert body.json()["accessToken"] != 0
            assert body.json()["refreshToken"] != 0
            assert body.json()["success"] == True
            assert body.json()["user"]["email"] == generate_registration_data['email']
            assert body.json()["user"]["name"] == generate_registration_data['name']

    def test_user_login_with_wrong_data(self, generate_registration_data_without_delete_method):
        with allure.step("Логин под несуществующим пользователем"):
            body = LoginMethods.login_in_system(generate_registration_data_without_delete_method['email'],
                                                generate_registration_data_without_delete_method['password'])
        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert body.status_code == 401
            assert body.json()["success"] == False
            assert body.json()["message"] == MessageData.MESSEGE_INC_LOGIN_401
