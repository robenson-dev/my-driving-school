from django.db import models
# from django.contrib.auth.models import AbstractUser

# from phone_field import PhoneField
# from ckeditor.fields import RichTextField


# GENDER_CHOICES = (
#     (0, 'male'),
#     (1, 'female'),
#     (2, 'not specified'),
# )
#
# ROLES = (
#     (0, 'Student'),
#     (1, 'Instructor'),
#     (2, 'Secretary'),
#     (3, 'not specified'),
# )
#
# class User(AbstractUser):
#
#     is_instructor = models.BooleanField()
#     is_student    = models.BooleanField()
#
#     def __str__(self):
#         return self.username
#
# class Instructor(models.Model):
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     gender = models.IntegerField(choices=GENDER_CHOICES, default=2)
#     phone = PhoneField(blank=True, help_text='Contact phone number')
#     birthday = models.DateField()
#     address = models.CharField(max_length=255, blank=True)
#     avatar = models.ImageField(default='user/Instructor/default.png', upload_to='user/', null=True, blank=True)
#     role = models.IntegerField(choices=ROLES, default=1, blank=True)
#     bio = RichTextField(blank=True)
#
#     def greet(self):
#         gender = self.get_gender_display()
#         if gender == 'male':
#             return 'Hi, boy.'
#         elif gender == 'female':
#             return 'Hello, girl.'
#         else:
#             return 'Hey there, user!'
#
#     def __str__(self):
#         return self.user.username
#
#
# class Student(models.Model):
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     gender = models.IntegerField(choices=GENDER_CHOICES, default=2)
#     phone = PhoneField(blank=True, help_text='Contact phone number')
#     birthday = models.DateField()
#     address = models.CharField(max_length=255)
#     avatar = models.ImageField(default='user/Instructor/default.png', upload_to='user/', null=True, blank=True)
#     role = models.IntegerField(choices=ROLES, default=0)
#
#     def __str__(self):
#         return self.user.username
