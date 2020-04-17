from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('planning/', views.student_planning)
]
