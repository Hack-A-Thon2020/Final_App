from django.shortcuts import render
from books.models import Book
from checkout.models import issue
# Create your views here.
def borrow(request, Book_id):
    obj = Book.objects.filter(pk=Book_id)
    obj1 = issue.objects.all()
    return render(request, "AddCart.html", {'obj': obj, 'obj1':obj1})