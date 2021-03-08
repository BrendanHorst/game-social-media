DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS games_genres;

CREATE TABLE users (
  id integer PRIMARY KEY AUTOINCREMENT,
  username varchar(50) NOT NULL,
  password varchar(50) NOT NULL,
  email varchar(50),
  phone varchar(50),
  role integer
);

CREATE TABLE posts (
  id integer PRIMARY KEY AUTOINCREMENT,
  user_id integer REFERENCES users (id),
  game_id integer REFERENCES games (id),
  title varchar(100),
  body text
);

CREATE TABLE comments (
  id integer PRIMARY KEY AUTOINCREMENT,
  user_id integer REFERENCES users (id),
  post_id integer REFERENCES posts (id),
  comment_id integer,
  content text,
  hidden boolean
);

CREATE TABLE games (
  id integer PRIMARY KEY AUTOINCREMENT,
  title varchar(50),
  description varchar(300)
);

CREATE TABLE genres (
  id integer PRIMARY KEY AUTOINCREMENT,
  name varchar(20)
);

CREATE TABLE games_genres (
  id integer PRIMARY KEY AUTOINCREMENT,
  game_id bigint REFERENCES games (id),
  genre_id bigint REFERENCES genres (id)
)
