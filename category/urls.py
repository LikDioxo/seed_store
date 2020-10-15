from django.urls import path, include

from . import views


app_name = 'category'
urlpatterns = [
    path('', views.get_all_categories),
    path('<int:category_id>/', include('kind.urls'))
]
