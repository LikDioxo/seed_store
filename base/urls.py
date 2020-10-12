from django.urls import path, include

from . import views

app_name = 'base'
urlpatterns = [
    path('', views.index),
    path('grades/', include('grades.urls')),
    path('test/', include('frontend.urls')),
    path('category/', include('category.urls'))
]
