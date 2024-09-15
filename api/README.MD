# API vroomvroom_backend

Cette API permet de gérer les données relatives aux véhicules, aux courses et aux données de capteurs du projet vroomvroom. Elle est construite avec Flask et utilise une base de données PostgreSQL, ainsi qu'un client MQTT pour la gestion des données en temps réel.

## Routes de l'API

### Véhicules

- **Ajouter un Véhicule**
  - **POST** `/vehicle`
  - **Corps de la Requête**: 
    ```json
    {
      "name": "Nom du véhicule"
    }
    ```

- **Obtenir un Véhicule par ID**
  - **GET** `/vehicle/<id>`

- **Obtenir tous les Véhicules**
  - **GET** `/vehicles`

- **Supprimer un Véhicule par ID**
  - **DELETE** `/vehicle/<id>`

- **Mettre à jour un Véhicule par ID**
  - **PUT** `/vehicle/<id>`
  - **Corps de la Requête**: 
    ```json
    {
      "name": "Nouveau nom du véhicule"
    }
    ```

### Courses

- **Ajouter une Course**
  - **POST** `/race`
  - **Corps de la Requête**: 
    ```json
    {
      "vehicle_id": "ID du véhicule",
      "name": "Nom de la course"
    }
    ```

- **Obtenir une Course par ID**
  - **GET** `/race/<id>`

- **Supprimer une Course par ID**
  - **DELETE** `/race/<id>`

- **Mettre à jour une Course par ID**
  - **PUT** `/race/<id>`
  - **Corps de la Requête**: 
    ```json
    {
      "name": "Nouveau nom de la course"
    }
    ```

- **Obtenir toutes les Courses**
  - **GET** `/races`

### Statistiques des Courses

- **Obtenir des Statistiques par ID de Course**
  - **GET** `/stats_race?race_id=<race_id>`

- **Supprimer des Statistiques par ID**
  - **DELETE** `/stats_race/<id>`

- **Mettre à jour des Statistiques par ID**
  - **PUT** `/stats_race/<id>`
  - **Corps de la Requête**: 
    ```json
    {
      "distance": "Distance",
      "speed_max": "Vitesse maximale",
      "speed_average": "Vitesse moyenne",
      "battery_max": "Batterie maximale",
      "battery_min": "Batterie minimale",
      "time": "Temps",
      "date": "Date"
    }
    ```

- **Obtenir toutes les Statistiques de Course**
  - **GET** `/get_stats_races`

### Données du Broker MQTT

- **Obtenir les Données du Broker**
  - **GET** `/get_broker_data`

### Statistiques toutes les 5 secondes

- **Obtenir des Statistiques de la cousr par tranches de 5 secondes**
  - **GET** `/stats_every_5_seconds`

## Pour lancer

1. **Cloner le dépôt :**
    ```bash
    git clone 
    cd api
    ```

2. **Construire l'image Docker :**
    ```bash
    docker build -t vroomvroom_backend .
    ```

3. **Exécuter le conteneur :**
    ```bash
    docker run -p 5000:5000 vroomvroom_backend
    ```

## Remarques

Assurez-vous que PostgreSQL et le Broker MQTT sont configurés et opérationnels avant de lancer l'API.