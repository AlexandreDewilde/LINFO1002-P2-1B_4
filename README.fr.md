# Projet2-P2

Ceci est le projet P2 du cours LINFO1002


## Installer le projet et le lancer

### Télécharger le projet

Si ce n'est pas déja fait, télécharger le projet, en téléchargeant le zip ou en clonant le repo de la manière suivante :

```
git clone https://github.com/allEyezOnCode/LINFO1002-P2-1B_4
cd  LINFO1002-P2-1B_4
```

### Installer les dépendances (si flask est déja installé vous pouvez passer cette étape)

Le projet est construit au dessus du framework flask, il vous faut donc installer cette dépendance, dans le dossier principal du projet lancer la commande suivante dans votre invite de commande dans le dossier du projet:

```
pip install -r requirements.txt
```

### Crée la base de données (le fichier de la base de données est déja présent, vous pouvez passer cette étape)


Pour lancer la création de la DB, il faut vous rendre dans le dossier src/db
```
cd src/db
```

Ensuite on peut lancer le script de création comme ceci et puis retourn dans le dossier src:

```
python create_db.py
cd ..
```


### Lancer le projet

Pour lancer le projet, il suffite d'éxécuter le fichier app.py dans le dossier src

```
python app.py
```

## Arborecense des fichiers

```
LINFO1002-P2
├── captures_d_ecran // Dossier contenant les captures d'ecran
├── README.fr.md // Le readme en markdown version FR
├── README.md
├── readme.txt
├── requirements.txt // Fichier contenant les dépendances du projets
├── src // Touts le projet se trouve dans ce dossier
│   ├── app.py // Le fichier principal, c'est celui qu'il faut lancer pour executer le projet
│   ├── config.py // Fichier de config contenant les variables principal du projet
│   ├── db // Touts les fichiers relié à la database
│   │   ├── 1002-sql-data // Dossier des fichiers d'insertion dans la base de données
│   │   ├── create_db.py // fichier qui init la base de données, insere les données et génère les types de chaque animaux
│   │   ├── create_db.sql // Script sql de la creation de la db, des tables et colonnes
│   │   ├── database.db // La base de données sql
│   │   ├── db.py // Interface pour la base de données, se trouve toutes les fonctions utilitaire
│   │   ├── generate_race.py // Contient la fonction de génération des types pour chaque animaux et les fonctions pour aider dans cette création
│   │   ├── __init__.py
│   ├── fam_pre.py // Fichier contenant la fonction permettant la génaration du graph sur les morts prématurés par famille
│   ├── moon_phase.py // Fichier ou se trouver les fonctions utilitaire de calcul pour les phases de la lune
│   ├── moon_phases.py // Fichier contenant la fonction qui permetts à partir d'une liste de date de générer un dinctionnaire par années en fonction des phases de la lune
│   ├── premature_death.py // Fichier contenant la fonction pour le graph 4.1 des morts en fonction des mois de l'année
│   ├── static // Touts les fichiers static du site
│   │   ├── chartjs // Les fichiers de la librairie chartjs
│   │   │   ├── Chart.bundle.min.js
│   │   │   ├── Chart.min.css
│   │   │   └── Chart.min.js
│   │   ├── css // Les styles pour le site
│   │   │   ├── base.css // Le style de base
│   │   │   ├── components-style // Les styles pour chaque components
│   │   │   │   ├── cards.css
│   │   │   │   ├── charts.css
│   │   │   │   └── filter.css
│   │   │   └── theme // Les styles en fonction du theme
│   │   │       ├── darkmode.css
│   │   │       └── light.css
│   │   ├── images
│   │   └── js
│   │       ├── base.js
│   │       └── index.js Le js de la page principal, contient les graphs etc
│   └── templates
│       ├── 404.html
│       ├── about.html
│       ├── components
│       │   ├── filter.html
│       │   ├── footer.html
│       │   └── header.html
│       └── index.html
├── tests // Les tests des fonctions
│   ├── test_db.py
│   └── test_moon_phases.py
```