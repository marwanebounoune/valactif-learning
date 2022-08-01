from turtle import title
from urllib import request
from django.shortcuts import render, redirect
from django.views import generic

from Accounts.models import User
from .models import Lecons, Desc, About, article

# Create your views here.
""" def Desc_list(request):
    name_chapitres = name_chapitres.objects.filter() """
def getDesc(request):
    Text = Text.objects.filter(id=request.type_desc.id)
    context = {
        'Text': Text
    }
    return render(request, 'Lecons/indexDec.html', context)

def PostList(request, id):
    courseOverviews = Desc.objects.filter(lecon_id=id).filter(type_desc='1')
    whatYouWillLearns = Desc.objects.filter(lecon_id=id).filter(type_desc='2')
    courseDescs = Desc.objects.filter(lecon_id=id).filter(type_desc='3').filter(image_or_text='1')
    coursePrograms = Desc.objects.filter(lecon_id=id).filter(type_desc='4')
    countCourseDescs = courseDescs.count()
    queryset = Desc.objects.filter(lecon_id=id)
    lecon = Lecons.objects.get(id=id)
    # nbrDesc3 = queryset
    print("lecon", round(countCourseDescs/2))
    context = {
        'courseOverviews': courseOverviews,
        'whatYouWillLearns': whatYouWillLearns,
        'courseDescs': courseDescs,
        'coursePrograms': coursePrograms,
        'countCourseDescs1' : countCourseDescs/2,
        'lecon': lecon,
        'i': round(countCourseDescs/2),
        'j': countCourseDescs/2
    }
    return render(request, 'Lecons/indexDec.html', context)
       
def home(request):
    user = User.objects.filter(id=request.user.id)
    lecons = Lecons.objects.all().order_by('-id')
    aboutus = About.objects.all()
    sarticle = article.objects.all().order_by('-id')


    context = {
        'user': user
    }
    return render(request, 'main/index.html', {"lecons":lecons,"aboutus" : aboutus,"sarticle": sarticle})

def home_view(request):
    qs = Lecons.objects.all()
    template_name = 'index.html'
    context = {'object_list': qs}
    return render (request, template_name, context)



def aboutus(request):
    about = About.objects.all()

    return render (request, 'main/about.html' ,{"about": about})


def Courses(request):
    course = Lecons.objects.all()
    lecons = Lecons.objects.all().order_by('-id')

    return render (request, 'main/courses.html',{"course": course,"lecons":lecons})


def articles(request):
    Article = article.objects.all()
    sarticle = article.objects.all().order_by('-id')


    return render (request, 'main/blog.html', {"Article": Article,"sarticle": sarticle})


def singlearticle(request, id):
    sarticle = article.objects.all()


    return render (request, 'main/article.html', {"sarticle":sarticle})

