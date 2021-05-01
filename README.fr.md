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