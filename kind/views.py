from django.shortcuts import render
from django.http import HttpResponse

from .models import Kind


def get_all_kinds_by_category_id(request, category_id):
    return HttpResponse(Kind.objects.filter(category_id=category_id))
