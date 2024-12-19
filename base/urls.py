from django.urls import path
from .views import (
    home,
    login_view,
    register,
    logout_view,
    profile,
    edit_profile,
    about,
    add_post,
    view_post,
    edit_post,
)

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("sign-up/", register, name="register"),
    path("logout/", logout_view, name="logout"),
    path("u/<str:username>/", profile, name="profile"),
    path("u/<str:username>/edit/", edit_profile, name="edit-profile"),
    path("about/", about, name="about"),
    path("post/<int:pk>/", view_post, name="post"),
    path("add-post/", add_post, name="add-post"),
    path("post/<int:pk>/edit/", edit_post, name="edit-post"),
]
