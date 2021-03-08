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
  role integer
);

CREATE TABLE posts (
  id bigserial PRIMARY KEY,
  user_id integer REFERENCES users (id),
  game_id integer REFERENCES games (id),
  title varchar(100),
  body text
);

CREATE TABLE comments (
  id bigserial PRIMARY KEY,
  user_id integer REFERENCES users (id),
  post_id integer REFERENCES posts (id),
  comment_id integer,
  content text,
  hidden boolean
);

CREATE TABLE games (
  id bigserial PRIMARY KEY,
  title varchar(50),
  description varchar(300)
);

CREATE TABLE genres (
  id bigserial PRIMARY KEY,
  name varchar(20)
);

INSERT INTO users(id, username, password, email, phone, role)
VALUES (1, 'JohnSmith01', 'password', 'example@email.com', '123-1234', 0);
