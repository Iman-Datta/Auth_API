from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import RegisterProfileSerializer, ProfileSerializer
from django.contrib.auth.models import User


@api_view(['POST'])
def register_user(request):
    # 1️⃣ Login details (User table)
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"error": "username and password are required"},status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "username already exists"},status=400)

    # 2️⃣ Create USER (auth)
    user = User.objects.create_user(username=username,password=password)

    # 3️⃣ Create PROFILE (personal info)
    serializer = RegisterProfileSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=user)
        return Response({"message": "User registered successfully"},status=201)

    # 4️⃣ If profile validation fails → rollback user
    user.delete()
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def login_user(request):
    """
    Login user
    - authenticate credentials
    - return JWT tokens
    """
    pass


@api_view(['GET'])
def get_profile(request):
    """
    Get logged-in user's profile
    """
    pass


@api_view(['PATCH'])
def update_profile(request):
    """
    Update allowed profile fields
    - age
    - gender
    - phone
    (first_name, last_name NOT allowed)
    """
    pass


@api_view(['POST'])
def change_password(request):
    """
    Change user password
    """
    pass


@api_view(['POST'])
def logout_user(request):
    """
    Logout user (JWT blacklist later)
    """
    pass
