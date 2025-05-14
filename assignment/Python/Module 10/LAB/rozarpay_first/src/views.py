from django.shortcuts import render

import razorpay 

from .models import Mobile
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    if request.method ==  'POST':
        name=request.POST.get('name')
        amount=int(request.POST.get('amount'))*100
        client=razorpay.Client(auth=("rzp_test_jLNRhcVnajRGUE","ysrnvTSc7v4dLd9Dd4XQ6MJy"))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1',})
        print("***************************",payment)

        mobile=Mobile(name=name,amount=amount,payment_id=payment['id'])
        mobile.save()
        return render(request,'index.html',{'payment':payment})


    return render(request,'index.html')
@csrf_exempt
def success(request):
    if request.method=="POST":
        a=request.POST
        order_id=""
        for key,value  in a.items():
            if  key == "razorpay_order_id":
                order_id = value
                break
        user=Mobile.objects.filter(payment_id=order_id).first()
        user.paid = True
        user.save()
        return render(request,'success.html')