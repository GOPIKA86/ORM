from django.db import models
from django.contrib import admin
class Customer(models.Model):

        Name=models.CharField(max_length=10)
        Accno=models.IntegerField(primary_key="Accno")
        Address=models.CharField(max_length=20)
        Email=models.EmailField()
        DoB=models.DateField()
class CustomerAdmin(admin.ModelAdmin):

        list_display=('Name','Accno','Address','Email','DoB')
