from django.contrib import admin
from .models import User,lecons,Chapitres,Desc,Villes,Pays
from django.contrib.auth.admin import UserAdmin as origin

#enregistrement du model User
class UserAdmin(origin):
    list_display =  ('id', 'username', 'tel1','adresse', 'dateNaissance', 'genre', 'pays', 'ville', 'lecons', 'url_linkedIn')
    add_fieldsets = origin.add_fieldsets + ((None, {'fields': ('tel1','adresse', 'dateNaissance', 'url_linkedIn', 'genre', 'pays', 'ville', 'lecons','photoProfile')}),)


admin.site.register(User, UserAdmin)
admin.site.register(lecons)
admin.site.register(Chapitres)
admin.site.register(Desc)

admin.site.register(Villes)
admin.site.register(Pays)


