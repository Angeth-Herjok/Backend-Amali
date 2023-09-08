# from django.urls import path
# from .views import SponsorListCreateView, SponsorRetrieveUpdateDestroyView

# urlpatterns = [
#     path('sponsors/', SponsorListCreateView.as_view(), name='sponsor-list-create'),
#     path('sponsors/<int:pk>/', SponsorRetrieveUpdateDestroyView.as_view(), name='sponsor-retrieve-update-destroy'),
    
# ]

from django.urls import path
from .views import SponsorListView, SponsorDetailView

urlpatterns = [
    path('sponsors/', SponsorListView.as_view(), name='sponsor-list'),
    path('sponsors/<int:id>/', SponsorDetailView.as_view(), name='sponsor-detail'),
]

