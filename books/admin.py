from django.contrib import admin
from .models import Book, count

# Register your models here.
admin.site.register(Book)
admin.site.register(count)