CREATE DATABASE agency;
USE agency;

CREATE TABLE IF NOT EXISTS user
(
	idUser int auto_increment,
    name varchar(50) not null,
    photo longblob,

	CONSTRAINT pk_user_idUser PRIMARY KEY(idUser)
);

SELECT * FROM user;