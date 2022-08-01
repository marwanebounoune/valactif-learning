from . import views
from django.urls import include, path

urlpatterns = [
    path('lecon/<int:id>/', views.PostList, name='lecons'),
    path('', views.home, name='home'),#account
    path('about', views.aboutus, name='about'),
    path('courses', views.Courses, name='courses'),
    path('blog', views.articles, name='blog'),
    path('article/<id>/', views.singlearticle, name='article'),

]