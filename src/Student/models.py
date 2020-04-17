from django.db import models
from Secretary.models import Course
from users.models import User


class Subscription(models.Model):

    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    valid = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.user.username
