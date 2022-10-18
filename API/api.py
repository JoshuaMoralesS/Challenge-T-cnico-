rom flask import Flask
from flask import Flask, jsonify, request, Response
import json
from flask import Blueprint
from datetime import date
import sqlalchemy as db
from datetime import datetime

app = Flask(__name__)
mime_type = 'application/json'

@app.route('/', methods = ['POST'])
def hello():
	try:
	
		content_to_json = request.json

		registro = {'informacion_procesador':content_to_json['informacion_procesador'],
                   'informacion_procesador2':content_to_json ['informacion_procesador2'],
                   'nombre_SO': content_to_json ['nombre_SO'],
                   'version_SO': content_to_json ['version_SO'],
                   'listadoprocesos': content_to_json ['listadoprocesos'],
                   'Usuarios_activos':content_to_json ['Usuarios_activos'],
                   'ip_address': content_to_json ['ip_address']
              }
		fecha = str(date.today())

                #IMPORTAR A JSON

		archivo = str(registro['ip_address']+ "_" + fecha + ".txt")
		new_file = open(archivo, "w+")
		new_file.write(json.dumps(registro, indent = 3))
		new_file.close()

                #CONEXIÓN A LA BD

		engine = db.create_engine('sqlite:///almacenamiento/basededatos/api.sqlite')
		connection = engine.connect()
		metadata = db.MetaData()
		
		t = datetime.now()
		timestr = t.strftime('%Y-%m-%d %H:%M:%S.%f')	
		formato_fecha = datetime.strptime(timestr,'%Y-%m-%d %H:%M:%S.%f')


                #INSERTS A TABLA INFO_SERVIDOR

		info_servidorTab = db.Table('info_servidor',metadata,autoload =True,autoload_with= engine)
		queryinfo_servidor= db.insert(info_servidorTab).values(
                                   informacion_procesador= registro['informacion_procesador'],
                                   informacion_procesador2= registro['informacion_procesador2'],
                                   nombre_SO= registro['nombre_SO'],
                                   version_SO= registro['version_SO'],
                                   ip_address= registro['ip_address'],
                                   fecha= formato_fecha
                                   )

		ResultProxy = connection.execute(queryinfo_servidor)

		i =db.select([info_servidorTab.columns.ID_SERVIDOR]).where(info_servidorTab.columns.fecha== fecha)

		for row in connection.execute(i):
			id_servidor=row['ID_SERVIDOR']

                #INSERTS A TABLA USUARIOS               
                
		usuariosTab = db.Table('usuarios',metadata,autoload=True,autoload_with=engine)
                
		for  users in registro['Usuarios_activos']:
                              queryusuarios = db.insert(usuariosTab).values(
                                      ID_SERVIDOR = id_servidor,
                                      name = users['name'],
                                      pid = users['pid']
                                               )
		ResultProxy = connection.execute(queryusuarios)


                #INSERT A TABLA PROCESOS
                
		ProcesosTab = db.Table('Procesos',metadata,autoload=True,autoload_with=engine)
		for process in registro['listadoprocesos']:
                               queryprocess = db.insert(procesosTab).values(
                                      ID_SERVIDOR = id_servidor,
                                      name = process['name'],
                                      pid = process['pid']
                                               )
		ResultProxy = connection.execute(queryprocess)

		print (json.dumps(registro,indent = 3))
		return Response(json.dumps(registro), status= 201 , mimetype=mime_type)
	except Exception as e:
		print(e)
		response_error = {"Error": e}
		return Response(json.dumps(response_error), status=400, mimetype=mime_type)


app.run(host="0.0.0.0", port=5000, debug=True)

