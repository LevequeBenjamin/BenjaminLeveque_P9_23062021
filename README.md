# BenjaminLeveque_P9_23062021

## Développez une application Web en utilisant Django

Le projet 9 de la formation Développeur d'application Python est le developpement d'une application
web django permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.

### Installation

Cet application web exécutable localement peut être installée en suivant les étapes décrites ci-dessous.

1. Clonez le [repository](https://github.com/LevequeBenjamin/BenjaminLeveque_P9_23062021.git) à l'aide de la commande suivante :

`$ git clone "https://github.com/LevequeBenjamin/BenjaminLeveque_P9_23062021.git"` 
(vous pouvez également télécharger le code en temps [qu'archive zip](https://github.com/LevequeBenjamin/BenjaminLeveque_P9_23062021/archive/refs/heads/master.zip))

2. Exécutez l'application dans un environnement virtuel

Rendez-vous depuis un terminal à la racine du répertoire BenjaminLeveque_P9_23062021/src avec la commande `$ cd BenjaminLeveque_P9_23062021/src`

Pour créez un environnement, utilisez la commande :

`$ python3 -m venv env` sous macos ou linux.

`$ python -m venv env` sous windows.

Pour activer l'environnement, exécutez la commande :

`$ source env/bin/activate` sous macos ou linux.

`$ env/Scripts/activate` sous windows.

3.  Installez les dépendances du projet avec la commande `$ pip install -r requirements.txt`

### Usage

Pour lancer l'application utilisez la commande:

```
$ python manage.py runserver
```

Puis rendez-vous sur votre [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
