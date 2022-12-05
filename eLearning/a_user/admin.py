from tkinter import HORIZONTAL
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from a_user.models import Student, Instructor, University, FieldOfStudy

class StudentAdminModel(UserAdmin):
    readonly_fields = ['password']
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','email', 'sex', 'phone', 'profile_picture', 'academic_level')}),
        ('Permissions', {'fields': ('is_superuser', 'is_active', 'is_instructor', 'is_staff', 'user_permissions', 'groups')}),
    )

    filter_horizontal = ('user_permissions', 'groups')

class InstructorAdminModel(admin.ModelAdmin):
    readonly_fields = ['password']

admin.site.register(Student, StudentAdminModel)
admin.site.register(Instructor, InstructorAdminModel)
admin.site.register(University)
admin.site.register(FieldOfStudy)
