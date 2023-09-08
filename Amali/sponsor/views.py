from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sponsor
from .serializers import SponsorSerializer

class SponsorListView(APIView):
    def get(self, request):
        sponsors = Sponsor.objects.all()
        serializer = SponsorSerializer(sponsors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SponsorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SponsorDetailView(APIView):
    def get(self, request, id, format=None):
        sponsor = Sponsor.objects.get(id=id)
        serializer = SponsorSerializer(sponsor)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        sponsor = Sponsor.objects.get(id=id)
        serializer = SponsorSerializer(sponsor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        sponsor = Sponsor.objects.get(id=id)
        sponsor.delete()
        return Response("Sponsor deleted", status=status.HTTP_204_NO_CONTENT)
