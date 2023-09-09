from django.urls import path
from .views import DonationListView, DonationDetailView

urlpatterns = [
    path('donations/', DonationListView.as_view(), name='donation-list'),
    path('donations/<int:id>/', DonationDetailView.as_view(), name='donation-detail'),
]