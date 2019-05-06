from django.db import models

import datetime as dt
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MaxValueValidator,MinValueValidator

from django.db.models.signals import post_save

from django.db.models import Q

class School(models.Model):
    user = models.OneToOneField(User,null=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    username = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name

    def save_school(self):
        self.save()

    def delete_school(self):
        self.delete()

class Level(models.Model):
    name = models.CharField(max_length=30)
    school = models.ForeignKey(School,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name

    def save_level(self):
        self.save()

    def delete_level(self):
        self.delete()

class Guide(models.Model):
    school = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    username = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.username

    def save_guide(self):
        self.save()

    def delete_guide(self):
        self.delete()

class Student(models.Model):
    level = models.ForeignKey(Level,on_delete=models.CASCADE,null=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    ID = models.CharField(max_length=30,null=True)

    # def __str__(self):
    #     return self.fname

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

class Marks(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    subject = models.CharField(max_length=30)
    points = models.CharField(max_length=30)
    comment = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    guide = models.ForeignKey(Guide,on_delete=models.CASCADE,null=True)

class Discipline(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    case = models.CharField(max_length=30)
    comment = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    guide = models.ForeignKey(Guide,on_delete=models.CASCADE,null=True)

class Role(models.Model):
    '''
    '''
    STUDENT = 1
    GUIDE = 2
    SCHOOL = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (STUDENT, 'student'),
        (GUIDE, 'guide'),
        (SCHOOL, 'school'),
        (ADMIN, 'admin'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()
