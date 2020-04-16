from django.shortcuts import render
from users.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from planning.models import Event

from django.core import serializers
from django.http import JsonResponse


def index(request):
    return render(request, 'instructor/home-list.html', locals())


#------------------------------------------------------------------------------[ USER-PLANNING ]-----------------------------------------------------------------#
@login_required
def planning_filter_student(request):
    qs = Event.objects.all()
    user_contains = request.GET.get('user_search')

    users = User.objects.filter(Q(username=user_contains)).distinct()

    for user in users:
        if user.is_student == True:
            events = qs.filter(creator=user.id)
            qs_json = serializers.serialize('json', events)


    return render(request, 'instructor/planning/calendar/index.html', locals())

@login_required
def student_detail(request):

    user_contains = request.GET.get('user_search')
    users = User.objects.filter(Q(username=user_contains))

    return render(request, 'instructor/student/detail.html', locals())
