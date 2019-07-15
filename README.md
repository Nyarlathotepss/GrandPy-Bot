 Papybot
============

##Présentation du projet GrandPy Bot

Le programme doit permettre à un utilisateur de saisir dans une page web une question à
papybot sur un lieu ou une adresse.
Si l'adresse est trouvé dans l'API wikimedia, une réponse à l'utilisateur est faite avec une description
ainsi que une minimap google map de la france avec un pointeur sur le lieu indiqué.
Sinon il est demandé a l'utilisateur de reformuler sa question

### Fonctionnement (en local)

1/ Dans api.py il est indiqué qu'il faut entrer votre clé google dans vos variables environnement.
Pour éviter de futurs bugs nommer la variable : gmap_key 

2/ Executer le script views.py

3/ Aller sur l'url suivante : http://127.0.0.1:5000/accueil/

4/ Saisissez votre question.
Exemple : bonjour paris

### Fonctionnement (en ligne)