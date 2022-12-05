from django.urls import include, path
from rest_framework import routers
# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )

from . import views

router = routers.DefaultRouter()
router.register(r'university', views.UniversityViewSet, basename='university')
router.register(r'field-of-study', views.FieldOfStudyViewSet, basename='field-of-study')
router.register(r'student', views.StudentViewSet, basename='student')
router.register(r'instructor', views.InstructorViewSet, basename='instructor')
router.register(r'profile-update', views.ProfileUpdateView, basename='profile')

app_name = "a_user"

urlpatterns = [
	path('auser-api/', include(router.urls)),
  	path('users-login/', views.UsersLoginView.as_view(), name='users-login'),
	# path('email-verify/', views.VerifyEmail.as_view(), name="email-verify"),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('request-reset-email/', views.RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    # path('password-reset/<uidb64>/<token>/', views.PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    # path('password-reset-complete', views.SetNewPasswordAPIView.as_view(), name='password-reset-complete')
]
