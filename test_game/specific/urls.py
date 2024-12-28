from django.urls import path
from . import views

urlpatterns = [
    path('specific/', views.add_specific, name='specific'),
]