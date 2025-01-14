# Utiliser une image Python légère comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers locaux dans l'image Docker
COPY . /app

# Installer les dépendances
RUN pip install flask

# Exposer le port utilisé par l'application Flask
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "app.py"]
