from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctor/', views.doctor_profile, name='doctor_profile'),
]
