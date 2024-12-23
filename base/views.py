from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse

from .forms import NewUserForm, PostForm, ProfileForm
from .models import Account, BlogPost, Tag

# Create your views here.


def home(request):
    latest_post = BlogPost.objects.all().order_by("-created_at")[:3]
    posts = BlogPost.objects.all().order_by('title')
    tags = Tag.objects.all()
    context = {"latest_post": latest_post, "posts": posts, 'tags':tags}
    return render(request, "base/index.html", context)


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user=user)
            messages.success(request, "Logged in successfully")
            return redirect("profile", request.user.username)
        else:
            messages.error(request, "Username or password incorrect")
    return render(request, "base/login.html")


class SignupView(CreateView):
    template_name = "base/register.html"
    form_class = NewUserForm

    def get_success_url(self):
        return reverse("login")


def logout_view(request):
    logout(request)
    return redirect("home")


def profile(request, username):
    user = get_object_or_404(Account, username=username)
    post = BlogPost.objects.filter(user=user)
    context = {"posts": post, "user": user}
    return render(request, "base/profile.html", context)


def edit_profile(request, username):
    user = get_object_or_404(Account, username=username)
    form = ProfileForm(instance=user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("profile", username=username)

    context = {"form": form}
    return render(request, "base/form.html", context)


def about(request):
    return render(request, "base/about.html")


def view_post(request, pk):
    post = BlogPost.objects.get(id=pk)
    context = {"post": post}
    return render(request, "base/post.html", context)


def add_post(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            form.save()
            return redirect("profile", username=request.user.username)
    context = {"form": form}

    return render(request, "base/form.html", context)


def edit_post(request, pk):
    post = BlogPost.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("profile", request.user.username)
    context = {"form": form}

    return render(request, "base/form.html", context)


def delete_post(request, pk):
    post = BlogPost.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect("profile")
    return render(request, "base/delete.html")
