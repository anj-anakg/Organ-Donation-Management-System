from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Donar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    bloodgroup = models.CharField(max_length=10)
    organ = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    place = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
