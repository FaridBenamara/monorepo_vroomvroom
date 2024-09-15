FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /dashboard

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers de l'application dans le conteneur
COPY . .

# Exposer le port 
EXPOSE 8501

# Définir la commande pour lancer l'application
CMD ["streamlit", "run", "dashboard_api.py", "--server.port=8501", "--server.address=0.0.0.0"]
