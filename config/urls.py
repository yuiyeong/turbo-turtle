import debug_toolbar

from django.contrib import admin
from django.urls import include
from django.urls import path

from config import settings

urlpatterns = [
    path(route="admin/", view=admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [path(route="__debug__/", view=include(debug_toolbar.urls))]
