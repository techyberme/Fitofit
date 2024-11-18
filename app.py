from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from config import config 
app = Flask(__name__)
conexion= MySQL(app)
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
