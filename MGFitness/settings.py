"""
Django settings for MGFitness project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ag_(+q5xsijj5krt36r#*_04#r3y35)pt!pk4b=h$w#!a178l('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'home',
    'material',
    'material.admin',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MGFitness.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'MGFitness.wsgi.application'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

APPEND_SLASH = True


LOGIN_REDIRECT_URL = 'index'  # Change this to your desired redirect URL


SESSION_COOKIE_AGE = 604800   # a week in seconds

# SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_CLEAR_ON_LOGOUT = True

STRIPE_PUBLISHABLE_KEY = "pk_test_51OKdDUSF5zr91hwv5WpFdbISkbXObaG7XdWF2RU9N9C8tv8E1tCjYYMTPMEvGV7xpJagMpHWWexin6sDC0QRiQWC00kg431266"
STRIPE_SECRET_KEY = "sk_test_51OKdDUSF5zr91hwvEgvdzzoBrnIgC8vXncowGimVw769t90vJ66TIi3jjNjg8NyqFNK0QSlfajNBEdOYR4bKPo1700ZtuxDv83"


# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '22amtics042@gmail.com'
EMAIL_HOST_PASSWORD = 'iblp trlj eppc ymta'

# FOR MATERIAL UI CUSTOMIZATION
MATERIAL_ADMIN_SITE = {
    'HEADER':  'MG Fitness',  # Admin site header
    'TITLE':  'MG Fitness',
    'FAVICON':  'images/logo-3.png',  # Admin site favicon (path to static should be specified)
    'MAIN_BG_COLOR':  '#020230',  # Admin site main color, css color should be specified
    'MAIN_HOVER_COLOR':  '#020230',  # Admin site main hover color, css color should be specified
    'PROFILE_PICTURE':  'images/MGFITNESS.png',  # Admin site profile picture (path to static should be specified)
    'PROFILE_BG':  'images/bg.png',  # Admin site profile background (path to static should be specified)
    'LOGIN_LOGO':  'images/MGFITNESS.png',  # Admin site logo on login page (path to static should be specified)
    'LOGOUT_BG':  'images/bg.png',  # Admin site background on login/logout pages (path to static should be specified)
    'SHOW_THEMES':  True,  #  Show default admin themes button
    'TRAY_REVERSE': False,  # Hide object-tools and additional-submit-line by default
    'NAVBAR_REVERSE': True,  # Hide side navbar by default
    'SHOW_COUNTS': True, # Show instances counts for each model
    # 'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
    #     'sites': 'send',
    # },
    # 'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
    #     'site': 'contact_mail',
    # }
}