from django import forms
from .models import Student, Guide, Level



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['level']

class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        exclude = ['school']

class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        exclude = ['school']
