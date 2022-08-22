
from django.urls import path
from . import views
from Accounts import views
from django.contrib.auth import views as auth_views
urlpatterns = [
	path('logout/', views.logout_custumized, name="logout"),
	path('login/', views.login, name="login"),
	path('profil/', views.profilUser, name="profilUser"),
    path('signup/', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
	############## Reset password urls ######################
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')
	############## /Reset password urls ######################
]