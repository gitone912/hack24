# Generated by Django 4.1.10 on 2023-07-22 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses_notes", "0011_note_color_note_icon_userprogress"),
    ]

    operations = [
        migrations.CreateModel(
            name="MonthlyUserProgress",
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
                ("hours_watched", models.IntegerField(blank=True, null=True)),
                ("playlists_completed", models.IntegerField(blank=True, null=True)),
                (
                    "month",
                    models.IntegerField(
                        choices=[
                            (1, "January"),
                            (2, "February"),
                            (3, "March"),
                            (4, "April"),
                            (5, "May"),
                            (6, "June"),
                            (7, "July"),
                            (8, "August"),
                            (9, "September"),
                            (10, "October"),
                            (11, "November"),
                            (12, "December"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        to_field="email",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="weeklyProgress",
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
                ("hours_watched", models.IntegerField(blank=True, null=True)),
                ("playlists_completed", models.IntegerField(blank=True, null=True)),
                (
                    "weekday",
                    models.IntegerField(
                        choices=[
                            (0, "Monday"),
                            (1, "Tuesday"),
                            (2, "Wednesday"),
                            (3, "Thursday"),
                            (4, "Friday"),
                            (5, "Saturday"),
                            (6, "Sunday"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        to_field="email",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="UserProgress",
        ),
    ]