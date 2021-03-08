--Mock data for development purposes

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
