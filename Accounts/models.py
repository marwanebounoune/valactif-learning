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


class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    title = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title