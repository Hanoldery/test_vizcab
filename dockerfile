# Utilise une image Python officielle comme parent
FROM python:3.9

# Définit le répertoire de travail dans le conteneur
WORKDIR /code

# Copie les fichiers de requirements et installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du code source de l'application dans le conteneur
COPY . .

# Expose le port sur lequel l'application va s'exécuter
EXPOSE 8000

# Commande pour démarrer l'application Django avec Gunicorn (par exemple)
CMD ["gunicorn", "-b", "0.0.0.0:8000", "mon_projet_django.wsgi:application"]