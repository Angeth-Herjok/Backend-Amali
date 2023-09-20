# from rest_framework.views import APIView
# from django.contrib.auth import authenticate, login
# from django.http import JsonResponse
# from django.shortcuts import render
# from regularuser.models import RegularUser
# from .serializers import RegularUserSerializer
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import JsonResponse
# from django.views import View


# from rest_framework.authtoken.models import Token
# # from rest_framework.permissions import IsAuthenticated
# import logging
# logger = logging.getLogger(__name__)


# class RegularUserListView(APIView):
#     def get(self, request, signup_id=None):
#         if signup_id is None:
#             signups = RegularUser.objects.all()
#             serializer = RegularUserSerializer(signups, many=True)
#             return Response(serializer.data)
#         else:
#             try:
#                 signup = RegularUser.objects.get(id=signup_id)
#                 serializer = RegularUserSerializer(signup)
#                 return Response(serializer.data)
#             except RegularUser.DoesNotExist:
#                 return Response({"error": "RegularUser not found"}, status=status.HTTP_404_NOT_FOUND)


#     def post(self, request):
#         serializer = RegularUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class RegularUserDetailView(APIView):
#     def patch(self, request, id, format=None):
#         try:
#             signup = RegularUser.objects.get(id=id)
#             serializer = RegularUserSerializer(signup, data=request.data, partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except RegularUser.DoesNotExist:
#             return Response("Regular user not found", status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id, format=None):
#         signup = RegularUser.objects.get(id=id)
#         serializer = RegularUserSerializer(signup)
#         return Response(serializer.data)

#     def put(self, request, id, format=None):
#         signup = RegularUser.objects.get(id=id)
#         serializer = RegularUserSerializer(signup, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id, format=None):
#         signup = RegularUser.objects.get(id=id)
#         signup.delete()
#         return Response("Regular user deleted", status=status.HTTP_204_NO_CONTENT)



# class RegularUserLoginView(APIView):
#     def login(request):
#         if request.method == 'POST':
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 if user.is_active:
#                     auth_login(request, user)
#                     return redirect('index')
#                 else:
#                     messages.error(request, 'Your account is inactive.')
#         else:
#             messages.error(request, 'Invalid username or password.')
#         return redirect('login')

    


    # def post(self, request):
    #     username = request.data.get('username')
    #     password = request.data.get('password')        
    #     logger.debug(f'Username: {username}, Password: {password}')        
    #     user = authenticate(request, username=username, password=password)        
    #     if user is not None:
    #         try:                
    #             token = Token.objects.get(user=user)
    #             token.delete()
    #         except Token.DoesNotExist:
    #             pass            
    #             token = Token.objects.create(user=user)            
    #             login(request, user)
    #         return Response({'token': token.key, 'detail': 'regularuser logged in successfully'}, status=status.HTTP_200_OK)
    #     else:
    #         logger.warning('Authentication failed')
    #         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)





# .........................................................................................




from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from user.models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import generics

from .serializers import CustomUserSerializer
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





@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({'message': 'Logged out successfully.'}, status=status.HTTP_200_OK)
@api_view(['POST'])
def user_logout_all(request):
     logout(request)
     return Response({'message': 'Logged out of all devices  successfully.'}, status=status.HTTP_200_OK) 



