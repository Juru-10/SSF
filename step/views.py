from django.shortcuts import render,redirect

from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required

from .forms import AddStudentForm, AddGuideForm, AddLevelForm, MarksForm, DisciplineForm

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  School,Student,Guide,Level,User,Marks,Discipline
from .serializer import StudentSerializer,GuideSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

@login_required(login_url='/accounts/login/')
def admin(request):
    return render(request)

# @login_required(login_url='/accounts/login/')
def school(request):
    levels=Level.objects.all()
    guides=Guide.objects.all()
    students=Student.objects.all()
    return render(request,'school.html',{"levels":levels,"guides":guides,"students":"students"})

@login_required(login_url='/accounts/login/')
def levels(request):
    levels=Level.objects.all()
    students=Student.objects.filter(level__name__icontains=Student.level)
    return render(request,'levels.html',{"levels":levels,"students":"students"})

@login_required(login_url='/accounts/login/')
def add_student(request):
    # current_user = request.user
    # user = User.objects.filter().first()
    if request.method == 'POST':
        form = AddStudentForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            student = form.save(commit=False)
            # student.user = current_user
            # profile=Profile.objects.update()
            student.save()
        return redirect('school')
    else:
        form = AddStudentForm()
    return render(request,'registration/add_student.html',{"form": form,"id":id})

@login_required(login_url='/accounts/login/')
def add_guide(request):
    # current_user = request.user
    # user = User.objects.filter().first()
    if request.method == 'POST':
        form = AddGuideForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            guide = form.save(commit=False)
            # profile.user = current_user
            # profile=Profile.objects.update()
            guide.save()
        return redirect('school')
    else:
        form = AddGuideForm()
    return render(request,'registration/add_guide.html',{"form": form,"id":id})

@login_required(login_url='/accounts/login/')
def add_level(request):
    # current_user = request.user
    # user = User.objects.filter().first()
    if request.method == 'POST':
        form = AddLevelForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            level = form.save(commit=False)
            # profile.user = current_user
            # profile=Profile.objects.update()
            level.save()
        return redirect('school')
    else:
        form = AddLevelForm()
    return render(request,'registration/add_level.html',{"form": form,"id":id})

@login_required(login_url='/accounts/login/')
def add_marks(request):
    # current_user = request.user
    # user = User.objects.filter().first()
    if request.method == 'POST':
        form = MarksForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            marks = form.save(commit=False)
            # profile.user = current_user
            # profile=Profile.objects.update()
            marks.save()
        return redirect('guide')
    else:
        form = MarksForm()
    return render(request,'registration/marks.html',{"form": form,"id":id})

@login_required(login_url='/accounts/login/')
def add_discipline(request):
    # current_user = request.user
    # user = User.objects.filter().first()
    if request.method == 'POST':
        form = DisciplineForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            discipline = form.save(commit=False)
            # profile.user = current_user
            # profile=Profile.objects.update()
            discipline.save()
        return redirect('guide')
    else:
        form = DisciplineForm()
    return render(request,'registration/discipline.html',{"form": form,"id":id})


@login_required(login_url='/accounts/login/')
def student(request,ID):
    student = Student.objects.filter(ID)
    marks = Marks.objects.all()
    discipline = Discipline.objects.all()
    return render(request,'student.html')


def student_login():
    form = StudentLoginForm()
    if form.validate_on_submit():
        student = Student.query.filter_by(email = form.email.data).first()
        if student is not None and student.verify_password(form.password.data):
            return redirect('registration/parent_login.html')

        flash('Invalid username or password')

    title = 'Login as Student'
    return render_template('registration/parent_login.html', title = title, StudentLoginForm= form)


def guide_login():
    form = GuideLoginForm()
    if form.validate_on_submit():
        guide = Guide.query.filter_by(email = form.email.data).first()
        if student is not None and guide.verify_password(form.password.data):
            return redirect('registration/guide_login.html')

        flash('Invalid username or password')

    title = 'Login as Guide'
    return render_template('registration/guide_login.html', title = title, GuideLoginForm= form)

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
