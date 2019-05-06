from django import forms
from .models import Student, Guide, Level, Marks, Discipline, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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
        exclude = []


class AddGuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        exclude = ['school']

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

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')

class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')