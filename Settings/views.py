from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Accounts.models import User
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
import logging

# Create your views here.
@login_required
def getProfile(request):
    return render(request, 'settings/profile.html')

@login_required
def editProfile(request):
    if request.method == 'GET':
        return render(request, 'settings/editProfile.html')
    elif request.method == 'POST':
        newFirstName = request.POST["newFirstName"]
        newLastName = request.POST["newLastName"]
        newPhone1 = request.POST["newPhone1"]
        newPhone2 = request.POST["newPhone2"]
        newGenre = request.POST["newGenre"]
        newBirthday = request.POST["newBirthday"]
        newPays = request.POST["newPays"]
        newVille = request.POST["newVille"]
        newEmailAddress = request.POST["newEmailAddress"]
        newPhotoProfile = request.POST["newPhotoProfile"]
        print("newGenre", newGenre)
        print("newBirthday", newBirthday)
        print("newPays", newPays)
        print("newVille", newVille)
        userUpdate = User.objects.get(username = request.user)
        userUpdate.first_name = newFirstName
        userUpdate.last_name = newLastName
        userUpdate.tel1 = newPhone1
        userUpdate.tel2 = newPhone2
        userUpdate.genre = newGenre
        userUpdate.dateNaissance = newBirthday
        userUpdate.country = newPays
        userUpdate.ville = newVille
        userUpdate.email = newEmailAddress
        newPhotoProfile.photoProfile = newPhotoProfile
        userUpdate.save()
        return redirect('getProfile')
      

@api_view(['GET'])
@login_required(login_url='login')
def user_detail(request):
    try:
        user = User.objects.get(id=request.userid)
        serializer = UserSerializer(user, many=False)
        return Response(user)
    except Exception as e:
        logging.getLogger("error_logger").error(repr(e))
        pass