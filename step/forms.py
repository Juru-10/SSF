from django import forms
from .models import School, Student, Guide, Level, Marks, Discipline

class SchoolLoginForm(forms.ModelForm):
    class Meta:
        model = School
        exclude = ['name','location']

class StudentLoginForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['level','school_key','fname','lname','user']

class GuideLoginForm(forms.ModelForm):
    class Meta:
        model = Guide
        exclude = ['school_key','fname','lname','user']

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['school_key','user']


class AddGuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        exclude = ['school_key','guide','user']

class AddLevelForm(forms.ModelForm):
    class Meta:
        model = Level
        exclude = ['school_key','user']

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        Marks.comment = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows': 3, 'cols': 40}))
        exclude = ['student','pub_date','guide']

class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        exclude = ['student','pub_date','guide']