# Vehicle and Race Stats Management

Panneau de controle et de data viz fait avec streamlit pour le projet vroomvroom

## Fonctionnalités

- Ajout de véhicules et de courses via une interface utilisateur.
- Visualisation des statistiques de course, y compris la vitesse, la distance et l'état de la batterie.
- Récupération et affichage des données en temps réel à partir d'une API.

## Prérequis

- [Docker](https://docs.docker.com/get-docker/) (si vous souhaitez utiliser Docker)
- [Python 3.7+](https://www.python.org/downloads/) (si vous souhaitez exécuter l'application localement)

## Installation

### Option 1: Utiliser Docker

1. Clonez le dépôt :

    ```bash
    git clone 
    cd dashboard
    ```

2. Construisez l'image Docker :

    ```bash
    docker build -t streamlit-app .
    ```

3. Lancez le conteneur :

    ```bash
    docker run -p 8501:8501 streamlit-app
    ```

4. Accédez à l'application via `http://localhost:8501` dans votre navigateur.

### Option 2: Exécuter localement

1. Clonez le dépôt :

    ```bash
    git clone 
    cd dashboard
    ```

2. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

3. Lancez l'application :

    ```bash
    streamlit run dashboard_api.py
    ```

4. Accédez à l'application via `http://localhost:8501` dans votre navigateur.

## Tests

Des tests unitaires sont disponibles pour les fonctions d'API. Pour exécuter les tests :

```bash
python -m unittest __test__.py
