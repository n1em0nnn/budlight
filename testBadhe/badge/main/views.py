from django.shortcuts import render


def index(request):

    return render(request,'main/index.html')
def mybadges(request):
    data = {
        'badgesample': {
            'title': 'Project нихуя не success',
            'about': 'You made a great job',
            'img': 'None'
        }
    }
    return render(request,'main/mybadge.html',data)