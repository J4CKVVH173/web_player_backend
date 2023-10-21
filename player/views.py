import json

from django.http import JsonResponse, HttpResponse
from django.conf import settings

from .models import Dir


# Create your views here.
def get_root(request):
    root = Dir.objects.get(code=settings.ROOT_DIR_UUID)
    return JsonResponse(data={'code': root.code, 'name': root.name})


def get_nested(request, code):
    nested = Dir.objects.filter(parent=code)
    return JsonResponse(data={'nested': tuple(instance.as_dict() for instance in nested)})


def add_dir(request):
    body = json.loads(request.body)
    Dir.objects.create(name=body['name'], parent=Dir.objects.get(code=body['parent']))
    return HttpResponse(200)


def get_dir_path(request, code):
    target = Dir.objects.get(code=code)
    path = []
    path.append(target.as_dict())
    while str(target.code) != settings.ROOT_DIR_UUID:
        target = Dir.objects.get(code=target.parent.code)
        path.append(target.as_dict())

    path.reverse()
    return JsonResponse(data={'path': path})
