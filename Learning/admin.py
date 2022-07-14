from django.contrib import admin
from .models import Lecons, Chapitres, Desc
from .models import Post

# Register your models here.


class DescAdmin(admin.ModelAdmin):
    list_display =  ('id', 'title', 'text', 'type_desc','image_or_text', 'image', 'lecon_id', 'chapitre_id')

class LeconsAdmin(admin.ModelAdmin):
    list_display =  ('name_lecon', 'nbr_chapitres', 'price', 'duree', 'url_photo')
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Lecons, LeconsAdmin)
admin.site.register(Chapitres)
admin.site.register(Desc, DescAdmin)
admin.site.register(Post)

