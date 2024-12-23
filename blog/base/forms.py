from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account, BlogPost, Tag, Category


class NewUserForm(UserCreationForm):

    class Meta:
        model = Account
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "bio",
            "password1",
            "password2",
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["bio", "first_name", "last_name"]


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "description", "category", "content"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "Enter post title",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "textarea textarea-bordered !h-24",
                    "placeholder": "Enter a brief excerpt of your post",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "textarea textarea-bordered h-64",
                    "placeholder": "Write your post content here",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "input select select-bordered rounded-lg", 
                }
            ),
            "featured_image": forms.ClearableFileInput(
                attrs={"class": "file-input file-input-bordered w-full"}
            ),
            "publish": forms.CheckboxInput(attrs={"class": "toggle toggle-primary"}),
        }
