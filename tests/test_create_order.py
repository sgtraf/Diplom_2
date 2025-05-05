import allure
import pytest
from data import MessageData
from methods.login_method import LoginMethods
from methods.change_method import ChangeMethods
from methods.generators import GenerateBody


class TestCreateOrder:
    @allure.title('Test Create Order')
    @allure.description('Тест создание заказа:    с авторизацией,    без авторизации,    с ингредиентами,   '
                        ' без ингредиентов,    с неверным хешем ингредиентов.')

    def test_create_order_with_authorization(self,generate_registration_data_for_change_user_data):

        with allure.step("Логин под пользователем"):
            body = LoginMethods.login_in_system(generate_registration_data_for_change_user_data['email'],
                                                generate_registration_data_for_change_user_data['password'])
        #print(body.json())
        #здесь мы подготавливаем тело запроса для изменения полей пользователя
        #print(new_user_data)
        #print(generate_registration_data_for_change_user_data)
        with allure.step("Меняем данные пользователя"):
            response_new_data = ChangeMethods.change_user_data_and_return_new_data(new_user_data, body.json()['accessToken'])
        #print(response_new_data.json())
        #print(ChangeMethods.get_user_data(body.json()["accessToken"]).json())
        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert response_new_data.status_code == 200
            assert response_new_data.json()["success"] == True
            assert response_new_data.json()["user"]["email"] == ChangeMethods.get_user_data(body.json()["accessToken"]).json()["user"]["email"]
            assert response_new_data.json()["user"]["name"] == ChangeMethods.get_user_data(body.json()['accessToken']).json()["user"]['name']
