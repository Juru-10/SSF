from django.db import models

import datetime as dt
from django.contrib.auth.models import User
# from tinymce.models import HTMLField
from django.core.validators import MaxValueValidator,MinValueValidator

from django.db.models.signals import post_save

from django.db.models import Q

class School(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def save_school(self):
        self.save()

    def delete_school(self):
        self.delete()

class Level(models.Model):
    name = models.CharField(max_length=30)
    school = models.ForeignKey(School,on_delete=models.CASCADE,null=True)

    def save_level(self):
        self.save()

    def delete_level(self):
        self.delete()

class Guide(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,null=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def save_guide(self):
        self.save()

    def delete_guide(self):
        self.delete()

class Student(models.Model):
    level = models.ForeignKey(Level,on_delete=models.CASCADE,null=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    ID = models.CharField(max_length=30)

    def save_student(self):
        self.save()

    def delete_student(self):
        self.delete()

    @classmethod
    def search_student(cls,fname,lname):
        student = cls.objects.filter(
        Q(fname__icontains=fname) |
        Q(lname__icontains=lname)
        )
        return student
