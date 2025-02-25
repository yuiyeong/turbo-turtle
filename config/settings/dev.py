from .base import *

INTERNAL_IPS = ["127.0.0.1"]

if DEBUG:
    # django-debug-toolbar 설정
    INSTALLED_APPS += ["debug_toolbar"]
    MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE
