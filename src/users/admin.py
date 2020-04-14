from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Student, Instructor


# Register your models here.
admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Instructor)
