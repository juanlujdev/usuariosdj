from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_sectret('DB_NAME'),
        'USER': get_sectret('USER'),
        'PASSWORD': get_sectret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',

    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

# EMAIL SETTINGS  activamos el envio de email con django, esta en las vistas de users, Los datos de email y pass
# estan en el fichero secret.json
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'  # le decimos que tipo de correo vamos a enviar
EMAIL_HOST_USER = get_sectret('EMAIL')
EMAIL_HOST_PASSWORD = get_sectret('PASS_EMAIL')
EMAIL_PORT = 587
