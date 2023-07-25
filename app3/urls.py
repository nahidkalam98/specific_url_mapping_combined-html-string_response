from django.urls import path
from app3.views import *
app_name='anything'

urlpatterns=[
    path('webpage5/', webpage5, name = 'webpage5'),
    path('webpage6/', webpage6, name = 'webpage6'),
    path('string/', string, name = 'string'),
]