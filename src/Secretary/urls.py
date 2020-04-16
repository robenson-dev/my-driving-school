from django.urls import path, include
from .views import (
    InstructorListView,
    InstructorDetailView,
    InstructorCreateView,
    InstructorUpdateView,
    InstructorDeleteView,

    StudentCreateView,
    StudentListView,
    StudentDetailView,
    StudentUpdateView,
    StudentDeleteView,

    EventCreateView,
    EventListView,
    EventDetailView,
    EventUpdateView,
    EventDeleteView,

    CourseListView
)
from . import views


app_name = 'secretary'
urlpatterns = [
    path('', views.index, name='home'),
    path('planning/', include([
        path('', views.planning_filter),
        path('appointment/', include([
            path('create/', EventCreateView.as_view(), name='appointment-create'),
            path('', EventListView.as_view(), name='appointment-list'),
            path('<int:pk>/', EventDetailView.as_view(), name='appointment-detail'),
            path('<int:pk>/update/', EventUpdateView.as_view(), name='appointment-update'),
            path('<int:pk>/delete/', EventDeleteView.as_view(), name='appointment-delete'),
        ]))

    ])),
    path('instructor/', include([
        path('create/', InstructorCreateView.as_view(), name="instructor-create"),
        path('', InstructorListView.as_view(), name='instructor-list'),
        path('<int:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),
        path('<int:pk>/update/', InstructorUpdateView.as_view(), name='instructor-update'),
        path('<int:pk>/delete/', InstructorDeleteView.as_view(), name='instructor-delete'),
    ])),
    path('student/', include([
        path('create/', StudentCreateView.as_view(), name="student-create"),
        path('', StudentListView.as_view(), name='student-list'),
        path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
        path('<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
        path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    ])),
    path('course/', include([
        path('', CourseListView.as_view(), name='course-list'),
        path('<int:pk>/', views.detail_course, name='course-detail')
    ]))

]
