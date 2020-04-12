from django.shortcuts import render


def index(request):

    return render(request, 'instructor/home-list.html', locals())
