from django.urls import path
from . import views
urlpatterns = [

 path('',views.mybadges,name = "users_home"),
 path('create/', views.createuser, name = "users_create"),
 path('edit/<int:id>/', views.edituser, name = "users_edit"),
 path('delete/<int:id>/', views.deleteuser, name = "users_delete")

]