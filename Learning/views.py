from multiprocessing import context
from Accounts.models import User
from .models import Chapitres, Lecons, Desc
from .models import Lecons, Desc, About, article
from django.shortcuts import  render

from django.core.paginator import Paginator


def getDesc(request):
    Text = Text.objects.filter(id=request.type_desc.id)
    context = {
        'Text': Text
    }
    return render(request, 'Lecons/indexDec.html', context)

def getLecon(request, id):
    courseOverviews = Desc.objects.filter(lecon_id=id).filter(type_desc='1')
    if(len(courseOverviews) == 0):
        courseOverviews = None
    whatYouWillLearns = Desc.objects.filter(lecon_id=id).filter(type_desc='2')
    if(len(whatYouWillLearns)==0):
        whatYouWillLearns = None
    courseDescs = Desc.objects.filter(lecon_id=id).filter(type_desc='3').filter(image_or_text='1')
    if(len(courseDescs)==0):
        courseDescs = None
    courseDescsImages = Desc.objects.filter(lecon_id=id).filter(type_desc='3').filter(image_or_text='2')
    if(len(courseDescsImages)==0):
        courseDescsImages = None
    coursePrograms = Desc.objects.filter(lecon_id=id).filter(type_desc='4')
    if(len(coursePrograms)==0):
        coursePrograms = None
    lecon = Lecons.objects.get(id=id)
    chapitres = Chapitres.objects.filter(lecon_id=id)
    chapitres_ = None
    for chap in chapitres:
        if len(chap.introduction) < 250:
            print("chap ->", len(chap.introduction))
        else:
            print("chap ->", chap.introduction[0:255])
            chap.introduction = chap.introduction[0:255]+"..."
    context = {
        'courseOverviews': courseOverviews,
        'whatYouWillLearns': whatYouWillLearns,
        'courseDescs': courseDescs,
        'courseDescsImages': courseDescsImages,
        'coursePrograms': coursePrograms,
        'lecon': lecon,
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
    for chap in chapitres:
        if len(chap.introduction) < 250:
            print("chap ->", len(chap.introduction))
        else:
            print("chap ->", chap.introduction[0:255])
            chap.introduction = chap.introduction[0:255]+"..."
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
    user = User.objects.filter(id=request.user.id)
    lecons = Lecons.objects.all().order_by('-id')
    aboutus = About.objects.all()
    sarticle = article.objects.all().order_by('-id')
    if len(sarticle) == 0:
        sarticle = None
    context = {
        "aboutus" : aboutus,
        "sarticle": sarticle,
        'lecons': lecons,
    }
    return render(request, 'main/index.html', context)

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
    if len(course) == 0:
        course=None
        page=1
    else:
        page = Paginator(course, 9)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
    context = {
        'course': course,
        'lecons': lecons,
        'page' : page
    }
    return render (request, 'main/courses.html',context)


def articles(request):
    Article = article.objects.all()
    sarticle = article.objects.all().order_by('-id')
    context = {
        'Article': Article,
        'sarticle': sarticle
        }
    return render (request, 'main/blog.html', context)

def singlearticle(request, id):
    sarticle = article.objects.filter(id = id)
    return render (request, 'main/article.html', {"sarticle":sarticle})

def allBlog(request):
    Article = article.objects.all()
    sarticle = article.objects.all().order_by('-id')
    if len(Article) == 0:
        Article=None
        page=1
    else:
        page = Paginator(Article, 9)
        page_list = request.GET.get('page')
        page = page.get_page(page_list)
    if len(sarticle) == 0:
        sarticle=None
    context = {
        'Article': Article,
        'sarticle': sarticle,
        'page' : page
    }
    
    
    return render (request, 'main/blog.html' ,context)


def singlearticle(request, id):
    Article = article.objects.all().exclude(id=id)
    sarticle = article.objects.filter(id = id)
    context = {
        "Article": Article,
        "sarticle": sarticle
    }
    return render (request, 'main/article.html', context)

def offline(request):
    return render (request, 'partials/offline.html')
