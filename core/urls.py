from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name = 'home'), 
    path('/resume', gen_resume, name = 'gen_resume'),
]
