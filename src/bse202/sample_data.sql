--
-- Users & Passwords
--

INSERT INTO 
	`users` (`user_id`, `created_at`, `username`, `account_type`) 
VALUES 
	--- this is the only account with admin privileges
	('01HXZ1G3CWZADWKVWEWZ0TAYMT', 1715807518, 'admin', 'admin'),
	('01HXZ91JCFWGKEYWSWRQCKMV4G', 1715807518, 'test_user', NULL)
;


INSERT INTO 
	`password_hashes` (`user_id`, `password_hash`)
VALUES
	-- this is the admin password, it is `admin_password`
	('01HXZ1G3CWZADWKVWEWZ0TAYMT', '$argon2id$v=19$m=16,t=2,p=1$MDFIWFoxRzNDV1pBRFdLVldFV1owVEFZTVQ$O8+EtclWefuxQv14bRjAhw'),
	-- this is the test_user password, it is `test_user_password`
	('01HXZ91JCFWGKEYWSWRQCKMV4G', '$argon2id$v=19$m=16,t=2,p=1$MDFIWFoxRzNDV1pBRFdLVldFV1owVEFZTVQ$ZWqu5Dk2A0so2whdxWHoLQ')
;

--
-- Games and Categories
--

INSERT INTO 
	`games` (`game_id`, `title`, `description`)
VALUES
	(1, 'VALORANT', 'A 5v5 character-based tactical shooter'),
	(2, 'Team Fortress 2', 'One of the most timeless classic shooter games in history.')
;

INSERT INTO 
	`game_assets` (`asset_id`, `game_id`, `description`, `asset_type`)
VALUES
	(1, 1, 'VALORANT Image', 'grid_banner'),
	(2, 2, 'Team Fortress 2 Image', 'grid_banner')
;

INSERT INTO
	`categories` (`category_id`, `title`, `description`)
VALUES
	(1, 'First Person Shooters', 'Staples of the gaming industry, using weapons of all kinds to eliminate virtual rivals.')
;

INSERT INTO
	`game_categories_link` (`game_id`, `category_id`)
VALUES
	(1, 1), -- Valorant > FPS
	(2, 1) -- Team Fortress 2 > FPS
;
