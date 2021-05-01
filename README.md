# Projet2-P2

This is the project for the course LINFO1002


## Install and run the project

### Download the project

Begin by cloning the repo, and go into the folder of the project

```
git clone https://github.com/allEyezOnCode/LINFO1002-P2-1B_4
cd  LINFO1002-P2-1B_4
```

### Install the dependencies

In the folder of the app the following command to install the dependencies

```
pip install -r requirements.txt
```

### Init the database (alreay done in the project you can skip this step)

after you need to init the database (it's alreay done), so in the db folder, run the create_db.py script, it will create the db, insert data and generate race for each animals.

```
cd src/db
python create_db.py
cd ..
```


### Run the project

To run the project in the src folder run the following command

```
python app.py
```


## Folder structure

```
LINFO1002-P2
├── captures_d_ecran // Screenshots of the website
├── README.fr.md // Readme in french
├── README.md
├── readme.txt
├── requirements.txt // File containing the dependecies
├── src // Folder containing all the project
│   ├── app.py // main file, the file to execute to run the site
│   ├── config.py // Fichier containing global variables
│   ├── db // Files related to the db
│   │   ├── 1002-sql-data // Folder containing the insertions files, the data
│   │   ├── create_db.py // File to init the db, generate race
│   │   ├── create_db.sql // Sql script that create the db, tables and columns
│   │   ├── database.db // Sql database
│   │   ├── db.py // Interface with the database
│   │   ├── generate_race.py // File containing the function to generate race and the utils function for it
│   │   ├── __init__.py
│   ├── fam_pre.py // File containing the function for the graph about premature_death by family
│   ├── moon_phase.py // File containing the utils to calculate moon phase for a date
│   ├── moon_phases.py // File to convert a list of date to a dict of year with list of number of moon phases according to date
│   ├── premature_death.py // File containing the utils for the graph about premature_death by months
│   ├── static // All static files of the sites
│   │   ├── chartjs // Chart js lib
│   │   │   ├── Chart.bundle.min.js
│   │   │   ├── Chart.min.css
│   │   │   └── Chart.min.js
│   │   ├── css // Styles for the website
│   │   │   ├── base.css
│   │   │   ├── components-style //styles foreach components
│   │   │   │   ├── cards.css
│   │   │   │   ├── charts.css
│   │   │   │   └── filter.css
│   │   │   └── theme // Style for the themes
│   │   │       ├── darkmode.css
│   │   │       └── light.css
│   │   ├── images
│   │   └── js
│   │       ├── base.js
│   │       └── index.js // Js containing all the js for the index page, it contains graph etc...
│   └── templates
│       ├── 404.html
│       ├── about.html
│       ├── components
│       │   ├── filter.html
│       │   ├── footer.html
│       │   └── header.html
│       └── index.html
├── tests
│   ├── test_db.py
│   └── test_moon_phases.py
```