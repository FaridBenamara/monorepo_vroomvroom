# Monorepo vroomvroom

Bienvenue dans le monorepo **vroomvroom** ! Ce projet contient plusieurs composants pour gérer les données relatives aux véhicules, aux courses et aux capteurs, ainsi que pour visualiser ces données en temps réel.

## Structure du Monorepo

Voici la structure des dossiers dans le monorepo :

- **api**: Contient l'API construite avec Flask, qui gère les données des véhicules, des courses et des capteurs.
  - **Chemin d'accès** : `/api`
  
- **dashboard**: Interface utilisateurd'un controle  d'intéraction avec l'api et de data visualisation 
  - **Chemin d'accès** : `/dashboard`
  
- **Database**: Scripts et configurations pour la base de données PostgreSQL utilisée par l'API.
  - **Chemin d'accès** : `/Database`
  
- **Frontend_Web**: Comprend le tableau de bord développé avec Nuxt.js et Vue.js pour visualiser les données de course en temps réel.
  - **Chemin d'accès** : `/Frontend_Web`
  
- **projet**: Dossier pour les fichiers de configuration et les scripts de gestion du projet.
  - **Chemin d'accès** : `/projet`
  
- **RabbitMQ**: Configuration et scripts pour la gestion des messages avec RabbitMQ.
  - **Chemin d'accès** : `/RabbitMQ`

  - **detection_ai**: Model YOLO pour la reconnaissance d'objet en video flux temps reel.
  - **Chemin d'accès** : `/detection_ai`

## Technologies Utilisées

- **Flask**: Framework pour construire l'API.
- **PostgreSQL**: Base de données pour stocker les données de l'application.
- **Nuxt.js**: Framework pour le rendu côté serveur et la génération de sites statiques.
- **Vue.js**: Framework JavaScript pour construire l'interface utilisateur.
- **Chart.js**: Bibliothèque pour créer des graphiques interactifs.
- **RabbitMQ**: Système de gestion de messages pour la communication entre les services.

## Installation et Lancement

### Prérequis

Assurez-vous d'avoir installé les éléments suivants :

- [Docker](https://www.docker.com/)
- [Node.js](https://nodejs.org/) pour le frontend
- [Python](https://www.python.org/) pour l'API

### Installation

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/FaridBenamara/monorepo_vroomvroom.git
   cd monorepo_vroomvroom