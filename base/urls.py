from django.urls import path
from .views import (
    about,
    edit_profile,
    login_view,
    logout_view,
    PostCreateView,
    PostDeleteView,
    PostListView,
    PostUpdateView,
    profile,
    SignupView,
    view_post,
)

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("login/", login_view, name="login"),
    path("sign-up/", SignupView.as_view(), name="register"),
    path("logout/", logout_view, name="logout"),
    path("u/<str:username>/", profile, name="profile"),
    path("u/<str:username>/edit/", edit_profile, name="edit-profile"),
    path("about/", about, name="about"),
    path("post/<str:slug>/", view_post, name="post"),
    path("add-post/", PostCreateView.as_view(), name="add-post"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="edit-post"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="delete-post"),
]
