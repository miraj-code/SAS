from random import choices
from django.db import models
from django.core.validators import FileExtensionValidator
from a_user.models import Student, Instructor

SUBJECT = (
    ('English', 'English'),
    ('Mathematics', 'Mathematics'),
    ('Biology', 'Biology'),
    ('Chemistry', 'Chemistry'),
    ('Physics', 'Physics'),
    ('Civics', 'Civics'),
    ('SAT', 'SAT')
)

YEAR = (
    ('2000', '2000'),
    ('2001', '2001'),
    ('2002', '2002'),
    ('2003', '2003'),
    ('2004', '2004'),
    ('2005', '2005'),
    ('2006', '2006'),
    ('2007', '2007'),
    ('2008', '2008'),
    ('2009', '2009'),
    ('2010', '2010'),
    ('2011', '2011'),
    ('2012', '2012'),
    ('2013', '2013'),
    ('2014', '2014'),
)

class Grade(models.Model):
    grade = models.CharField(max_length=2)
    description = models.CharField(max_length=2000)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.grade

class Course(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='Course Thumbnails', validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Week(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='Week Thumbnails', validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    video = models.FileField(upload_to='Weely Lessons', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    book = models.FileField(upload_to='Weekly Books', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Quiz(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    question = models.TextField()
    choice_one = models.CharField(max_length=400)
    choice_two = models.CharField(max_length=400)
    choice_three = models.CharField(max_length=400)
    choice_four = models.CharField(max_length=400)
    solution = models.CharField(max_length=400)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Enroll(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.student) + '|' + str(self.course)

class EntranceExam(models.Model):
    year = models.CharField(max_length=4, choices=YEAR)
    subject = models.CharField(max_length=20, choices=SUBJECT)
    exam = models.FileField(upload_to='Entrance Exams', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    def __str__(self) -> str:
        return str(self.subject) + ' | ' + str(self.year)

class CourseProgress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.student) + '|' + str(self.course) + '|' + str(self.week) + ' - ' + str(self.is_completed)


