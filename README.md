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