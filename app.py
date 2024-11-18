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
