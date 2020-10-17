from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

from .forms import LoginForm


def register(request):
    return render(request, 'authenticate/register.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponse("Ok")

    else:
        form = LoginForm()

    return render(request, 'authenticate/login.html', {'form': form})
