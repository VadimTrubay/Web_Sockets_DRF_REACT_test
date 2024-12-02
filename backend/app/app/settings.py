import os
from datetime import timedelta
from pathlib import Path

import environ

# basedir from path
BASE_DIR = Path(__file__).resolve().parent.parent

# basedir from location .env file
BASE_DIR_ENV = Path(__file__).resolve().parent.parent.parent

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR_ENV, ".env"))

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env("DJANGO_DEBUG")

ALLOWED_HOSTS = ["*"] if DEBUG else env.list("DJANGO_ALLOWED_HOSTS")

POSTGRES_DB = env("POSTGRES_DB")
POSTGRES_USER = env("POSTGRES_USER")
POSTGRES_PASSWORD = env("POSTGRES_PASSWORD")
POSTGRES_HOST = env("POSTGRES_HOST")
POSTGRES_PORT = env("POSTGRES_PORT")

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_spectacular",  # include swegger docs
    "rest_framework",  # include django rest framework
    "rest_framework_simplejwt",  # include django simple jwt
    "corsheaders",  # include django cors

    "dialogs",
    "users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # include corsheaders
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:5173',
# ]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"
# ASGI_APPLICATION = 'app.asgi.application'

# include database sqlite3
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# include database postgresql
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": POSTGRES_DB,
#         "USER": POSTGRES_USER,
#         "PASSWORD": POSTGRES_PASSWORD,
#         "HOST": POSTGRES_HOST,
#         "PORT": POSTGRES_PORT,
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:3000",
#     "http://127.0.0.1:5173",
#     "http://127.0.0.1:5174",
#     "http://127.0.0.1:8000",
#     "http://127.0.0.1:8001",
#     "http://0.0.0.0:8000",
# ]


CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # "DEFAULT_PERMISSION_CLASSES": [
    #     "rest_framework.permissions.IsAuthenticated",
    # ],
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(os.getenv('REDIS_HOST'), int(os.getenv('REDIS_PORT')))],
        },
    },
}


# AUTH_USER_MODEL = "authenticate.CustomUserModel"

# For Gmail
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_ADMIN = env("GMAIL_ADMIN")
EMAIL_SERVER = env("GMAIL_SERVER")
EMAIL_HOST = env("GMAIL_HOST")
EMAIL_PORT = env("GMAIL_PORT")
EMAIL_HOST_USER = env("GMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("GMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_STARTTLS = True
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=50),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('JWT',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=50),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

DJOSER = {
    "EMAIL": {
        "activation": "users.emails.CustomActivationEmail",
        "password_reset": "users.emails.CustomPasswordResetEmail",
        "password_changed_confirmation": "users.emails.CustomPasswordChangedConfirmationEmail",
        "username_reset": "users.emails.CustomUsernameResetEmail",
        "username_changed_confirmation": "users.emails.CustomUsernameChangedConfirmationEmail",
    },
    "PASSWORD_RESET_CONFIRM_URL": "auth/users/reset_password_confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "auth/users/reset_username_confirm/{uid}/{token}",
    "ACTIVATION_URL": "auth/users/activate/{uid}/{token}/",
    "SEND_ACTIVATION_EMAIL": True,

    # "USER_ID_FIELD": "user_id",
    # "SERIALIZER_CLASS": "users.serializers.UserSerializer",
    # "LOGIN_FIELD": "username",
    # "USERNAME_RESET_TIMEOUT_DAYS": 1,
    # "PASSWORD_VALIDATORS": [
    #     "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    #     "django.contrib.auth.password_validation.MinimumLengthValidator",
    #     "django.contrib.auth.password_validation.CommonPasswordValidator",
    #     "django.contrib.auth.password_validation.NumericPasswordValidator",
    #     "django.core.validators.EmailValidator",
    # ],
    # "PASSWORD_RESET_CONFIRM_VIEW": "users.views.PasswordResetConfirmView",
    # "USERNAME_RESET_CONFIRM_VIEW": "users.views.UsernameResetConfirmView",
    # "ACTIVATION_VIEW": "users.views.ActivationView",
    # "SEND_ACTIVATION_EMAIL_ON_REGISTER": True,
    # "SERIALIZE_USER_DETAILS": True,
    # "PASSWORD_RESET_TIMEOUT_DAYS": 1,
    # "PASSWORD_RESET_EMAIL_TEMPLATE_NAME": "users/password_reset_email.html",
    # "USERNAME_RESET_EMAIL_TEMPLATE_NAME": "users/username_reset_email.html",
    # "ACTIVATION_EMAIL_TEMPLATE_NAME": "users/activation_email.html",
    # "PASSWORD_CHANGED_EMAIL_TEMPLATE_NAME": "users/password_changed_confirmation_email.html",
    # "USERNAME_CHANGED_EMAIL_TEMPLATE_NAME": "users/username_changed_confirmation_email.html",
    # "PASSWORD_RESET_SUBJECT_TEMPLATE_NAME": "users/password_reset_subject.txt",
    # "USERNAME_RESET_SUBJECT_TEMPLATE_NAME": "users/username_reset_subject.txt",
    # "ACTIVATION_SUBJECT_TEMPLATE_NAME": "users/activation_subject.txt",
    # "PASSWORD_CHANGED_SUBJECT_TEMPLATE_NAME": "users/password_changed_subject.txt",
    # "USERNAME_CHANGED_SUBJECT_TEMPLATE_NAME": "users/username_changed_subject.txt",
    # "DEFAULT_FROM_EMAIL": "your_email@domain.com",
    # "FORBIDDEN_USER_FIELDS": ["username", "email"],
    # "USERNAME_FIELD": "username",
    # "UNIQUE_USERNAME_FIELD": True,
    # "USERNAME_REGEX": "^[a-zA-Z0-9_.+-]+$",
    # "USER_MODEL": "users.CustomUserModel",
    # "PASSWORD_REQUIRED": True,
    # "PASSWORD_RETYPE": True,
    # "PASSWORD_COMPLEXITY": {
    #     "UPPERCASE": 1,
    #     "LOWERCASE": 1,
    # },
    # "PASSWORD_COMPLEXITY_REQUIRED": True,
    # "PASSWORD_COMPLEXITY_ERROR_MESSAGE": "Password must contain at least one uppercase letter, one lowercase letter, and one numeric digit.",
    # "PASSWORD_RETYPE_ERROR_MESSAGE": "Passwords do not match.",
    # "PASSWORD_REQUIRED_ERROR_MESSAGE": "Password is required.",
    # "PASSWORD_RETYPE_REQUIRED_ERROR_MESSAGE": "Password confirmation is required.",
    # "PASSWORD_COMPLEXITY_CHARACTERS": {
    #     "UPPERCASE": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    #     "LOWERCASE": "abcdefghijklmnopqrstuvwxyz",
    #     "DIGITS": "0123456789",
    #     "SPECIAL_CHARACTERS": "!@#$%^&*()-_=+[{]};:'\",<.>/?~`",
    # },
    # "PASSWORD_COMPLEXITY_MIN_LENGTH": 8,
    # "PASSWORD_COMPLEXITY_MAX_LENGTH": 20,
    # "PASSWORD_COMPLEXITY_REQUIRE_NUMBER": True,
    # "PASSWORD_COMPLEXITY_REQUIRE_SPECIAL_CHARACTER": True,
    # "PASSWORD_COMPLEXITY_REQUIRE_UPPERCASE": True,
    # "PASSWORD_COMPLEXITY_REQUIRE_LOWERCASE": True,
    # "PASSWORD_COMPLEXITY_REQUIRE_ASCII": True,
    # "PASSWORD_COMPLEXITY_REQUIRE_DICTIONARY_WORDS": True,
    # "PASSWORD_COMPLEXITY_DICTIONARY_WORDS": ["password", "123456", "qwerty", "admin", "user", "admin123", "1234567890"],
    # "PASSWORD_COMPLEXITY_REQUIRE_NON_ASCII": True,
    # "PASSWORD_COMPLEXITY_REQUIRE_UNIQUE_CHARS": True,
    # "PASSWORD_COMPLEXITY_UNIQUE_CHARS_LIMIT": 3,
    # "PASSWORD_COMPLEXITY_REQUIRE_NO_DICTIONARY_WORDS": True,
    # "PASSWORD_COMPLEXITY_NO_DICTIONARY_WORDS_LIMIT": 3,
    # "PASSWORD_COMPLEXITY_REQUIRE_NO_NUMERIC": True,
    # "PASSWORD_COMPLEXITY_REQUIRE_NO_SPECIAL_CHARACTER": True,
    # "PASSWORD_COMPLEXITY_REQUIRE_NO_UPPERCASE": True,
    # "PASSWORD_COMPLEXITY_REQUIRE_NO_LOWERCASE": True,
    # "PASSWORD_COMPLEXITY_REQUIRE_NO_ASCII": True,
}

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     },
# }

