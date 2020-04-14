from django.urls import path, include
from .views import (
    InstructorListView,
    InstructorDetailView,
    InstructorCreateView,
    InstructorUpdateView,
    InstructorDeleteView
)
from . import views


app_name = 'secretary'
urlpatterns = [
    path('', views.index, name='home'),

    path('instructor/', include([
        path('create/', InstructorCreateView.as_view(), name="instructor-create"),
        path('', InstructorListView.as_view(), name='instructor-list'),
        path('<int:pk>/', InstructorDetailView.as_view(), name='instructor-detail'),
        path('<int:pk>/update/', InstructorUpdateView.as_view(), name='instructor-update'),
        path('<int:pk>/delete/', InstructorDeleteView.as_view(), name='instructor-delete'),
    ]))

]
