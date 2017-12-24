from django.contrib import admin

from .models import Student, Group, Discipline, Faculty, Department

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Discipline)
admin.site.register(Faculty)
admin.site.register(Department)
