from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'grade', views.GradeViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'week', views.WeekViewSet)
router.register(r'quiz', views.QuizViewSet)
router.register(r'enroll', views.EnrollViewSet)
router.register(r'entrance-exam', views.EntranceExamViewSet)
router.register(r'course-progress', views.CourseProgressViewSet)

app_name = "core"

urlpatterns = [
	path('core-api/', include(router.urls)),
]