from rest_framework import generics
from.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
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
        
class UserView(APIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def post(self, request):
        print(request)
        username = request.data.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'message': 'User exists'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)