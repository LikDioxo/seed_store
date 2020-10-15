from django.urls import path

from . import views


app_name = 'grades'
urlpatterns = [
    path('', views.get_all_grades_by_category_and_kind_id),
    path('<int:grade_id>/', views.get_grade_by_id),
]
