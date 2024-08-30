from dbm import error

from django.shortcuts import render, redirect
from .models import Badge
from .forms import BadgeForm
# Create your views here.
def mybadges(request):
    badges = Badge.objects.all()

    return render(request,'badges/mybadge.html',{'badges':badges})

def createbadge(request):
    error = ''
    if request.method == 'POST':
        form = BadgeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return redirect('badge_home')
        else:
            error = 'Форма заполнена не верно'
    form = BadgeForm()
    data= {
        'form': form,
        'error': error
    }
    return render(request,'badges/createbadge.html',data)
def editbadge(request, id):
    error = ''
    if request.method == 'POST':
        form = BadgeForm(request.POST,request.FILES, instance=Badge.objects.get(id=id))
        if form.is_valid():
            form.save()
            return redirect('badge_home')
        else:
            error = 'Форма заполнена не верно'
    form = BadgeForm(instance=Badge.objects.get(id=id))
    data = {
        'form': form,
        'error': error
    }
    return render(request,'badges/edit.html',data)

def deletebadge(request, id):
    Badge.objects.filter(id=id).delete()
    return redirect('badge_home')