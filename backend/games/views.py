from datetime import datetime, timedelta
from django.http import JsonResponse
import jwt
from django.conf import settings
from rest_framework import generics
from.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        # Create a new user using the serializer
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'User created successfully!',
                'user': serializer.data
            }
            # Return response with 201 status code
            response = Response(response_data, status=status.HTTP_201_CREATED)
            # Access the status code
            print(f"Status Code: {response.status_code}")
            return response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TokenView(APIView):
    """
    View to handle the creation of access and refresh tokens.
    """
    
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Accepts username or email to authenticate and return both access and refresh tokens.
        """
        username_or_email = request.data.get('username_or_email')
        password = request.data.get('password')

        if not username_or_email or not password:
            return Response({'error': 'Username/Email and Password are required'}, status=400)

        # Try to find user by username or email
        try:
            user = User.objects.get(username=username_or_email)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                return Response({'error': 'Invalid username or email'}, status=404)

        # Check if password is correct
        if not user.check_password(password):
            raise AuthenticationFailed('Invalid credentials')

        # Generate Access Token (short-lived, e.g., 15 minutes)
        access_token = generate_access_token(user)

        # Generate Refresh Token (longer-lived, e.g., 7 days)
        refresh_token = generate_refresh_token(user)

        response = JsonResponse({'message': 'Tokens set'})
        response.set_cookie(
            'access_token', access_token, 
            httponly=True, secure=True, 
            max_age=30 * 60,  # 30 minutes
            samesite='None'  # Ensures the cookie is sent only to same-site requests
        )
    
        # Set the refresh token as an HTTP-only cookie
        response.set_cookie(
            'refresh_token', refresh_token, 
            httponly=True, secure=True, 
            max_age=7 * 24 * 60 * 60,  # 7 days
            samesite='None'
        )
    
        return response

def generate_access_token(user):
    """
    Helper method to generate the access token.
    Access token is short-lived (e.g., 15 minutes).
    """
    access_payload = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'exp': datetime.now() + timedelta(minutes=30),  # Expiration time for access token
        'iat': datetime.now(),  # Issued at
    }

    return jwt.encode(access_payload, settings.SECRET_KEY, algorithm='HS256')

def generate_refresh_token(user):
    """
    Helper method to generate the refresh token.
    Refresh token is long-lived (e.g., 7 days).
    """
    refresh_payload = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'exp': datetime.now() + timedelta(days=7),  # Expiration time for refresh token
        'iat': datetime.now(),  # Issued at
    }

    return jwt.encode(refresh_payload, settings.SECRET_KEY, algorithm='HS256')
    
class RefreshToken(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        # Get refresh token from cookie
        refresh_token = request.COOKIES.get('refresh_token')

        if not refresh_token:
            return JsonResponse({'error': 'Refresh token missing'}, status=400)

        try:
            # Decode refresh token
            payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['id'])

            # Generate a new access token
            new_access_token = generate_access_token(user)

            response = JsonResponse({'message': 'Refreshed Access Token'})
            response.set_cookie(
                'access_token', new_access_token, 
                httponly=True, secure=True, 
                max_age=30 * 60,  # 30 minutes
                samesite='None'  # Ensures the cookie is sent only to same-site requests
            )

            return response

        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Refresh token expired'}, status=401)

        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid refresh token'}, status=401)