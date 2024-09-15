# Commit 1 : Initialisation du projet avec des fonctions vides

import streamlit as st
import requests
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dateutil import parser

# Initialisation des configurations de la page
st.set_page_config(page_title="Vehicle and Race Stats Management", layout="wide")

# URL de base de l'API
BASE_URL = 'http://localhost:5000'

# Fonctions pour les statistiques (vides pour l'instant)
def get_stats_every_5_seconds():
    pass

def get_all_vehicles():
    pass

def add_vehicle(name):
    pass

def get_all_races():
    pass

def add_race(vehicle_id, name):
    pass

# Point d'entrée principal de l'application
def main():
    pass

if __name__ == '__main__':
    main()
