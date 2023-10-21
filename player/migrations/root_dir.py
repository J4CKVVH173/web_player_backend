from django.db import migrations
from django.core.exceptions import ObjectDoesNotExist

from django.conf import settings


def forwards(apps, _):
    DirModel = apps.get_model("player", "Dir")

    try:
        DirModel.objects.get(code=settings.ROOT_DIR_UUID)
    except ObjectDoesNotExist:
        DirModel.objects.create(code=settings.ROOT_DIR_UUID, name='root')

class Migration(migrations.Migration):
    dependencies = [
        ("player", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]
