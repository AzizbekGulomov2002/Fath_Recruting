from pathlib import Path
from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.

import os
BASE_DIR = Path(__file__).resolve().parent.parent
import environ
env = environ.Env()
environ.Env.read_env()
# SECRET_KEY = env('SECRET_KEY')
SECRET_KEY = 'django-insecure-a_%!6l@7_&h+gjz%v^2cz()60b)1k4dojfi(p+0$ywp1cp5o=3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'apps.blog',
    'apps.company',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # noqa 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ================================================== PostgresSQL =======================================================
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': "fath_recuter",
#         'USER': "postgres",
#         'PASSWORD': "1",
#         'HOST': 'localhost',
#         'PORT': 5432,
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



LANGUAGES = (
    ('en', _('English')),
    ('uz', _('Uzbek')),
    ('ru', _('Russian')),
)
LOCALE_PATHS = [
    BASE_DIR/'locale/',
]
LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('en', 'uz', 'ru')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('ru', 'uz', 'en')

MODELTRANSLATION_TRANSLATION_FILES = (
    'apps.product.translation',
)

import os

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_DIRS = [
#     BASE_DIR / 'static'
# ]
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "show_ui_builder": True,
    "site_title": "Fath Recruting",
    "site_header": "Fath Recruting",
    "site_brand": "Fath Recruting",
    "site_logo": None,
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": "images/title.png",
    "welcome_sign": "Fath Recruting Logistic Company",
    "copyright": "Fath Recruter",
    "user_avatar": None,
    "topmenu_links": [
        {"name": ("Home"), "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": ("Support"), "url": "https://t.me/AzizbekGulomov", "new_window": True},
        {"model": "auth.User"},
        {"app": "books"},
    ],
    "usermenu_links": [
        {"name": ("Support"), "url": "https://t.me/AzizbekGulomov", "new_window": True},
        {"model": "auth.user"},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
    "custom_links": {
        "books": [
            {
                "name": "Make Messages",
                "url": "make_messages",
                "icon": "fas fa-comments",
                "permissions": ["books.view_book"],
            }
        ]
    },
    "icons": {
        "auth.Group": "fas fa-users",
        "auth.User": "fa fa-id-badge",
        "company.Company": "fas fa-building",
        "company.Statistic": "fas fa-chart-bar",    
        "company.About": "fa fa-file",
        "company.Team": "fa fa-users",
        "company.Contact": "fa fa-phone",
        "company.Blog": "fa fa-sticky-note",
        "company.Service": "fa fa-cogs",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},


    
}
JAZZMIN_SETTINGS["show_ui_builder"] = False
JAZZMIN_UI_TWEAKS = {}





EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'azizgulomov1529@gmail.com'
EMAIL_HOST_PASSWORD = 'azizbek1529'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

