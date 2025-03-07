from django.urls import path
from .views import Home, CreateUserView, TokenView, RefreshToken


urlpatterns = [
    path('', Home.as_view()),
    path('api/user/register', CreateUserView.as_view()),
    path('api/user/login', TokenView.as_view()),
    path('api/token/refresh', RefreshToken.as_view())
]