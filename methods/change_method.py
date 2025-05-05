import allure
import requests
import urls


class ChangeMethods:

    @staticmethod
    # метод изменения данных пользователя
    # Тело ответа содержит success, email, name
    def change_user_data_and_return_new_data(body, accessToken):
        with allure.step("Создаем запрос изменения данных пользователя"):
            response = requests.patch(f'{urls.Url.MAIN_URL}{urls.Url.UPDATE_USER_INFO_URL}', data=body, headers={'Authorization': accessToken})

        return response

    @staticmethod
    # метод изменения данных пользователя
    # Тело ответа содержит success, email, name
    def get_user_data(accessToken):
        with allure.step("Создаем запрос на получение данных пользователя"):
            response = requests.get(f'{urls.Url.MAIN_URL}{urls.Url.UPDATE_USER_INFO_URL}', headers={'Authorization': accessToken})

        return response
