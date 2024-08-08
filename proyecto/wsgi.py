"""
WSGI config for proyecto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import environ
env = environ.Env()

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

application = get_wsgi_application()


from django.contrib.auth.models import User
try:
    user = User.objects.get(username=env('J_ADMIN_USER'))
except:
    User.objects.create_superuser(username=env('J_ADMIN_USER'), email="xxx@example.com", password=env('J_ADMIN_PASS'), is_active=True, is_staff=True)

#
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from app_newfms.models import *
if not Group.objects.filter(name='nocadmin').exists():
    group = Group.objects.create(name='nocadmin')
if not Group.objects.filter(name='nocviewer').exists():
    group = Group.objects.create(name='nocviewer')

####
modelos=[Alarma]
group, created = Group.objects.get_or_create(name='nocadmin')
for modelo in modelos:
    content_type = ContentType.objects.get_for_model(modelo)
    permissions = Permission.objects.filter(content_type=content_type)
    for permission in permissions:
        group.permissions.add(permission)
group.save()
#
modelos=[Alarma]
group, created = Group.objects.get_or_create(name='nocviewer')
for modelo in modelos:
    log_content_type = ContentType.objects.get_for_model(modelo)
    view_permission = Permission.objects.get(content_type=log_content_type, codename=f'view_{(modelo._meta.model_name).lower()}')
    group.permissions.add(view_permission)
group.save()
###
###
try:
    user = User.objects.get(username='visita')
except:
    user = User.objects.create_user(username='visita', password='Noc,,2024', email='devops_goc@clarovtr.cl', is_active=True, is_staff=False)
    group, created = Group.objects.get_or_create(name='nocviewer')
    user.groups.add(group)
    user.save()
