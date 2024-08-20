from django.shortcuts import render
from .models import Badges

def index(request):

    return render(request,'main/index.html')
def mybadges(request):
    badges = Badges.objects.all()
    return render(request,'main/mybadge.html',{'badges':badges})