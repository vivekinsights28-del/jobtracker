from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    date_applied = models.DateField()

    def __str__(self):
        return self.company