from rest_framework.exceptions import APIException


class UserNotFound(APIException):
    status_code = 404
    default_detail = 'This user doesn\'t exist'
    default_code = '4026'


class BadPassword(APIException):
    status_code = 401
    default_detail = 'Incorrect password'
    default_code = '4026'