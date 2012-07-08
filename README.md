Form-site
=========

Virtualenv y pip
----------------

Para hacer funcionar esta pequeña aplicacion, lo que se recomienda es hacer es
utilizar virtualenvwrapper y pip, los cuales pueden ser instalados por medio
del gestor de paquetes de su distribucion favorita o por medio de easy_install.

* Pagina del proyecto pip:

http://www.pip-installer.org/en/latest/index.html

* Pagina del proyecto virtualenvwrapper:

http://www.doughellmann.com/projects/virtualenvwrapper/

Cuando se tenga configurado un entorno virtual con virtualenvwrapper podemos
seguir con el ejercicio.


Copia del repositorio en la maquina
-----------------------------------

Puedes hacer un fork de este repositorio con la cuenta de github para despues
clonarlo en tu maquina, o simplemente puedes descargar el codigo fuente sin la
necesidad de tener que instalar git en tu computadora.

Una vez te hagas con el codigo fuente podemos continuar.


Creacion de base de datos
-------------------------

Solo he probado esta aplicacion con postgresql version 9.1, pero probablemente
tambien sirva con mysql y sqlite.

para la creacion de la base de datos en postgres, primero tenermos que entrar
a psql con el usuario postgres y crear un nuevo usuario que solo tenga permisos
sobre nuestra nueva base de datos, hace con la siguiente linea de codigo.


CREATE ROLE nombreNuevoUsuario LOGIN ENCRYPTED PASSWORD 'passNuevoUsuario' NOINHERIT VALID UNTIL 'infinity';
CREATE DATABASE nombreNuevaDB WITH ENCODING='UTF8' OWNER=nombreNuevoUsuario TEMPLATE=template0;

Configuracion de la base de datos
---------------------------------

Para configurar en nuestra aplicacion la base de datos que necesitamos es necesario 
abrir el archivo llamado settings.py ubicado en la carpeta app_example, cuando este
archivo este este abierto tenemos que modificar las siguientes lineas:


DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.

        'NAME': 'dbapp',                      # Or path to database file if using sqlite3.

        'USER': 'postgres',                      # Not used with sqlite3.

        'PASSWORD': '123456',                  # Not used with sqlite3.

        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.

        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.

    }

}


La variable ENGINE especifica el controlador de nuestra base de datos, si nuestro
motor de base de datos es postresql la definicion de esta variables seria

'ENGINE': 'django.db.backends.postgresql_psycopg2',

si es mysql seria:

'ENGINE': 'django.db.backends.mysql',

y si es sqlite seria:

'ENGINE': 'django.db.backends.sqlite3',


En la variable NAME se especifica el nombre de nuestra base de datos creada con
anterioridad.

Las Variables USER y PASSWORD, definen el usuario de la base de datos con su respectiva
contraseña.

La variable HOST es donde se especifica la direccion ip de la maquina donde se aloja la
db, si se esta usando una base de datos local se dajaria este campo vacio o se escribiria
localhost.

Por ultimo, en la variable PORT es en donde se especifica el puerto de escucha del motor
de la base de datos.

Para la configuracion total de este archivo se pueden seguir al pie de la letra los comentarios


Instalacion de aplicaciones y librerias
---------------------------------------

Primero tenemos que instalar django y otras libreria con pip, esto se hace de la siguiente manera:

* pip install django
* pip install south
* pip install django-uniform
* pip install psycopg2


Sincronizar la aplicacion con la base de datos
----------------------------------------------

Ahora que ya configuramos la base de datos, lo que tendriamos que hacer es sincronizar nuestra
aplicacion con la base de datos, para hacer esto, tenemos que ir al dirctorio raiz del proyecto
y ejecutar la siguiente linea:

./manage.py syncdb --all

Cuando se ejecuta el anterior comando las tablas de nuestra aplicacion se crean en la base de datos
y nos pedira un nombre de usuario de administracion con la clave.


Hechar a andar nuestra aplicacion
---------------------------------

Despues de haber terminado de sincronizar nuestra aplicacion podemos correr la aplicacion con el
siguiente comando:

./manage.py runserver


Para acceder a la aplicacion es necesario entrar a un navegador y digitar en la barra de direcciones
http://localhost:8000