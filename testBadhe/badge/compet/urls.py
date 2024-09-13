from django.urls import path
from . import views
urlpatterns = [

 path('',views.allcomps,name = "compets_home"),
 path('create/', views.createcompet, name = "compets_create"),
 path('edit/<int:id>/', views.editcompet, name = "compets_edit"),
 path('delete/<int:id>/', views.deletecompet, name = "compets_delete")

]