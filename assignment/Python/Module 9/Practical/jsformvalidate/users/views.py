from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Basic backend validation (just for demonstration)
        if username and email and password:
            return HttpResponse("Registration Successful!")
        return HttpResponse("Missing fields!")
    return render(request, 'users/register.html')
