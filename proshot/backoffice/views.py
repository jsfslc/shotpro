from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


# Create your views here.

def index(request):
    print("back office")
    return render(request, "dashboard.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def profile(request):
    print("profile")
    return render(request, "profile.html")