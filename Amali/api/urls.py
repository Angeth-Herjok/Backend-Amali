from django.urls import path
from .views import SignupListView
from .views import SignupDetailView


urlpatterns = [
    path("regularuser/", SignupListView.as_view(), name="regular_user_list_view"),
    path("regularuser/<int:id>/", SignupDetailView.as_view(), name="regular_user_detail"),
    ]
