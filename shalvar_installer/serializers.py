from rest_framework.serializers import Serializer
from rest_framework import serializers
from django.utils.translation import ugettext as _
from rest_framework import exceptions
from validate_email import validate_email


class ShalvarInstallerFirstStepSerializer(Serializer):
    database_type = serializers.CharField(max_length=15)
    database_username = serializers.CharField(allow_blank=True, allow_null=True)
    database_password = serializers.CharField(allow_blank=True, allow_null=True)
    database_name = serializers.CharField(allow_blank=True, allow_null=True)
    database_port = serializers.IntegerField(allow_null=True)

    def validate_database_type(self, database_type):
        database_types: list = [
            "mysql", "postgresql", "mongodb", "sqlite"
        ]
        if database_type not in database_types:
            raise exceptions.ValidationError(_(
                'invalid database type'
            ))
        return database_type


class ShalvarInstallerSecondStepSerializer(Serializer):
    website_name = serializers.CharField(min_length=1, max_length=100)
    admin_path = serializers.CharField(min_length=1, max_length=50)
    website_subject = serializers.CharField(max_length=200)
    admin_username = serializers.CharField(max_length=200)
    admin_password = serializers.CharField(max_length=250)
    admin_email = serializers.EmailField()
    website_domain = serializers.CharField()
    website_description = serializers.CharField()

    def validate_admin_password(self, admin_password):
        if admin_password is None or admin_password == "":
            raise exceptions.ValidationError(_(
                "کلمه‌ی عبور نمیتواند خالی باشد"
            ))

        if not any(ch.isdigit() for ch in admin_password):
            raise exceptions.ValidationError(_(
                'کلمه‌ی عبور شما باید حتما دارای اعداد و کلمات انگلیسی باشد'
            ))

        if not any(ch.isalpha() for ch in admin_password):
            raise exceptions.ValidationError(_(
                'کلمه‌ی عبور شما باید حتما دارای اعداد و کلمات انگلیسی باشد'
            ))
        return admin_password

    def validate_admin_email(self, admin_email):
        if not validate_email(email=admin_email):
            raise exceptions.ValidationError(_(
                "ایمیل وارد شده اشتباه است"
            ))
        return admin_email
