from django.urls import path
from . import views

urlpatterns = [
    path('specific/', views.specifics, name='specific'),
]