import cpuinfo
import platform
import psutil
import sys
import datetime
import requests
import socket
from configparser import ConfigParser

parser = ConfigParser()
parser.read('ip.ini')

url = str("http://" + parser.get('api', 'ip') + ":" + parser.get('api', 'puerto') + "/")

#INFORMACION DEL PROCESADOR

informacion_procesador=cpuinfo.get_cpu_info()['arch_string_raw']
informacion_procesador2=cpuinfo.get_cpu_info()['brand_raw']

print ("INFORMACION PROCESADOR:  " ,informacion_procesador, " ", informacion_procesador2)


#INFORMACION DEL SISTEMA OPERATIVO (Nombre y versión)

nombre_SO= platform.system()
version_SO= platform.version()

print("NOMBRE SISTEMA OPERATIVO:  ",nombre_SO)  
print("VERSION SISTEMA OPERATIVO: ",version_SO) 



#LISTADO DE PROCESOS CORRIENDO 

listadoprocesos = []

for proceso in psutil.process_iter():
 
 listadoprocesos.append({"Nombre del proceso": proceso.name(), "ID Proceso":proceso.pid})
   
# print("Nombre del Proceso: ",proceso.name())
 #print("ID Proceso: ",proceso.pid)

#USUARIOS CON UNA SESIÓN ABIERTA EN EL SISTEMA

Usuarios_activos=[]
for u in psutil.users():
    Usuarios_activos.append({'name': u.name, 'pid': u.pid})

for i in Usuarios_activos:
    print ("Usuarios Activos: ", i)


#OBTENER IP DEL SERVIDOR

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
ip_address = s.getsockname()[0]

print (s.getsockname()[0])
s.close()

#FUNCION POST EN JSON

infoproceso = {'informacion_procesador':informacion_procesador,
               'informacion_procesador2':informacion_procesador2,
               'nombre_SO':nombre_SO,
               'version_SO':version_SO,
               'listadoprocesos': listadoprocesos,
               'Usuarios_activos':Usuarios_activos,
               'ip_address': ip_address
              }
print(infoproceso)

i = requests.post(url,json=infoproceso)
print(i.content)
