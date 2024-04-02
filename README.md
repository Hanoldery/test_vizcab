
# Projet Construction Data Analysis

Ce projet est une application web Django destinée à l'analyse de données de construction. Il permet d'effectuer des calculs spécifiques tels que la surface totale d'un bâtiment, son usage principal, et l'impact carbone sur son cycle de vie, en s'appuyant sur des données structurées fournies sous forme de fichiers JSON.

## Fonctionnalités Principales

- **Calcul de la Surface Totale** : Détermine la surface cumulée des zones d'un bâtiment donné.
- **Détermination de l'Usage Principal** : Identifie l'usage principal d'un bâtiment en fonction de la surface des zones qu'il comprend.
- **Analyse de l'Impact Carbone** : Calcule l'impact carbone total d'un bâtiment sur son cycle de vie complet, en prenant en compte différents éléments de construction.

## Comment Lancer le Projet

Pour lancer l'application, assurez-vous d'avoir Docker installé sur votre système. Suivez ensuite ces étapes :

1. **Cloner le dépôt Git** :
   ```bash
   git clone https://exempledepot.com/projet.git
   cd projet
   ```

2. **Construire l'Image Docker** :
   Depuis le répertoire racine du projet, lancez la commande suivante pour construire l'image Docker à partir du `Dockerfile` :
   ```bash
   docker build -t construction-data-analysis .
   ```

3. **Démarrer le Conteneur Docker** :
   Lancez l'application en exécutant :
   ```bash
   docker run -d -p 8000:8000 construction-data-analysis
   ```
   Votre application devrait maintenant être accessible à l'adresse `http://localhost:8000`.

## Structure du Projet

- `construction_project/` : Dossier de configuration du projet Django.
- `construction_data/` : L'application Django principale (modèles, vues, urls, et scripts de chargement de données)
  - `models/` : Définitions des modèles Django pour les entités du projet comme les bâtiments, zones, et éléments de construction. Ici j'ai utilisé des classes python qui n'héritent pas des modèles Django comme je n'ai pas utilisé de base de donnée.
  - `views.py` : Vues qui implémentent la logique des fonctionnalités principales.
  - `urls.py` : Définition des routes URL de l'application.
  - `services/` : Contient la logique métier pour les calculs, séparée des vues pour une meilleure lisibilité.
  - `data/` : Fichiers JSON contenant les données de base.
  - `loaders.py` : Script pour charger les données JSON en mémoire au démarrage de l'application.

## Choix de Structure

La structure du projet est conçue pour séparer clairement les préoccupations :

- Les **modèles** définissent la structure des données.
- Les **vues** gèrent la logique de présentation, dans un seul fichier, le nombre de logiques me semblant assez faible pour cela. Au-delà il faudra subdiviser les vues.
- Les **services** encapsulent la logique métier, permettant de garder les vues simples et centrées sur l'appel de fonctions et la réponse aux requêtes HTTP. Les calculs dans services sont simples, mais ça permet d'isoler leur fonctionnement et de les changer si le projet évolue.
- Le script **loaders.py** charge les données du dossier **data** permettant une initialisation rapide sans base de donnée. Possible seulement grâce au faible volume de donnée.

