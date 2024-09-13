from dbm import error

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import CompModel,CompLevel, Result
from .forms import CompCreateForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def allcomps(request):
    comps = CompModel.objects.all()

    return render(request,'compets/allcompet.html',{'comps':comps})

def createcompet(request):
    error = ''
    if request.method == 'POST':
        form = CompCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compets_home')
        else:
            error = 'Форма заполнена не верно'
    form = CompCreateForm()
    data= {
        'form': form,
        'error': error
    }
    return render(request,'compets/createcompet.html',data)
def editcompet(request, id):
    error = ''
    if request.method == 'POST':
        form = CompCreateForm(request.POST,request.FILES, instance=CompModel.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('compets_home')
        else:
            error = 'Форма заполнена не верно'
    form = CompCreateForm(instance=CompModel.objects.get(id=id))
    data = {
        'form': form,
        'error': error
    }
    return render(request,'compets/editcompet.html',data)

def deletecompet(request, id):
    CompModel.objects.filter(id=id).delete()
    return redirect('compets_home')