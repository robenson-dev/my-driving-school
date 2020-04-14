from django.forms import ModelForm
from .models import Instructor
from django.contrib.auth.models import User


# class UserForm(ModelForm):
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username']
#
#
# class InstructorForm(ModelForm):
#
#     class Meta:
#         model = Instructor
#         fields = '__all__'
        # fields = ['gender', 'phone', 'birthday','address', 'avatar', 'role', 'bio']
