from django.urls import path
from .views import SignupListView
from .views import SignupDetailView


urlpatterns = [
    path("RegularUser/", SignupListView.as_view(), name="regular_user_list_view"),
    path("Signup/<int:id>/", SignupDetailView.as_view(), name="regular_user_detail"),
    ]
