from django.db import models
from django.shortcuts import render
from django.http import JsonResponse
from api.models import User, Profile
from api.serializer import MyTokenObtainPairSerializer, ProfileSerializer, RegisterSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from .models import Profile

# crud
# from . import serializer
# from rest_framework.views import APIView
# from rest_framework.response import Response

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        profile = Profile.objects.create(user=user)
        profile.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/',
        '/api/profile/',  # Add your new endpoint here
        '/api/update_profile/',  # Add your new update endpoint here
        '/api/profiles/',
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        data = {
            'nom_enfant': profile.nom_enfant,
            'genre': profile.genre,
            'ville_residence': profile.ville_residence,
            'ville_naissance': profile.ville_naissance,
            'ecole': profile.ecole,
            'classe': profile.classe,
            'verified': profile.verified
        }
        return Response(data, status=status.HTTP_200_OK)
    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)

        profile.nom_enfant = request.data.get("nom_enfant", profile.nom_enfant)
        profile.genre = request.data.get("genre", profile.genre)
        profile.ville_residence = request.data.get("ville_residence", profile.ville_residence)
        profile.ville_naissance = request.data.get("ville_naissance", profile.ville_naissance)
        profile.ecole = request.data.get("ecole", profile.ecole)
        profile.classe = request.data.get("classe", profile.classe)
        profile.verified = request.data.get("verified", profile.verified)

        if request.FILES.get("image"):
            profile.image = request.FILES["image"]

        profile.save()

        return Response({"success": True, "message": "Profile updated successfully"}, status=status.HTTP_200_OK)

    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)


# crud
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profiles(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

'''from django.shortcuts import render
from django.http import JsonResponse
from api.models import User, Profile  # Import Profile

from api.serializer import MyTokenObtainPairSerializer, RegisterSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# Get All Routes

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)

# Update RegisterView to create Profile
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Extract relevant fields for Profile
        # type = serializer.validated_data.get('type')  # Get the type field

        # Create Profile instance, only passing the 'user' field
        profile = Profile.objects.create(user=user) 

        # If you need to set additional fields directly from the form,
        # you can do it here:
        # profile.nom_enfant = serializer.validated_data.get('nom_enfant')
        # profile.age_enfant = serializer.validated_data.get('age_enfant') 
        # ... (add other fields as needed)

        profile.save()  # Save the profile changes

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
'''