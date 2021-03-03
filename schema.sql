CREATE DATABASE IF NOT EXISTS 'game-social';
USE 'game-social';

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS genres;

CREATE TABLE users (
  id bigserial PRIMARY KEY,
  username varchar(50) NOT NULL,
  password varchar(50) NOT NULL,
  email varchar(50),
  phone varchar(50),
  role int,
);

CREATE TABLE posts (
  id bigserial PRIMARY KEY,
  user_id int REFERENCES users(id),
  game_id int REFERENCES games(id),
  title varchar(100),
  body text,
);

CREATE TABLE comments (
  id bigserial PRIMARY KEY,
  user_id int REFERENCES users(id),
  post_id int REFERENCES posts(id),
  comment_id int,
  content text,
  hidden boolean,
);

CREATE TABLE games (
  id bigserial PRIMARY KEY,
  title varchar(50),
  description varchar(300),
);

CREATE TABLE genres (
  id bigserial PRIMARY KEY,
  name varchar(20),
);
