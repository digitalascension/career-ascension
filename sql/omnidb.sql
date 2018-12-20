-- Create the OMNI database. --
CREATE DATABASE OMNI;
USE OMNI;

-- Create the ModelData table where NLP and ML models will be stored --
CREATE TABLE ModelData (
  DataID int AUTO_INCREMENT NOT NULL,
  ModelName VARCHAR(256) NOT NULL,
  CreatedBy VARCHAR(256) NOT NULL,
  LastUpdated TIMESTAMP NOT NULL,
  Tags BLOB NULL,
  URL VARCHAR(256) NOT NULL,
  PRIMARY KEY (DataID)
);

-- Create the Model table to store the models in the database. --
CREATE TABLE Model (
  ModelID int AUTO_INCREMENT NOT NULL,
  DataID int NOT NULL ,
  ModelName VARCHAR(256) NOT NULL,
  ModelBlob LONGBLOB NOT NULL,
  FOREIGN KEY (DataID) REFERENCES ModelData(DataID),
  PRIMARY KEY (ModelID)
);

-- Insert some test data. --
INSERT INTO ModelData (ModelName, CreatedBy, LastUpdated, Tags, URL)
    VALUES (
        "testmodel2",
        "Luke Brady",
        CURRENT_TIMESTAMP(),
        NULL,
        "/model/testmodel2843849843"
    );