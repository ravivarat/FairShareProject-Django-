from django.db import models

# Create your models here.
from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

from django.db import models

class Expense(models.Model):
    payer = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payer} paid ₹{self.amount}"