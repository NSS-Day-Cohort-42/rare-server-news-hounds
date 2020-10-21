CREATE TABLE `user` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `email` TEXT,
  `first_name` TEXT,
  `last_name` TEXT,
  `username` TEXT,
  `password` TEXT
);

CREATE TABLE `category` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT
);

CREATE TABLE `tag` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `name` TEXT
);

CREATE TABLE `post_tag` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `post_id` INTEGER,
  `tag_id` INTEGER,
  FOREIGN KEY (`post_id`) REFERENCES `post` (`id`),
  FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`)
);

CREATE TABLE `post` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `user_id` INTEGER,
  `category_id` INTEGER,
  `title` TEXT,
  `content` TEXT,
  `publication_time` INTEGER,
  `creation_time` INTEGER,
  `image` TEXT,
  `publish_status` boolean,
  `approve_status` boolean,
  FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
);


INSERT INTO 'category' VALUES (null, 'Buisness');
INSERT INTO 'category' VALUES (null, 'Sports');
INSERT INTO 'category' VALUES (null, 'Entertainment');
INSERT INTO 'category' VALUES (null, 'Funnies');

INSERT INTO 'tag' VALUES (null, 'gossip');
INSERT INTO 'tag' VALUES (null, 'fake news');
INSERT INTO 'tag' VALUES (null, 'clickbait');
INSERT INTO 'tag' VALUES (null, 'realpolitik');
INSERT INTO 'tag' VALUES (null, 'sensationalism');


SELECT * FROM 'category';
SELECT * FROM 'post';
SELECT * FROM 'post_tag';
SELECT * FROM 'tag';
SELECT * FROM 'user';


-- DROP TABLE 'category';
-- DROP TABLE 'post';
-- DROP TABLE 'post_tag';
-- DROP TABLE 'tag';
-- DROP TABLE 'user';