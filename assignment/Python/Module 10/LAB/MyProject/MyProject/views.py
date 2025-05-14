from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    prams={'name': 'Abhinandan', 'age': '24'}
    return render(request,'index.html', prams)


def analyze(request):
    text1=request.GET.get('text1')
    upper=request.GET.get('upper','off')
    lower=request.GET.get('lower','off')
    title=request.GET.get('title','off')
    if upper == 'on':
        prams={'text1':text1.upper()}
    elif lower == 'on':
        prams={'text1':text1.lower()}
    elif title == 'on':
        prams={'text1':text1.title()}
    else:
        prams={'text1':text1}
    
    return render(request,'analyze.html', prams)