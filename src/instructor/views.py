from django.shortcuts import render
from users.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from planning.models import Event

from django.core import serializers
from django.http import JsonResponse

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    return render(request, 'instructor/home-list.html', locals())

#------------------------------------------------------------------------------[ USER-PLANNING ]-----------------------------------------------------------------#
@login_required
def planning_filter_student(request):

    if request.user.is_instructor == True:
        events = Event.objects.filter(creator=request.user.id)
        qs_json = serializers.serialize('json', events)

    return render(request, 'instructor/planning/calendar/index.html', locals())


@login_required
def student_detail(request):

    user_contains = request.GET.get('user_search')
    users = User.objects.filter(Q(username=user_contains))

    return render(request, 'instructor/student/detail.html', locals())


@login_required
def student_planning(request):
    events = Event.objects.filter(person=request.user.id)
    return render(request, 'instructor/planning/event/read-list.html', locals())


class StudentEventCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Event
    fields = '__all__'
    template_name = 'secretary/planning/event/create.html'
    success_message = f' The event has been created'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StudentEventUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Event
    fields = '__all__'
    template_name = 'secretary/planning/event/update.html'
    success_message = f' The event has been updated'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StudentEventDeleteView(DeleteView):

    model = Event
    template_name = 'secretary/planning/event/delete.html'
    success_url = '/instructor/planning/appointment/'
