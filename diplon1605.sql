CREATE DATABASE users;

CREATE TABLE IF NOT EXISTS users (
	user_id INTEGER PRIMARY KEY,
	bdate VARCHAR(20) NOT NULL,
    sex INTEGER,
    relation VARCHAR (30),
    home_town VARCHAR (30),
    age INTEGER,
    name_user VARCHAR (30),
    lastname_user VARCHAR (30),
    status INTEGER
);

CREATE TABLE IF NOT EXISTS serch_user (
	user_id INTEGER PRIMARY key references user(id),
	name_user VARCHAR (20),	
	city VARCHAR (20),
	now_year INTEGER,
	user_year INTEGER,
	age INTEGER,
	status VARCHAR (20)
	id_closed INTEGER
)



