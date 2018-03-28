# Python imports
from os.path import join

# project imports
from .common import *
from .i18n import *
# uncomment the following line to include i18n
# from .i18n import *


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

INTERNAL_IPS = ["127.0.0.1"]

# allow all hosts during development
ALLOWED_HOSTS = ['*']

# adjust the minimal login
LOGIN_URL = 'core_login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'core_login'


# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': 'haystack_test',
        'USER': 'yugo',
        'PASSWORD': '123456789',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
}

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS

INSTALLED_APPS += [
    'customers',
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache"
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# haystack search engine conection
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}

# TENANT SCHEMAS SETTINGS

DATABASE_ROUTERS = ('tenant_schemas.routers.TenantSyncRouter',)

# shared apps are migrated from public and just in public
SHARED_APPS = (
    'tenant_schemas',  # mandatory, should always be before any django app
    'customers',  # you must list the app where your tenant model resides in
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
)

# apps migrated in tenant schemas
TENANT_APPS = (
    'django.contrib.contenttypes',
    # your tenant-specific apps
    # 'myapp.model',
    # 'myapp.model2',
)
# tenant schemas mandatory, should always be before any django app
# http://django-tenant-schemas.readthedocs.io/en/latest/install.html#configure-tenant-and-shared-applications
INSTALLED_APPS = ['tenant_schemas'] + INSTALLED_APPS

# Model to manipulate Client Request using Shared and Tenant
TENANT_MODEL = 'customers.Client'

# Tenant storage
DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'


# DJANGO DEBUG TOOLBAR SETTINGS
# https://django-debug-toolbar.readthedocs.org


def show_toolbar(request):
    return not request.is_ajax() and request.user and request.user.is_superuser


MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
MIDDLEWARE = [
    "core.middleware.XHeaderTenantMiddleware",
] + MIDDLEWARE

INSTALLED_APPS += [
    "debug_toolbar",
]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'HIDE_DJANGO_SQL': True,
    'TAG': 'body',
    'SHOW_TEMPLATE_CONTEXT': True,
    'ENABLE_STACKTRACES': True,
    'SHOW_TOOLBAR_CALLBACK': 'haystack_test.settings.development.show_toolbar',
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
)
LOGGING = {
    'version': 1,
    'filters': {
        'tenant_context': {
            '()': 'tenant_schemas.log.TenantContextFilter'
        },
    },
    'formatters': {
        'tenant_context': {
            'format':
                '[%(schema_name)s:%(domain_url)s] %(levelname)-7s %(asctime)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'tenant_context',
            'filters': ['tenant_context'],
        },
    },
}
