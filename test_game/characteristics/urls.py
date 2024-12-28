from django.urls import path
from . import views

urlpatterns = [
    path('characteristics/', views.add_characteristics, name='characteristicsPhone'),
]