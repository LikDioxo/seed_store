from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET

from .models import Grade


@require_GET
def get_all_grades_by_category_and_kind_id(request, category_id, kind_id):
    grades = Grade.objects.filter(kind__category_id=category_id, kind_id=kind_id)
    return HttpResponse(grades)


@require_GET
def get_grade_by_id(request, category_id, kind_id, grade_id):
    return HttpResponse(Grade.objects.filter(kind__category_id=category_id, kind_id=kind_id, id=grade_id))
