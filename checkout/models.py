from django.db import models
from books.models import Book

# Create your models here.
class issue(models.Model):
    Deliverd =  models.BooleanField(default=True)
    book_id = models.ForeignKey(Book, blank=True, null=True, on_delete=models.SET_NULL)

class FeedBack(models.Model):

    Message=models.TextField()
    Rates=models.IntegerField()
    Book_Recieved = models.CharField(max_length=10)
    SameBook = models.CharField(max_length=10)
