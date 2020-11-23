from django.apps import apps 
from django.urls import reverse
from django.conf import settings
from packagebinder.bind import PackageBinding, SettingsBinding, TaskBinding, SidebarBinding
import logging 

logger = logging.getLogger(__name__)

app_config = apps.get_app_config('django_pathfinder_statcrunch')

package_binding = PackageBinding(
    package_name=app_config.name, 
    version=app_config.version, 
    url_slug='eveonline', 
)

sidebar_binding = SidebarBinding(
    package_name=app_config.name,
    parent_menu_item={
        "fa_icon": 'fa-chart-pie',
        "name": "Pathfinder Statistics",
        "url": reverse('django-pathfinder-statcrunch-list-reports'), 
    },
    child_menu_items=[]
)


def create_bindings():
    package_binding.save()
    sidebar_binding.save()