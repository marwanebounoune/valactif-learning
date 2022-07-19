from . import views
from django.urls import path

urlpatterns = [
    path('lecon/<id>/', views.PostList, name='lecons'),
    path('', views.home, name='home'),#account
]