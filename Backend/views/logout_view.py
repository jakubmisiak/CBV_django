from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import View
from django.http import HttpResponseRedirect


def user_logout(request):
    logout(request)
    return redirect('login')