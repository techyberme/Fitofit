import streamlit as st
import pandas as pd
import requests
import csv
import time
from streamlit_calendar import calendar

with st.sidebar:
     st.title('Bienvenido a FitoFit!')
     st.info('Qué quieres hacer?')
     choice = st.radio('Menú', ['Consultar una carrera', 'Subir una actividad', 'Consultar un evento',"FitoFito"])
if choice == 'Consultar una carrera':
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
                ('Carrera', 'Ciclismo', 'Otro'),
            )
        with st.form("my_form"):
            # User selects the type of sport
            
            nombre = st.text_input("Nombre de la actividad")      
            if option == "Otro":        
             deporte = st.text_input("Deporte")
            desc = st.text_input("Descripción")
            fc = st.text_input("FC")
            km = None
            if option in ["Carrera", "Ciclismo"]:
                km = st.text_input("KM")
            else:
                km = "NULL"
            
            kcal = st.text_input("Kcal")
            
            
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.balloons()

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
if choice == 'FitoFito':
    st.write("¿A quién quieres cotillear?")