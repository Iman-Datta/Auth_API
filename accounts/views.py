from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def register_user(request: Request):
    fnm = request.data.get('first_name')
    lnm = request.data.get('last_name')
    ph = request.data.get('phone')
    age = request.data.get('age')
    gen = request.data.get('gender')



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
