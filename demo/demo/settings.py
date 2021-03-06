# Django settings for demo project.
import sys
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

PROJECT_ROOT = os.path.split(os.path.realpath(os.path.dirname(__file__)))[0]

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('demo admin', 'demo@localhost'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

if not 'test' in sys.argv:
    DATABASES['default'].update({
        'NAME': os.path.join(PROJECT_ROOT, 'demo.sql')
    })

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '%s/.media' % PROJECT_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%-$k-+*0v1853)js61nc3$$(^7$sv6axmxgvbed5_257q(62+f'

# List of callables that know how to import templates from various sources.
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)
TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.request',)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader')

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware')

ROOT_URLCONF = 'demo.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'demo.wsgi.application'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
    'django_extensions',
    'easy_thumbnails',
    'radpress')

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

RADPRESS_TITLE = 'Radpress demo'
RADPRESS_DESCRIPTION = "Let's write a simple description to here."
RADPRESS_LIMIT = 5
RADPRESS_DISQUS = ''
# RADPRESS_DEFAULT_MARKUP = 'markdown'
