from django.urls import path
from app2.views import *
app_name='nothing'

urlpatterns=[
    path('webpage3/', webpage3, name = 'webpage3'),
    path('webpage4/', webpage4, name = 'webpage4'),
    path('string/', string, name = 'string'),
]