# Generated by Django 4.2 on 2024-12-18 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "email",
                    models.EmailField(max_length=80, unique=True, verbose_name="Email"),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Username"
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(auto_now=True, verbose_name="Last Login"),
                ),
                (
                    "date_joined",
                    models.DateField(auto_now_add=True, verbose_name="Date Joined"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                (
                    "is_superuser",
                    models.BooleanField(default=False, verbose_name="Super User"),
                ),
                ("is_staff", models.BooleanField(default=False, verbose_name="Staff")),
                ("is_admin", models.BooleanField(default=False, verbose_name="Admin")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=50, verbose_name="Category")),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Created"),
                ),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag", models.CharField(max_length=50, verbose_name="Tag")),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Created"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Post Title")),
                ("description", models.TextField(verbose_name="Description")),
                ("content", models.TextField(verbose_name="Post Content")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.category",
                        verbose_name="Category",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        related_name="post", to="base.tag", verbose_name="Tags"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
        ),
    ]
