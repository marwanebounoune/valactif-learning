from urllib import request
from django.shortcuts import render, redirect
from django.views import generic
from .models import Post


# Create your views here.
""" def Desc_list(request):
    name_chapitres = name_chapitres.objects.filter() """
def Desc(request):
    Text = Text.objects.filter(id=request.type_desc.id)
    context = {
        'Text': Text
    }
    return render(request, 'Lecons/indexDec.html', context)

def PostList(request):
    queryset = Post.objects.filter(status=1)
    print("Hello", queryset[1].title)
    template_name = 'indexDec.html'
    context = {
        'queryset' : queryset,
       
    }
    return render(request, 'Lecons/indexDec.html', context)

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'indexDec.html'

def blogs(request):
    posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-dateTime')
    return render(request, "indexDec.html", {'posts':posts})