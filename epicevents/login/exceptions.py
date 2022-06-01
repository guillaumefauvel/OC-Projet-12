from rest_framework.exceptions import APIException


class UserNotFound(APIException):
    status_code = 404
    default_detail = 'This user doesn\'t exist'
    default_code = '4026'


class BadPassword(APIException):
    status_code = 401
    default_detail = 'Incorrect password'
    default_code = '4026'
    

class InvalidToken(APIException):
    status_code = 401
    default_detail = 'The token you furnished is not valid'
    default_code = '4026'
    

class MissingToken(APIException):
    status_code = 401
    default_detail = 'Please, provide a token'
    default_code = '4026'
    
    
class ObjectDeleted(APIException):
    status_code = 410
    default_detail = 'The object has been deleted'
    default_code = '4027'
    
    
class MissingSalesContact(APIException):
    status_code = 403
    default_detail = 'You should specified a sales_contact'
    default_code = '4027'
    
    
