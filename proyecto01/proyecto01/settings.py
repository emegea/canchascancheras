from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4g=@zx_w3vfb#a0id68tca0y)sbgqtp&l0leg_oler^p8622f#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web'
]

# Opciones de Jazzmin (para customizar el admin)
JAZZMIN_SETTINGS = {
    "site_title": "Canchas Cancheras Admin",
    "site_header": "Canchas Cancheras",
    "site_brand": "Canchas Cancheras",
    "site_logo": "web/img/iconoBlanco.svg",
    "site_logo_classes": "img-circle logoAdmin",
    "site_icon": "web/img/iconoColor.svg",
    # Login
    "login_logo": "web/img/logo.svg",
    "login_logo_dark": "web/img/logo.svg",
    "welcome_sign": "Bienvenido a Canchas Cancheras",
    # Footer
    "copyright": "Emegea",
    # Usuario
    "user_avatar": "web/img/icono.svg",
    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": ["auth", "web"],
    # Custom CSS y JS
    "custom_css": "web/css/customAdmin.css",
    "custom_js": "web/js/customAdmin.js",
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "web.Cancha": "fas fa-regular fa-futbol",
        "web.Cliente": "fas fa-users",
        "web.Venta": "fas fa-money-bill",
        "web.MensajeContacto": "fas fa-envelope",
    },
    "custom_links": {
        "web": [{
            "name": "Visitar el sitio",
            "url": "index",
            "icon": "fas fa-external-link-alt",
            "permissions": ["auth.view_user"]
        }]
    },
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "horizontal_tabs",
        "auth.group": "horizontal_tabs",
        "web.cancha": "horizontal_tabs",
        "web.cleinte": "horizontal_tabs",
        "web.ventas": "horizontal_tabs"
        },
    # Mostrar botón para acceder a la barra de personalización UI
    "show_ui_builder": True,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto01.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'web/templates/web/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyecto01.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',

        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'canchascancheras',
        'USER': 'postgres',
        'PASSWORD': 'CONTRASEÑA',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True

# Configurar los idiomas disponibles
LANGUAGES = [
    ('es', 'Español'),
]
# Ruta a los archivos de traducción
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
