import streamlit as st
import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import datetime
# Variables globales para almacenar información del usuario
usuario=""
name=""
#Ejemplo de programación orientada a objetos
class Evento:
 def __init__(self, id, fecha, hora, precio):
    self.id = id # Attribute
    self.fecha = fecha
    self.hora=hora
    self.precio=precio 
# Devuelve una descripción del evento como texto
 def info(self):
    return f"El evento {self.id} será el {self.fecha} a las {self.hora} y tiene un costo de {self.precio} €"
# Crear un menú en la barra lateral de Streamlit
with st.sidebar: 
    sesion = st.radio(" ",['Iniciar Sesión', 'Nuevo Usuario','Eliminar Cuenta'])  
    if sesion=='Iniciar Sesión':
        with st.form('Iniciar Sesión'):
            usuario=st.text_input("Usuario")
            contrasena=st.text_input("Contraseña",type="password") #La contraseña se escribe con asteriscos
            submitted = st.form_submit_button("Submit")  # Botón para enviar el formulario
            if submitted:                   
                    url="http://127.0.0.1:5000/usuarios/contrasena/"+usuario   #Comprobación de que la contraseña es correcta
                    try:
                        dato = requests.get(url).json()                         #obtención de datos del servidador
                        
                        x=list(dato.keys())
                        #si ha enviado un mensaje: usuario no encontrado, levanta flag de excepción
                        if x =='mensaje':                           
                            raise Exception()  
                        contra=dato["contrasena"]
                        if contra!=contrasena:
                                usuario=""
                                st.warning('Contraseña Incorrecta', icon="⚠️")    #muestra advertencia
                        else:
                                st.balloons()                                       #globos para indicar que se ha registrado bien
                                ##sacar nombre_usuario
                                url="http://127.0.0.1:5000/usuarios/nombre_usuario/"+ usuario
                                try:
                                    dato = requests.get(url).json()
                                    name=dato["nombre_usuario"]
                                    name=", "+name[0:name.index(" ")]               #se extrae el primer nombre dle usuario
                                    
                                except requests.exceptions.RequestException as e:
                                    st.write("")
                                
                    except requests.exceptions.RequestException as e:
                            st.write("")
                    except Exception as e:
                            usuario=""
                            st.warning('Usuario Incorrecto', icon="⚠️")            #advertencia si el usuario es incorrecto

                        
    bienvenida= 'Te damos la bienvenida a FitoFit' + name +'!'
    st.title(bienvenida)
    if sesion=='Nuevo Usuario': #formulario para crear nueva cuenta
        with st.form("Nueva Cuenta"):
            newname=st.text_input("Nombre")
            newcorreo=st.text_input("Correo")
            newcontrasena=st.text_input("Contraseña")
            min_date = datetime.date(1960, 1, 1)
            default_date = datetime.date(2002, 4, 5)
            newfecha = st.date_input("Tu año de nacimiento", default_date,min_date)
            newfecha=str(newfecha)                          #convierte la fecha a string para la comunicación con sql
            newsexo=st.selectbox(
            "Sexo",
            ("M", "F", "-"),
                )
            submitted = st.form_submit_button("Submit")
            if submitted: 
                url="http://127.0.0.1:5000/ultimousuario"
                try:
                    dato = requests.get(url).json()
                    id_usuario=dato["usuario"]["ID_USUARIO"]
                    id_usuario = int(id_usuario[11:]) 
                    id=id_usuario+1
                    id_usuario= f"id_usuario_{id}"
                except requests.exceptions.RequestException as e:
                    st.write("")
                st.balloons()
                # Crea un diccionario con la información del nuevo usuario
                dict1= {
                        "ID_USUARIO" : id_usuario,
                        "NOMBRE_USUARIO" : newname,
                        "CORREO": newcorreo,
                        "CONTRASENA": newcontrasena,
                        "FECHA_NAC": newfecha,
                        "SEXO": newsexo
                    }
                url="http://127.0.0.1:5000/nuevousuario"


                try:
                    # Sending POST request with data as JSON
                        response = requests.post(url, json=dict1)
                    
                    # Check if the request was successful
                        response.raise_for_status()  # Raises an error for 4xx/5xx HTTP status codes
                except requests.exceptions.RequestException as e:
                        st.error(f"An error occurred: {e}")
    if sesion=='Eliminar Cuenta':
         with st.form('Iniciar Sesión'):
            usuario=st.text_input("Usuario")
            contrasena=st.text_input("Contraseña",type="password")
            submitted = st.form_submit_button("Submit")
            if submitted:                   
                    url="http://127.0.0.1:5000/usuarios/contrasena/"+usuario
                    try:
                        dato = requests.get(url).json()
                        contra=dato["contrasena"]
                        x=list(dato.keys())
                        if x =='mensaje':                           
                            raise Exception()   
                        if contra!=contrasena:
                                usuario=""
                                st.warning('Contraseña Incorrecta, prueba de nuevo', icon="⚠️")
                        else:
                            url = "http://127.0.0.1:5000/eliminarusuario/" + usuario
                            try:
                                response = requests.delete(url)  # Send DELETE request
                                response.raise_for_status()  # Raise an error if the request fails (4xx or 5xx response codes)
                                st.write("¡Esperamos volver a verte pronto!")
                                usuario=""
                            except requests.exceptions.RequestException as e:
                                st.error(f"An error occurred: {e}")  # Handle errors

                            

                    except requests.exceptions.RequestException as e:
                            st.write("")
                    except Exception as e:
                            usuario=""
                            st.warning('Usuario Incorrecto', icon="⚠️")
                     
    st.info('Qué quieres hacer?')
    choice = st.radio('Menú', ['Tu actividad', 'Subir una actividad', 'Consultar un evento',"FitoFito","Encuentra Paisanos de tu edad","Subir actividades de mi reloj"])   
if choice == 'Tu actividad':
    ##si no se ha iniciado sesión, no se mostrará nada
    if usuario =="":
         st.write("## Primero, inicia sesión")
    if usuario !="":
        st.write("""
    ## ¡Aquí tienes tus estadísticas!

    """)
        col1, col2 = st.columns(2)
        with col1:
        
            url="http://127.0.0.1:5000/kcals/" + usuario
            try:
                    data = requests.get(url).json()
                    # Extraer etiquetas y valores del diccionario
                    etiquetas = list(data["kcal_por_deporte_por_usuario"].keys())
                    valores = list(data["kcal_por_deporte_por_usuario"].values())
                    print(valores)
                    print(etiquetas)
                    # Generar colores aleatorios en formato hexadecimal
                    colores = ['#%06X' % np.random.randint(0, 0xFFFFFF) for _ in range(len(data["kcal_por_deporte_por_usuario"]))]
                    fig, ax = plt.subplots(figsize=(6, 6))
                    ax.bar(etiquetas, valores,color=colores)
                    ax.set_title(f'Kcal promedio')
                    ax.set_xlabel('Deportes')
                    ax.set_ylabel('Kcal promedio')
                    
                    # Mostrar el gráfico en Streamlit
                    st.pyplot(fig)
            except requests.exceptions.RequestException as e:
                st.write("")
            #se crea el df
            df=pd.DataFrame(data=valores,index=etiquetas,columns=[''])
            print(df)
            #conversión a csv
            csv =df.to_csv().encode("utf-8")
            #opción para descargar
            st.download_button(
            label="Descárgate estos resultados",
            data=csv,
            file_name="results.csv",
            mime="text/csv",
                    )
        
        with col2:

            url="http://127.0.0.1:5000/eventos_mes/" + usuario
            try:
                    data = requests.get(url).json()
                    # Extraer etiquetas y valores del diccionario
                    etiquetas = list(data["eventos_mes_usuario"].keys())
                    valores = list(data["eventos_mes_usuario"].values())
                    print(valores)
                    print(etiquetas)
                    df=pd.DataFrame(data=valores,index=etiquetas,columns=[''])
                    print(df)
                    df.to_csv("results.csv")

                    # Generar colores aleatorios en formato hexadecimal
                    colores = ['#%06X' % np.random.randint(0, 0xFFFFFF) for _ in range(len(data["eventos_mes_usuario"]))]
                    fig, ax = plt.subplots(figsize=(6, 6))
                    ax.scatter(etiquetas, valores,color=colores,marker='*')
                    ax.set_title(f'Tu número de eventos en los últimos meses')
                    ax.set_xlabel('Mes')
                    ax.set_ylabel('Numero de eventos')
                    
                    # Mostrar el gráfico en Streamlit
                    st.pyplot(fig)
            except requests.exceptions.RequestException as e:
                st.write("")
     
if choice == 'Subir una actividad':
    if usuario =="":
         st.write("## Primero, inicia sesión")
    if usuario !="":
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
        except requests.exceptions.RequestException as e:
            st.write("")
        col1, col2 = st.columns(2)
        #botón para preguntar si ha sido parte de algún evento
        on = col2.toggle("¿Ha sido parte de algún evento?")
        if on:
                with col2:
                    #si hay, se introduce el id. Si no el evento es nulo
                    event=st.text_input("Nombre del Evento")
        else: 
            event = None
        with col1:
            #aquí, según el deporte el formulario cambia. Si es deporte de distancia se muestran kms.
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
                    km = None
                desc = st.text_input("Descripción")
                fc = st.text_input("FC")
                dur=st.text_input("duracion")
                
                if option in ["CARRERA", "CICLISMO"]:
                    km = st.text_input("KM")
                kcal = st.text_input("Kcal")

                
                submitted = st.form_submit_button("Submit")
                if submitted:
                    st.balloons()
                    
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
                        st.write("")
                    dict= {
                        "ID_ACTIVIDAD" : id_act,
                        "NOMBRE_ACTIVIDAD": nombre,
                        "TEXTO": desc,
                        "KM":km,
                        "FC": fc,
                        "KCAL": kcal,
                        "DURACION": dur,
                        "ID_EVENTO": event,
                        "NOMBRE_DEPORTE": deporte    
                        }
                    url="http://127.0.0.1:5000/actividades"


                    try:
                        # Sending POST request with data as JSON
                        response = requests.post(url, json=dict)
                        # Check if the request was successful
                        response.raise_for_status()  # Raises an error for 4xx/5xx HTTP status codes
                    except requests.exceptions.RequestException as e:
                        st.write("El deporte que has practicado todavía no está incluido en la app.")

                
                

if choice == 'Consultar un evento':
    col1, col2,col3 = st.columns(3)
    with col1:
        city= st.text_input("### dime dónde quieres el evento")
    url="http://127.0.0.1:5000/eventos/lugar/"+city
    try:
        data = requests.get(url).json()
        try:
            print(data["ciudades"][0])   ##lo hago para que salte la excepción antes de que se printee el titulo
            st.write("#### ¡Hemos encontrado los siguientes eventos en tu zona!")
            
            for i in range(len(data["ciudades"])):
                event = Evento(data["ciudades"][i]["ID_EVENTO"], data["ciudades"][i]["FECHA"],data["ciudades"][i]["HORA"],data["ciudades"][i]["PRECIO"])
                st.write(event.info())
        except Exception:
            st.write(f"#### No hemos encontrado eventos en {city}")
    except requests.exceptions.RequestException as e:
        st.write("")


##aquí tengo que hacer una consulta y devolveré un gráfico con las actividades del usuario,desglosado por deportes
if choice == 'FitoFito':
        id= st.text_input("### A quién quieres cotillear")
        #creación de la url
        url="http://127.0.0.1:5000/usuario_deportes/" + id
        try:
            data = requests.get(url).json()
            try:
                print(data["deportes_por_usuario"])   ##lo hago para que salte la excepción antes de que se printee el titulo
                st.write("#### ¡Hemos encontrado los siguientes eventos en tu zona!")
                etiquetas = list(data["deportes_por_usuario"].keys())
                valores = list(data["deportes_por_usuario"].values())

                # Generar colores aleatorios en formato hexadecimal
                colores = ['#%06X' % np.random.randint(0, 0xFFFFFF) for _ in range(len(data["deportes_por_usuario"]))]
                url="http://127.0.0.1:5000/usuarios/nombre_usuario/"+ id
                try:
                        dato = requests.get(url).json()
                        name=dato["nombre_usuario"]
                                
                except requests.exceptions.RequestException as e:
                        st.write("")
                # Crear gráfico de pastel
                fig, ax = plt.subplots(figsize=(6, 6))
                ax.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=colores)
                ax.set_title(f'Deportes realizados por {name}')

                # Mostrar el gráfico en Streamlit
                st.pyplot(fig)
             
            except Exception as e:
                st.write(f"#### El usuario {id} no existe")
            # Extraer etiquetas y valores del diccionario
            


        except requests.exceptions.RequestException as e:
            st.write("")

if choice == 'Encuentra Paisanos de tu edad':
    col1, col2,col3 = st.columns(3)
    with col1:
        city= st.text_input("### dime dónde quieres las actividades")
    with col2:
        edad= st.text_input("### dime de qué edad buscas gente")
    url="http://127.0.0.1:5000/todos/"+city+"/"+edad
    try:
        data = requests.get(url).json()
        try:
            print(data["ciudades"][0])   ##lo hago para que salte la excepción antes de que se printee el titulo
            st.write("#### ¡Hemos encontrado las siguientes actividades en tu zona y con tu edad!")           
            for i in range(len(data["ciudades"])):
                st.write("La actividad en ",data["ciudades"][i]["LOCALIZACION"], "hecha por  ",data["ciudades"][i]["NOMBRE_USUARIO"],"con ",data["ciudades"][i]["EDAD"],",del deporte",data["ciudades"][i]["NOMBRE_DEPORTE"])
        except Exception:
            st.write(f"#### No hemos encontrado personas de tu edad que sean fitofitters en {city}:-1:")
    except requests.exceptions.RequestException as e:
        st.write("")

if choice== "Subir actividades de mi reloj":
    if usuario =="":
         st.write("## Primero, inicia sesión")
    if usuario !="":
        st.write("""
    ## ¡Aquí puedes subir actividades realizadas con el reloj!

    """)
        actividades = st.file_uploader("Súbelas aquí", type={"csv"})
        if actividades is not None:
            st.balloons()
            #leer el archivo csv y pasarlo a dv
            actividades_df = pd.read_csv(actividades)
            listas=[]
            #ahora se crean las listas para ir incluyendo los diferentes eventos en el csv
            for i in range(len(actividades_df)):
                lista = []
                for x in actividades_df.iloc[i]:
                    #modificación de valores si en función del tipo de los valores
                    if pd.isna(x):
                        lista.append(None)
                    elif isinstance(x, (np.int64)):  
                        lista.append(int(x))  # lo tengo que hacer así porque se me añadían como np.int64
                    else:
                        lista.append(x)                  
                url="http://127.0.0.1:5000/ultimaactividad"
                try:
                    dato = requests.get(url).json()
                    id_act=dato["actividad"]["ID_ACTIVIDAD"]
                    id_act = int(id_act[(id_act.index('t') + 1):]) # Start just after 't'
                    id=id_act+1
                    id_act= f"id_act{id}"
                    print(id_act)
                except requests.exceptions.RequestException as e:
                    st.write("")
                ##añado nueva act del usuario
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
                        st.write("")
                dict={}
                dict= {
                        "ID_ACTIVIDAD" : id_act,
                        "NOMBRE_ACTIVIDAD": lista[0],
                        "TEXTO": lista[1],
                        "KM":lista[2],
                        "FC": lista[3],
                        "KCAL": lista[4],
                        "DURACION": lista[5],
                        "ID_EVENTO": lista[6],
                        "NOMBRE_DEPORTE": lista[7]    
                        }
                url="http://127.0.0.1:5000/actividades"


                try:
                            # Sending POST request with data as JSON
                            response = requests.post(url, json=dict)
                            # Check if the request was successful
                            response.raise_for_status()  # Raises an error for 4xx/5xx HTTP status codes
                except requests.exceptions.RequestException as e:
                            st.write("El deporte que has practicado todavía no está incluido en la app.")
                            print(dict)

     



