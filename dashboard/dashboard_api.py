import streamlit as st
import requests
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dateutil import parser

# Configuration de la page
st.set_page_config(page_title="Vehicle and Race Stats Management", layout="wide")

# URL de base de l'API Flask
BASE_URL = 'http://localhost:5000'


# Fonction pour obtenir les statistiques toutes les 5 secondes
def get_stats_every_5_seconds():
    response = requests.get(f'{BASE_URL}/stats_every_5_seconds')
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.json()['message']}")
        return None


# Fonction pour obtenir tous les véhicules
def get_all_vehicles():
    response = requests.get(f'{BASE_URL}/vehicles')
    if response.status_code == 200:
        return response.json()['data']
    else:
        st.error(f"Error: {response.json()['message']}")
        return []


# Fonction pour ajouter un véhicule
def add_vehicle(name):
    response = requests.post(f'{BASE_URL}/vehicle', json={'name': name})
    if response.status_code == 201:
        st.success("Vehicle successfully added!")
    else:
        st.error(f"Error: {response.json()['message']}")


# Fonction pour obtenir toutes les courses
def get_all_races():
    response = requests.get(f'{BASE_URL}/races')
    if response.status_code == 200:
        return response.json()['data']
    else:
        st.error(f"Error: {response.json()['message']}")
        return []


# Fonction pour ajouter une course
def add_race(vehicle_id, name):
    response = requests.post(f'{BASE_URL}/race', json={'vehicle_id': vehicle_id, 'name': name})
    if response.status_code == 201:
        st.success("Race successfully added!")
    else:
        st.error(f"Error: {response.json()['message']}")


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


# Page principale de l'application
def main():
    st.markdown('<div class="title">Vehicle and Race Stats Management</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        # Section pour ajouter un véhicule
        st.markdown('<div class="header">Add a Vehicle</div>', unsafe_allow_html=True)
        vehicle_name = st.text_input("Vehicle Name", "")
        if st.button("Add Vehicle"):
            if vehicle_name:
                add_vehicle(vehicle_name)
                vehicle_name = ""  # Réinitialiser le champ après ajout
            else:
                st.error("Vehicle name is required!")

        # Section pour voir tous les véhicules
        st.markdown('<div class="header">Available Vehicles</div>', unsafe_allow_html=True)
        vehicles = get_all_vehicles()
        if vehicles:
            st.write("Here are the available vehicles:")
            for vehicle in vehicles:
                st.markdown(f"""
                    <div class="vehicle-item">
                        <strong>ID:</strong> {vehicle['id']} - <strong>Name:</strong> {vehicle['name']}
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.write("No vehicles available.")

        # Section pour ajouter une course
        st.markdown('<div class="header">Add a Race</div>', unsafe_allow_html=True)
        vehicle_ids = [vehicle['id'] for vehicle in vehicles]
        selected_vehicle_id = st.selectbox("Select Vehicle", options=vehicle_ids)
        race_name = st.text_input("Race Name", "")
        if st.button("Add Race"):
            if race_name and selected_vehicle_id:
                add_race(selected_vehicle_id, race_name)
                race_name = ""  # Réinitialiser le champ après ajout
            else:
                st.error("Race name and vehicle ID are required!")

        # Section pour voir toutes les courses
        st.markdown('<div class="header">Available Races</div>', unsafe_allow_html=True)
        races = get_all_races()
        if races:
            st.write("Here are the available races:")
            for race in races:
                st.markdown(f"""
                    <div class="vehicle-item">
                        <strong>ID:</strong> {race['id']} - <strong>Vehicle ID:</strong> {race['vehicle_id']} - <strong>Name:</strong> {race['name']}
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.write("No races available.")

    with col2:
        # Section pour les statistiques
        st.markdown('<div class="header">Race Statistics</div>', unsafe_allow_html=True)
        stats = get_stats_every_5_seconds()

        if stats:
            # Organiser les données par race_id
            organized_stats = {}
            for entry in stats:
                race_id = entry['race_id']
                if race_id not in organized_stats:
                    organized_stats[race_id] = []
                organized_stats[race_id].append(entry)

            for race_id, data in organized_stats.items():
                # Extraire les données pour le graphique
                dates = [parser.parse(stat['date']) for stat in data]
                distances = [stat['distance'] for stat in data]
                speeds = [stat['speed'] for stat in data]
                batteries = [stat['battery'] for stat in data]

                # Créer un subplot pour chaque race_id
                fig = make_subplots(rows=3, cols=1, shared_xaxes=True,
                                    subplot_titles=(f"Speed - Race {race_id}",
                                                    f"Distance - Race {race_id}",
                                                    f"Battery - Race {race_id}"),
                                    vertical_spacing=0.1)

                # Graphique de la vitesse
                fig.add_trace(go.Scatter(
                    x=dates,
                    y=speeds,
                    mode='lines+markers',
                    name='Speed',
                    line=dict(color='blue')
                ), row=1, col=1)

                # Graphique de la distance
                fig.add_trace(go.Scatter(
                    x=dates,
                    y=distances,
                    mode='lines+markers',
                    name='Distance',
                    line=dict(color='red')
                ), row=2, col=1)

                # Graphique de la batterie
                fig.add_trace(go.Scatter(
                    x=dates,
                    y=batteries,
                    mode='lines+markers',
                    name='Battery',
                    line=dict(color='green')
                ), row=3, col=1)

                # Mise en forme du graphique
                fig.update_layout(
                    title=f'Race ID {race_id} - Stats toutes les 5 secondes',
                    xaxis_title='Date',
                    yaxis_title='Value',
                    xaxis=dict(type='date'),
                    height=800
                )

                st.markdown('<div class="graph-container">', unsafe_allow_html=True)
                st.plotly_chart(fig, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)


if __name__ == '__main__':
    main()