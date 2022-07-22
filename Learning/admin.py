from django.contrib import admin
from .models import Lecons, Chapitres, Desc

# Register your models here.


class DescAdmin(admin.ModelAdmin):
    list_display =  ('id', 'title', 'description', 'type_desc','image_or_text', 'image', 'lecon_id', 'chapitre_id')

class LeconsAdmin(admin.ModelAdmin):
    list_display =  ('name_lecon', 'nbr_chapitres', 'price', 'duree', 'url_photo')
class ChapitresAdmin(admin.ModelAdmin):
    list_display =  ('name_chapitres', 'type_chapitres', 'lecon_id', 'duree', 'status')
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Lecons, LeconsAdmin)
admin.site.register(Chapitres, ChapitresAdmin)
admin.site.register(Desc, DescAdmin)

