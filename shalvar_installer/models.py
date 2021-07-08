from django.db import models


class ShalvarInstallerModel(models.Model):
    install_date = models.DateTimeField(auto_now=True)
    website_name = models.CharField(max_length=300)
    website_subject = models.CharField(max_length=300)
    website_description = models.TextField()
    website_domain = models.CharField(max_length=100)
    admin_username = models.CharField(max_length=100)
    admin_password = models.CharField(max_length=300)
    admin_email = models.EmailField()
    admin_path = models.CharField(max_length=100)

    def __str__(self):
        return self.website_name
