"""
Django settings for expDjango project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import expDjango.config as config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w@hb3%9dq8_sfzsx7cq@mrwr(^ai_fw7n9a77nnn0u_$o9_0*7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [] # IF DEBUG == FALSE, I NEED TO PUT '*'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'expDjango',
    'treinoPrevisao',
    'Dataset',
    'users'
]

AUTH_USER_MODEL = 'users.CustomUser'

#REF --> https://docs.djangoproject.com/en/3.0/ref/settings/
LOGOUT_REDIRECT_URL = config.LOGOUT_REDIRECT_URL #URL TO HOMEPAGE, AFTER A LOGOUT
LOGIN_REDIRECT_URL = config.LOGIN_REDIRECT_URL #REDIRECT DPS DE EFETUADO UM LOGIN--> TERA DE SER PARA A PAGINA DE DETALHES DE UM UTILIZADOR
#LOGIN_URL = '' #REDIRECT OF A LOGIN, WHEN I USE LOGIN_REQUIRED OR LOGINREQUIREDMIXIN

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'expDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")]
        ,
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

WSGI_APPLICATION = 'expDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'app',
        'USER': 'gustavo',
        'PASSWORD': 'gustavo',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
#ESTAS LINHAS FORAM COMENTADAS, DE MODO A PERMITIR A CRIACAO DE UTILIZADORES, SEM TANTAS RESTRIÇÕES (ATENÇÃO, QUE ISTO APENAS ACONTECE, QUANDO O PROJETO ESTA EM DESENVOLVIMENTO, DAÍ A SUA ALTERACAO NOS SETTINGS, EM PRODUÇÃO MANTEM-SE AS VALIDACOES
AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/' #DEFINICAO DO NOME DA VARIAVEL A SER CHAMADA--> POR EXEMPLO NO LOAD STATIC, NUM FICHEIRO HTML

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"Projeto_Mestrado/static_cdn") #content delivery network