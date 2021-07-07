from django.urls import path
from shalvar_installer.views import IndexOfInstallerView

urlpatterns = [
    path('', IndexOfInstallerView.as_view(), name='shalvar_installer_class'),
]
