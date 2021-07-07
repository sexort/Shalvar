from abc import ABC

from rest_framework.serializers import Serializer
from rest_framework import serializers


class ShalvarInstallerSerializer(Serializer, ABC):
    website_name = serializers.CharField(min_length=10, max_length=100)
    admin_path = serializers.CharField(min_length=10, max_length=50)
    website_subject = serializers.CharField(max_length=200)
    admin_username = serializers.CharField(max_length=200)
    admin_password = serializers.CharField(max_length=250)
    admin_email = serializers.EmailField()
    website_domain = serializers.URLField()
    website_description = serializers.CharField()
