from django.shortcuts import render, redirect
from .models import Book, count
from django.contrib.auth.models import User
from django.http import Http404


# Create your views here.
def index(request):
    User_top = count.objects.latest('count_book')
    User_middle = User.objects.get(id='10')
    User_last = User.objects.get(id='11')
    return render(request, "index1.html", {'User_det': User_top, 'User_middle': User_middle, 'User_last': User_last})

def cart(request):
    return render(request, "cart.html")

def about(request):
    return render(request, "about.html")

def book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        user = User.objects.all()
    except Book.DoesNotExist:
        raise Http404("Book not found")
    context = {
        "Book_det": book, 'user_det': user,
    }
    return render(request, "books.html", context)

def donate(request):
    return render(request, "book_donate.html")

def dept_civil(request):
    Book_dets = Book.objects.all()
    return render(request, "show_by_dept/civil.html", {'Book_dets': Book_dets})

def dept_ce(request):
    Book_dets = Book.objects.all()
    return render(request, "show_by_dept/ce.html", {'Book_dets': Book_dets})

def dept_ec(request):
    Book_dets = Book.objects.all()
    return render(request, "show_by_dept/ec.html", {'Book_dets': Book_dets})

def dept_mechanical(request):
    Book_dets = Book.objects.all()
    return render(request, "show_by_dept/mechanical.html", {'Book_dets': Book_dets})

def dept_mba(request):
    Book_dets = Book.objects.all()
    return render(request, "show_by_dept/mba.html", {'Book_dets': Book_dets})

def dept_maths(request):
    Book_dets = Book.objects.all()
    return render(request, "show_by_dept/maths.html", {'Book_dets': Book_dets})