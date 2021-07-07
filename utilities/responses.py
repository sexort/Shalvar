from rest_framework.response import Response
from rest_framework import status as st
from datetime import datetime


class BaseResponse:
    def send_response(self):
        code = self.__dict__.get('code')
        return Response({
            self.__dict__
        }, status=code)


class BadRequestResponse(BaseResponse):
    def __init(self, result, status=False, current_datetime=datetime.now(), code=st.HTTP_400_BAD_REQUEST):
        self.result = result
        self.status = status
        self.current_datetime = current_datetime
        self.code = code


class NotFoundResponse(BaseResponse):
    def __init(self, result=None, status=False, current_datetime=datetime.now(), code=st.HTTP_404_NOT_FOUND):
        self.result = result
        self.status = status
        self.current_time = current_datetime
        self.code = code


class PermissionDeniedResponse(BaseResponse):
    def __init__(self, result=None, status=False, current_datetime=datetime.now(), code=st.HTTP_403_FORBIDDEN):
        self.result = result
        self.status = status
        self.current_datetime = current_datetime
        self.code = code


class SuccessResponse(BaseResponse):
    def __init__(self, result=None, status=None, current_datetime=datetime.now(), code=st.HTTP_200_OK):
        self.result = result
        self.status = status
        self.current_datetime = current_datetime
        self.code = code
