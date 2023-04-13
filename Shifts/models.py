from django.db import models
from Accounts.models import User

# Create your models here.

class Shift(models.Model):
    hospital = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.IntegerField()
    price = models.IntegerField()

    created_on = models.DateTimeField(auto_now=True)
