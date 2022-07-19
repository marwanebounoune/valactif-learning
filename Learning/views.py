from urllib import request
from django.shortcuts import render, redirect
from django.views import generic
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
    queryset = Desc.objects.filter(lecon_id=id)
    lecon = Lecons.objects.get(id=id)
    # nbrDesc3 = queryset
    print("lecon", lecon.name_lecon)
    context = {
        'queryset' : queryset,
        'lecon': lecon
    }
    return render(request, 'Lecons/indexDec.html', context)
    