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
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.db.models import Q
from users.models import User
from planning.models import Event
from Secretary.models import Course
from Student.models import Subscription

from users.forms import UserRegisterForm

from django.core import serializers
from django.http import JsonResponse
import stripe

stripe.api_key = "sk_test_T28WIocgbLEBrnuoAZ6P4R7000vjrtYfb3"


def index(request):
    return render(request, 'secretary/home-list.html', locals())


#------------------------------------------------------------------------------[ USER-INSTRUCTOR ]-----------------------------------------------------------------#
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


#------------------------------------------------------------------------------[ USER-STUDENT ]-----------------------------------------------------------------#
class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, FormView):

    template_name = 'secretary/user/student/create.html'
    form_class = UserRegisterForm
    success_message = f' The user account has been created'
    success_url = '/secretary/student/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StudentListView(LoginRequiredMixin, ListView):

    model = User
    template_name = 'secretary/user/student/read-list.html'
    context_object_name = 'users_form'
    ordering = ['-date_joined']


class StudentDetailView(DetailView):

    model = User
    template_name = 'secretary/user/student/read-detail.html'


class StudentUpdateView(LoginRequiredMixin,UpdateView):

    model = User
    template_name = 'secretary/user/student/update.html'
    fields = ['first_name', 'last_name', 'username', 'email']
    context_object_name = 'form'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StudentDeleteView(DeleteView):

    model = User
    template_name = 'secretary/user/student/delete.html'
    success_url = '/secretary/student/'


#------------------------------------------------------------------------------[ USER-PLANNING-EVENT ]-----------------------------------------------------------------#
class EventCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Event
    fields = '__all__'
    template_name = 'secretary/planning/event/create.html'
    success_message = f' The event has been created'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EventListView(LoginRequiredMixin, ListView):

    model = Event
    template_name = 'secretary/planning/event/read-list.html'
    context_object_name = 'planning_form'
    ordering = ['-start']


class EventDetailView(DetailView):

    model = Event
    template_name = 'secretary/planning/event/read-detail.html'


class EventUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Event
    fields = '__all__'
    template_name = 'secretary/planning/event/update.html'
    success_message = f' The event has been updated'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EventDeleteView(DeleteView):

    model = Event
    template_name = 'secretary/planning/event/delete.html'
    success_url = '/secretary/appointment/'


#------------------------------------------------------------------------------[ USER-PLANNING ]-----------------------------------------------------------------#
@login_required
def planning_filter(request):
    qs = Event.objects.all()
    user_contains = request.GET.get('user_search')

    try:
        users = User.objects.filter(Q(username=user_contains)).distinct()
    except User.DoesNotExist:
        users = None

    if not users:
        events = qs.filter()
    else:
        for user in users:
            events = qs.filter(creator=user.id)

    qs_json = serializers.serialize('json', events)
    return render(request, 'secretary/planning/calendar/index.html', locals())


#------------------------------------------------------------------------------[ COURSE ]-----------------------------------------------------------------#
class CourseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Course
    fields = '__all__'
    template_name = 'secretary/course/create.html'
    success_message = f' The event has been created'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CourseListView(LoginRequiredMixin, ListView):

    model = Course
    template_name = 'secretary/course/read-list.html'
    context_object_name = 'course_form'
    # ordering = ['-start']

@login_required
def detail_course(request, pk):
    course = get_object_or_404(Course, id=pk)

    if request.method == 'POST':

        customer = stripe.Customer.create(
            email=request.user.email,
            name=request.user,
            source=request.POST.get('stripeToken')
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=course.course_price*100,
            currency='usd',
            description=course.course_name,
        )

        Subscription.objects.create(course=course, user=request.user, valid=True)
        messages.success(request, f'thank you for purchasing our course')

        return redirect('secretary:course-list')

    return render(request, 'secretary/course/read-detail.html', locals())
