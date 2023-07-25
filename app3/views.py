from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def webpage5(request):
    return render(request, 'webpage5.html')
def webpage6(request):
    return render(request, 'webpage6.html')
def string(request):
    return HttpResponse('<i>This is the string response of app3</i>')