
from django.urls import path
from . import views
urlpatterns = [
	path('profile/', views.getProfile, name='getProfile'),
	path('editProfile/', views.editProfile, name='editProfile'),
	path('user_detail/', views.user_detail, name='user_detail'),
]