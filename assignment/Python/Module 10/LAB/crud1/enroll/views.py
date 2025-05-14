from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import StudentsRegisteration
from .models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#send email
import os
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.template.loader import render_to_string

#Send OTP
import random
from django.core.cache import cache
from twilio.rest import Client

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm=StudentsRegisteration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg =User(name=nm,email=em,password=pw)
            reg.save()
            fm=StudentsRegisteration()
            # fm.save()
    else:
        fm=StudentsRegisteration()
    stud=User.objects.all()
    
    return render(request,'enroll/add_show.html',{'form':fm,'stu':stud})
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm=StudentsRegisteration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm=StudentsRegisteration(instance=pi)
    return render(request,'enroll/update_students.html',{'form':fm})

#this function for delete the data
def delete_data(request, id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return  HttpResponseRedirect('/')

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm=StudentsRegisteration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm=StudentsRegisteration(instance=pi)
    return render(request,'enroll/update_students.html',{'form':fm})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('add_show')
    else:
        form = UserCreationForm()
    return render(request, 'enroll\signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('add_show')
    else:
        form = AuthenticationForm()
    return render(request, 'enroll\login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('add_show')

def javascriptvalid(request):
    return render(request,'enroll\javascriptvalid.html')

#send email

def send_email(request):
    subject = 'Test Email with Template'
    recipient_list = ['rajababu19012001@gmail.com','urajalajaan@gmail.com','gpgunjan716@gmail.com']
   
    # Render email template
    context = {'username': 'Hello Everyone !'}
    message = render_to_string('enroll\email_template.html', context)
   
    try:
        send_mail(subject, '', settings.EMAIL_HOST_USER, recipient_list, html_message=message)
        return JsonResponse({'message': 'Email sent successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    
#Send OTP

def generate_otp():
    return str(random.randint(100000, 999999))


def send_sms(request):
    phone_number = "+917488671231"
    otp = generate_otp()
   
    # Store OTP in cache for 5 minutes
    cache.set(phone_number, otp, timeout=300)
   
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f'Your OTP is {otp}',
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )
   
    return JsonResponse({'message': 'OTP sent successfully'})


def verify_otp(request):
    phone_number = request.GET.get('phone')
    entered_otp = request.GET.get('otp')
    stored_otp = cache.get(phone_number)
   
    if stored_otp and entered_otp == stored_otp:
        cache.delete(phone_number)
        return JsonResponse({'message': 'OTP verified successfully'})
    else:
        return JsonResponse({'error': 'Invalid OTP'})