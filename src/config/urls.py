from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Student.urls')),
    path('secretary/', include('Secretary.urls')),
    path('instructor/', include('instructor.urls')),
    path('planning/', include('planning.urls')),
]
