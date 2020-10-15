from django.urls import path, include

from . import views

app_name = 'base'
urlpatterns = [
    path('', views.index),
    path('category/', include('category.urls'))
]
