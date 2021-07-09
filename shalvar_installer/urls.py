from django.urls import path
from shalvar_installer.views import IndexOfInstallerView
from shalvar_installer.apis import *

urlpatterns = [
    path('', IndexOfInstallerView.as_view(), name='shalvar_installer_class'),
    path('api/first-step/', ShalvarInstallerFirstStepAPI.as_view(), name='shalvar_installer_first_step_api'),
    path('api/second-step/', ShalvarInstallerSecondStepAPI.as_view(), name='shalvar_installer_second_step_api'),
    path('api/databases/', CheckInstalledDatabase.as_view(), name='check_databases'),
]
