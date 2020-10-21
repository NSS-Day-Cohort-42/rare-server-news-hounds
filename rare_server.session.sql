CREATE TABLE `user` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `email` varchar(255),
  `first_name` varchar(255),
  `last_name` varchar(255),
  `username` varchar(255),
  `password` varchar(255)
);

CREATE TABLE `post` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `user_id` INTEGER,
  `category_id` INTEGER,
  `title` varchar(255),
  `content` varchar(255),
  `publication_time` INTEGER,
  `creation_time` INTEGER,
  `image` url,
  `publish_status` boolean,
  `approve_status` boolean
);

CREATE TABLE `category` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` varchar(255)
);

CREATE TABLE `tag` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` varchar(255)
);

CREATE TABLE `post_tag` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `post_id` INTEGER,
  `tag_id` INTEGER
);

ALTER TABLE `post` ADD FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);

ALTER TABLE `post` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `post_tag` ADD FOREIGN KEY (`post_id`) REFERENCES `post` (`id`);

ALTER TABLE `post_tag` ADD FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`);

INSERT INTO 'category' VALUES (null, 'Buisness');
INSERT INTO 'category' VALUES (null, 'Sports');
INSERT INTO 'category' VALUES (null, 'Entertainment');
INSERT INTO 'category' VALUES (null, 'Funnies');

INSERT INTO 'tag' VALUES (null, 'gossip');
INSERT INTO 'tag' VALUES (null, 'fake news');
INSERT INTO 'tag' VALUES (null, 'clickbait');
INSERT INTO 'tag' VALUES (null, 'real potlitic');
INSERT INTO 'tag' VALUES (null, 'sensationalism');


SELECT * FROM 'category';
SELECT * FROM 'post';
SELECT * FROM 'post_tag';
SELECT * FROM 'tag';
SELECT * FROM 'user';
