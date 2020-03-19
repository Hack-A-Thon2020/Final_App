from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from books.models import Book
from stationary.models import Stationary
from django.http import Http404
# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['number']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Number Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save();
                print('user created')
        else:
            messages.info(request, 'Password Mismatch')
            return redirect('register')
        return redirect('login')
    else:
        return render(request, 'accounts/Register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/Login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")

def profile(request):
    Book_dets = Book.objects.all()
    return render(request, 'accounts/userprofile.html', {'Book_dets': Book_dets})

def user_book(request, user_id):
    book = Book.objects.filter(user_id_id=user_id)
    stationary = Stationary.objects.filter(user_id_id=user_id)
    context = {
        "Book_det": book,
        "stationary_det": stationary
    }
    return render(request, 'accounts/user_book.html', context)