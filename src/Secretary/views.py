from django.shortcuts import render
from .Forms import UserForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    form = UserForm(request.POST)
    all_user = User.objects.all()
    return render(request, 'secretary/home-list.html', locals())
