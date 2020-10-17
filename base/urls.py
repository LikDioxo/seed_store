from django.urls import path, include

from . import views
from customer import views as customer_views

app_name = 'base'
urlpatterns = [
    path('', views.index),
    path('category/', include('category.urls')),
    path('register/', customer_views.register),
    path('login/', customer_views.login),
]
