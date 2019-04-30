from django.contrib import admin

from .models import School,Level,Guide,Student,Role,User

admin.site.register(School)
admin.site.register(Level)
admin.site.register(Guide)
admin.site.register(Student)
admin.site.register(Role)
admin.site.register(User)
