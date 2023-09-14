from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserListView.as_view(), name='customuser-list'),
    path('users/<int:id>/', views.CustomUserDetailView.as_view(), name='customuser-detail'),
    path('users/register/', views.CustomUserRegistrationView.as_view(), name='customuser-register'),
    path('users/login/', views.CustomUserLoginView.as_view(), name='customuser-login'),
]
