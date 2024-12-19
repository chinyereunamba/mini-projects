from django.urls import path
from .views import home, login_view, register, logout_view, profile, about, add_post

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("sign-up/", register, name="register"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile, name="profile"),
    path("about/", about, name="about"),
    path("add-post/", add_post, name="add-post"),
]
