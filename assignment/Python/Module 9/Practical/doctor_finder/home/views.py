from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def doctor_profile(request):
    return render(request, 'home/doctor_profile.html')
 