from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from users.models import User
from users.forms import UserRegisterForm
from django.contrib import messages


def index(request):
    return render(request, 'secretary/home-list.html', locals())


class InstructorCreateView(LoginRequiredMixin, SuccessMessageMixin, FormView):

    template_name = 'secretary/user/instructor/create.html'
    form_class = UserRegisterForm
    success_message = f' The user account has been created'
    success_url = '/secretary/instructor/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class InstructorListView(LoginRequiredMixin, ListView):

    model = User
    template_name = 'secretary/user/instructor/read-list.html'
    context_object_name = 'users_form'
    ordering = ['-date_joined']

        # if user.is_secretary:
            # return True
        # return False


class InstructorDetailView(DetailView):

    model = User
    template_name = 'secretary/user/instructor/read-detail.html'


class InstructorUpdateView(LoginRequiredMixin,UpdateView):

    model = User
    template_name = 'secretary/user/instructor/update.html'
    fields = ['first_name', 'last_name', 'username', 'email']
    context_object_name = 'form'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class InstructorDeleteView(DeleteView):

    model = User
    template_name = 'secretary/user/instructor/delete.html'
    success_url = '/secretary/instructor/'
