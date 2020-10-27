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

INSERT INTO 'post_tag' VALUES (null, '1', '1');
INSERT INTO 'post_tag' VALUES (null, '1', '2');
INSERT INTO 'post_tag' VALUES (null, '1', '3');
INSERT INTO 'post_tag' VALUES (null, '2', '3');

INSERT INTO 'user' VALUES (null, 'bryan@ford.com', 'bryan', 'ford', 'fordba', 'password');
INSERT INTO 'user' VALUES (null, 'another@person.com', 'another', 'person', 'anperson', 'password');

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

INSERT INTO post_tag VALUES (null, 1, 1);

SELECT * FROM 'post_tag';

INSERT INTO 'post_tag' VALUES (null, '1', '2');
INSERT INTO 'post_tag' VALUES (null, '1', '3');
INSERT INTO 'post_tag' VALUES (null, '2', '3');

 SELECT * FROM post;

 INSERT INTO 'post' VALUES (null, 1, 1, 'Test Post', 'Here is the test content.', 1, 1, '', true, true);
 INSERT INTO 'post' VALUES (null, 2, 2, 'CONTENT', 'Here is the test content.', 1, 1, '', true, true);
 INSERT INTO 'post' VALUES (null, 2, 3, 'AWESOME TITLE', 'Here is the test content.', 1, 1, '', true, true);
 INSERT INTO 'post' VALUES (null, 3, 4, 'ALSO A TITLE', 'Here is the test content.', 1, 1, '', true, true);
 INSERT INTO 'post' VALUES (null, 3, 2, 'SOME TITLES', 'Here is the test content.', 1, 1, '', true, true);
 INSERT INTO 'post' VALUES (null, 2, 4, 'YES TITLEEE', 'Here is the test content.', 1, 1, '', true, true);
 INSERT INTO 'post_tag' VALUES (null, '5', '1');

UPDATE post SET image ='https://www.gannett-cdn.com/media/USATODAY/USATODAY/2013/02/20/c03-barkley-before-13-16_9.jpg' WHERE id = 6; 

INSERT INTO 'post' VALUES (null, 2, 2, 'SOME TITLE', 'Here is STUFF.', 1, 1, 'https://www.gannett-cdn.com/media/USATODAY/USATODAY/2013/02/20/c03-barkley-before-13-16_9.jpg', true, true);

UPDATE post SET publication_time = 1318781876406

INSERT INTO 'post' VALUES (null, 3, 2, 'I NEED', 'SOME TEST DATA', 1, 1, 'https://www.gannett-cdn.com/media/USATODAY/USATODAY/2013/02/20/c03-barkley-before-13-16_9.jpg', true, true);

SELECT * FROM  post WHERE id = 3;

CREATE TABLE `comment` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `content` INTEGER NOT NULL,
  `timestamp` INTEGER NOT NULL,
  `post_id` INTEGER NOT NULL,
  `user_id` INTEGER NOT NULL,
  FOREIGN KEY (`post_id`) REFERENCES `post` (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
);

INSERT INTO 'comment' VALUES (null, 'this is a bad take', '3458694038', 15, 3);
INSERT INTO 'comment' VALUES (null, 'this is a GREAT TAKE', '35739393933', 12, 4);



