from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('car/<car_id>', views.car, name='car'),
    path('category/<category_name>', views.category, name='category')
]