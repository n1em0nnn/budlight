from django.shortcuts import render
from .models import Title_news

def index(request):
    news = Title_news.objects.order_by('-dates')
    return render(request,'main/index.html', {'news': news})
