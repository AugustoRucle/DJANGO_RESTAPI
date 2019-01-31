Para conectarte a tu base de datos deberas instalar "pip instal mysqlclient==1.3.12"

Tu archivo "DATABASE" debera quedar de la siguiente manera:

Amigo te propongo que utilices mysqlclient==1.3.12 que sirve tanto para maridb y mysql:

pip instal mysqlclient==1.3.12

Luego en el settings:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tubasededatos',
        'USER': 'tuusuario',
        'PASSWORD': 'tupassword',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS' :  { 
            'init_command' :  "SET sql_mode = 'STRICT_TRANS_TABLES'" , 
        }, 
    }
}

>pip manage.py migrate
>pip manege.py makemigrations
>python manage.py showmigrations
>--fake "forzada"
>python manage.py startapp 


from Profile.models import Profile