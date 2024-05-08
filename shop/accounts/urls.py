from django.urls import path

from .views import UserLoginView, UserLogoutView, UserRegisterView, \
    UserProfileView, UserAvatarView, UserChangePasswordView

app_name = 'accounts'

urlpatterns = [
    path('sign-in', UserLoginView.as_view(), name='sign_in'),
    path('sign-out', UserLogoutView.as_view(), name='sign_out'),
    path('sign-up', UserRegisterView.as_view(), name='sign_up'),
    path('profile', UserProfileView.as_view(), name='profile'),
    path('profile/avatar', UserAvatarView.as_view(), name='avatar'),
    path('profile/password', UserChangePasswordView.as_view(), name='password')
]
