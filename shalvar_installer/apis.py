from rest_framework import generics
from shalvar_installer.models import ShalvarInstallerModel
from shalvar_installer.serializers import ShalvarInstallerSecondStepSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import permissions
from utilities import responses


class ShalvarInstallerSecondStepAPI(generics.CreateAPIView):
    serializer_class = ShalvarInstallerSecondStepSerializer
    permission_classes = (permissions.AllowAny,)
    user_model = User
    model = ShalvarInstallerModel

    def post(self, request, *args, **kwargs):
        serialized_data = ShalvarInstallerSecondStepSerializer(data=self.request.data)
        if not serialized_data.is_valid():
            result = {'errors': serialized_data.errors}
            return responses.BadRequestResponse(result=result).send_response()

        self.user_model.objects.create(
            username=serialized_data.data.get('admin_username'),
            password=make_password(serialized_data.data.get('password')),
            email=serialized_data.data.get('admin_email'),
            first_name='مدیر',
            last_name=serialized_data.data.get('website_name'),
        )

        self.model.objects.create(
            **serialized_data.data
        )
        return responses.SuccessResponse().send_response()
