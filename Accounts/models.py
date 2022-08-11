from cgitb import text
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.contrib.postgres.fields import ArrayField
from django.dispatch import receiver 
from django.db.models.signals import post_save 
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator


# Create your models here.
GENRE_CHOICES = (
    (1, 'Femme'),
    (2, 'Homme')
)
class Pays(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return str(self.name)
    class Meta:
        db_table = "Pays" 

class Villes(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    pays = models.ForeignKey(Pays, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)
    class Meta:
        db_table = "Villes" 

class User(AbstractUser):
    photoProfile = models.FileField(upload_to='images/profiles/',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg','tiff'])])
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    tel1 = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    tel2 = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    dateNaissance = models.DateField(max_length=1, null=True, blank=True)
    adresse = models.CharField(max_length=500, null=True, blank=True)
    url_linkedIn = models.CharField(max_length=500, null=True, blank=True)
    genre = models.IntegerField(null=True, blank=True, choices=GENRE_CHOICES)
    ville = models.CharField(max_length=100, null=True, blank=True)
    lecons = ArrayField(ArrayField(ArrayField(models.IntegerField(null=True)), null=True, blank=True),null=True, blank=True)
    is_connected = models.BooleanField(default=False)
    country = models.CharField(max_length=100, null=True, blank=True)
    pass
    class Meta:
        db_table = "User" 


# @receiver(post_save, sender=User) #add this
# def create_user_profile(sender, instance, created, **kwargs):
# 		if created:
# 			User.objects.create(user=instance)

# @receiver(post_save, sender=User) #add this
# def save_user_profile(sender, instance, **kwargs):
# 		instance.User.save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField()
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
