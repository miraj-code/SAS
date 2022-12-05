from django.contrib.auth.backends import ModelBackend
from a_user.models import Student, Instructor

class StudentAndInstructorBackend(ModelBackend):
    """
    Backend using ModelBackend, but attempts to "downcast"
    the user into a Student or Instructor.
    """

    def authenticate(self, *args, **kwargs):
        return self.downcast_user_type(super().authenticate(*args, **kwargs))
        
    def get_user(self, *args, **kwargs):
        return self.downcast_user_type(super().get_user(*args, **kwargs))

    def downcast_user_type(self, user):
        try:
            student_user = Student.objects.get(pk=user.pk)
            return student_user
        except:
            pass

        try:
            instructor_user = Instructor.objects.get(pk=user.pk)
            return instructor_user
        except:
            pass

        return user