CREATE TABLE `user` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `email` TEXT NOT NULL,
  `first_name` TEXT NOT NULL,
  `last_name` TEXT NOT NULL,
  `username` TEXT NOT NULL,
  `password` TEXT NOT NULL
);

CREATE TABLE `category` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` TEXT NOT NULL
);

CREATE TABLE `tag` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `name` TEXT NOT NULL
);

CREATE TABLE `post_tag` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `post_id` INTEGER NOT NULL,
  `tag_id` INTEGER NOT NULL,
  FOREIGN KEY (`post_id`) REFERENCES `post` (`id`),
  FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`)
);

CREATE TABLE `post` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `user_id` INTEGER NOT NULL,
  `category_id` INTEGER NOT NULL,
  `title` TEXT NOT NULL,
  `content` TEXT NOT NULL,
  `publication_time` INTEGER NOT NULL,
  `creation_time` INTEGER NOT NULL,
  `image` TEXT NOT NULL,
  `publish_status` boolean NOT NULL,
  `approve_status` boolean NOT NULL,
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

INSERT INTO 'user' VALUES (null, 'bryan@ford.com', 'bryan', 'ford', 'fordba', 'password');
INSERT INTO 'user' VALUES (null, 'another@person.com', 'another', 'person', 'anperson', 'password');

INSERT INTO 'post' VALUES (null, 1, 1, 'Local Business Needs More People', 'A local business today decided that they needed more employees', 1, 1, '', true, true);
INSERT INTO 'post' VALUES (null, 1, 1, 'Test Post', 'Here is the test content.', 1, 1, '', true, true);

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