<h1 align="center"> Compliance continuo en Servidores </h1>
   <p align="left">
   <img src="https://img.shields.io/badge/CHALLENGE TECNICO-green">
   </p>
      <p align="left">
   <img src="https://img.shields.io/badge/PYTHON-blue">
   </p>
   
   <h1 align="left"> Objetivo del Proyecto </h1>
   
   Desarrollar dos programas en Python sobre una máquina virtual Linux (Debian 10). El primer programa *"Agente"*, será el encargado de extraer información del servidory enviarlo mediante un JSON a una *"API"*. 
   La *"API* será el encargado de recibirlo y almacenar la información extraida en un .txt , así como enviar la información a una BD normalizada los datos.
   
   <h1 align="left" > Ejecución de la aplicación </h1>
   
   Paso 1. Instalar librerías.
   
   Como primer paso, se instalan todas las librerías de Python que usamos para el desarrollo, 
   
        - Las librerias a instalar son: cpuinfo,psutil,datetime,requests,flask,response,pandas y sqlAlchemy. 
          El comando completo se puede enocntrar en el archivo "Scriptslibrerias.sh".
         
   Paso 2 Ejecutar la creación de la base de datos.
   
        - Para esto vamos a posicionarnos en la ruta "BD/crearBD.py" y ejecutar el script "crearBD.py" con el comando "python3 crearBD.py".
          El resultado será un archivo llamado "api.sqlite" que se creará en la ruta API/almacenamiento/basededatos.
         
    Paso 3 Levantar el servicio de la API.
    
       - 
   
