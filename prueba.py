import streamlit as st
import pandas as pd
import requests
import csv
import time
with st.sidebar:
     st.title('Bienvenido a FitoFit!')
     st.info('Qué quieres hacer?')
     choice = st.radio('Menú', ['Iniciar sesión','Tu actividad', 'Subir una actividad', 'Consultar un evento',"FitoFito","Crear un Evento"])
if choice == 'Iniciar sesión':
    with st.form('Iniciar Sesión'):
        usuario=st.text_input("Usuario")
        contrasena=st.text_input("Contraseña")
        submitted = st.form_submit_button("Submit")
if choice == 'Tu actividad':
     st.write("Input Carrera")
     st.title('Gráfica de precios')
     
if choice == 'Subir una actividad':
    st.write("""
## ¡¿Qué has hecho hoy?!

""")
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
            id_act= st.text_input("id la actividad")
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
                
                # Print the response from the server
                st.write("Response:", response.json())
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
        
