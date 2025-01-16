from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Friend, Expense

admin.site.register(Friend)
admin.site.register(Expense)