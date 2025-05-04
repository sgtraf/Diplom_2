import allure
import pytest
from methods.login_method import LoginMethods
from methods.generators import GenerateBody


@pytest.fixture
def generate_registration_data():
    test_body = GenerateBody.generate_user_data()
    yield test_body
    with allure.step("Удаляем пользователя"):
        #print(LoginMethods.login_in_system(test_body['email'], test_body['password']).
                                  #json())
        LoginMethods.delete_login(LoginMethods.login_in_system(test_body['email'], test_body['password']).
                                  json()["accessToken"])

@pytest.fixture
def generate_two_courier_with_same_login_data():
    test_body = GenerateBody.generate_body()
    with allure.step("Создаем курьера"):
        LoginMethods.register_new_courier_and_return_login_password(test_body)
    yield test_body
    with allure.step("Удаляем курьера"):
        LoginMethods.delete_login(LoginMethods.login_in_system(test_body['login'], test_body['password']).json()["id"])

#Фикстуры второго задания.

#Вход под несуществующим пользователем.
@pytest.fixture
def get_login_with_unreal_data():
    test_body = GenerateBody.generate_body()
    return test_body
