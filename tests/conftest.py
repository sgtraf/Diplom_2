import allure
import pytest
from methods.login_method import LoginMethods
from methods.generators import GenerateBody


#Создание данных для регистрации и удаление пользователя.
@pytest.fixture
def generate_registration_data():
    test_body = GenerateBody.generate_user_data()
    yield test_body
    with allure.step("Удаляем пользователя"):
        LoginMethods.delete_login(LoginMethods.login_in_system(test_body['email'], test_body['password']).
                                  json()["accessToken"])

#Создание данных для регистрации.
@pytest.fixture
def generate_registration_data_without_delete_method():
    test_body = GenerateBody.generate_user_data()
    return test_body

#Создание данных для изменения данных пользователя.
@pytest.fixture
def generate_registration_data_for_change_user_data():
    test_body = GenerateBody.generate_user_data()
    with allure.step("Создаем пользователя"):
        response = LoginMethods.register_new_user_and_return_login_password(test_body)
    yield test_body
    with allure.step("Удаляем пользователя"):
        LoginMethods.delete_login(response.json()["accessToken"])
