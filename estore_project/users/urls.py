from django.urls import path

from .views import Login, Signup

app_name = "users"
urlpatterns = [
    path("signup/", view=Signup.as_view(), name="signup"),
    path("login/", view=Login.as_view(), name="login"),
]
