import allure
import pytest
from data import MessageData
from methods.login_method import LoginMethods
from methods.change_method import ChangeMethods
from methods.generators import GenerateBody


class TestChangeUserData:
    @allure.title('Test Change User Data')
    @allure.description('Тут меняем данные пользователя, регистрируемся на сайте, входим на сайт, проверяем можно ли'
                        ' изменить поля сведений для пользователя' 
                        'проверяем код и тело ответа. Затем удаляем пользователя')
    @pytest.mark.parametrize('user_data_field', ['email', 'password', 'name'])
    #В этом методе есть баг, повторно использовать email, который уже был когда-то использован при изменении
    # данных пользователя невозможно, даже если пользователь был удален. Необходимо каждый раз использовать
    # уникальные почтовые адреса
    def test_change_user_data_with_authorization(self,generate_registration_data_for_change_user_data, user_data_field):

        with allure.step("Логин под пользователем"):
            body = LoginMethods.login_in_system(generate_registration_data_for_change_user_data['email'],
                                                generate_registration_data_for_change_user_data['password'])
        #здесь мы подготавливаем тело запроса для изменения полей пользователя
        new_user_data = GenerateBody.generate_lonely_user_data()[user_data_field]
        with allure.step("Меняем данные пользователя"):
            response_new_data = ChangeMethods.change_user_data_and_return_new_data(new_user_data, body.json()['accessToken'])
        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert response_new_data.status_code == 200
            assert response_new_data.json()["success"] == True
            assert response_new_data.json()["user"]["email"] == ChangeMethods.get_user_data(body.json()["accessToken"]).json()["user"]["email"]
            assert response_new_data.json()["user"]["name"] == ChangeMethods.get_user_data(body.json()['accessToken']).json()["user"]['name']

    @allure.title('Test Change User Data Without Authorization')
    @allure.description('Тут пытаемся менять данные пользователя без авторизации, регистрируемся на сайте, '
                        'проверяем можно ли изменить поля сведений для пользователя'
                        'проверяем код и тело ответа. Затем удаляем пользователя')
    @pytest.mark.parametrize('user_data_field', ['email', 'password', 'name'])
    def test_change_user_data_without_authorization(self,generate_registration_data_for_change_user_data, user_data_field):
        # здесь мы подготавливаем тело запроса для изменения полей пользователя
        new_user_data = GenerateBody.generate_lonely_user_data()[user_data_field]

        with allure.step("Меняем данные пользователя"):
            response_new_data = ChangeMethods.change_user_data_and_return_new_data(new_user_data, '')

        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert response_new_data.status_code == 401
            assert response_new_data.json()["success"] == False
            assert response_new_data.json()["message"]== MessageData.MESSEGE_NOT_AUTHORISED_401
