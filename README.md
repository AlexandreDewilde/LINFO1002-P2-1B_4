# Projet2-P2

This is the project for the course LINFO1002


## Run the project

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

### Init the database (alreay done)

after you need to init the database (it's alreay done), so in the db folder, run the create_db.py script, it will create the db, insert data and generate race for each animals.

```
cd src/db
python create_db.py
```


### Run the project

To run the project go back to the src folder and run de app.py script

```
cd ..
python app.py
```