from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard),
    path('symptoms/',views.disease),
    path('notification/', views.notifications),
    path('dashboard/edit',views.edit_profile,name="edit"),
    path('map/',views.maps)

]
