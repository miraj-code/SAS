from django.contrib import admin
from core.models import Grade, Course, Week, Enroll, Quiz, EntranceExam, CourseProgress

admin.site.register(Grade)
admin.site.register(Course)
admin.site.register(Week)
admin.site.register(Enroll)
admin.site.register(Quiz)
admin.site.register(EntranceExam)
admin.site.register(CourseProgress)
