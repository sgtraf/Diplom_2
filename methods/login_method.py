import json

import allure
import requests
import urls


class LoginMethods:

    @staticmethod
    # метод регистрации нового пользователя возвращает код 200
    # Тело ответа содержит success, email, name, два токена accessToken и refreshToken
    def register_new_user_and_return_login_password(body):

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        with allure.step("Создаем запрос создания пользователя"):
            response = requests.post(f'{urls.Url.MAIN_URL}{urls.Url.CREATE_AND_REGISTRATION_USER_URL}', data=body)

        return response

    @staticmethod
    def login_in_system(email, password):
        params = {'email': email, 'password': password}
        with allure.step("Создаем запрос залогинивания пользователя"):
            response = requests.post(f'{urls.Url.MAIN_URL}{urls.Url.LOGIN_USER_URL}/', json = params )
        return response

    @staticmethod
    def delete_login(accessToken):
        with allure.step("Создаем запрос удаления пользователя"):
            response_delete = requests.delete(f"{urls.Url.MAIN_URL}{urls.Url.DELETE_USER_URL}", headers={'Authorization': accessToken})
        return response_delete
