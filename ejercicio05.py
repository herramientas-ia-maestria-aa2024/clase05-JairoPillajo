#!pip install requests
#iPython ejercicio05.py

import requests
import pandas as pd

data = pd.read_csv('frases.csv', header=None)

numero=0
for index, row in data.iterrows():
    frase=row[0]
    url=f"http://127.0.0.1:8080/prediccion/{frase}"
    response = requests.get(url)
    #print(response.json())
    prediction = response.json()['prediction']
    numero += 1
    print(numero,f" Frase: {frase} - Predicción resultante: {prediction}")
