CREATE TABLE animaux(
    id             INT PRIMARY KEY,
    famille_id     INT                   NOT NULL,

    sexe           TEXT                  NOT NULL,
    presence       INT                   NOT NULL,
    apprivoise     INT                   NOT NULL,                 
    mort_ne        INT                   NOT NULL, 
    decede         INT                   NOT NULL
);



CREATE TABLE familles(
    id             INT PRIMARY KEY,
    nom            TEXT        NOT NULL        
);



CREATE TABLE types(
    id             INT PRIMARY KEY,
    type           TEXT     NOT NULL            
);



CREATE TABLE animaux_types(
    animal_id INT,
    type_id INT        NOT NULL,
    pourcentage REAL           NOT NULL
);



CREATE TABLE velages(
    id INT PRIMARY KEY,
    mere_id INT                NOT NULL,
    pere_id INT                NOT NULL,
    date INT                 NOT NULL
);


CREATE TABLE animaux_velages(
    animal_id INT NOT NULL,
    velage_id INT NOT NULL
);


CREATE TABLE complications(
    id INT PRIMARY KEY,
    complication TEXT   NOT NULL
);



CREATE TABLE velages_complications(
    velage_id INT NOT NULL,
    complication_id INT NOT NULL
);