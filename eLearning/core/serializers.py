from configparser import MAX_INTERPOLATION_DEPTH
from dataclasses import fields
from unittest.util import _MAX_LENGTH
from wsgiref import validate
from rest_framework import serializers
from a_user.models import Student
from core.models import Grade, Course, Week, Enroll, Quiz, EntranceExam, CourseProgress

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = '__all__'

class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = ['student', 'course', 'is_active']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class EntranceExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntranceExam
        fields = '__all__'

class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgress
        fields = '__all__'



        


