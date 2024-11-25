from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from config import config 
app = Flask(__name__)
conexion= MySQL(app)

##lista
@app.route('/eventos', methods= ['GET'])
def listar_eventos():
    try:
        cursor =conexion.connection.cursor()
        sql = "SELECT * FROM eventos"
        cursor.execute(sql)
        datos= cursor.fetchall()
        eventos =[]
        for fila in datos:
            evento={'ID_EVENTO': fila[0],'FECHA': str(fila[1]),'HORA':str(fila[2]),
                      'PRECIO':fila[3],'LOCALIZACION': fila[4]}
            eventos.append(evento)
        print(datos)
        return jsonify({'eventos': eventos,'mensaje': 'eventos listados'})

    except Exception as ex:
        return jsonify({'mensaje': ex})
    
@app.route('/usuarios', methods= ['GET'])
def listar_usuarios():
    try:
        cursor =conexion.connection.cursor()
        sql = "SELECT * FROM usuarios"
        cursor.execute(sql)
        datos= cursor.fetchall()
        usuarios =[]
        for fila in datos:
            usuario={'ID_USUARIO': fila[0],'NOMBRE_USUARIO': fila[1],'CORREO':str(fila[2]),
                      'CONTRASEÑA':fila[3],'FECHA_NAC': str(fila[4]),'SEXO':fila[5]}
            print(usuario)
            usuarios.append(usuario)
        print(datos)
        return jsonify({'usuario': usuarios ,'mensaje': 'usuarios listados'})

    except Exception as ex:
        return jsonify({'mensaje': ex})
                        
@app.route('/deportes', methods= ['GET'])
def listar_deportes():
    try:
        cursor =conexion.connection.cursor()
        sql = "SELECT * FROM deportes"
        cursor.execute(sql)
        datos= cursor.fetchall()
        deportes =[]
        for fila in datos:
            deporte={'NOMBRE_DEPORTE': fila[0],'TIPO_DEPORTE': fila[1],'EQUIPO':fila[2]}
            deportes.append(deporte)
        print(datos)
        return jsonify({'deporte': deportes ,'mensaje': 'deportes listados'})

    except Exception as ex:
        return jsonify({'mensaje': ex})
                        

@app.route('/usuario_actividad', methods= ['GET'])
def listar_usuario_actividad():
    try:
        cursor =conexion.connection.cursor()
        sql = "SELECT * FROM USUARIOACTIVIDAD"
        cursor.execute(sql)
        datos= cursor.fetchall()
        usuario_actividades =[]
        for fila in datos:
            usuario_actividad={'ID_USUARIO': fila[0],'ID_ACTIVIDAD': fila[1]}
            usuario_actividades.append(usuario_actividad)
        print(datos)
        return jsonify({'usuario_actividad': usuario_actividades ,'mensaje': 'usuario_actividad'})

    except Exception as ex:
        return jsonify({'mensaje': ex})
    
@app.route('/actividades', methods= ['GET'])
def listar_actividades():
    try:
        cursor =conexion.connection.cursor()
        sql = "SELECT * FROM ACTIVIDADES"
        cursor.execute(sql)
        datos= cursor.fetchall()
        actividades =[]
        for fila in datos:
            actividad={'ID_ACTIVIDAD': fila[0],'NOMBRE_ACTIVIDAD': fila[1],'TEXTO': fila[2],
                       'KM': fila[3],'FC': fila[4],'KCAL': fila[5],'DURACION': str(fila[6]),
                       'ID_EVENTO': fila[7],'NOMBRE_DEPORTE': fila[8]}
            actividades.append(actividad)
        print(datos)
        return jsonify({'actividad': actividades ,'mensaje': 'actividad'})

    except Exception as ex:
        return jsonify({'mensaje': ex})


                        
##REGISTROS

#eventos 

@app.route('/eventos', methods= ['POST']) 
def registrar_evento(): 
#print(request) 
    try: 
        cursor = conexion.connection.cursor() 
        sql = """INSERT INTO eventos 
        (ID_EVENTO, FECHA, HORA, PRECIO, LOCALIZACION, PLAZAS) 
        VALUES ('{0}','{1}','{2}','{3}','{4}','{5}') """.format(request.json ['evento'], 
        request.json['fecha'], 
        request.json['hora'], 
        request.json['precio'], 
        request.json['localizacion'], 
        request.json['plazas'] 
        ) 
        cursor. execute(sql) 
        conexion.connection.commit() 

        #confirma acción inserción
        #print(request.json) 

        return jsonify({'mensaje': 'evento registrado'}) 

    except Exception as ex: 
        return jsonify({'mensaje': "error"}) 
    

@app.route('/actividades', methods= ['POST'])
def registrar_actividad():
    #print(request)
    try:
        cursor = conexion.connection.cursor()

    # Define the SQL query with placeholders
        sql = """
            INSERT INTO actividades
            (ID_ACTIVIDAD, NOMBRE_ACTIVIDAD, TEXTO, KM, FC, KCAL, DURACION, ID_EVENTO, NOMBRE_DEPORTE)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Extract the values from request.json
        values = (
            request.json.get('ID_ACTIVIDAD'),
            request.json.get('NOMBRE_ACTIVIDAD'),
            request.json.get('TEXTO'),
            request.json.get('KM'),  # Will be None if not provided
            request.json.get('FC'),
            request.json.get('KCAL'),
            request.json.get('DURACION'),
            request.json.get('ID_EVENTO'),
            request.json.get('NOMBRE_DEPORTE')
        )

        # Execute the query with parameters
        cursor.execute(sql, values)
        conexion.connection.commit()

        # Confirm successful insertion
        return jsonify({'mensaje': 'actividad registrada'})

    except Exception as ex: 
        return jsonify({'mensaje': ex}) 

@app.route('/usuarioactividad', methods= ['POST'])
def registrar_usuarioactividad():
    #print(request)
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO usuarioactividad
        (ID_USUARIO,ID_ACTIVIDAD)
        VALUES ('{0}','{1}') """.format(request.json ['ID_USUARIO'],
        request.json['ID_ACTIVIDAD']
            )
     
        cursor. execute(sql)
        conexion.connection.commit()
#confirma acción inserción
    #print(request.json)
        return jsonify({'mensaje': 'actividad registrada'})
    except Exception as ex: 
        return jsonify({'mensaje': ex})    
@app.route('/nuevousuario', methods= ['POST'])
def registrar_usuario():
    #print(request)
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO usuarios
        (ID_USUARIO,NOMBRE_USUARIO,CORREO,CONTRASENA,FECHA_NAC,SEXO)
        VALUES ('{0}','{1}','{2}','{3}','{4}','{5}') """.format(request.json ['ID_USUARIO'],
        request.json['NOMBRE_USUARIO'],
        request.json['CORREO'],
        request.json['CONTRASENA'],
        request.json['FECHA_NAC'],
        request.json['SEXO']
            )
     
        cursor. execute(sql)
        conexion.connection.commit()
#confirma acción inserción
    #print(request.json)
        return jsonify({'mensaje': 'usuario registrado'})
    except Exception as ex: 
        return jsonify({'mensaje': ex})    




##lecturas
@app.route('/eventos/<codigo>', methods= ['GET'])
def leer_evento(codigo):
    try:
        cursor =conexion.connection.cursor()
        sql = "SELECT * FROM eventos WHERE ID_EVENTO = '{0}'".format(codigo)
        cursor.execute(sql)
        fila=cursor.fetchone()
        if fila != None:
            evento={'ID_EVENTO': fila[0],'FECHA': str(fila[1]),'HORA':str(fila[2]),
                      'PRECIO':fila[3],'LOCALIZACION': fila[4]}
            return jsonify({'ciudades': evento,'mensaje': 'ciudad encontrada'})
        else:
            return jsonify({'mensaje': 'ciudad no encontrada'})
    except Exception as ex:
        return jsonify({'mensaje': 'error'})
    

@app.route('/eventos/lugar/<codigo>', methods= ['GET'])
def leer_eventociudad(codigo):
    try:
        cursor =conexion.connection.cursor()
        sql = "SELECT * FROM eventos WHERE LOCALIZACION LIKE '%{0}'".format(codigo)
        cursor.execute(sql)
        datos=cursor.fetchall()
        eventos =[]
        if datos == None:
            return jsonify({'mensaje': 'ciudad no encontrada'})
        else: 
            eventos =[]
            for fila in datos:
                evento={'ID_EVENTO': fila[0],'FECHA': str(fila[1]),'HORA':str(fila[2]),
                        'PRECIO':fila[3],'LOCALIZACION': fila[4]}
                eventos.append(evento)
            print(eventos)
            return jsonify({'ciudades': eventos,'mensaje': 'ciudad encontrada'})
    except Exception as ex:
        return jsonify({'mensaje': 'error'})
    
    

@app.route('/ultimousuario', methods= ['GET'])
def ultimo_usuario():
    try:
        cursor =conexion.connection.cursor()
        sql = "SELECT ID_USUARIO FROM USUARIOS ORDER BY CAST(SUBSTR(ID_USUARIO,12,LENGTH(ID_USUARIO)-11) AS UNSIGNED)"
        cursor.execute(sql)
        datos= cursor.fetchall()
        fila =datos[-1]
        actividad={'ID_USUARIO': fila[0]}
        print(datos)
        return jsonify({'usuario': actividad ,'mensaje': 'usuario'})

    except Exception as ex:
        return jsonify({'mensaje': ex})
         


@app.route('/ultimaactividad', methods= ['GET'])
def ultima_actividad():
    try:
        cursor =conexion.connection.cursor()
        sql = "SELECT ID_ACTIVIDAD FROM ACTIVIDADES ORDER BY CAST(SUBSTR(ID_ACTIVIDAD,7,LENGTH(ID_ACTIVIDAD)-6) AS UNSIGNED)"
        cursor.execute(sql)
        datos= cursor.fetchall()
        actividades =[]
        fila =datos[-1]
        actividad={'ID_ACTIVIDAD': fila[0]}
        print(datos)
        return jsonify({'actividad': actividad ,'mensaje': 'actividad'})

    except Exception as ex:
        return jsonify({'mensaje': ex})

@app.route('/usuario_deportes/<usuariocotilleo>', methods=['GET'])
def listar_usuario_deportes(usuariocotilleo):
    try:
        cursor = conexion.connection.cursor()
        sql= """
        SELECT A.NOMBRE_DEPORTE, COUNT(*)
        FROM ACTIVIDADES A, USUARIOACTIVIDAD UA
        WHERE A.ID_ACTIVIDAD=UA.ID_ACTIVIDAD AND UA.ID_USUARIO= '{0}'
        GROUP BY A.NOMBRE_DEPORTE""".format(usuariocotilleo)
        
        
        # Ejecutar la consulta con el valor de id_usuario
        cursor.execute(sql)
        datos = cursor.fetchall()

        # Diccionario para guardar las actividades por usuario
        deportes_por_usuario = {}

        # Construir el diccionario con los datos obtenidos
        for fila in datos:
            deporte = fila[0]  # Nombre del deporte
            cantidad = fila[1]  # Número de veces que hizo el deporte
            deportes_por_usuario[deporte] = cantidad

        # Retornar el diccionario en formato JSON
        return jsonify({'deportes_por_usuario': deportes_por_usuario, 'mensaje': 'Actividades listadas correctamente'})
    
    except Exception as e:
        return jsonify({'mensaje': 'Error al listar actividades', 'error': str(e)})




@app.route('/usuarios/contrasena/<codigo>', methods= ['GET'])
def obtener_contrasena(codigo):
    try:
        cursor =conexion.connection.cursor()

        sql = "SELECT CONTRASENA FROM USUARIOS WHERE ID_USUARIO LIKE '%{0}'".format(codigo)
        cursor.execute(sql)
        fila=cursor.fetchone()
        if fila:
            return jsonify({'contrasena': fila[0]})
        else:
            return jsonify({'mensaje': 'Usuario no encontrado'})
    
    except Exception as ex:
        return jsonify({'mensaje': 'Error al obtener la contraseña', 'error': str(ex)})

@app.route('/usuarios/nombre_usuario/<codigo>', methods= ['GET'])
def obtener_nombre(codigo):
    try:
        cursor =conexion.connection.cursor()

        sql = "SELECT NOMBRE_USUARIO FROM USUARIOS WHERE ID_USUARIO LIKE '%{0}'".format(codigo)
        cursor.execute(sql)
        fila=cursor.fetchone()
        if fila:
            return jsonify({'nombre_usuario': fila[0]})
        else:
            return jsonify({'mensaje': 'Usuario no encontrado'})
    
    except Exception as ex:
        return jsonify({'mensaje': 'Error al obtener el usuario', 'error': str(ex)})


def pagina_no_encontrada(error):
    return "<h1> la pagina no existe </h1>", 404

if __name__=="__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()
