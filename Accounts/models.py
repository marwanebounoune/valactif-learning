from cgitb import text
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.contrib.postgres.fields import ArrayField


# Create your models here.
GENRE_CHOICES=(
    ('1', 'Femme'),
    ('2', 'Homme')
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
    tel1 = models.CharField(max_length=13, null=True, blank=True)
    dateNaissance = models.CharField(max_length=1, null=True, blank=True)
    adresse = models.CharField(max_length=500, null=True, blank=True)
    url_linkedIn = models.CharField(max_length=500, null=True, blank=True)
    genre = models.CharField(max_length=1, null=True, blank=True, choices=GENRE_CHOICES)
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE, null=True, blank=True)
    ville = models.ForeignKey(Villes, on_delete=models.CASCADE, null=True, blank=True)
    lecons = ArrayField(ArrayField(ArrayField(models.IntegerField(null=True)), null=True, blank=True),null=True, blank=True)
    pass
    class Meta:
        db_table = "User" 

class lecons(models.Model):
    name_lecon = models.CharField(max_length=255, null=True, blank=True)
    nbr_chapitres = models.CharField(max_length=60, null=True, blank=True)
    url_photo = models.ImageField(upload_to='images/profiles/',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg','tiff'])])
    pass
    class Meta:
        db_table = "lecons" 

class Chapitres (models.Model):
    name_chapitres =  models.CharField(max_length=255, null=True, blank=True)
    type_chapitres = models.CharField(max_length=255, null=True, blank=True)
    url  = models.FileField(upload_to='videos/')
    lecon = models.ForeignKey(lecons, on_delete=models.CASCADE)


    pass
    class Meta:
        db_table = "Chapitres" 


class Desc (models.Model):
    overview_dec = models.TextField()
    first_dec = models.TextField()
    second_dec = models.TextField()
    second2_dec = models.TextField()
    program_dec = models.TextField()
    lecon = models.ForeignKey(lecons, on_delete=models.CASCADE)
    chapitre = models.ForeignKey(Chapitres, on_delete=models.CASCADE)
    pass
    class Meta:
        db_table = "Desc" 



