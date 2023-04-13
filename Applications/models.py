from django.db import models
from Accounts.models import User
from Shifts.models import Shift

# Create your models here.
STATUS_CHOICES = (
    ('Applied','applied'),
    ('Accepted','accepted'),
    ('Rejected','rejected'),
)

class Application(models.Model):
    nurse = models.ForeignKey(User, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES)

    created_on = models.DateTimeField(auto_now=True)

