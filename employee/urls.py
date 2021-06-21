from . import views
from django.urls import path

urlpatterns = [
    path('', views.employee),
    path('salary/', views.salary),
]