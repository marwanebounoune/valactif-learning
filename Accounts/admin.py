from django.contrib import admin
from .models import BlogPost, User
from django.contrib.auth.admin import UserAdmin as origin

#enregistrement du model User
class UserAdmin(origin):
    list_display =  ('id', 'username', 'tel1','tel2','adresse')
    add_fieldsets = origin.add_fieldsets + ((None, {'fields': ('tel1','tel2','adresse','photoProfile')}),)

admin.site.register(BlogPost)