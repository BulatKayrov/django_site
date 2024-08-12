from django.contrib.auth.views import LogoutView
from django.urls import path

from user.views import UserLoginView, UserRegisterView, ProfileView, logout

app_name = 'user'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', logout, name='logout'),
]

