from collections.abc import Iterable
import uuid
from django.db import models

# Create your models here.


class Dir(models.Model):
    code = models.UUIDField(verbose_name='Код', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, verbose_name='Наименование')
    parent = models.ForeignKey('Dir', on_delete=models.CASCADE, blank=True, null=True)
    preview = models.FileField(upload_to='dir_privies', verbose_name='Превью')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def as_dict(self):
        return {'name': self.name, 'code': str(self.code), 'updated': self.updated}


class Tag(models.Model):
    code = models.UUIDField(verbose_name='Код', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    code = models.UUIDField(verbose_name='Код', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self) -> str:
        return self.name


class File(models.Model):
    code = models.UUIDField(verbose_name='Код', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, verbose_name='Название')
    extension = models.CharField(max_length=10, verbose_name='Расширение')
    file = models.FileField(upload_to='videos', verbose_name='Видео')
    preview = models.FileField(upload_to='privies', verbose_name='Превью')
    updated = models.DateTimeField(auto_now=True)
    studio = models.CharField(max_length=50, verbose_name='Студия', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Теги', blank=True)
    genre = models.ForeignKey(Genre, verbose_name='Жанр', on_delete=models.CASCADE)
    dir_name = models.ForeignKey(Dir, verbose_name='Папка хранения', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
