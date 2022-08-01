from django.contrib import admin
from .models import Lecons, Chapitres, Desc, About, article

# Register your models here.


class DescAdmin(admin.ModelAdmin):
    list_display =  ('id', 'title', 'description', 'type_desc','image_or_text', 'image', 'lecon_id', 'chapitre_id')

class LeconsAdmin(admin.ModelAdmin):
    list_display =  ('name_lecon', 'nbr_chapitres', 'price', 'duree', 'url_photo','level')
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class AboutAdmin (admin.ModelAdmin):
    list_display = ('title', 'description')
class articleadmin (admin.ModelAdmin):
    list_display = ('title','description','url_photo','title1','description1','title2','description2','title3','description3','title4','description4','title5','description5')

admin.site.register(Lecons, LeconsAdmin)
admin.site.register(Chapitres)
admin.site.register(Desc, DescAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(article,articleadmin)