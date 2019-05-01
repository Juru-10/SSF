from django import forms
from .models import Student, Guide, Level


class StudentLoginForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['level']

class GuideLoginForm(forms.ModelForm):
    class Meta:
        model = Guide
        exclude = ['school']

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['level']


class AddGuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        exclude = ['school']

class AddLevelForm(forms.ModelForm):
    class Meta:
        model = Level
        exclude = ['school']
