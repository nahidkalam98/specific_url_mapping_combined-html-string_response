from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def webpage3(request):
    return render(request, 'webpage3.html')
def webpage4(request):
    return render(request, 'webpage4.html')
def string(request):
    return HttpResponse('<b>This is the string response of app2</b>')