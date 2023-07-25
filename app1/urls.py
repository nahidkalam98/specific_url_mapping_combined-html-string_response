from django.urls import path
from app1.views import *
app_name='something'

urlpatterns=[
    path('webpage1/', webpage1, name = 'webpage1'),
    path('webpage2/', webpage2, name = 'webpage2'),
    path('string/', string, name = 'string'),
]