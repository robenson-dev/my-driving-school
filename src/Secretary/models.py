from django.db import models
from users.models import User
from ckeditor.fields import RichTextField


class Course(models.Model):

    course_name = models.CharField(max_length=255)
    course_code = models.CharField(blank=True, max_length=255, null=True)
    course_details = RichTextField()

    start = models.DateTimeField('start', db_index=True, blank=True)
    end = models.DateTimeField('end', blank=True)
    course_time = models.TimeField(blank=True, null=True)
    course_price = models.IntegerField(blank=True, null=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

    course_photo = models.ImageField(default='secretary/courses/default.png', upload_to='courses/', null=True, blank=True)

    def __str__(self):
        return self.course_name
