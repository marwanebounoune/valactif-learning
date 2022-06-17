import imp
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages, auth
from django.urls import reverse_lazy

# Create your views here.
   
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'GET':
            return render(request, 'accounts/login2.html')
        if request.method == 'POST':
            erreur=0
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            # user.save()
            if (user is not None):
                user.save()
                print("Hello")
                auth.login(request, user)
                return redirect('home')
            else:
                erreur=1
                messages.error(request, "Votre login ou mot de passe et incorrect.")
                return render(request, 'accounts/login2.html', {'erreur':erreur})
        else:
            return render(request, 'accounts/login2.html')

def logout_custumized(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    user = User.objects.filter(id=request.user.id)
    context = {
        'user': user
    }
    return render(request, 'main/index.html', context)



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