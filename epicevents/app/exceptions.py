from rest_framework.exceptions import APIException


class NotAllowedRessource(APIException):
    status_code = 404
    default_detail = 'Ressource access is not allowed'
    default_code = '4026'