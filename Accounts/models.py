from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from storages.backends.s3boto3 import S3Boto3Storage

# Create your models here.


class User(AbstractUser):
    photoProfile = models.FileField(upload_to='images/profiles/',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg','tiff'])])
    tel1 = models.CharField(max_length=10, null=True, blank=True)
    dateNaissance = models.CharField(max_length=10, null=True, blank=True)
    adresse = models.CharField(max_length=500, null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    pass
    class Meta:
        db_table = "User" 

