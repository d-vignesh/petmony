from rest_framework.exceptions import APIException

class ProfileDoesNotExist(APIException):

    status_code = 400
    default_detail = 'the request detail does not exist'