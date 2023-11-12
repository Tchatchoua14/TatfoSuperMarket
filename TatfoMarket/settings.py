"""
Django settings for TatfoMarket project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config #new
from django.contrib import messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^p&fn33z_8)+3zz%4v!yy3$d2^n&l5a&(sozq*k^7y+6=3&1tf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'order.apps.OrderConfig',
    # 'corsheaders',
    # 'allauth',
    # 'allauth.account',
    'social_django',
    'social_core',
    'captcha',
    'account',
    'Ecommerce',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.github',
    # 'allauth.socialaccount.providers.google',
]


MIDDLEWARE = [
    'social_django.middleware.SocialAuthExceptionMiddleware', #new
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #  "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'TatfoMarket.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', #new
                'social_django.context_processors.login_redirect', #new

            ],
        },
    },
]

WSGI_APPLICATION = 'TatfoMarket.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join (BASE_DIR, 'static/'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CRISPY_TEMPLATE_PACK = 'bootstrap4'

# CART_SESSION_ID = 'cart'

LOGIN_URL = 'account:login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'welcome'

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "vinyassou@yahoo.fr"
# EMAIL_HOST_PASSWORD = "vinyassou"


MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')


# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
        
#          'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         },


#         'APP': {
#             'client_id': '574111392765-150nfpg6sn2dql8o0m78j2cfqduuu7an.apps.googleusercontent.com',
#             'secret': '574111392765-150nfpg6sn2dql8o0m78j2cfqduuu7an.apps.googleusercontent.com',
#             'key': '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'
#         }
#     },

    # 'github': {
    #     # For each OAuth based provider, either add a ``SocialApp``
    #     # (``socialaccount`` app) containing the required client
    #     # credentials, or list them here:
        
    #      'SCOPE': [
    #         'profile',
    #         'email',
    #     ],
    #     'AUTH_PARAMS': {
    #         'access_type': 'online',
    #     },


    #     'APP': {
    #         'client_id': '9e85d9492e25f149252b',
    #         'secret': '9e85d9492e25f149252b',
    #         'key': 'f190d24327ee5ffdc6063caf02b4590f9cf586ed'
    #     }
    # },

    # 'facebook': {
    #     # For each OAuth based provider, either add a ``SocialApp``
    #     # (``socialaccount`` app) containing the required client
    #     # credentials, or list them here:
        
    #      'SCOPE': [
    #         'profile',
    #         'email',
    #     ],
    #     'AUTH_PARAMS': {
    #         'access_type': 'online',
    #     },


    #     'APP': {
    #         'client_id': '701820614848473',
    #         'secret': '701820614848473',
    #         'key': '58ee2658c1903c398f2dc9c215a1111f'
    #     }
    # }
# }

SOCIALACCOUNT_LOGIN_ON_GET=True

# SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # 'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.github.GithubOAuth2', #new
    'social_core.backends.google.GoogleOAuth2', #new
    'social_core.backends.google.GoogleOAuth', #new cccc
    'social_core.backends.facebook.FacebookOAuth2', #new

    'django.contrib.auth.backends.ModelBackend', #new
    ]

# http://127.0.0.1:8000/google/login/callback
# http://127.0.0.1:8000/google/

# SOCIAL_AUTH_REQUIRE_POST = True

# SOCIAL_AUTH_URL_NAMESPACE = 'social'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_GITHUB_KEY = config('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = config('SOCIAL_AUTH_GITHUB_SECRET')

SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET')


