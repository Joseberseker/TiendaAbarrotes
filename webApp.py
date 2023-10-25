import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.tree import DecisionTreeClassifier

st.header("Proyecto final Predicción usando Arbol de Clasificación")


product = st.selectbox("Elija un producto del stock",
('Salchicha', 'Mermelada', 'Chorizo', 'Sardinas', 'Sal', 'Arroz', 'Atún', 'Cereal', 'Papa', 'Avena', 'Margarina', 'Queso', 'Jamón', 'Yogur',
 'Tocino', 'Gelatina', 'Frijoles', 'Harina', 'Pasta', 'Café', 'Mantequilla', 'Leche entera', 'Vinagre', 'Miel', 'Vino', 'Mortadela', 'Huevo',
 'Salsa de tomate', 'Aceitunas', 'Mayonesa', 'Azúcar', 'Cacahuate'))


if (product == 'Salchicha'):
    product = 0
if (product == 'Mermelada'):
    product = 1
if (product == 'Chorizo'):
    product = 2
if (product == 'Sardinas'):
    product = 3
if (product == 'Sal'):
    product = 4
if (product == 'Arroz'):
    product = 5
if (product == 'Atún'):
    product = 6
if (product == 'Cereal'):
    product = 7
if (product == 'Papa'):
    product = 8
if (product == 'Avena'):
    product = 9
if (product == 'Margarina'):
    product = 10
if (product == 'Queso'):
    product = 11
if (product == 'Jamón'):
    product = 12
if (product == 'Yogur'):
    product = 13
if (product == 'Tocino'):
    product = 14
if (product == 'Gelatina'):
    product = 15
if (product == 'Frijoles'):
    product = 16
if (product == 'Harina'):
    product = 17
if (product == 'Pasta'):
    product = 18
if (product == 'Café'):
    product = 19
if (product == 'Mantequilla'):
    product = 20
if (product == 'Leche entera'):
    product = 21
if (product == 'Vinagre'):
    product = 22
if (product == 'Miel'):
    product = 23
if (product == 'Vino'):
    product = 24
if (product == 'Mortadela'):
    product = 25
if (product == 'Huevo'):
    product = 26
if (product == 'Salsa de Tomate'):
    product = 27
if (product == 'Aceitunas'):
    product = 28
if (product == 'Mayonesa'):
    product = 29
if (product == 'Azúcar'):
    product = 30
if (product == 'Cacahuate'):
    product = 31

unit_price = st.number_input("Digite el precio unitario del producto")

quantity = st.number_input("Ingrese la cantidad del producto a vender")

total = unit_price*quantity




if st.button("Submit"):
    
    model = joblib.load("model.pkl")

    prediction = model.predict([[product, unit_price, quantity,total]])

    if prediction[0] == 0:
        resultado = "Less"

    elif prediction[0] == 1:
        resultado = "More"
       
    elif prediction[0] == 2:
        resultado = "Normal"
       
    st.text(f"Usted debe comprar : {resultado}")

