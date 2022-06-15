
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='account'),
	path('logout/', views.login, name="logout"),
	path('home/', views.login, name="home"),
	path('products/', views.login, name="products"),
]