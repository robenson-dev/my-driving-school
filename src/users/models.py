from django.db import models
from django.contrib.auth.models import AbstractUser

from phone_field import PhoneField
from ckeditor.fields import RichTextField


GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)

class User(AbstractUser):

    is_secretary    = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_student    = models.BooleanField(default=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username


class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    gender = models.IntegerField(choices=GENDER_CHOICES, default=2)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255)
    avatar = models.ImageField(default='user/Student/default.png', upload_to='user/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Instructor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    gender = models.IntegerField(choices=GENDER_CHOICES, default=2)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(default='user/Instructor/default.png', upload_to='user/', null=True, blank=True)
    bio = RichTextField(blank=True)


    def greet(self):
        gender = self.get_gender_display()
        if gender == 'male':
            return 'Hi, boy.'
        elif gender == 'female':
            return 'Hello, girl.'
        else:
            return 'Hey there, user!'

    def __str__(self):
        return self.user.username
