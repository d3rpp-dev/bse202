--
-- Users & Passwords
--

INSERT INTO 
	`users` (`user_id`, `created_at`, `username`, `account_type`, `profile_bg`, `text_colour`) 
VALUES 
	--- this is the only account with admin privileges
	('01hxz1g3cwzadwkvwewz0taymt', 1715807518, 'admin', 'admin', NULL, NULL),
	('01hxz91jcfwgkeywswrqckmv4g', 1715807518, 'test_user', NULL, '#02060e', '#eeeeee')
;


INSERT INTO 
	`password_hashes` (`user_id`, `password_hash`)
VALUES
	-- this is the admin password, it is `admin_password`
	('01hxz1g3cwzadwkvwewz0taymt', '$argon2id$v=19$m=16,t=2,p=1$MDFIWFoxRzNDV1pBRFdLVldFV1owVEFZTVQ$O8+EtclWefuxQv14bRjAhw'),
	-- this is the test_user password, it is `test_user_password`
	('01hxz91jcfwgkeywswrqckmv4g', '$argon2id$v=19$m=16,t=2,p=1$MDFIWFoxRzNDV1pBRFdLVldFV1owVEFZTVQ$ZWqu5Dk2A0so2whdxWHoLQ')
;

--
-- Games and Categories
--

INSERT INTO 
	`games` (`game_id`, `title`, `description`)
VALUES
	( 1, 'DOOM Eternal', 'Experience the ultimate combination of speed and power with the next leap in push-forward, first-person combat.'),
	( 2, 'Sekiro: Shadows Die Twice', 'Carve your own clever path to vengeance in this critically acclaimed adventure from developer FromSoftware.'),
	( 3, 'Monster Hunter: World', 'Battle gigantic monsters in epic locales. As a hunter, you''ll take on quests to hunt monsters in a variety of habitats.'),
	( 4, 'Devil May Cry 5', 'The threat of demonic power has returned to menace the world once again in this action-packed game.'),
	( 5, 'Resident Evil Village', 'Experience survival horror like never before in the 8th major installment in the Resident Evil franchise.'),

	( 6, 'Football Manager 2022', 'Football isn''t just about being the best and winning. It''s about overcoming the odds, realizing your dreams, and earning your success.'),
	( 7, 'NBA 2K22', 'NBA 2K22 puts the entire basketball universe in your hands. Play now in real NBA and WNBA environments against authentic teams and players.'),
	( 8, 'EA Sports UFC 4', 'Shape your legend in the EA SPORTS UFC 4. In EA SPORTS UFC 4 the fighter you become is shaped by your fight style, achievements, and personality.'),
	( 9, 'Tony Hawk''s Pro Skater 1 + 2', 'Drop back in with the most iconic skateboarding games ever made. Play Tony Hawk''s Pro Skater & Tony Hawk''s Pro Skater 2 in one epic collection.'),
	(10, 'WWE 2K22', 'Get ripped out of the stands and hit with complete control of the WWE Universe. Throw down with the biggest and most realistic-looking WWE Superstars and Legends.'),

	(11, 'Sid Meier''s Civilization VI', 'Civilization VI offers new ways to interact with your world, expand your empire across the map, advance your culture, and compete against history''s greatest leaders.'),
	(12, 'Total War: Three Kingdoms', 'Three Kingdoms is the first in the award-winning series to recreate epic conflict across ancient China.'),
	(13, 'Age of Empires IV', 'One of the most beloved real-time strategy games returns to glory with Age of Empires IV, putting you at the center of epic historical battles.'),
	(14, 'Crusader Kings III', 'Your legacy awaits. Choose your noble house and lead your dynasty to greatness in a Middle Ages epic that will have you plotting, conquering, and sitting on the throne.'),
	(15, 'Stellaris', 'Explore a vast galaxy full of wonder! Paradox Development Studio brings you the grand strategy game with space exploration at its core.'),

	(16, 'The Witcher 3: Wild Hunt', 'As war rages on, you must take on the contract of your life and track down the Child of Prophecy, a key to saving or destroying this world.'),
	(17, 'Divinity: Original Sin 2', 'The Divine is dead. The Void approaches. And the powers lying dormant within you are soon to awaken. The battle for Divinity has begun.'),
	(18, 'Disco Elysium', 'Disco Elysium - The Final Cut is the definitive edition of the groundbreaking role-playing game. You''re a detective with a unique skill system at your disposal.'),
	(19, 'Pillars of Eternity II: Deadfire', 'Pursue a rogue god over land and sea in the sequel to the multi-award-winning RPG Pillars of Eternity. Captain your ship on a dangerous voyage of discovery.'),
	(20, 'GreedFall', 'Explore uncharted new lands as you set foot on a remote island seeping with magic, and filled with riches, lost secrets, and fantastic creatures.'),

	(21, 'Hades', 'Defy the god of the dead as you hack and slash out of the Underworld in this rogue-like dungeon crawler.'),
	(22, 'Stardew Valley', 'You''ve inherited your grandfather''s old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life.'),
	(23, 'Celeste', 'Help Madeline survive her inner demons on her journey to the top of Celeste Mountain, in this super-tight, hand-crafted platformer from the creators of TowerFall.'),
	(24, 'Undertale', 'The RPG game where you don''t have to destroy anyone. Each enemy can be “defeated” nonviolently.'),
	(25, 'Dead Cells', 'Dead Cells is a rogue-lite, metroidvania inspired, action-platformer. You''ll explore a sprawling, ever-changing castle...')
;

INSERT INTO 
	`game_assets` (`asset_id`, `game_id`, `description`, `asset_type`)
VALUES
	( 1, 25, 'Dead Cells Image', 'main_image'),
	( 2, 16, 'Witcher 3 Image', 'main_image'),
	( 3, 17, 'Divinty 2: Original Sin Image', 'main_image'),
	( 4, 18, 'Disco Elysium Image', 'main_image'),
	( 5, 19, 'Pillars of Eternity Image', 'main_image'),
	( 6, 20, 'GreedFall Image', 'main_image'),
	( 7,  6, 'Football Manager 2022 Image', 'main_image'),
	( 8,  7, 'NBA 2K22 Image', 'main_image'),
	( 9,  8, 'EA UFC 4 Image', 'main_image'),
	(10,  9, 'Tony Hawk Image', 'main_image'),
	(11,  1, 'DOOM Eternal Image', 'main_image'),
	(12, 10, 'WWE 2K22 Image', 'main_image'),
	(13, 11, 'Civ 6 Image', 'main_image'),
	(14, 12, 'Total War Image', 'main_image'),
	(15, 13, 'Age of Empires Image', 'main_image'),
	(16, 14, 'Crusader Kings Image', 'main_image'),
	(17, 15, 'Stellaris Image', 'main_image'),
	(18,  2, 'Sekiro Image', 'main_image'),
	(19,  3, 'Monster Hunter Image', 'main_image'),
	(20,  4, 'Devil May Cry Image', 'main_image'),
	(21,  5, 'Resident Evil Village Image', 'main_image'),
	(22, 21, 'Hades Image', 'main_image'),
	(23, 22, 'Stardew Valley', 'main_image'),
	(24, 23, 'Celeste Image', 'main_image'),
	(25, 24, 'UNDERTALE Image', 'main_image')
;

INSERT INTO
	`categories` (`category_id`, `title`, `description`)
VALUES
	(1, 'First Person Shooters', 'Staples of the gaming industry, using weapons of all kinds to eliminate virtual rivals.'),
	(2, 'Online', 'Interract with other players from all around the world via the World Wide Web')
;

INSERT INTO
	`game_categories_link` (`game_id`, `category_id`)
VALUES
	(1, 1), -- Valorant > FPS
	(1, 2), -- Valorant > Online
	(2, 1), -- Team Fortress 2 > FPS
	(2, 2) -- Team Fortress 2 > Online
;
