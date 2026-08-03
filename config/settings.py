import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Read .env file ───────────────────────────────────────
def get_env(key, default=None):
    return os.environ.get(key, default)

# ── Security ─────────────────────────────────────────────
SECRET_KEY = get_env('SECRET_KEY', 'django-insecure-dev-only')
DEBUG = get_env('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = get_env('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# ── Apps ─────────────────────────────────────────────────
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
]

THIRD_PARTY_APPS = [
    'crispy_forms',
    'crispy_bootstrap5',
    'django_htmx',
]

LOCAL_APPS = [
    'apps.core',
    'apps.pages',
    'apps.projects',
    'apps.gallery',
    'apps.news',
    'apps.volunteers',
    'apps.contact',
    'apps.donations',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ── Middleware ────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
]

ROOT_URLCONF = 'config.urls'

# ── Templates ─────────────────────────────────────────────
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

# ── Database ──────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':     get_env('POSTGRES_DB',       'safina_db'),
        'USER':     get_env('POSTGRES_USER',     'safina_user'),
        'PASSWORD': get_env('POSTGRES_PASSWORD', ''),
        'HOST':     get_env('POSTGRES_HOST',     'localhost'),
        'PORT':     get_env('POSTGRES_PORT',     '5433'),
    }
}

# ── Password Validation ───────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── Localisation ──────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE     = 'Africa/Nairobi'
USE_I18N      = True
USE_TZ        = True

# ── Static & Media ────────────────────────────────────────
STATIC_URL    = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT   = get_env('DJANGO_STATIC_ROOT', str(BASE_DIR / 'staticfiles'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL     = '/media/'
MEDIA_ROOT    = get_env('DJANGO_MEDIA_ROOT', str(BASE_DIR / 'media'))

# ── Crispy Forms ──────────────────────────────────────────
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK          = 'bootstrap5'

# ── Default PK ───────────────────────────────────────────
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── Email ─────────────────────────────────────────────────
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ── Security headers (production only) ───────────────────
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER       = True
    SECURE_CONTENT_TYPE_NOSNIFF     = True
    X_FRAME_OPTIONS                  = 'DENY'
    SECURE_REFERRER_POLICY           = 'same-origin'