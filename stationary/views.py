from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Stationary
from django.http import Http404


# Create your views here.
def index(request):
    Stationary_dets = Stationary.objects.all()
    return render(request, "stationary.html", {'Stationary_dets': Stationary_dets})

def donate(request):
    return render(request, "stationary_donate.html")