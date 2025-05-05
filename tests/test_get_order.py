import allure
from data import MessageData
from data import OrderData
from methods.login_method import LoginMethods
from methods.order_methods import OrderMethods


class TestGetOrder:
    @allure.title('Test Get Order')
    @allure.description('Тест получения списка заказа пользователя, с авторизацией и без.')
    def test_get_order_with_authorization(self,generate_registration_data_for_change_user_data):

        with allure.step("Логин под пользователем"):
            body = LoginMethods.login_in_system(generate_registration_data_for_change_user_data['email'],
                                                generate_registration_data_for_change_user_data['password'])

        #здесь мы подготавливаем тело запроса для заказа из валидных ингредиентов
        new_user_data = OrderData.VALID_INGREDIENT
        with allure.step("Делаем заказ"):
            response_new_data = OrderMethods.take_order(new_user_data, body.json()['accessToken'])
        with allure.step("Получаем список заказов пользователя"):
            response_new_data = OrderMethods.get_order(body.json()['accessToken'])

        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert response_new_data.status_code == 200
            assert response_new_data.json()["success"] == True
            assert response_new_data.json()["total"] != 0

    def test_get_order_without_authorization(self,generate_registration_data_for_change_user_data):

        with allure.step("Логин под пользователем"):
            body = LoginMethods.login_in_system(generate_registration_data_for_change_user_data['email'],
                                                generate_registration_data_for_change_user_data['password'])

        #здесь мы подготавливаем тело запроса для заказа из валидных ингредиентов
        new_user_data = OrderData.VALID_INGREDIENT
        with allure.step("Делаем заказ"):
            response_new_data = OrderMethods.take_order(new_user_data, body.json()['accessToken'])
        with allure.step("Получаем список заказов пользователя, без авторизации"):
            response_new_data = OrderMethods.get_order('')

        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert response_new_data.status_code == 401
            assert response_new_data.json()["success"] == False
            assert response_new_data.json()["message"] == MessageData.MESSEGE_NOT_AUTHORISED_401

