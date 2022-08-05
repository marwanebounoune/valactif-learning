from django.shortcuts import render
from threading import Thread
from django.contrib import messages
import re
from .models import Contacts
from smtplib import SMTPException
from django.conf import settings
from threading import Thread
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect, render
from django.utils.html import strip_tags

# Create your views here.

def homeContact(request):
    if request.method == 'GET':
        return render(request, 'main/contact.html')
    elif request.method == 'POST':
        erreur = 0
        valid_email=0
        nom = request.POST['name']
        mail = request.POST['email']
        sujet = request.POST['subject']
        message = request.POST['message']
        print("nom ->", nom)
        print("mail ->", mail)
        print("sujet ->", sujet)
        print("message ->", message)
        if len(nom) == 0:
            erreur = 1
            messages.error(request, 'Merci de compléter le champs relatif au nom complet')
        elif len(nom)>50:
            erreur = 1
            messages.error(request, 'Le champs relatif au nom ne doit pas dépasser 50 caractères')
        if len(mail) == 0:
            erreur = 1
            messages.error(request, 'Merci de compléter le champs relatif à l\'email')
        else:
            if len(mail) > 254:
                erreur = 1
                messages.error(request, 'Le champs relatif à l\'email ne doit pas dépasser 254 caractères')
            if validateEmail(mail) == 0:
                valid_email=1
                erreur = 1
                messages.error(request, "Format de l'adresse e-mail est non valide")
        if len(sujet) == 0:
            erreur = 1
            messages.error(request, 'Merci de compléter le champs relatif au subject complet')
        elif len(sujet)>50:
            erreur = 1
            messages.error(request, 'Le champs relatif au subject ne doit pas dépasser 50 caractères')
        if len(message) == 0:
            erreur = 1
            messages.error(request, 'Merci de compléter le champs relatif au message')
        if erreur == 0:
            contact_validation = Contacts(nom=nom, email=mail, sujet=sujet, message=message)
            contact_validation.save()
            html_content = render_to_string("partials/email_template.html",{'Title':sujet,'Content': message})
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                "Demande de devis",
                text_content,
                settings.EMAIL_HOST_USER,
                {mail}
            )
            try:
                email.attach_alternative(html_content, "text/html")
                EmailThread(email).start()
            except SMTPException as e:
                print('There was an error sending an email: ', e)
            messages.success(request, 'Votre demande a été bien enregistrée, Une confirmation vous sera envoyée à l\'adresse email indiquée,  Merci de bien vouloir vérifier votre boîte de réception: '+ mail)
            return redirect('login') 
        else:
            contact_validation = Contacts(nom=nom, email=mail, sujet=sujet, message=message)
            context = {
                'contact_validation': contact_validation,
                'valid_email': valid_email,
                'erreur': erreur
            }
            return render(request, 'quotes/quote.html',context)

def quotation(request):
    if request.method == 'GET':
        return render(request, 'quotes/quote.html')
    if request.method == 'POST':

        #Variable
        erreur = 0
        # devis_validation = Contacts()
        valid_email=0
        valid_phone=0
        #Récupération de la Data
        nom = request.POST['nom']
        mail = request.POST['email']
        societe = request.POST['societe']
        secteur = request.POST['secteur']
        message = request.POST['message']
        
        #Vérification de la Data
        if len(nom) == 0:
            erreur = 1
            messages.error(request, 'Merci de compléter le champs relatif au nom complet')
        elif len(nom)>50:
            erreur = 1
            messages.error(request, 'Le champs relatif au nom ne doit pas dépasser 50 caractères')
        if len(mail) == 0:
            erreur = 1
            messages.error(request, 'Merci de compléter le champs relatif à l\'email')
        else:
            if len(mail) > 254:
                erreur = 1
                messages.error(request, 'Le champs relatif à l\'email ne doit pas dépasser 254 caractères')
            if validateEmail(mail) == 0:
                valid_email=1
                erreur = 1
                messages.error(request, "Format de l'adresse e-mail est non valide")
        if len(societe) == 0:
            erreur = 1
            messages.error(request, 'Merci de compléter le champs relatif à la société')
        elif len(societe) > 200:
            erreur = 1
            messages.error(request, 'Le champs relatif à la société ne doit pas dépasser 200 caractères')      
        if len(secteur) == 0:
            erreur = 1
            messages.error(request, 'Merci de compléter le champs relatif au activité de la société')
        if len(message) == 0:
            erreur = 1
            messages.error(request, 'Merci de compléter le champs relatif au message')
        if erreur == 0:
            #Enregistrer le devis
            devis = Contacts(nom=nom, email=mail, societe=societe, secteur=secteur, message=message)
            devis.save()
            #Envoyer une email  
            html_content = render_to_string("email_template.html",{'Title':'Demande de devis','Content': 'message content'})   
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                #subject
                "Demande de devis",
                #content
                text_content,
                #from_email
                settings.EMAIL_HOST_USER,
                #recepient
                {mail},
                #fail_silently=True
            )
            try:
                email.attach_alternative(html_content, "text/html")
                EmailThread(email).start()
            except SMTPException as e:
                print('There was an error sending an email: ', e)
            messages.success(request, 'Votre demande a été bien enregistrée, Une confirmation vous sera envoyée à l\'adresse email indiquée,  Merci de bien vouloir vérifier votre boîte de réception: '+ mail)
            return redirect('login')
        if erreur == 1:
            devis_validation = Contacts(nom=nom, email=mail, societe=societe, secteur=secteur, message=message)
            context = {
                'devis_validation': devis_validation,
                'valid_phone': valid_phone,
                'valid_email': valid_email,
                'erreur': erreur
                }
            return render(request, 'quotes/quote.html',context)
    

#multithreading pour accélérer l'envoie de l'email
class EmailThread(Thread):
    def __init__(self, email):
        self.email = email
        Thread.__init__(self)

    def run (self):
        self.email.send()

#regex mail
def validateEmail(email):
    if len(email) > 6:
        if re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email) != None:
            return 1
    return 0
