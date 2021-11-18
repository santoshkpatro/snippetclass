from rest_framework.exceptions import APIException


class UserAuthException(APIException):
    status_code = 404
    default_detail = 'Invalid email or password'
