from django.urls import path
from .views import *


urlpatterns = [
    path('main/', index),
    path('about/', about)
]