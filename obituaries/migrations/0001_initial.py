# Generated by Django 5.1.3 on 2024-11-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Obituary",
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
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("author_name", models.CharField(max_length=100)),
                ("contact_email", models.EmailField(max_length=254)),
                ("date_posted", models.DateTimeField(auto_now_add=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="obituary_images/"
                    ),
                ),
            ],
        ),
    ]
