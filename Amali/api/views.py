
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from user.models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import generics

from django.contrib.auth import logout
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role='regular_user')
    serializer_class = CustomUserSerializer

class AthleteListView(generics.ListAPIView):
    queryset = CustomUser.objects.filter(role="athlete")
    serializer_class = CustomUserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(role='regular_user')
    serializer_class = CustomUserSerializer
    lookup_field='id'

class AthleteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.filter(role="athlete")
    serializer_class = CustomUserSerializer
    lookup_field='id'

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    role = request.data.get('role')
    if role not in ['regular_user','athlete']:
        return Response({'message': 'Invalid role'}, staus=status.HTTP_400_BAD_REQUEST)
    serializer = None
    if role == 'regular_user':
        serializer = CustomUserSerializer(data=request.data)
    elif role == 'athlete':
        serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response({'message': 'Registration successful.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    if user.check_password(password):
        login(request, user)
        return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

=======
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sponsors.models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from donation.models import Donation
from .serializers import DonationSerializer
import logging   
logger = logging.getLogger(__name__)


class CustomUserListView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)


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




@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({'message': 'Logged out successfully.'}, status=status.HTTP_200_OK)
@api_view(['POST'])
def user_logout_all(request):
     logout(request)
     return Response({'message': 'Logged out of all devices  successfully.'}, status=status.HTTP_200_OK) 



class CustomUserRegistrationView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            
            password = serializer.validated_data['password']
            hashed_password = make_password(password)
            serializer.validated_data['password'] = hashed_password

            
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Sponsor logged in successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


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
