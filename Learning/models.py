from tkinter.tix import STATUS
from django.db import models
from django.core.validators import FileExtensionValidator

from Accounts.models import User


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

class Lecons(models.Model):
    name_lecon = models.CharField(max_length=255, null=True, blank=True)
    nbr_chapitres = models.CharField(max_length=60, null=True, blank=True)
    url_photo = models.ImageField(upload_to='images/lecons/',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg','tiff'])])
    price = models.IntegerField(null=True, blank=True)
    duree = models.CharField(max_length=21, null=True, blank=True)
    pass
    class Meta:
        db_table = "Lecons" 

class Chapitres(models.Model):
    name_chapitres =  models.CharField(max_length=255, null=True, blank=True)
    type_chapitres = models.CharField(max_length=255, null=True, blank=True)
    url  = models.FileField(upload_to='videos/')
    lecon = models.ForeignKey(Lecons, on_delete=models.CASCADE)
    pass
    class Meta:
        db_table = "Chapitres" 

class Desc(models.Model):
    text = models.TextField()
    type_desc = models.CharField(max_length=1, null=True, blank=True, choices=PERMISSION_CHOICES)
    image_or_text = models.CharField(max_length=1, null=True, blank=True, choices=IMAGE_OR_TEXT_CHOICES)
    image = models.ImageField(upload_to='images/description/',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg','tiff'])])
    lecon = models.ForeignKey(Lecons, on_delete=models.CASCADE)
    chapitre = models.ForeignKey(Chapitres, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    pass
    class Meta:
        db_table = "Desc" 

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)   
    dateTime=models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.user.username +  " Comment: " + self.content