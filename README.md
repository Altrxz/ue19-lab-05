Description

Cette application Python interroge le service JokeAPI afin d'afficher une blague aléatoire en anglais. Elle
utilise la bibliothèque requests pour envoyer une requête HTTP et afficher le résultat dans la
console.

Fonctionnalités

Interrogation d'une API publique (JokeAPI)
Récupération et affichage d'une blague aléatoire
Gestion simple des erreurs réseau

Installation

Clonez ou téléchargez le projet
Assurez-vous d'avoir Python 3.8+ installé
Installez les dépendances :
pip install -r requirements.txt

Utilisation
Exécutez simplement :
python app.py

Exécution via Docker

Construire l'image Docker :

docker build -t joke-app .

Lancer le conteneur :

docker run --rm joke-app
