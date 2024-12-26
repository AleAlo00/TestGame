from django.urls import path
from . import views

urlpatterns = [
    path('characteristics/', views.characteristicsPhone, name='characteristicsPhone'),
]