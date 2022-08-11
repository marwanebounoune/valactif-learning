from django.contrib import admin
from .models import User,Villes,Pays
from django.contrib.auth.admin import UserAdmin as origin
from .models import Profile


#enregistrement du model User
class UserAdmin(origin):
    list_display =  ('id', 'username', 'tel1','adresse', 'dateNaissance', 'genre', 'ville', 'lecons', 'url_linkedIn')
    add_fieldsets = origin.add_fieldsets + ((None, {'fields': ('tel1','adresse', 'dateNaissance', 'url_linkedIn', 'genre', 'ville', 'lecons','photoProfile', 'country')}),)


admin.site.register(User, UserAdmin)
admin.site.register(Villes)
admin.site.register(Pays)
admin.site.register(Profile)


