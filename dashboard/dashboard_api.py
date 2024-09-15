import streamlit as st
import requests
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dateutil import parser

# Initialisation des configurations de la page
st.set_page_config(page_title="Vehicle and Race Stats Management", layout="wide")

# URL de base de l'API
BASE_URL = 'http://localhost:5000'

# Fonctions pour les statistiques (toujours vides)
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

# Code pour ajouter des styles CSS
st.markdown("""
    <style>
    .title {
        color: #FF6347;
        font-size: 36px;
        font-weight: bold;
    }
    .header {
        color: #4682B4;
        font-size: 24px;
        font-weight: bold;
    }
    .subheader {
        color: #20B2AA;
        font-size: 20px;
        font-weight: bold;
    }
    .section {
        margin-bottom: 30px;
    }
    .vehicle-container {
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        background-color: #f9f9f9;
    }
    .vehicle-item {
        margin-bottom: 10px;
        padding: 10px;
        border: 1px solid #eee;
        border-radius: 5px;
        background-color: #ffffff;
    }
    .graph-container {
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Point d'entrée principal de l'application
def main():
    # Placeholder for future code
    st.markdown('<div class="title">Vehicle and Race Stats Management</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
