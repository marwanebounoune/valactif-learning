from . import views
from django.urls import include, path

urlpatterns = [
    path('lecon/<id>/', views.getLecon, name='lecons'),
    path('lecon/<id>/chapitre/<pk>', views.getChapitre, name='chapitre'),
    # path('lecon/<int:id>/', views.PostList, name='lecons'),
    path('', views.home, name='home'),#account
    path('about', views.aboutus, name='about'),
    path('courses', views.Courses, name='courses'),
    path('blogs/', views.allBlog, name='blogs'),
    path('article/<id>/', views.singlearticle, name='article'),
    path('offline/', views.offline, name='offline'),




]