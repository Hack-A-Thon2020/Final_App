from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Stationary(models.Model):
        Item_Name = models.CharField(max_length=35)
        img = models.ImageField(upload_to='Spics')
        Item_Description = models.CharField(max_length=1000)
        user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)