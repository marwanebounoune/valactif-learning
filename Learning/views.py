from urllib import request
from django.shortcuts import render, redirect
from django.views import generic

from Accounts.models import User
from .models import Chapitres, Lecons, Desc


def getDesc(request):
    Text = Text.objects.filter(id=request.type_desc.id)
    context = {
        'Text': Text
    }
    return render(request, 'Lecons/indexDec.html', context)

def getLecon(request, id):
    courseOverviews = Desc.objects.filter(lecon_id=id).filter(type_desc='1')
    if(len(courseOverviews) == 0):
        print("courseOverviews", len(courseOverviews))
        courseOverviews = None
    whatYouWillLearns = Desc.objects.filter(lecon_id=id).filter(type_desc='2')
    courseDescs = Desc.objects.filter(lecon_id=id).filter(type_desc='3').filter(image_or_text='1')
    courseDescsImages = Desc.objects.filter(lecon_id=id).filter(type_desc='3').filter(image_or_text='2')
    coursePrograms = Desc.objects.filter(lecon_id=id).filter(type_desc='4')
    countCourseDescs = courseDescs.count()
    lecon = Lecons.objects.get(id=id)
    chapitres = Chapitres.objects.filter(lecon_id=id)
    context = {
        'courseOverviews': courseOverviews,
        'whatYouWillLearns': whatYouWillLearns,
        'courseDescs': courseDescs,
        'courseDescsImages': courseDescsImages,
        'coursePrograms': coursePrograms,
        'countCourseDescs1' : countCourseDescs/2,
        'lecon': lecon,
        'i': round(countCourseDescs/2),
        'j': countCourseDescs/2,
        'chapitres': chapitres
    }
    return render(request, 'Lecons/indexDec.html', context)

def getChapitre(request, id, pk):
    if(request.user.id != None):
        userId = request.user.id
        user = User.objects.get(id=userId)
        print("User ->", user)
    courseOverviews = Desc.objects.filter(lecon_id=id).filter(chapitre_id=pk).filter(type_desc='1')
    if(len(courseOverviews)==0):
        courseOverviews = None
    whatYouWillLearns = Desc.objects.filter(lecon_id=id).filter(chapitre_id=pk).filter(type_desc='2')
    if(len(whatYouWillLearns)==0):
        whatYouWillLearns = None
    courseDescs = Desc.objects.filter(lecon_id=id).filter(chapitre_id=pk).filter(type_desc='3').filter(image_or_text='1')
    if(len(courseDescs)==0):
        courseDescs = None
    courseDescsImages = Desc.objects.filter(lecon_id=id).filter(chapitre_id=pk).filter(type_desc='3').filter(image_or_text='2')
    if(len(courseDescsImages)==0):
        courseDescsImages = None
    coursePrograms = Desc.objects.filter(lecon_id=id).filter(chapitre_id=pk).filter(type_desc='4')
    if(len(coursePrograms)==0):
        coursePrograms = None
    lecon = Lecons.objects.get(id=id)
    chapitres = Chapitres.objects.filter(lecon_id=id)
    chapitre = Chapitres.objects.get(id=pk)
    context = {
        'courseOverviews': courseOverviews,
        'whatYouWillLearns': whatYouWillLearns,
        'courseDescs': courseDescs,
        'courseDescsImages': courseDescsImages,
        'coursePrograms': coursePrograms,
        'lecon': lecon,
        'chapitre': chapitre,
        'chapitres': chapitres
    }
    return render(request, 'Lecons/VideoLec.html', context)
    
def home(request):
    # user = User.objects.get(id=request.user.id)
    lecons = Lecons.objects.all().order_by('-id')
    count = len(lecons)
    context = {
        # 'user': user,
        'count': count,
        'lecons': lecons
    }
    return render(request, 'main/index.html', context)