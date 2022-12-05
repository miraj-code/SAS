from pyexpat import version_info
from django.shortcuts import render
from core.serializers import (GradeSerializer, CourseSerializer,
                                WeekSerializer, EnrollSerializer,
                                QuizSerializer, EntranceExamSerializer, 
                                CourseProgressSerializer)
from rest_framework import viewsets
from core.models import Grade, Course, Week, Enroll, Quiz, EntranceExam, CourseProgress

class GradeViewSet(viewsets.ModelViewSet):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class WeekViewSet(viewsets.ModelViewSet):
    serializer_class = WeekSerializer
    queryset = Week.objects.all()

class EnrollViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollSerializer
    queryset = Enroll.objects.all()

class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

class EntranceExamViewSet(viewsets.ModelViewSet):
    serializer_class = EntranceExamSerializer
    queryset = EntranceExam.objects.all()

class CourseProgressViewSet(viewsets.ModelViewSet):
    serializer_class = CourseProgressSerializer
    queryset = CourseProgress.objects.all()

