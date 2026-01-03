from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import RegisterProfileSerializer, ProfileSerializer
from django.contrib.auth.models import User
from .models import Profile


@api_view(['POST'])
def register_user(request: Request):
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "username and password are required"},status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "username already exists"},status=400)

    user = User.objects.create_user(username=username,password=password)

    serializer = RegisterProfileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=user)
        return Response({"message": "User registered successfully"},status=201)

    user.delete()
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request: Request):
    try:
        profile = request.user.profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=202)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=404)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_profile(request: Request):
    try:
        profile = request.user.profile
        serializer = ProfileSerializer(profile, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400)
    except Profile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=404)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    old_password = request.data.get("old_password")
    new_password = request.data.get("new_password")

    if not old_password or not new_password:
        return Response(
            {"error": "old_password and new_password are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = request.user

    if not user.check_password(old_password):
        return Response(
            {"error": "Old password is incorrect"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Set new password (hashed automatically)
    user.set_password(new_password)
    user.save()

    return Response(
        {"message": "Password changed successfully"},
        status=status.HTTP_200_OK
    )



@api_view(['POST'])
def logout_user(request):
    """
    Logout user (JWT blacklist later)
    """
    pass
