from django.urls import path
from .views import SponsorListView, SponsorDetailView

urlpatterns = [
    path('sponsors/', SponsorListView.as_view(), name='sponsor-list'),
    path('sponsors/<int:id>/', SponsorDetailView.as_view(), name='sponsor-detail'),
]
                                                                                                                                                                                                    