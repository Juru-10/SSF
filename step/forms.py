from django import forms
from .models import School, Student, Guide, Level, Marks, Discipline

class SchoolLoginForm(forms.ModelForm):
    class Meta:
        model = School
        exclude = ['name','location']

class StudentLoginForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['level','fname','lname']

class GuideLoginForm(forms.ModelForm):
    class Meta:
        model = Guide
        exclude = ['school','fname','lname']

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = []


class AddGuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        exclude = ['school','guide']

class AddLevelForm(forms.ModelForm):
    class Meta:
        model = Level
        exclude = ['school']

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        exclude = ['student','pub_date','guide']

class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        exclude = ['student','pub_date','guide']
