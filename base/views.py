from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import NewUserForm, PostForm

# Create your views here.


def home(request):
    return render(request, "base/index.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, email=email, password=password)
        print(user)

        if user is not None:
            login(request, user=user)
            messages.success(request, "Logged in successfully")
            return redirect("profile")
        else:
            messages.error(request, "Username or password incorrect")
    return render(request, "base/login.html")


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = NewUserForm()
    return render(request, "base/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


def profile(request):
    return render(request, "base/profile.html")


def about(request):
    return render(request, "base/about.html")


def add_post(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("profile")
    context = {"form": form}

    return render(request, "base/form.html", context)


def edit_post(request, pk):
    pass


def delete_post(request, pk):
    pass
