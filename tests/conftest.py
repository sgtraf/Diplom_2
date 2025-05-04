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
        #print(LoginMethods.login_in_system(test_body['email'], test_body['password']).
                                  #json())
        LoginMethods.delete_login(LoginMethods.login_in_system(test_body['email'], test_body['password']).
                                  json()["accessToken"])

#Создание данных для регистрации.
@pytest.fixture
def generate_registration_data_without_delete_method():
    test_body = GenerateBody.generate_user_data()
    return test_body


