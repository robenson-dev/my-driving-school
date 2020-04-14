from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from users.forms import UserRegisterForm, UserUpdateForm, InstructorForm
from django.contrib import messages



def index(request):
    return render(request, 'secretary/home-list.html', locals())


def create_instructor(request):

    user_form = UserRegisterForm(request.POST or None)
    if user_form.is_valid():
        user_form.save()
        username = user_form.cleaned_data.get('username')
        messages.success(request, f' The {username} account has been created')
        return redirect('secretary:read-list')

    return render(request, 'secretary/user/instructor/created.html', locals())


def read_instructor(request):
    users_form = User.objects.all()
    return render(request, 'secretary/user/instructor/read-list.html', locals())


def update_instructor(request, userID=None):

    user = get_object_or_404(User, id=userID)

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f' The {username} account has been updated')
            return redirect('secretary:read-list')
    else:
        user_form = UserRegisterForm(instance=user)

    return render(request, 'secretary/user/instructor/update.html', locals())
