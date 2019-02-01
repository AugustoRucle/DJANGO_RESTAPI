Para conectarte a tu base de datos deberas instalar "pip install mysqlclient==1.3.12"

Tu archivo "DATABASE" debera quedar de la siguiente manera:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS' :  { 
            'init_command' :  "SET sql_mode = 'STRICT_TRANS_TABLES'" , 
        }, 
    }
}

--Otros comandos
>pip manage.py migrate
>pip manege.py makemigrations
>python manage.py showmigrations
>--fake "forzada"
>python manage.py startapp 