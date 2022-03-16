import datetime
from django.db import models

# Create your models here.

class StudentDetail(models.Model):
    stud_name = models.CharField(max_length=200)
    deptt = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

