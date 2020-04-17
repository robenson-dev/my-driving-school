from django.shortcuts import render
from users.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from planning.models import Event

from django.core import serializers
from django.http import JsonResponse, HttpResponse


def index(request):
    return render(request, 'student/home-list.html', locals())


@login_required
def student_planning(request):

    if request.user.is_student == True:
        events = Event.objects.filter(creator=request.user.id)
        qs_json = serializers.serialize('json', events)

    return render(request, 'student/planning/calendar/index.html', locals())
