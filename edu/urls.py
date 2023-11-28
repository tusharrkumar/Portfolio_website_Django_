from django.urls import path
from .views import *

urlpatterns = [
    path('skill/',skill,name='skill'),
    path('project/',project,name='project'),
]