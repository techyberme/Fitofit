import streamlit as st
import pandas as pd
import requests
import csv
import time
usuario="id_usuario_1"
with st.sidebar:
     nombre=""
     bienvenida= 'Bienvenido a FitoFit!' + nombre
     st.title(bienvenida)
     st.info('Qué quieres hacer?')
     choice = st.radio('Menú', ['Iniciar sesión','Tu actividad', 'Subir una actividad', 'Consultar un evento',"FitoFito","Crear un Evento"])
if choice == 'Iniciar sesión':
    with st.form('Iniciar Sesión'):
        usuario=st.text_input("Usuario")
        contrasena=st.text_input("Contraseña")
        submitted = st.form_submit_button("Submit")
        if submitted:
                
                url="http://127.0.0.1:5000/usuarios/contrasena/"+usuario
                try:
                    dato = requests.get(url).json()
                    contra=dato["contrasena"]
                    
                    if contra!=contrasena:
                        usuario=0
                        st.warning('Contraseña Incorrecta', icon="⚠️")
                    else:
                        st.balloons()

                except requests.exceptions.RequestException as e:
                    st.write("")

                ##sacar nombre_usuario
                url="http://127.0.0.1:5000/usuarios/nombre_usuario/"+ usuario
                try:
                    dato = requests.get(url).json()
                    nombre=dato["nombre_usuario"]
                    with st.sidebar:
                            bienvenida= 'Te damos la bienvenida a FitoFit,' + nombre +'!'
                            st.title(bienvenida)
                except requests.exceptions.RequestException as e:
                    st.write("")

    
if choice == 'Tu actividad':
     st.write("Input Carrera")
     st.title('Gráfica de precios')
     
if choice == 'Subir una actividad':
    st.write("""
## ¡¿Qué has hecho hoy?!

""")
    url="http://127.0.0.1:5000/ultimaactividad"
    try:
        dato = requests.get(url).json()
        id_act=dato["actividad"]["ID_ACTIVIDAD"]
        id_act = int(id_act[(id_act.index('t') + 1):]) # Start just after 't'
        id=id_act+1
        id_act= f"id_act{id}"
        st.write(id_act)
    except requests.exceptions.RequestException as e:
        st.write("")
    col1, col2 = st.columns(2)
    on = col2.toggle("¿Ha sido parte de algún evento?")
    if on:
            with col2:
                event=st.text_input("Nombre del Evento")
    with col1:
        option = st.selectbox(
                "Deporte",
                ('CARRERA', 'CICLISMO', 'Otro'),
            )
        with st.form("my_form"):
            # User selects the type of sport
            nombre = st.text_input("Nombre de la actividad")
            deporte= option      
            if option == "Otro":        
             deporte = st.text_input("Deporte")
            desc = st.text_input("Descripción")
            fc = st.text_input("FC")
            dur=st.text_input("duracion")
            km = None
            if option in ["CARRERA", "CICLISMO"]:
                km = st.text_input("KM")
            else:
                km = "NULL"
            
            kcal = st.text_input("Kcal")

            
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.balloons()
                dict= {
                    "ID_ACTIVIDAD" : id_act,
                    "NOMBRE_ACTIVIDAD": nombre,
                    "TEXTO": desc,
                    "KM":km,
                    "FC": fc,
                    "KCAL": kcal,
                    "DURACION": dur,
                    "ID_EVENTO": "EV_001",
                    "NOMBRE_DEPORTE": deporte    
                    }
                url="http://127.0.0.1:5000/actividades"


                try:
                    # Sending POST request with data as JSON
                    response = requests.post(url, json=dict)
                    
                    # Check if the request was successful
                    response.raise_for_status()  # Raises an error for 4xx/5xx HTTP status codes
                except requests.exceptions.RequestException as e:
                    st.error(f"An error occurred: {e}")

                
                ##mirar esto
                dict1= {
                    "ID_USUARIO" : usuario,
                    "ID_ACTIVIDAD" : id_act  
                }
                url="http://127.0.0.1:5000/usuarioactividad"


                try:
                # Sending POST request with data as JSON
                    response = requests.post(url, json=dict1)
                
                # Check if the request was successful
                    response.raise_for_status()  # Raises an error for 4xx/5xx HTTP status codes
                except requests.exceptions.RequestException as e:
                    st.error(f"An error occurred: {e}")
            
                
           

            


if choice == 'Consultar un evento':
    col1, col2,col3 = st.columns(3)
    with col1:
        city= st.text_input("### dime dónde quieres el evento")
    url="http://127.0.0.1:5000/eventos/lugar/"+city
    try:
        data = requests.get(url).json()
        st.write("#### ¡Hemos encontrado los siguientes eventos en tu zona!")
        st.write("#### El evento",data["ciudades"]["ID_EVENTO"], "será el ",data["ciudades"]["FECHA"],"a las",data["ciudades"]["HORA"],"y tiene un costo de",data["ciudades"]["PRECIO"],"€")
    except requests.exceptions.RequestException as e:
        st.write("")


##aquí tengo que hacer una consulta y devolveré un gráfico con las actividades del usuario,desglosado por deportes
if choice == 'FitoFito':
    st.write("## ¿A quién quieres cotillear?")
    usuariocotilleo=st.text_input("Introduce el Id del Usuario")
    url="http://127.0.0.1:5000/eventos/usuarios/"+usuariocotilleo
    try:
        data = requests.get(url).json()
        st.write("#### Aquí tienes un resuman de la actividad de",data["usuarios"]["nombre_usuario"])
    except requests.exceptions.RequestException as e:
        st.write("")

if choice == 'Crear un evento':
    st.write("Aquí puedes crear tu propio evento!")
    col1, col2 = st.columns(2)
    with col1:
        with st.form("my_form"):
            # User selects the type of sport
            nombre= st.text_input("Nombre del evento")   
            deporte = st.text_input("Deporte")
            desc = st.text_input("Descripción")
            loc = st.text_input("Localización")
            hora= st.text_input("hour")
            plazas=st.text_input("plazas")
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.balloons()
                st.write("Evento Registrado")
f choice == 'FitoFito':
    col1, col2,col3 = st.columns(3)
    with col1:
        st.write("## ¿A quién quieres cotillear?")
        usuariocotilleo=st.text_input("Introduce el Id del Usuario")
       url="http://127.0.0.1:5000/eventos/usuarios/"+usuariocotilleo
    try:
        data = requests.get(url).json()
        cursor = conexion.connection.cursor()
        sql= """
        SELECT A.NOMBRE_DEPORTE, COUNT(*)
        FROM ACTIVIDADES A, USUARIOACTIVIDAD UA
        WHERE A.ID_ACTIVIDAD=UA.ID_ACTIVIDAD AND UA.ID_USUARIO= '{0}'".format(usuariocotilleo)
        GROUP BY A.NOMBRE_DEPORTE;
        """
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
        # Extraer etiquetas y valores del diccionario
       # Extraer etiquetas y valores del diccionario
        etiquetas = list(deportes_por_usuario.keys())
        valores = list(deportes_por_usuario.values())

        # Generar colores aleatorios en formato hexadecimal
        colores = ['#%06X' % np.random.randint(0, 0xFFFFFF) for _ in range(len(diccionario))]

        # Crear gráfico de pastel
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=colores)
        ax.set_title('Deportes realizados por el usuario')

# Mostrar el gráfico en Streamlit
        st.pyplot(fig)
    except requests.exceptions.RequestException as e:
        st.write("")
        
