import os
from os.path import abspath

import environ

try:
    from django.utils.translation import ugettext_lazy as _
except ImportError:
    _ = lambda s: s  # noqa: E731


root = environ.Path(__file__) - 3
BASE_DIR = root()

env = environ.Env()
environ.Env.read_env(env_file=root(".env"))

file_path = abspath(__file__)
home_path = file_path.split("/")
user_name = home_path[2]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

SECRET_KEY = env.str(
    "SECRET_KEY", default="PRe0vrb9nRb1qMftrg1gEuETn6ui9FbyeRVx6Y1716lN30Dg0qL8BhdOkzW"
)

DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "djangomix",
    "{{cookiecutter.project_name}}",
]

if DEBUG:
    INSTALLED_APPS.append("django_extensions")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = True

LANGUAGES = [
    ("en", _("English")),
]

ROOT_URLCONF = "{{cookiecutter.project_name}}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = "{{cookiecutter.project_name}}.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": env.str("DATABASE_NAME", f"{{cookiecutter.project_name}}.sqlite"),
        "USER": env.str("DATABASE_USER", env.NOTSET),
        "PASSWORD": env.str("DATABASE_PASSWORD", env.NOTSET),
        "HOST": env.str(
            "DATABASE_HOST",
            env.NOTSET,
        ),
        "PORT": env.str("DATABASE_PORT", env.NOTSET),
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Uncomment to use custom user model
# AUTH_USER_MODEL = "{{cookiecutter.project_name}}_user.User"
# AUTHENTICATION_BACKENDS = ["{{cookiecutter.project_name}}.auth.AuthBackend"]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# EMAIL_BACKEND = "django_ses.SESBackend"
# AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", env.NOTSET)
# AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", env.NOTSET)
# AWS_SES_REGION_NAME = env.str("AWS_SES_REGION_NAME", env.NOTSET)
# AWS_SES_REGION_ENDPOINT = env.str("AWS_SES_REGION_ENDPOINT", env.NOTSET)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# DJANGOMIX
LARAVELMIX_PUBLIC_URL = STATIC_URL + 'build/'
# END DJANGOMIX
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
SIMPLE_CUSTOMIZE_MODE = env.str("SIMPLE_CUSTOMIZE_MODE", True)

LOGIN_URL = "/login/start/"
LOGIN_REDIRECT_URL = "/user/"
LOGOUT_REDIRECT_URL = "/"
