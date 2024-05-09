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
	`salt` TEXT NOT NULL,

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