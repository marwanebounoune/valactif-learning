from . import views
from django.urls import path

urlpatterns = [
    path('lecon/<id>/', views.PostList, name='lecons'),
]