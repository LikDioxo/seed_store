from django.urls import path, include

from . import views


app_name = 'kind'
urlpatterns = [
    path('', views.get_all_kinds_by_category_id),
    path('<int:kind_id>/', include('grades.urls')),
]

