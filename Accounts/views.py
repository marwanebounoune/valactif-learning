import imp
from django.shortcuts import render
from .models import BlogPost, User, Document
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.

def login(request):
    user = User.objects.filter(id=request.user.id)
    context = {
        'user': user
    }
    
    return render(request, 'accounts/account_settings.html', context)



# class DocumentCreateView(CreateView):
#     model = Document
#     fields = ['upload', ]
#     success_url = reverse_lazy('home')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         documents = Document.objects.all()
#         context['documents'] = documents
#         return context

# def home(request):
#     return render(request, 'home.html', {'posts': BlogPost.objects.all()})