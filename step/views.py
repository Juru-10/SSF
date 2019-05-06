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
    levels=Level.objects.all()
    level=Level.objects.filter(id=id).first()
    # students=Student.objects.filter(level__name__icontains=Student.level)
    students=Student.objects.filter(level=level).all()
    # print(id)
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
    # current_user = request.user
    # user = User.objects.filter().first()
    if request.method == 'POST':
        form = AddStudentForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            student = form.save(commit=False)
            student.school = current_user
            # profile=Profile.objects.update()
            student.save()
        return redirect('school')
    else:
        form = AddStudentForm()
    return render(request,'registration/add_student.html',{"form": form,"id":id})

# @login_required(login_url='/accounts/login/')
def add_guide(request):
    current_user = request.user
    print(current_user)
    # user = User.objects.filter().first()
    if request.method == 'POST':
        form = AddGuideForm(request.POST,request.FILES)
        print(form.errors.as_text())
        if form.is_valid():
            guide = form.save(commit=False)
            guide.school = current_user
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
            marks.save()
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
            discipline.save()
            return redirect('levels', id=guide_id)
    else:
        form = DisciplineForm()
    return render(request,'registration/discipline.html',{"form": form,"id":id, "id_guide":guide_id, "id_student":student_id})


def student(request):
    form = StudentLoginForm(request.POST,request.FILES)
    marks = Marks.objects.all()
    print(marks)
    disciplines = Discipline.objects.all()
    student = Student.objects.all()
    print(student)
    if request.method == 'POST':
        if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            student = Student.objects.filter(email = form.cleaned_data['email']).first()
            if student is not None and student.ID==form.cleaned_data['ID']:
                student = Student.objects.filter(student.ID).first()
                print(marks)
                return render(request,'student.html',{"form": form, "student":student, "marks":marks, "disciplines":disciplines})
    else:
        form = StudentLoginForm()
    return render(request,'student.html',{"form": form, "marks":marks, "student":student, "disciplines":disciplines})

@login_required(login_url='/accounts/login/')
def school_login(request):
    form = SchoolLoginForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            school = School.objects.filter(username = form.cleaned_data['username']).first()
            if school is not None and school.password==form.cleaned_data['password']:
                return redirect('school')
            # else:
                # raise form.Error('Password or Username is incorrect!')
    return render(request, 'registration/school_login.html',{"form":form})

def student_login(request):
    form = StudentLoginForm(request.POST,request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            student = Student.objects.filter(email = form.cleaned_data['email']).first()
            if student is not None and student.ID==form.cleaned_data['ID']:
                return redirect('student')

    else:
                # print(guide.password)
        message = 'Invalid username or password'
        form = StudentLoginForm()
    # title = 'Login as Student'
    return render(request,'registration/parent_login.html',{'form':form})


def guide_login(request):
    form = GuideLoginForm(request.POST,request.FILES)
    # kwargs = {"range": range(int(layout))}
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            guide = Guide.objects.filter(username = username).first()
            if guide.username==username and guide.password==password:
                # return levels(request, guide.id)
                return redirect('levels', id=guide.id)

    else:
        # print(guide.password)
        message = f'Invalid use title = title,rname or password'
        form = GuideLoginForm()
    # title = 'Login as Guide'
    return render(request,'registration/guide_login.html',{'form':form})

def guides(request):
    guides=Guide.objects.all()
    # schools=School.objects.filter(school__name__icontains=School.guide)
    return render(request,'guides.html',{"guides":guides})




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
