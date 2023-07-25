from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def webpage1(request):
    return render(request, 'webpage1.html')
def webpage2(request):
    return render(request, 'webpage2.html')
def string(request):
    return HttpResponse('<marquee>This is the string response of app1</marquee>')