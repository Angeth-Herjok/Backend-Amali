from django.urls import path
from .views import SignupListCreateView

urlpatterns = [
    path('signups/', SignupListCreateView.as_view(), name='signup-list-create'),
]
