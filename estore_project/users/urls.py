from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginView, Signup

app_name = "users"
urlpatterns = [
    path("signup/", view=Signup.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
