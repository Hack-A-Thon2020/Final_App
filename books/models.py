from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    BookName = models.CharField(max_length=35)
    Edition = models.IntegerField()
    AuthorName = models.CharField(max_length=25)
    Publication = models.CharField(max_length=25)
    BookCategory = models.CharField(max_length=25)
    img = models.ImageField(upload_to='pics')
    user_id = models.ForeignKey(User, blank=True,null=True, on_delete=models.SET_NULL)
    pdf = models.FileField(upload_to='pdf')
    Department = models.CharField(max_length=25, null=True)
    Semester = models.IntegerField()
    Return = models.BooleanField(default=False)

class count(models.Model):
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    count_book = models.IntegerField()
