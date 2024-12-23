from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse

from .forms import NewUserForm, PostForm, ProfileForm
from .models import Account, BlogPost, Tag
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

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


class PostDetailView(DetailView):
    model = BlogPost
    template_name = "base/post.html"
    context_object_name = "post"


class PostListView(ListView):
    model = BlogPost
    template_name = "base/index.html"
    context_object_name = "posts"
    ordering = ("title",)

    def get_queryset(self):
        status = self.request.GET.get("status", "published") 
        queryset = BlogPost.objects.filter(status=status).order_by("-created_at")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_post"] = BlogPost.objects.filter(status="published").order_by("-created_at")[:3]
        context["tags"] = Tag.objects.all()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = "base/add-post.html"
    login_url = '/login/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user 
        post.save()

        if "save_draft" in self.request.POST:  # If "Save as Draft" button is clicked
            post.status = "draft"
        elif "publish" in self.request.POST:  # If "Publish" button is clicked
            post.status = "published"

        tags_input = self.request.POST.get("tags", "")  # Get tags from hidden input
        tag_list = [tag.strip() for tag in tags_input.split(",") if tag.strip()]  # Clean tags

        for tag_name in tag_list:
            tag, created = Tag.objects.get_or_create(tag=tag_name)
            post.tags.add(tag)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("profile", kwargs={"username": self.request.user.username})


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = PostForm
    template_name = "base/edit-post.html"
    login_url = "/login/"

    def get_object(self):
        return get_object_or_404(BlogPost, id=self.kwargs["pk"], user=self.request.user)

    def form_valid(self, form):
        post = form.save(commit=False)
        # Process the tags submitted with the form
        tag_names = self.request.POST.get("tags", "").split(
            ","
        )  # Get the tags from the hidden input
        tags = []
        for tag_name in tag_names:
            tag_name = tag_name.strip()
            if tag_name:  # Only add non-empty tag names
                tag, created = Tag.objects.get_or_create(tag=tag_name)
                tags.append(tag)

        # Clear existing tags and set the new ones
        post.tags.set(tags)
        post.save()

        # Optionally, handle saving as draft or publish status
        if self.request.POST.get("save_draft"):
            post.status = "draft"
            post.save()
        elif self.request.POST.get("publish"):
            post.status = "published"
            post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("profile", kwargs={"username": self.request.user.username})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = "base/delete.html"
    success_url = reverse_lazy("profile")
    login_url = "/login/"
