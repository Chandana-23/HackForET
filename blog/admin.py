from django.contrib import admin

from blog.models import Blog, Student, Teacher

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Blog)