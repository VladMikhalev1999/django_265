from django.urls import path
from .views import *

app_name = "app"

urlpatterns = [
    path('category/', index, name="main"),
    path('about/', about, name='about')
]