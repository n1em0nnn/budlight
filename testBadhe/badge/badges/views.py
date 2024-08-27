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
        form = BadgeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('badge_home')
        else:
            error = 'Форма заполнена не верно'
    form = BadgeForm()
    data= {
        'form': form,
        'error': error
    }
    return render(request,'badges/createbadge.html',data)