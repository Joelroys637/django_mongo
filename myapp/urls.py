from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_person, name='form'),
    path('success/', views.success, name='success'),
]
