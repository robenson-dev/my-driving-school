from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

from .models import Event


def calendar_index(request):
    events = Event.objects.all()
    qs_json = serializers.serialize('json', events)
    return render(request, 'planning/home-list.html', locals())
