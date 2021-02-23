from django.urls import path, include

from rest_framework import routers


from .views import UserAPIView, RegisterAPIView, VerifyEmail, ChangePasswordView, RequestPasswordResetEmail, \
    PasswordTokenCheckAPI, SetNewPasswordAPIView

router = routers.DefaultRouter()
router.register('users', UserAPIView)

# router_add = routers.DefaultRouter()
# router_add.register('users', ProfileAPIView)



urlpatterns = [


    path('register/', RegisterAPIView.as_view(),name='register'),
    # path('profile/', ProfileAPIView.as_view(),name='profile'),

    path('', include(router.urls)),

path('email-verify/', VerifyEmail.as_view(), name="email-verify"),

    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')





]