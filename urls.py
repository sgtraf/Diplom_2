class Url:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/api'
    CREATE_AND_REGISTRATION_USER_URL = f'{MAIN_URL}/auth/register' #POST
    LOGIN_USER_URL = f'{MAIN_URL}/auth/login' #POST
    UPDATE_USER_INFO_URL = f'{MAIN_URL}/auth/user' #PATCH
    DELETE_USER_URL = f'{MAIN_URL}/auth/user'  # DELETE
    CREATE_ORDERS_URL = f'{MAIN_URL}/orders' #POST
    GET_ORDER_URL = f'{MAIN_URL}/orders' #GET

