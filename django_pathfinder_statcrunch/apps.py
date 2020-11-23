from django.apps import AppConfig


class DjangoPathfinderStatcrunchConfig(AppConfig):
    name = 'django_pathfinder_statcrunch'
    url_slug = 'pathfinder'
    package_name = __import__(name).__package_name__
    version = __import__(name).__version__

    def ready(self):
        from .bindings import create_bindings
        create_bindings()