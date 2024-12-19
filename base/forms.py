from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account, BlogPost, Tag, Category


class NewUserForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ["email", "username", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["bio", "first_name", "last_name"]


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "description", "category", "content", "tags"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple,  # Use checkboxes for the tags field
        }
