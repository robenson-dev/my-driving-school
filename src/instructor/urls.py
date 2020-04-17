from django.urls import path, include
from .views import (
    StudentEventCreateView,
    StudentEventCreateView,
    StudentEventDeleteView
)
from . import views


app_name ='instructor'
urlpatterns = [
    path('', views.index),

    path('planning/', include([
        path('', views.planning_filter_student),
        path('appointment/', include([
            path('', views.student_planning),
            path('create/', StudentEventCreateView.as_view(), name="appointment-create"),
            path('<int:pk>/update/', StudentEventCreateView.as_view(), name='appointment-update'),
            path('<int:pk>/delete/', StudentEventDeleteView.as_view(), name='appointment-delete'),
        ]))
    ])),

    path('student/', include([
        path('detail/', views.student_detail),
    ]))
]
