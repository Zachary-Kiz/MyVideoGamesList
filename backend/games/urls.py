from django.urls import path
from .views import Home, CreateUserView, UserView


urlpatterns = [
    path('', Home.as_view()),
    path('api/user/register', CreateUserView.as_view()),
    path('api/user/login', UserView.as_view())
]