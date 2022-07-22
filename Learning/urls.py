from . import views
from django.urls import path

urlpatterns = [
    path('lecon/<id>/', views.getLecon, name='lecons'),
    path('lecon/<id>/chapitre/<pk>', views.getChapitre, name='chapitre'),
    path('', views.home, name='home'),#account
]