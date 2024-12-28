from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('phone/', views.phones, name='phone'),
    path('phone/details/<int:id>', views.details, name='details'),
    path('add_phone/', views.add_phone, name='add_phone'),
]