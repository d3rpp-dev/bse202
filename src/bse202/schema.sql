-- Reset and Create `users` Table 
DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
	`user_id` TEXT PRIMARY KEY,
	`created_at` INTEGER NOT NULL,
	`username` TEXT UNIQUE ON CONFLICT ROLLBACK,
	`profile_bg` TEXT, -- used as profile background, optional
	`description` TEXT -- profile description, optional
);


-- Reset and Create `password_hashes` Table 
DROP TABLE IF EXISTS `password_hashes`; 

CREATE TABLE `password_hashes` (
	`user_id` TEXT PRIMARY KEY,
	`password_hash` TEXT NOT NULL,

	FOREIGN KEY (user_id) REFERENCES users(user_id)
);


-- Reset and Create `games` Table 
DROP TABLE IF EXISTS `games`;

CREATE TABLE `games` (
	`game_id` INTEGER PRIMARY KEY,
	`title` TEXT NOT NULL,
	`description` TEXT NOT NULL
);


-- Reset and Create `categories` Table 
DROP TABLE IF EXISTS `categories`;

CREATE TABLE `categories` (
	`category_id` INTEGER PRIMARY KEY,
	`title` TEXT NOT NULL UNIQUE,
	`description` TEXT NOT NULL
);

-- Reset and Create the `reviews` Table

DROP TABLE IF EXISTS `reviews`;

CREATE TABLE `reviews` (
	`review_id` INTEGER PRIMARY KEY,
	`user_id` TEXT NOT NULL,
	`game_id` INTEGER NOT NULL,
	`title` TEXT NOT NULL,
	`body` TEXT NOT NULL,
	`star_count` SMALLINT NOT NULL,
	`ts` BIGINT NOT NULL,

	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (game_id) REFERENCES games(game_id)
);

-- Reset and Create the `purchases` Table

DROP TABLE IF EXISTS `purchases`;

CREATE TABLE `purchases` (
	`purchase_id` BIGINT PRIMARY KEY,
	`user_id` TEXT NOT NULL,
	`game_id` TEXT NOT NULL,
	`purchased_at` BIGINT NOT NULL,

	FOREIGN KEY (user_id) REFERENCES users(user_id),
	FOREIGN KEY (game_id) REFERENCES games(game_id)
);

-- Reset and Create the `game_categories_link` Table

DROP TABLE IF EXISTS `game_categories_link`;

CREATE TABLE `game_categories_link` (
	`game_id` INTEGER NOT NULL,
	`category_id` INTEGER NOT NULL,

	FOREIGN KEY (game_id) REFERENCES games(game_id),
	FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
