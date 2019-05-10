from django.shortcuts import render,redirect

from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required

from .forms import AddStudentForm, AddGuideForm, AddLevelForm, MarksForm, DisciplineForm, StudentLoginForm, GuideLoginForm, SchoolLoginForm

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  School,Student,Guide,Level,User,Marks,Discipline
from .serializer import StudentSerializer,GuideSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from .email import marks_message,discipline_message

import requests

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from decouple import config,Csv

from django.core.mail import send_mail



@login_required(login_url='/accounts/login/')
def admin(request):
    return render(request)

# @login_required(login_url='/accounts/login/')
def school(request):
    current_user = request.user
    guide = current_user
    return render(request,'school.html',{"guide":guide})

@login_required(login_url='/accounts/login/')
def guides(request):
    guides=Guide.objects.all()
    return render(request,'school.html',{"levels":levels,"guides":guides,"students":"students"})

# @login_required(login_url='/accounts/login/')
def levels(request, id):
    # levels=Level.objects.all()
    # level=Level.objects.filter(id=id).first()
    guide=Guide.objects.filter(id=id).first()
    school = School.objects.filter(id=guide.school_key.id).first()
    levels=Level.objects.filter(school_key=school.id).all()
    # students=Student.objects.filter(level__name__icontains=Student.level)
    students=Student.objects.all()
    # print(students)
    # students=Student.objects.all()
    return render(request,'levels.html',{"levels":levels, "students":students, "id_guide":id})

def index(request):
    # levels=Level.objects.all()
    # students=Student.objects.filter(level__name__icontains=Student.level)
    return render(request,'index.html')

def about(request):
    # levels=Level.objects.all()
    # students=Student.objects.filter(level__name__icontains=Student.level)
    return render(request,'about.html')


@login_required(login_url='/accounts/login/')
def add_student(request):
    current_user = request.user
    school = School.objects.filter(user=current_user.id).first()
    # user = User.objects.filter().first()
    if request.method == 'POST':
        form = AddStudentForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            student = form.save(commit=False)
            student.school_key = school
            student.user = current_user
            # profile=Profile.objects.update()
            student.save()
        return redirect('school')
    else:
        form = AddStudentForm()
    return render(request,'registration/add_student.html',{"form": form,"id":id})

# @login_required(login_url='/accounts/login/')
def add_guide(request):
    current_user = request.user
    school = School.objects.filter(user=current_user.id).first()
    print(current_user)
    # user = User.objects.filter().first()
    if request.method == 'POST':
        form = AddGuideForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            guide = form.save(commit=False)
            guide.school_key = school
            guide.user = current_user
            # profile=Profile.objects.update()
            guide.save()
        return redirect('school')
    else:
        form = AddGuideForm()
    return render(request,'registration/add_guide.html',{"form": form,"id":id})

@login_required(login_url='/accounts/login/')
def add_level(request):
    current_user = request.user
    school = School.objects.filter(user=current_user.id).first()
    # user = User.objects.filter().first()
    if request.method == 'POST':
        form = AddLevelForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            level = form.save(commit=False)
            level.school_key = school
            level.user = current_user
            # profile=Profile.objects.update()
            level.save()
        return redirect('school')
    else:
        form = AddLevelForm()
    return render(request,'registration/add_level.html',{"form": form,"id":id})

# @login_required(login_url='/accounts/login/')
def add_marks(request, guide_id, student_id):
    current_user = request.user
    guide = Guide.objects.filter(id=guide_id).first()
    student = Student.objects.filter(id=student_id).first()
    if request.method == 'POST':
        form = MarksForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            marks = form.save(commit=False)
            marks.guide = guide
            marks.student = student
            # profile=Profile.objects.update()
            recipient = student
            name = recipient.fname+' '+recipient.lname
            email = recipient.email

            # marks.save()
            marks_message(name,email)
            return redirect('levels', id=guide_id)
    else:
        form = MarksForm()
    return render(request,'registration/marks.html',{"form": form,"id":id, "id_guide":guide_id, "id_student":student_id})

# @login_required(login_url='/accounts/login/')
def add_discipline(request, guide_id, student_id):
    current_user = request.user
    guide = Guide.objects.filter(id=guide_id).first()
    student = Student.objects.filter(id=student_id).first()
    if request.method == 'POST':
        form = DisciplineForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            discipline = form.save(commit=False)
            discipline.guide = guide
            discipline.student = student
            # profile=Profile.objects.update()
            recipient = student
            name = recipient.fname+' '+recipient.lname
            email = recipient.email
            discipline.save()
            discipline_message(name,email)
            return redirect('levels', id=guide_id)
    else:
        form = DisciplineForm()
    return render(request,'registration/discipline.html',{"form": form,"id":id, "id_guide":guide_id, "id_student":student_id})


def student(request,id):
    # form = StudentLoginForm(request.POST,request.FILES)
    marks = Marks.objects.filter(student=id).all()
    # print(marks)
    disciplines = Discipline.objects.filter(student=id).all()
    student = Student.objects.filter(id=id).first()
    # print(student)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         # username = form.cleaned_data['username']
    #         # password = form.cleaned_data['password']
    #         student = Student.objects.filter(email = form.cleaned_data['email']).first()
    #         if student is not None and student.ID==form.cleaned_data['ID']:
    #             student = Student.objects.filter(student.ID).first()
    #             marks = Marks.objects.filter(student.ID).all()
    #             disciplines = Discipline.objects.filter(student.ID).all()
    #             print(marks)
    #             return render(request,'student.html',{"form": form, "student":student, "marks":marks, "disciplines":disciplines})
    # else:
    #     form = StudentLoginForm()
    return render(request,'student.html',{"student":student,"marks":marks, "disciplines":disciplines})

@login_required(login_url='/accounts/login/')
def school_login(request):
    form = SchoolLoginForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            school = School.objects.filter(username = form.cleaned_data['username']).first()
            if school is not None and school.password==form.cleaned_data['password']:
                return redirect('school')
            # else:
            #     raise form.Error('Password or Username is incorrect!')
    return render(request, 'registration/school_login.html',{"form":form})

def student_login(request):
    form = StudentLoginForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            ID = form.cleaned_data['ID']
            student = Student.objects.filter(ID = ID, email = email).first()
            if student:
                return redirect('student', id=student.id)
            else:
                message = "Invalid username or password"
                return render(request,'registration/parent_login.html', {'form':form, "message":message})
    else:
        form = StudentLoginForm()
    return render(request,'registration/parent_login.html',{'form':form})


def guide_login(request):
    form = GuideLoginForm(request.POST,request.FILES)
    # kwargs = {"range": range(int(layout))}
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            guide = Guide.objects.filter(password = password, username = username).first()

            if guide:
                return redirect('levels', id=guide.id)
            else:
                message = "Invalid username or password"
                return render(request,'registration/guide_login.html', {'form':form, "message":message})
    else:
        form = GuideLoginForm()
        message = "Invalid username or password"
    return render(request,'registration/guide_login.html',{'form':form})

def guides(request):
    guides=Guide.objects.all()
    # schools=School.objects.filter(school__name__icontains=School.guide)
    return render(request,'guides.html',{"guides":guides})

# def ssf(request):
#     name = request.POST.get('your_name')
#     email = request.POST.get('email')
#
#     recipient = NewsLetterRecipients(name=name, email=email)
#     recipient.save()
#     send_welcome_email(name, email)
#     data = {'success': 'You have been successfully added to mailing list'}
#     return JsonResponse(data)






class StudentList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)

class GuideList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        permission_classes = (IsAdminOrReadOnly,)

class StudentDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GuideDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
