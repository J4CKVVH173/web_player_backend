# Generated by Django 4.2.6 on 2023-10-20 22:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name="Dir",
            fields=[
                (
                    "code",
                    models.UUIDField(
                        default=uuid.UUID("4efd6e72-c8e5-4fee-8fe3-37a2a890d13d"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Код",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Наименование")),
                (
                    "preview",
                    models.FileField(upload_to="dir_privies", verbose_name="Превью"),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="player.dir",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "code",
                    models.UUIDField(
                        default=uuid.UUID("73cabe48-eb2b-46c8-b62d-7ed091d043ca"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Код",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Название")),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "code",
                    models.UUIDField(
                        default=uuid.UUID("b7b3df9d-65f6-4945-8c34-3762f4ae6fc9"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Код",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Название")),
            ],
        ),
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "code",
                    models.UUIDField(
                        default=uuid.UUID("109f90de-2428-42bf-9879-f0a5631413c8"),
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Код",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Название")),
                (
                    "extension",
                    models.CharField(max_length=10, verbose_name="Расширение"),
                ),
                ("file", models.FileField(upload_to="videos", verbose_name="Видео")),
                (
                    "preview",
                    models.FileField(upload_to="privies", verbose_name="Превью"),
                ),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "studio",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Студия"
                    ),
                ),
                (
                    "dir_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="player.dir",
                        verbose_name="Папка хранения",
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="player.genre",
                        verbose_name="Жанр",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, null=True, to="player.tag", verbose_name="Теги"
                    ),
                ),
            ],
        ),
    ]
