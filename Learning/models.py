from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
PERMISSION_CHOICES = (
    ('1','Course overview'),
    ('2', 'What you will learn'),
    ('3', 'Desc'),
    ('4', 'Footer desc')
)
TYPE_CHAPITRE = (
    (1,'Vidéo'),
    (2, 'PDF')
)
IMAGE_OR_TEXT_CHOICES = (
    ('1','Text'),
    ('2', 'Image')
)
STATUS_CHAPITRE = (
    (0,"Non démaré"),
    (1,"Encours"),
    (2,"Términé")
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
    url_demo  = models.FileField(upload_to='videos/',null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    duree = models.CharField(max_length=21, null=True, blank=True)
    level = models.IntegerField( null=True, blank=True, choices=LEVELS)
    deleted = models.BooleanField(default=False, blank=True, null=True)

    pass
    class Meta:
        db_table = "Lecons" 

class Chapitres(models.Model):
    name_chapitres =  models.CharField(max_length=255, null=True, blank=True)
    type_chapitres = models.IntegerField(null=True, blank=True, choices=TYPE_CHAPITRE)
    url  = models.FileField(upload_to='videos/', blank=True, null=True)
    lecon = models.ForeignKey(Lecons, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    duree = models.CharField(max_length=21, null=True, blank=True)
    status = models.IntegerField(null=True, blank=True, choices=STATUS_CHAPITRE)
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
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    url_photo = models.ImageField(upload_to='images/article/',null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png','jpeg','jpg','tiff'])])
    title1 = models.CharField(max_length=255, null=True, blank=True)
    description1 = models.TextField(null=True, blank=True)
    title2 = models.CharField(max_length=255, null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    title3 = models.CharField(max_length=255, null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)
    title4 = models.CharField(max_length=255, null=True, blank=True)
    description4 = models.TextField(null=True, blank=True)
    title5 = models.CharField(max_length=255, null=True, blank=True)
    description5 = models.TextField(null=True, blank=True)
    pass
    class Meta:
        db_table = "article"
