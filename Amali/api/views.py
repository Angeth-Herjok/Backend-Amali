from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sponsors.models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
import logging

logger = logging.getLogger(__name__)

class CustomUserListView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserDetailView(APIView):
    def get(self, request, id, format=None):
        user = CustomUser.objects.get(id=id)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        user = CustomUser.objects.get(id=id)
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        user = CustomUser.objects.get(id=id)
        user.delete()
        return Response("User deleted", status=status.HTTP_204_NO_CONTENT)

class CustomUserRegistrationView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        logger.debug(f'Username: {username}, Password: {password}')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                token = Token.objects.get(user=user)
                token.delete()
            except Token.DoesNotExist:
                pass
            token = Token.objects.create(user=user)
            login(request, user)
            return Response({'token': token.key, 'detail': 'Sonsor logged in successfully'}, status=status.HTTP_200_OK)
        else:
            logger.warning('Authentication failed')
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)








