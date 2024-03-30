from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=130)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=126)

