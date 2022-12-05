from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

SEX = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

STUDENT_ACADEMIC_LEVEL = (
    ('Lower School', 'Lower School'),
    ('Elementery School', 'Elementery School'),
    ('High School', 'High School'),
    ('Preparatory School', 'Preparatory School')
)

FIELDS_OF_STUDY = (
    ('Architecture', 'Architecture'),
    ('Biology', 'Biology'),
    ('Biological Laboratory Science', 'Biological Laboratory Science'),
    ('Bio-Medical Engineering', 'Bio-Medical Engineering'),
    ('Bio-systems Engineering', 'Bio-systems Engineering'),
    ('Biotechnology', 'Biotechnology'),
    ('Chemistry', 'Chemistry'),
    ('Chemical Engineering', 'Chemical Engineering'),
    ('Construction and Building Technology', 'Construction and Building Technology'),
    ('Civil Engineering', 'Civil Engineering'),
    ('Computer Engineering', 'Computer Engineering'),
    ('Computer Science', 'Computer Science'),
    ('Civics & Ethics', 'Civics & Ethics'),
    ('English language and Literature', 'English language and Literature'),
    ('Health and Physical Education', 'Health and Physical Education'),
    ('Information Science', 'Information Science'),
    ('Information Systems', 'Information Systems'),
    ('Information Technology', 'Information Technology'),
    ('Mathematics', 'Mathematics'),
    ('Management Information Systems', 'Management Information Systems'),
    ('Physics', 'Physics'),
    ('Sport Management', 'Sport Management'),
    ('Sport Science', 'Sport Science'),
    ('Software Engineering', 'Software Engineering')
)

INSTRUCTOR_ACADEMIC_COMPLETION_UNIVERSITY = (
    ('Addis Ababa University', 'Addis Ababa University'),
    ('Mekelle University', 'Mekelle University'),
    ('Bahir Dar University', 'Bahir Dar University'),
    ('Jimma University', 'Jimma University'),
    ('University of Gondar', 'University of Gondar'),
    ('Haramaya University (Alemaya)', 'Haramaya University (Alemaya)'),
    ('Hawassa University (Debub University)', 'Hawassa University (Debub University)'),
    ('Arba Minch University', 'Arba Minch University'),
    ('Debre Markos University', 'Debre Markos University'),
    ('Wollo University', 'Wollo University'),
    ('Wolaita Sodo University', 'Wolaita Sodo University'),
    ('Aksum University', 'Aksum University'),
    ('Arsi University','Arsi University'),
    ('Adama Science & Technology University', 'Adama Science & Technology University'),
    ('Kebri Dehar University', 'Kebri Dehar University'),
    ('Addis Ababa Science and Technology University', 'Addis Ababa Science and Technology University'),
    ('Wachemo University', 'Wachemo University'),
    ('Addis Ababa Institute of Technology', 'Addis Ababa Institute of Technology'),
    ('Debre Berhan University', 'Debre Berhan University'),
    ('Ambo University', 'Ambo University'),
    ('Dire Dawa University', 'Dire Dawa University'),
    ('Welkete University', 'Welkete University'),
    ('Ethiopian Civil Service University', 'Ethiopian Civil Service University'),
    ('Saint Mary`s University College Ethiopia', 'Saint Mary`s University College Ethiopia'),
    ('Ethiopian Institute of Architecture', 'Ethiopian Institute of Architecture'),
    ('Adigrat University', 'Adigrat University'),
    ('Mizan Tepi University', 'Mizan Tepi University'),
    ('Assosa University', 'Assosa University'),
    ('Dilla University', 'Dilla University'),
    ('Madawalabu University', 'Madawalabu University'),
    ('Jigjiga University', 'Jigjiga University'),
    ('Wollega University', 'Wollega University'),
    ('Micro Link Information Technology College', 'Micro Link Information Technology College'),
    ('Kotebe Metropolitan University', 'Kotebe Metropolitan University'),
    ('Samara University', 'Samara University'),
    ('Addis Continental Institute of Public Health', 'Addis Continental Institute of Public Health'),
    ('Rift Valley University', 'Rift Valley University'),
    ('Bule Hora University', 'Bule Hora University'),
    ('Western University College Ethiopia', 'Western University College Ethiopia'),
    ('Mettu University', 'Mettu University'),
    ('Hope University College', 'Hope University College'),
    ('Meserete Kristos College', 'Meserete Kristos College'),
    ('Addis Ababa Medical University College Hargiesa', 'Addis Ababa Medical University College Hargiesa'),
    ('Woldia University', 'Woldia University'),
    ('GAGE University College', 'GAGE University College'),
    ('Unity University College', 'Unity University College'),
    ('Haramaya University Haramaya Institute of Technology', 'Haramaya University Haramaya Institute of Technology'),
    ('CPU College', 'CPU College'),
    ('Ethiopian Graduate School of Theology', 'Ethiopian Graduate School of Theology'),
    ('HiLCoE School of Computer Science and Technology College', 'HiLCoE School of Computer Science and Technology College'),
    ('Defence Engineering College', 'Defence Engineering College'),
    ('International Leadership Institute', 'International Leadership Institute'),
    ('Oda Bultum University', 'Oda Bultum University'),
    ('Admas University Ethiopia', 'Admas University Ethiopia'),
    ('Injibara University', 'Injibara University'),
    ('Ethiopian Management Institute', 'Ethiopian Management Institute'),
    ('Oromia State University', 'Oromia State University'),
    ('Myungsung Medical College', 'Myungsung Medical College'),
    ('Federal TVET Institute', 'Federal TVET Institute'),
    ('Holy Trinity University', 'Holy Trinity University'),
    ('Catering and Tourism Training Institute Addis Ababa', 'Catering and Tourism Training Institute Addis Ababa'),
    ('Addis Ababa University College of Commerce', 'Addis Ababa University College of Commerce'),
    ('Ethiopia Adventist College', 'Ethiopia Adventist College'),
    ('St Paul`s Hospital Millennium Medical College', 'St Paul`s Hospital Millennium Medical College'),
    ('PESC College Addis Ababa', 'PESC College Addis Ababa'),
    ('Tech Zone Engineering & Business College', 'Tech Zone Engineering & Business College'),
    ('Sante Medical College', 'Sante Medical College'),
    ('Royal College Ethiopia', 'Royal College Ethiopia'),
    ('Addis Ababa Medical and Business College', 'Addis Ababa Medical and Business College'),
    ('Sri Sai College', 'Sri Sai College'),
    ('Universal Medical Collage', 'Universal Medical Collage')
)

class University(models.Model):
    name = models.CharField(max_length=300, choices=INSTRUCTOR_ACADEMIC_COMPLETION_UNIVERSITY)

    def __str__(self):
        return self.name

class FieldOfStudy(models.Model):
    name = models.CharField(max_length=300, choices=FIELDS_OF_STUDY)

    def __str__(self):
        return self.name

class User(AbstractUser):
    is_instructor = models.BooleanField(default=False)

class Student(User):
    sex = models.CharField(max_length=6, choices=SEX)
    phone = models.CharField(max_length=13)
    profile_picture = models.ImageField(upload_to='Profile Pictures', validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    academic_level = models.CharField(max_length=20, choices=STUDENT_ACADEMIC_LEVEL)

    def __str__(self) -> str:
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class Instructor(User):
    sex = models.CharField(max_length=6, choices=SEX)
    phone = models.CharField(max_length=13)
    profile_picture = models.ImageField(upload_to='Profile Pictures', validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    academic_completion_university = models.ForeignKey(University, default='', on_delete=models.CASCADE)
    field_of_study = models.ForeignKey(FieldOfStudy, default='', on_delete=models.CASCADE)
    description = models.TextField(default='')

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'
    
    



    





