# Generated by Django 4.1.7 on 2023-05-08 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="about_me",
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
                ("img", models.FileField(null=True, upload_to="")),
                ("information", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=100, null=True)),
                ("img", models.FileField(null=True, upload_to="")),
                ("video", models.FileField(blank=True, null=True, upload_to="")),
                ("short_description", models.TextField(null=True)),
                ("long_description", models.TextField(null=True)),
            ],
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
                ("name", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Home_page",
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
                ("img1", models.FileField(null=True, upload_to="")),
                ("img2", models.FileField(null=True, upload_to="")),
                ("img3", models.FileField(null=True, upload_to="")),
                ("video", models.FileField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="message_detail",
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
                ("name", models.CharField(max_length=100, null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("contact_no", models.IntegerField(max_length=10, null=True)),
                ("message", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Work",
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
                (
                    "type",
                    models.CharField(
                        choices=[
                            ["video", "video"],
                            ["images", "images"],
                            ["zip", "zip"],
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("title", models.CharField(max_length=100, null=True)),
                ("img1", models.FileField(null=True, upload_to="")),
                ("img2", models.FileField(null=True, upload_to="")),
                ("img3", models.FileField(null=True, upload_to="")),
                ("short_description", models.TextField(null=True)),
                ("long_description", models.TextField(null=True)),
                (
                    "catdata",
                    models.ForeignKey(
                        max_length=100,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="My_Portfolio.category",
                    ),
                ),
            ],
        ),
    ]
