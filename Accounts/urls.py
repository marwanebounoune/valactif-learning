
from django.urls import path,include
from . import views
from Accounts import views
urlpatterns = [
    path('', views.home, name='home'),#account
	path('logout/', views.logout_custumized, name="logout"),
	path('login/', views.login, name="login"),
	path('home/', views.home, name="home"),
	path('products/', views.home, name="products"),
	path('edit_profile/', views.UpdateUserView.as_view(), name="edit_user"),
	path('lecons/', views.lecons, name="lecons"),
]