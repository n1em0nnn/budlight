from django.urls import path
from . import views
urlpatterns = [

 path('',views.mybadges,name = "badge_home"),
 path('create/', views.createbadge, name = "badge_create"),
 path('edit/<int:id>/', views.editbadge, name = "badge_edit")
]

