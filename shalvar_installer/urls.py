from django.urls import path
from shalvar_installer.views import IndexOfInstallerView
from shalvar_installer.apis import ShalvarInstallerSecondStepAPI

urlpatterns = [
    path('', IndexOfInstallerView.as_view(), name='shalvar_installer_class'),
    path('api/', ShalvarInstallerSecondStepAPI.as_view(), name='shalvar_installer_api'),
]
