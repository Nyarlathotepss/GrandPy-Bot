 Papybot
============

##Présentation du projet GrandPy Bot

Le programme doit permettre à un utilisateur de saisir dans une page web une question à
papybot sur un lieu ou une adresse.
Si l'adresse est trouvé dans l'API wikimedia, une réponse à l'utilisateur est faite avec une description
ainsi que une minimap google map de la france avec un pointeur sur le lieu indiqué.
Sinon il est demandé a l'utilisateur de reformuler sa question

### Fonctionnement (en local)

1/ Dans api.py il est indiqué qu'il faut entrer votre clé google dans votre variable environnement.
Indiquer le nom de votre variable `self.googlemap_key = os.environ.get("votre nom de variable")`

2/ Executer le script views.py

3/ Allez sur l'url suivante : http://127.0.0.1:5000/accueil/

4/ Saisissez votre question.
Exemple : bonjour papybot donne moi des infos sur paris
Exemple : salut papy tu sais quoi sur paris

### Fonctionnement (en ligne)

1/ Dans api.py il est indiqué qu'il faut entrer votre clé google dans votre variable environnement.
Indiquer le nom de votre variable `self.googlemap_key = os.environ.get("votre nom de variable")`

2/ Créer un compte sur Heroku

3/ Suivre la documentation : https://devcenter.heroku.com/articles/getting-started-with-python

4/ Une fois votre projet pushé sur le site distant d'Heroku rendez vous l'url que vous obtenez en allant
sur votre page d'administration Heroku (https://dashboard.heroku.com/) et ajouté /accueil/ a la fin de cette url.
exemple: https://fast-lake-29762.herokuapp.com/accueil/
