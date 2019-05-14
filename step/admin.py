from django.contrib import admin
from django.contrib.auth.models import User, AbstractUser
from .models import School,Level,Guide,Student,Role,User

admin.site.register(School)
# admin.site.register(User)
