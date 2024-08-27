from django.shortcuts import render
from .models import Badge
# Create your views here.
def mybadges(request):
    badges = Badge.objects.all()

    return render(request,'badges/mybadge.html',{'badges':badges})