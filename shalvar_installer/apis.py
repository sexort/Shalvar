from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import response, status
from shalvar_installer.models import ShalvarInstallerModel
from shalvar_installer.serializers import ShalvarInstallerSecondStepSerializer, ShalvarInstallerFirstStepSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import permissions
from utilities import responses, utilities


class ShalvarInstallerFirstStepAPI(generics.CreateAPIView):
    serializer_class = ShalvarInstallerFirstStepSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(data=self.request.data)
        if not serialized_data.is_valid():
            result = {'errors': serialized_data.errors}
            return responses.BadRequestResponse(result=result).send_response()

        database_name = serialized_data.data.get('database_name')
        database_username = serialized_data.data.get('database_username')
        database_password = serialized_data.data.get('database_password')
        database_port = serialized_data.data.get('database_port')
        database_type = serialized_data.data.get('database_type')

        if database_type == "sqlite":
            with open("database.py", mode="w") as make_database_config:
                make_database_config.write("database_type = 'sqlite'")
                make_database_config.close()

        elif database_type == "mysql":
            if not utilities.mysql_connection(
                database_name=database_name,
                database_username=database_username,
                database_password=database_password,
                database_port=database_port
            ):
                return responses.BadRequestResponse().send_response()
            with open("database.py", mode="w") as make_database_config:
                if int(database_port) == 0:
                    make_database_config.write(
                        f"database_type = 'mysql'\ndatabase_name = '{database_name}'\ndatabase_username = "
                        f"'{database_username}'\ndatabase_password = '{database_password}'"
                    )
                else:
                    make_database_config.write(
                        f"database_type = 'mysql'\ndatabase_name = '{database_name}'\ndatabase_username = "
                        f"'{database_username}'\ndatabase_password = '{database_password}'\ndatabase_port = "
                        f"{database_port}"
                    )
                make_database_config.close()

            return responses.SuccessResponse.send_response()

        elif database_type == 'postgresql':
            if not utilities.postgresql_connection(
                    database_name=database_name,
                    database_username=database_username,
                    database_password=database_password,
                    database_port=database_port
            ):
                return responses.BadRequestResponse().send_response()

            with open("database.py", mode="w") as make_database_config:
                if int(database_port) == 0:
                    make_database_config.write(
                        f"database_type = 'postgresql'\ndatabase_name = '{database_name}'\ndatabase_username = "
                        f"'{database_username}'\ndatabase_password = '{database_password}'"
                    )
                else:
                    make_database_config.write(
                        f"database_type = 'postgresql'\ndatabase_name = '{database_name}'\ndatabase_username = "
                        f"'{database_username}'\ndatabase_password = '{database_password}'\ndatabase_port = "
                        f"{database_port}"
                    )
                make_database_config.close()

            return responses.SuccessResponse().send_response()

        elif database_type == 'mongo':
            if not utilities.mongo_connection(
                    database_name=database_name,
                    database_username=database_username,
                    database_password=database_password,
                    database_port=database_port
            ):
                return responses.BadRequestResponse().send_response()

            with open("database.py", mode="w") as make_database_config:
                if int(database_port) == 0:
                    make_database_config.write(
                        f"database_type = 'mongodb'\ndatabase_name = '{database_name}'\ndatabase_username = "
                        f"'{database_username}'\ndatabase_password = '{database_password}'"
                    )
                else:
                    make_database_config.write(
                        f"database_type = 'mongodb'\ndatabase_name = '{database_name}'\ndatabase_username = "
                        f"'{database_username}'\ndatabase_password = '{database_password}'\ndatabase_port = "
                        f"{database_port}"
                    )
                make_database_config.close()

            return responses.SuccessResponse.send_response()


class ShalvarInstallerSecondStepAPI(generics.CreateAPIView):
    serializer_class = ShalvarInstallerSecondStepSerializer
    permission_classes = (permissions.AllowAny,)
    user_model = User
    model = ShalvarInstallerModel

    def post(self, request, *args, **kwargs):
        serialized_data = self.serializer_class(data=self.request.data)
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


class CheckInstalledDatabase(APIView):

    def get(self, request, *args, **kwargs):
        return responses.Response({
            'status': True,
            'code': 200,
            'result': {
                'mysql': utilities.mysql_installed(),
                'postgresql': utilities.postgresql_installed(),
                'sqlite': True,
                'mongodb': utilities.mongo_installed()
            }
        }, status=status.HTTP_200_OK)

