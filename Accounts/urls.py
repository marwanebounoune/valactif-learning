
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='account'),
	path('logout/', views.logout_custumized, name="logout"),
	path('login/', views.login, name="login"),
	path('home/', views.home, name="home"),
	path('products/', views.home, name="products"),
]