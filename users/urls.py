from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, VerifyEmailView, ProfileView, UserListView, UserBlockView, UserUnblockView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify_email/<str:uid>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users_list/', UserListView.as_view(), name='users_list'),
    path('user-block/<int:pk>/', UserBlockView.as_view(), name='user_block'),
    path('user-unblock/<int:pk>/', UserUnblockView.as_view(), name='user_unblock'),
]