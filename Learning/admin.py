from django.contrib import admin
from .models import Lecons, Chapitres, Desc

# Register your models here.


class DescAdmin(admin.ModelAdmin):
    list_display =  ('id', 'title', 'text', 'type_desc','image_or_text', 'image', 'lecon_id', 'chapitre_id')

class LeconsAdmin(admin.ModelAdmin):
    list_display =  ('name_lecon', 'nbr_chapitres', 'price', 'duree', 'url_photo')

admin.site.register(Lecons, LeconsAdmin)
admin.site.register(Chapitres)
admin.site.register(Desc, DescAdmin)