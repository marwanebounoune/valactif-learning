
from django.urls import path,include
from . import views
from Accounts import views
urlpatterns = [
	path('logout/', views.logout_custumized, name="logout"),
	path('login/', views.login, name="login"),
	path('edit_profile/', views.UpdateUserView.as_view(), name="edit_user"),
	#path('lecons/', views.lecons, name="lecons"),
	path('profil/', views.profilUser, name="profilUser"), 	#path{'leconsVideo/', views.lecons, name="leconsVideo" },
 

]