import allure
import requests
import urls


class OrderMethods:

    @staticmethod
    # метод создания заказа
    def take_order(body, accessToken):
        with allure.step("Создаем запрос на создание заказа"):
            response = requests.post(f'{urls.Url.MAIN_URL}{urls.Url.CREATE_ORDERS_URL}', data=body, headers={'Authorization': accessToken})

        return response

    @staticmethod
    # метод получения заказов конкретного пользователя
    def get_order(accessToken):
        with allure.step("Создаем запрос на получение заказов"):
            response = requests.get(f'{urls.Url.MAIN_URL}{urls.Url.GET_ORDER_URL}', headers={'Authorization': accessToken})

        return response