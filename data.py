class MessageData:

    MESSEGE_TEXT_403 = "User already exists"
    MESSEGE_TEXT_403_WITHOUT_ONE = "Email, password and name are required fields"
    MESSEGE_INC_LOGIN_401 = "email or password are incorrect"
    MESSEGE_NOT_AUTHORISED_401 = "You should be authorised"

class OrderData:
    VALID_INGREDIENT = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]}
    INVALID_INGREDIENT = {"ingredients": ["61c0c533341d1f82001bdaaa6d---","614433271d1f82001bdaaa6f---"]}