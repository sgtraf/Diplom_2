import allure
from data import MessageData
from data import OrderData
from methods.login_method import LoginMethods
from methods.order_methods import OrderMethods


class TestCreateOrder:
    @allure.title('Test Create Order')
    @allure.description('Тест создание заказа:    с авторизацией,    без авторизации,    с ингредиентами,   '
                        ' без ингредиентов,    с неверным хешем ингредиентов.')
    def test_create_order_with_authorization(self,generate_registration_data_for_change_user_data):

        with allure.step("Логин под пользователем"):
            body = LoginMethods.login_in_system(generate_registration_data_for_change_user_data['email'],
                                                generate_registration_data_for_change_user_data['password'])

        #здесь мы подготавливаем тело запроса для заказа из валидных ингредиентов
        new_user_data = OrderData.VALID_INGREDIENT
        with allure.step("Делаем заказ"):
            response_new_data = OrderMethods.take_order(new_user_data, body.json()['accessToken'])
        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert response_new_data.status_code == 200
            assert response_new_data.json()["success"] == True
            assert response_new_data.json()["order"]["ingredients"][0]['_id'] == OrderData.VALID_INGREDIENT['ingredients'][0]
            assert response_new_data.json()["order"]["ingredients"][1]['_id'] == OrderData.VALID_INGREDIENT['ingredients'][1]

    def test_create_order_with_authorization_without_ingredients(self,generate_registration_data_for_change_user_data):
        with allure.step("Логин под пользователем"):
            body = LoginMethods.login_in_system(generate_registration_data_for_change_user_data['email'],
                                                generate_registration_data_for_change_user_data['password'])

        #здесь мы подготавливаем тело запроса для заказа c пустым списком ингредиентов
        new_user_data = OrderData.NONE_INGREDIENT
        with allure.step("Делаем заказ"):
            response_new_data = OrderMethods.take_order(new_user_data, body.json()['accessToken'])
        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert response_new_data.status_code == 400
            assert response_new_data.json()["success"] == False
            assert response_new_data.json()["message"] == MessageData.MESSEGE_NOT_INGREDIENT_400

    def test_create_order_with_authorization_with_invalid_ingredients(self,generate_registration_data_for_change_user_data):
        with allure.step("Логин под пользователем"):
            body = LoginMethods.login_in_system(generate_registration_data_for_change_user_data['email'],
                                                generate_registration_data_for_change_user_data['password'])

        #здесь мы подготавливаем тело запроса для заказа с неверным хэшем ингредиентов
        new_user_data = OrderData.INVALID_INGREDIENT
        with allure.step("Делаем заказ"):
            response_new_data = OrderMethods.take_order(new_user_data, body.json()['accessToken'])
        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert response_new_data.status_code == 500

    def test_create_order_without_authorization(self,generate_registration_data_for_change_user_data):

        with allure.step("Логин под пользователем"):
            body = LoginMethods.login_in_system(generate_registration_data_for_change_user_data['email'],
                                                generate_registration_data_for_change_user_data['password'])

        #без авторизации, здесь мы подготавливаем тело запроса для заказа из валидных ингредиентов
        new_user_data = OrderData.VALID_INGREDIENT
        with allure.step("Делаем заказ"):
            response_new_data = OrderMethods.take_order(new_user_data, '')
        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert response_new_data.status_code == 200
            assert response_new_data.json()["success"] == True
            assert response_new_data.json()["order"]["number"] != 0

    def test_create_order_without_authorization_without_ingredients(self,generate_registration_data_for_change_user_data):
        with allure.step("Логин под пользователем"):
            body = LoginMethods.login_in_system(generate_registration_data_for_change_user_data['email'],
                                                generate_registration_data_for_change_user_data['password'])

        #без авторизации, здесь мы подготавливаем тело запроса для заказа c пустым списком ингредиентов
        new_user_data = OrderData.NONE_INGREDIENT
        with allure.step("Делаем заказ"):
            response_new_data = OrderMethods.take_order(new_user_data, '')
        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert response_new_data.status_code == 400
            assert response_new_data.json()["success"] == False
            assert response_new_data.json()["message"] == MessageData.MESSEGE_NOT_INGREDIENT_400

    def test_create_order_without_authorization_with_invalid_ingredients(self,generate_registration_data_for_change_user_data):
        with allure.step("Логин под пользователем"):
            body = LoginMethods.login_in_system(generate_registration_data_for_change_user_data['email'],
                                                generate_registration_data_for_change_user_data['password'])

        #без авторизации, здесь мы подготавливаем тело запроса для заказа с неверным хэшем ингредиентов
        new_user_data = OrderData.INVALID_INGREDIENT
        with allure.step("Делаем заказ"):
            response_new_data = OrderMethods.take_order(new_user_data, '')
        with (allure.step("Проверяем, что код ответа и тело соответствует документации")):
            assert response_new_data.status_code == 500
