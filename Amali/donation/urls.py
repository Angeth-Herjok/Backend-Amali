from django.urls import path
from . import views

urlpatterns = [
    path('donations/', views.DonationListCreateView.as_view(), name='donation-list-create'),
    path('donations/<int:pk>/', views.DonationDetailView.as_view(), name='donation-detail'),
]