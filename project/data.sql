--Mock data for development purposes

INSERT INTO users(id, username, password, email, phone, role)
VALUES (1, 'JohnSmith01', 'password', 'example@email.com', '123-1234', 0);

INSERT INTO games (title)
VALUES ('Super Smash Bros'),
       ('Xenoblade Chronicles'),
       ('Minecraft'),
       ('Terraria');

INSERT INTO genres (name)
VALUES ('Fighting'),
       ('JRPG'),
       ('Sandbox');

INSERT INTO games_genres (game_id, genre_id)
VALUES (1, 1),
       (2, 2),
       (3, 3),
       (4, 3);
