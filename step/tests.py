from django.test import TestCase

from .models import User,School,Level,Guide,Student
import datetime as dt

class SchoolTest(TestCase):
    """Test model for class School."""

    def setUp(self):
        self.juru = School(name = 'Test',location = 'Test')

    def test_instance(self):
        self.assertTrue(isinstance(self.juru,School))

    def test_save(self):
        self.juru.save_school()
        schools = School.objects.all()
        self.assertTrue(len(schools) >0 )

class LevelTest(TestCase):
    """Test model for class Level."""

    def setUp(self):
        self.juru = School(name = 'Test',location = 'Test')
        self.juru.save_school()

        self.new_level = Level(school = self.juru, name = 'test')

    def tearDown(self):
        School.objects.all().delete()
        Level.objects.all().delete()
        Student.objects.all().delete()

    def test_save(self):
        self.juru.save_level()
        levels = Level.objects.all()
        self.assertTrue(len(levels) >0 )

class GuideTest(TestCase):
    """Test model for class Guide."""

    def setUp(self):
        self.juru = School(name = 'Test',location = 'Test')
        self.juru.save_school()

        self.new_guide = Guide(school = self.juru, fname = 'Test', lname = 'test', username = 'test', password = 'test')

    def test_save(self):
        self.juru.save_level()
        levels = Level.objects.all()
        self.assertTrue(len(levels) >0 )

class StudentTest(TestCase):
    """Test model for class Student."""

    def setUp(self):
        self.juru = Level(name = 'Test')
        self.juru.save_level()

        self.new_student = Student(level = self.juru, fname = 'Test', lname = 'test', email = 'test', ID = 'test')

    def test_save(self):
        self.juru.save_student()
        students = Student.objects.all()
        self.assertTrue(len(students) >0 )
