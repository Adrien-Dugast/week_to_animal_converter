import streamlit as st
import datetime
import random
import pandas as pd
import os

st.title("Panda calculator")
st.text('''Vos amis vous demandent tout le temps quel genre de panda vous êtes ? Gros panda ? Bébé panda ? Fiat panda ? Difficile à dire. Mais aussi difficile pour vous d'aller calculer le nombre de jour, convertir en semaine, avoir une idée clair du poids d'un panda adulte... Beaucoup de complications. \n Mais aujourd'hui tout devient plus simple ! Avec Panda calculator, rentrez la date de votre dernier... panda tué... et laissez l'IA calculer pour vous ! Grace à mon nouveau moteur LLM agent 780 millions de paramètre, profitez d'une estimation rapide, sur vendez_votre_voiture.fr euhh non une estimation rapide de votre panda !''')


df = pd.read_csv('animals_preprocessed.csv')

def days_between(d1, d2) -> int:
    # Convert both to date objects if they're datetime
    if isinstance(d1, datetime.datetime):
        d1 = d1.date()
    if isinstance(d2, datetime.datetime):
        d2 = d2.date()

    # Return the absolute difference in days
    return abs((d2 - d1).days)/7

def find_random_animal(df,weight):
    weight = float(weight)
    df_ok = df[(df['weight_min']<weight)&(df['weight_max']>weight)]
    list_animaux = df_ok['Animal'].tolist()
    if len(list_animaux)!=0:
        animal = random.choice(list_animaux)
        return(df[df['Animal']==animal])
    else:
        return(False)

d = st.date_input(' Entrez ici la date de votre dernier... "meutre de panda"')
weeks_diff = days_between(d, datetime.datetime.today())
st.write("Nombre de semaine depuis la dernière fois : ", weeks_diff)
animal_chosen = find_random_animal(df,weeks_diff)

if type(animal_chosen) == bool:
    st.write("Aucun animal n'a été trouvé. Bizarre !")
else:
    animal_name = animal_chosen['Animal'].values[0]
    st.write("You are a " + animal_name)
    st.image(f"Animals_picture_bing/{animal_name}.jpg")