from django.db import models


# Create your models here.
class student(models.Model):
    sname=models.CharField(max_length=190)
    sage=models.IntegerField()
    def __str__(self):
        return self.sname
