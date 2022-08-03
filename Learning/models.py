from tkinter.tix import STATUS
from turtle import title
from unicodedata import name
from django import forms
from django.db import models
from django.core.validators import FileExtensionValidator

from Accounts.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm




# Create your models here.
PERMISSION_CHOICES = (
    ('1','Course overview'),
    ('2', 'What you will learn'),
    ('3', 'Desc'),
    ('4', 'Footer desc')
)
IMAGE_OR_TEXT_CHOICES = (
    ('1','Text'),
    ('2', 'Image')
)
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
LEVELS = (
    (1,'Beginner'),
    (2,'Intermediate'),
    (3,'Advanced')
)

class Lecons(models.Model):
    name_lecon = models.CharField(max_length=255, null=True, blank=True)
    nbr_chapitres = models.CharField(max_length=60, null=True, blank=True)
    url_photo = models.ImageField(upload_to='images/lecons/',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg','tiff'])])
    price = models.IntegerField(null=True, blank=True)
    duree = models.CharField(max_length=21, null=True, blank=True)
    level = models.IntegerField( null=True, blank=True, choices=LEVELS)
    deleted = models.BooleanField(default=False, blank=True, null=True)

    pass
    class Meta:
        db_table = "Lecons" 

class Chapitres(models.Model):
    name_chapitres =  models.CharField(max_length=255, null=True, blank=True)
    type_chapitres = models.CharField(max_length=255, null=True, blank=True)
    url  = models.FileField(upload_to='videos/')
    lecon = models.ForeignKey(Lecons, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False, blank=True, null=True)
    pass
    class Meta:
        db_table = "Chapitres" 

class Desc(models.Model):
    description = models.TextField()
    type_desc = models.CharField(max_length=1, null=True, blank=True, choices=PERMISSION_CHOICES)
    image_or_text = models.CharField(max_length=1, null=True, blank=True, choices=IMAGE_OR_TEXT_CHOICES)
    image = models.ImageField(upload_to='images/description/',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg','tiff'])])
    lecon = models.ForeignKey(Lecons, on_delete=models.CASCADE)
    chapitre = models.ForeignKey(Chapitres, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    deleted = models.BooleanField(default=False, blank=True, null=True)
    pass
    class Meta:
        db_table = "Desc" 



class About(models.Model):
    title = models.TextField()
    description = models.TextField()
    pass
    class Meta:
        db_table = "About"


class article(models.Model):
    title = models.TextField()
    description = models.TextField()
    url_photo = models.ImageField(upload_to='images/article/',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg','tiff'])])
    title1 = models.TextField()
    description1 = models.TextField()
    title2 = models.TextField()
    description2 = models.TextField()
    title3 = models.TextField()
    description3 = models.TextField()
    title4 = models.TextField()
    description4 = models.TextField()
    title5 = models.TextField()
    description5 = models.TextField()
    pass
    class Meta:
        db_table = "article"
