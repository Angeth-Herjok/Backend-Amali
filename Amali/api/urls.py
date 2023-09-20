from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('logout_all/', views.user_logout_all, name='user_logout_all'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('athletes/', views.AthleteListView.as_view(), name='user-list'),
    path('athletes/<int:id>/', views.AthleteDetailView.as_view(), name='user-list'),
    path('users/<int:id>/', views.UserDetailView.as_view(), name='user-list'),


from .import views

urlpatterns = [
    path('users/', views.CustomUserListView.as_view(), name='customuser-list'),
    path('users/<int:id>/', views.CustomUserDetailView.as_view(), name='customuser-detail'),
    path('users/register/', views.CustomUserRegistrationView.as_view(), name='customuser-register'),
    path('users/login/', views.CustomUserLoginView.as_view(), name='customuser-login'),

]




from .views import DonationListView, DonationDetailView

urlpatterns = [
    path('donations/', DonationListView.as_view(), name='donation-list'),
    path('donations/<int:id>/', DonationDetailView.as_view(), name='donation-detail'),
]
