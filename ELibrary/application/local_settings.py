# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'elibrary',
        'USER': 'quack',
        'PASSWORD': 'qwerty',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}