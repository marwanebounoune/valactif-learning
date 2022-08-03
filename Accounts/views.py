import imp
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from Learning.models import Lecons, Desc
from .models import User
from django.contrib import messages, auth
from django.urls import reverse_lazy
from .forms import EditUserProfileForm
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from Valactif_Learning import settings
from . token import generate_token
from django.core.mail import EmailMessage, send_mail
from django.utils.encoding import force_str
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin







# Create your views here.
def index(request):
    return render (request, 'home.html',{})
    
def lecons(request):
     """ descriptions = Desc.objects.get(lecon_id=1)
     lecon = Lecons.objects.filter(id = 1)
     context = {
         'descriptions' : descriptions,
         'lecon': lecon
     } """
     return render(request, 'Lecons/indexDec.html')

def leconsVideo(request):
        
       
    return render(request, 'Lecons/VideoLec.html')
  
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'GET':
            return render(request, 'accounts/login2.html')
        if request.method == "POST":
            erreur=0
            username = request.POST['username']
            password = request.POST['password']
            print("username:", username)
            print("password:", password)
            user = auth.authenticate(username=username, password=password)
            # user.save()
            if (user is not None):
                print(user.is_connected)
                user.is_connected = True
                user.save()
                auth.login(request, user)
                return redirect('home')
            else:
                erreur=1
                messages.error(request, "Votre login ou mot de passe et incorrect.")
                return render(request, 'accounts/login2.html', {'erreur':erreur})
        else:
            return render(request, 'accounts/login2.html')

def logout_custumized(request):
    user = request.user
    print(user)
    user.is_connected = False
    user.save()
    auth.logout(request)
    return redirect('login')

# @login_required(login_url='login')



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
class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    form_class = EditUserProfileForm
    login_url = 'login'
    template_name = "Accounts/edit_user_profile.html"
    success_url = reverse_lazy('home')
    success_message = "User updated"
    
    def get_object(slef):
        return slef.request.user 
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please submit the form carefully")
        return redirect('home') 

def index(request):
    Desc = {
        'overview_dec' : request.Desc.overview_dec,
        'first_dec' : request.Desc.first_dec,
        'second_dec' : request.Desc.second_dec,
    }
    return render(request, 'Lecons/indexDec.html',{'Desc':Desc})



def signup(request):
    if request.method == "POST":
        username = request.POST['newUsername']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['newEmail']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print("username:",username)
        print("fname:",fname)
        print("lname:",lname)
        print("email:",email)
        print("pass1:",pass1)
        print("pass2:",pass2)
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        # if User.objects.filter(email=email).exists():
        #     messages.error(request, "Email Already Registered!!")
        #     return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        
        # Welcome Email
        subject = "Welcome to VLEARNING!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nVLEARNING team"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email VLearning!!"
        message2 = render_to_string('Accounts/email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('login')
        
        
    return render(request, "Accounts/signup.html")

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        messages.success(request, "Your Account has been activated!!")
        return redirect('login')
    else:
        return render(request,'signup')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')