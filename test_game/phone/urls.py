from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('phone/', views.phones, name='phone'),
    path('phone/details/<int:id>/', views.details, name='details'),
    path('phone/details/<int:phone_id>/add_specific/', views.add_specific, name='add_specific'),
    path('add_phone/', views.add_phone, name='add_phone'),
]