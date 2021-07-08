from rest_framework import generics
from shalvar_installer.models import ShalvarInstallerModel
from shalvar_installer.serializers import ShalvarInstallerSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from utilities import responses


class ShalvarInstallerAPI(generics.CreateAPIView):
    serializer_class = ShalvarInstallerSerializer
    permission_classes = (permissions.AllowAny,)
    model = ShalvarInstallerModel

    def post(self, request, *args, **kwargs):
        serialized_data = self.request.data
        if not serialized_data.is_valid():
            return responses.BadRequestResponse.send_response()

        print(serialized_data)
