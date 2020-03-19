from django.shortcuts import render, redirect
from . models import issue, FeedBack
from books.models import Book

# Create your views here.
def checkout(request):
    return render(request, 'inbox.html')

def message(request):

    if request.method =="POST":

        mess=request.POST['msg']
    return render(request, 'index.html')

