from dbm import error

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def mybadges(request):
    users = User.objects.all()

    return render(request,'badges/allusers.html',{'users':users})

def createuser(request):
    error = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=form.save(), fullname=form.cleaned_data.get('fullname'))

            usergroup = form.cleaned_data.get('groups')
            user.groups.add(usergroup)

            return redirect('users_home')
        else:
            error = 'Форма заполнена не верно'
    form = SignUpForm()
    data= {
        'form': form,
        'error': error
    }
    return render(request,'badges/createuser.html',data)
def edituser(request, id):
    error = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES, instance=User.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('users_home')
        else:
            error = 'Форма заполнена не верно'
    form = SignUpForm(instance=User.objects.get(id=id))
    data = {
        'form': form,
        'error': error
    }
    return render(request,'badges/edituser.html',data)

def deleteuser(request, id):
    User.objects.filter(id=id).delete()
    return redirect('users_home')