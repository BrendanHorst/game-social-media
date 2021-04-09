--Mock data for development purposes

INSERT INTO users(id, username, password, email, phone, role)
VALUES (1, 'JohnSmith01', 'password', 'example@email.com', '123-1234', 0),
(2, 'baned', 'baned1', 'baned@email.com', '321-4321', 2);

INSERT INTO posts(user_id, game_id, title, body)
VALUES (1, 1, 'Title', 'This is a test post for testing purposes'),
       (1, 2, 'Title2', 'This is another test post, but about Xenoblade this time');

INSERT INTO games (title, description)
VALUES ('Super Smash Bros', "Nintendo's signature crossover fighting game"),
       ('Xenoblade Chronicles', 'Action JRPG developed by MonolithSoft'),
       ('Minecraft', '3d creative sandbox game'),
       ('Terraria', '2d action sandbox game');

INSERT INTO genres (name)
VALUES ('Fighting'),
       ('JRPG'),
       ('Sandbox');

INSERT INTO games_genres (game_id, genre_id)
VALUES (1, 1),
       (2, 2),
       (3, 3),
       (4, 3);
