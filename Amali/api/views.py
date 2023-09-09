from rest_framework.views import APIView
from django.shortcuts import render
from regularuser.models import Signup
from .serializers import SignupSerializer
from rest_framework.response import Response
from rest_framework import status


class SignupListView(APIView):
    def get(self, request):
        signups = Signup.objects.all()
        serializer = SignupSerializer(signups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignupDetailView(APIView):
    def get(self, request, id, format=None):
        signup = Signup.objects.get(id=id)
        serializer = SignupSerializer(signup)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        signup = Signup.objects.get(id=id)
        serializer = SignupSerializer(signup, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        signup = Signup.objects.get(id=id)
        signup.delete()
        return Response("Regular user deleted", status=status.HTTP_204_NO_CONTENT)


