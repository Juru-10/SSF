from rest_framework import serializers
from .models import Student,Guide

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('level' ,'fname', 'lname', 'email', 'ID')

class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = ('school', 'fname', 'lname', 'username', 'password')
