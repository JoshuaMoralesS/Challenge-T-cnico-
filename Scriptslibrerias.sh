#Scripts para correr python3 el servidor

Validar versiòn del PYhton instalada:

$ python3 

Intalar python3:

$ sudo apt-get install python3.pip

Actualizar los paquetes instalados del sistema:

$ sudo apt-get update


#SCripts para instalar las librerias para que corra bien los .py del Agente y la API:

#Agente:

$ sudo pip3 install py-cpuinfo
$ sudo pip3 install psutil
$ sudo pip3 install datetime
$ sudo pip3 install requests
$ python3 Agente.py

#API:

$ sudo pip3 install flask
$ sudo pip3 install Response
$ python3 api.py

#BD

$ sudo pip3 install pandas
$ sudo pip3 install SQLAlchemy
