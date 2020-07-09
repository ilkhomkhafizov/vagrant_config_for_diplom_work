__author__ = "Ilkhom Khafizov"


DEBUG = True
TEMPLATE_DEBUG = DEBUG


DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ pg_db_name }}',
        'USER': '{{ pg_db_user }}',
        'PASSWORD': '{{ pg_db_password }}'
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '{{ static_path }}'

DEBUG_STATICS = ('{{ src_static_path }}',)

PROD_STATICS = ('{{ uncollected_static }}',)

STATICFILES_DIRS = DEBUG_STATICS if DEBUG else PROD_STATICS

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

__all__ = ['DATABASES', 'DEBUG', 'STATIC_URL', 'STATIC_ROOT', 'STATICFILES_DIRS', 'STATICFILES_FINDERS']