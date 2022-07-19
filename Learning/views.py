from urllib import request
from django.shortcuts import render, redirect
from django.views import generic

from Accounts.models import User
from .models import Lecons, Desc


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
    print("lecon", lecon.name_lecon)
    context = {
        'courseOverviews': courseOverviews,
        'whatYouWillLearns': whatYouWillLearns,
        'courseDescs': courseDescs,
        'coursePrograms': coursePrograms,
        'countCourseDescs' : countCourseDescs,
        'lecon': lecon
    }
    return render(request, 'Lecons/indexDec.html', context)
    
def home(request):
    user = User.objects.filter(id=request.user.id)
    context = {
        'user': user
    }
    return render(request, 'main/index.html', context)