from django.shortcuts import render, redirect
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
    errors = {}
    categories = Category.objects.all().order_by("name", "id")
    if request.method == "POST":
        id = request.POST.get("id")
        try:
            category = Category.objects.get(pk=id)
            category.delete()
        except:
            errors["id"] = f"Категории с id = {id} не существует"
    return render(request, "app/index.html", {"cate": categories, "title": "Главная", "errors": errors})


def category_add(request):
    name = request.POST.get("name", "")
    errors = {}
    if request.method == "POST":
        if name == "":
            errors["name"] = "Поле Наименование не может быть пустым"
        else:
            try:
                category = Category()
                category.name = name
                category.save()
                return redirect("app:main")
            except:
                errors["name"] = "Категория с таким названием уже существует"
    return render(request, "app/category_add.html", {"name": name, "errors": errors})


def category_edit(request, id=-1):
    try:
        category = Category.objects.get(pk=id)
    except:
        return redirect("app:category_add")
    errors = {}
    if request.method == "POST":
        name = request.POST.get("name")
        if name == "":
            errors["name"] = "Поле Наименование не может быть пустым"
        else:
            try:
                category.name = name
                category.save()
                return redirect("app:main")
            except:
                errors["name"] = "Категория с таким названием уже существует"
    return render(request, "app/category_edit.html", {"cat": category, "errors": errors})


def about(request):
    return render(request, "app/about.html")




