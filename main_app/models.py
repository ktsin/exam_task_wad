from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Good(models.Model):
    name=models.CharField(max_length=511)
    unit=models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Price')


class GoodIncome(models.Model):
    good=models.ForeignKey(Good, on_delete=models.CASCADE)
    date=models.DateField()
    checkout_number=models.IntegerField()


class SystemUser(User):
    isWorker=models.BooleanField(default=False)