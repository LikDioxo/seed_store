from django.shortcuts import render
from django.http import HttpResponse
from .models import Category


def get_category_by_id(request, category_id):
    a = Category.objects.get(id=category_id)
    return HttpResponse(a)


def get_all_categories(request):
    return HttpResponse(Category.objects.all())
