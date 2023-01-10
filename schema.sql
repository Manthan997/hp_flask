-- this file is a sql file and thus uses sql syntax
/*
used to define the structure of .db file
all tables to be made with there colums are defined here
you can add other DMLs here as an sql file but better keep ot seperate for understanding 
*/

DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

