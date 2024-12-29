from django.urls import path
from . import views

urlpatterns = [
    path('specific/<int:phone_id>/', views.add_specific, name='specific'),
]