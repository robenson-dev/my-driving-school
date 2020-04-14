from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User, Instructor

from ckeditor.widgets import CKEditorWidget


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email','password1', 'password2', 'is_secretary', 'is_instructor', 'is_student']


# class InstructorForm(forms.ModelForm):
#
#     class Meta:
#         model = Instructor
#         fields = ('bio','address')
