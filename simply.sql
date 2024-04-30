CREATE TABLE `Book` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`title`	  TEXT NOT NULL,
	`image`	  TEXT NOT NULL,
  `price`   INTEGER NOT NULL,
  `sale`   BOOL NOT NULL,
  `description`   TEXT NOT NULL
);

CREATE TABLE `Author` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `email`    TEXT NOT NULL,
    `first_name`    TEXT NOT NULL,
    `last_name`    TEXT NOT NULL,
    `image`    TEXT NOT NULL,
    `favorite`    BOOL NOT NULL
);

CREATE TABLE `Author_Books` (
    `id`    INTEGER PRIMARY KEY AUTOINCREMENT,
    `author_id`    INTEGER,
    `book_id` INTEGER,
    FOREIGN KEY (author_id) REFERENCES Authors(id),
    FOREIGN KEY (book_id) REFERENCES Books(id)
);

INSERT INTO `Book` VALUES (null, "Kafka on the Shore", "url.png", 24, FALSE, "Everyone has the power to make choices to change their fate");
INSERT INTO `Book` VALUES (null, "Circe", "url.jpeg", 21, FALSE, "Retelling of Circe from Greek myth");
INSERT INTO `Book` VALUES (null, "Tender is the Flesh", "url2.png", 18, TRUE, "A tale of what humans are willing to excuse");
INSERT INTO `Book` VALUES (null, "Six of Crows", "url2.jpeg", 26, TRUE, "An unlikely band of thieves pull of an unbelievable heist");
INSERT INTO `Book` VALUES (null, "A Horse and His Boy", "url3.png", 15, FALSE, "Fantasy involving enlightenment and reform");
INSERT INTO `Book` VALUES (null, "Backslider", "url3.jpeg", 60, FALSE, "A man desperately hoping for someone to fall in love with him");

INSERT INTO `Author` VALUES (null, "csthemyth@gmail.com", "C.S.", "Lewis", "image.png", False);
INSERT INTO `Author` VALUES (null, "backslider@aol.com", "Chris", "Thile", "image.jpg", False);
INSERT INTO `Author` VALUES (null, "redheadsinger@gmail.com", "Fleming", "McWilliams", "image2.png", False);
INSERT INTO `Author` VALUES (null, "lazlodaddy.com", "Mr. M", "Thiessen", "image2.jpg", False);


INSERT INTO `Author_Books` (author_id, book_id) VALUES
(1, 1),
(3, 1),
(2, 3),
(2, 6),
(4, 2),
(4, 5),
(3, 4);
