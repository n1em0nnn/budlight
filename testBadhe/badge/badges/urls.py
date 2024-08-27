from django.urls import path
from . import views
urlpatterns = [

 path('',views.mybadges,name = "badge_home")
]

