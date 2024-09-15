# Dashboard des Données de Course

Un tableau de bord pour visualiser les données de course en temps réel, développé avec Nuxt.js, Vue.js et Chart.js. Il récupère et affiche les statistiques de la voiture .

## Fonctionnalités

- Affichage en temps réel de la vitesse, la distance, le niveau de batterie et la durée des courses.
- Visualisation des historiques de course sous forme de graphiques interactifs.
- Récupération des données depuis les API.

## Technologies

- **Nuxt.js** 
- **Vue.js** 
- **Chart.js**
- **Node.js**
- **Websocket**
## Installation et Configuration

1. Clonez ce dépôt :

    ```bash
    git clone link
    ```

2. Installez les dépendances :

    ```bash
    cd Frontend_Web\VroomVroom_front
    npm install
    ```

3. Lancez le serveur Nuxt :

    ```bash
    npm run dev
    ```
4. Lancez le serveur WebSocket :

    ```bash
    node server/server.js
    ```
5. Ouvrez votre navigateur à l'adresse : [http://localhost:3000](http://localhost:3000)