from django.urls import path, include
from .views import index


# app_name = 'secretary'
urlpatterns = [
    path('', index, name='home')
]
