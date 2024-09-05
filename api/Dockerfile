# Utiliser l'image officielle de Python comme image de base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app/ ./app
COPY run.py .

# Exposer le port sur lequel l'application tourne
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "run.py"]