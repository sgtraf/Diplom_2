import allure
import requests
from urls import Url


class OrderMethods:

    @staticmethod
    # метод создания заказа
    def take_order(body, accessToken):
        with allure.step("Создаем запрос на создание заказа"):
            response = requests.post(Url.CREATE_ORDERS_URL, data=body, headers={'Authorization': accessToken})

        return response

    @staticmethod
    # метод получения заказов конкретного пользователя
    def get_order(accessToken):
        with allure.step("Создаем запрос на получение заказов"):
            response = requests.get(Url.GET_ORDER_URL, headers={'Authorization': accessToken})

        return response
