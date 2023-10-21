from django.urls import path

from .views import get_root, get_nested, add_dir, get_dir_path

urlpatterns = [
    path('root_dir/', get_root),
    path('get_nested/<str:code>/', get_nested),
    path('add_dir/', add_dir),
    path('get_dir_path/<str:code>/', get_dir_path),
]
