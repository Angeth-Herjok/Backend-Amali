from rest_framework.views import APIView
from donation.models import Donation
from .serializers import DonationSerializer
from rest_framework.response import Response
from rest_framework import status

class DonationListView(APIView):
    def get(self, request):
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DonationDetailView(APIView):
    def get(self, request, id, format=None):
        donation = Donation.objects.get(id=id)
        serializer = DonationSerializer(donation)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        donation = Donation.objects.get(id=id)
        serializer = DonationSerializer(donation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        donation = Donation.objects.get(id=id)
        donation.delete()
        return Response("Donation deleted", status=status.HTTP_204_NO_CONTENT)
