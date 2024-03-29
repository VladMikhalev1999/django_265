from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import Category

"""
def index(request):
    return HttpResponse("<h1>Главная</h1>")



def about(request):
    return HttpResponse("<h1>О нас</h1>")
"""


def index(request):
    categories = Category.objects.all().order_by("name", "id")
    Category.objects.filter(name="Колье")
    return render(request, "app/index.html", {"cate": categories, "title": "Главная"})


def about(request):
    return render(request, "app/about.html")




