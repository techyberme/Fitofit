from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from config import config 
app = Flask(__name__)
conexion= MySQL(app)

##listar
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
        usuario =[]
        for fila in datos:
            usuario={'ID_USUARIO': fila[0],'NOMBRE_USUARIO': fila[1],'CORREO':str(fila[2]),
                      'CONTRASEÑA':fila[3],'FECHA_NAC': str(fila[4]),'SEXO':fila[5]}
            usuario.append(usuario)
        print(datos)
        return jsonify({'usuario': usuario ,'mensaje': 'usuarios listados'})

    except Exception as ex:
        return jsonify({'mensaje': ex})
                        
@app.route('/deportes', methods= ['GET'])
def listar_deportes():
    try:
        cursor =conexion.connection.cursor()
        sql = "SELECT * FROM deportes"
        cursor.execute(sql)
        datos= cursor.fetchall()
        deporte =[]
        for fila in datos:
            deporte={'NOMBRE_DEPORTE': fila[0],'TIPO_DEPORTE': fila[1],'EQUIPO':fila[2]}
            deporte.append(deporte)
        print(datos)
        return jsonify({'deporte': deporte ,'mensaje': 'deportes listados'})

    except Exception as ex:
        return jsonify({'mensaje': ex})
                        

@app.route('/usuario_actividad', methods= ['GET'])
def listar_usuario_actividad():
    try:
        cursor =conexion.connection.cursor()
        sql = "SELECT * FROM USUARIOACTIVIDAD"
        cursor.execute(sql)
        datos= cursor.fetchall()
        usuario_actividad =[]
        for fila in datos:
            usuario_actividad={'ID_USUARIO': fila[0],'ID_ACTIVIDAD': fila[1]}
            usuario_actividad.append(usuario_actividad)
        print(datos)
        return jsonify({'usuario_actividad': usuario_actividad ,'mensaje': 'usuario_actividad'})

    except Exception as ex:
        return jsonify({'mensaje': ex})
                        

#eventos
@app.route('/cursos', methods= ['POST'])
def registrar_evento():
    #print(request)
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO eventos
(ID_EVENTO, FECHA, HORA, PRECIO, LOCALIZACION,PLAZAS)
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
    

#usuarios
@app.route('/cursos', methods= ['POST'])
def registrar_usuario():
    #print(request)
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO usuarios
(ID_USUARIO, NOMBRE_USUARIO, CORREO, CONTRASEÑA, FECHA_NAC,SEXO)
VALUES ('{0}','{1}','{2}','{3}','{4}','{5}') """.format(request.json ['id del usuario'],
request.json['nombre de usuario'],

request.json['direccion de correo'],

request.json['contraseña'],

request.json['fecha nacimiento'],

request.json['sexo']
            
            )
        
        cursor. execute(sql)
        conexion.connection.commit()
#confirma acción inserción
    #print(request.json)
        return jsonify({'mensaje': 'usuario registrado'})
    except Exception as ex:
        return jsonify({'mensaje': "error"})


#deportes
@app.route('/cursos', methods= ['POST'])
def registrar_deporte():
    #print(request)
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO deportes
(NOMBRE_DEPORTE, TIPO_DEPORTE, EQUIPO)
VALUES ('{0}','{1}','{2}') """.format(request.json ['nombre del deporte'],
request.json['tipo de deporte'],

request.json['equipo']
            
            )
        
        cursor. execute(sql)
        conexion.connection.commit()
#confirma acción inserción
    #print(request.json)
        return jsonify({'mensaje': 'deporte registrado'})
    except Exception as ex:
        return jsonify({'mensaje': "error"})




#actividades
@app.route('/cursos', methods= ['POST'])
def registrar_actividad():
    #print(request)
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO actividades
(ID_ACTIVIDAD, NOMBRE_ACTIVIDAD, TEXTO, KM, FRECUENCIACARDIACA,KCAL, DURACION, ID_EVENTO,NOMBRE_DEPORTE)
VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}') """.format(request.json ['id de la actividad'],
request.json['nombre de la actividad'],

request.json['texto'],

request.json['km'],

request.json['frecuencia cardiaca'],

request.json['kcal'],
            
request.json['duracion'],

request.json['id del evento'],

request.json['nombre del deporte']
    
            )
        
        cursor. execute(sql)
        conexion.connection.commit()
#confirma acción inserción
    #print(request.json)
        return jsonify({'mensaje': 'actividad registrada'})
    except Exception as ex:
        return jsonify({'mensaje': "error"})
    

#eventousuario
@app.route('/cursos', methods= ['POST'])
def registrar_eventousuario():
    #print(request)
    try:
        cursor = conexion.connection.cursor()
        sql = """INSERT INTO eventousuario
(ID_EVENTO,ID_USUARIO)
VALUES ('{0}','{1}','{2}') """.format(request.json ['id del evento'],
request.json['id del usuario']
            
            )
        
        cursor. execute(sql)
        conexion.connection.commit()
#confirma acción inserción
    #print(request.json)
        return jsonify({'mensaje': 'eventousuario registrado'})
    except Exception as ex:
        return jsonify({'mensaje': "error"})



##leer
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
        fila=cursor.fetchone()
        if fila != None:
            evento={'ID_EVENTO': fila[0],'FECHA': str(fila[1]),'HORA':str(fila[2]),
                      'PRECIO':fila[3],'LOCALIZACION': fila[4]}
            return jsonify({'ciudades': evento,'mensaje': 'ciudad encontrada'})
        else:
            return jsonify({'mensaje': 'ciudad no encontrada'})
    except Exception as ex:
        return jsonify({'mensaje': 'error'})

 

def pagina_no_encontrada(error):
    return "<h1> la pagina no existe </h1>", 404

if __name__=="__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()