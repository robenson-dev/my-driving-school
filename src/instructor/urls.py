from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),

    path('planning/', include([
        path('', views.planning_filter_student),
    ])),

    path('student/', include([
        path('detail/', views.student_detail),
    ]))
]
