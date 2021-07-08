from django.urls import path
from shalvar_installer.views import IndexOfInstallerView
from shalvar_installer.apis import ShalvarInstallerAPI

urlpatterns = [
    path('', IndexOfInstallerView.as_view(), name='shalvar_installer_class'),
    path('', ShalvarInstallerAPI.as_view(), name='shalvar_installer_api')m
]
