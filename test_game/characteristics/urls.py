from django.urls import path
from . import views

urlpatterns = [
    path('characteristics/<int:phone_id>/', views.add_characteristics, name='characteristicsPhone'),
]