DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
	user_id SERIAL PRIMARY KEY NOT NULL,
	name TEXT NOT NULL
);

INSERT INTO users (name) 
VALUES ('Tony Maguire'), ('Eren Yeager');
