--
-- Users & Passwords
--

INSERT INTO 
	`users` (`user_id`, `created_at`, `username`, `account_balance`, `account_type`, `profile_bg`, `text_colour`, `description`) 
VALUES 
	--- this is the only account with admin privileges
	('01hxz1g3cwzadwkvwewz0taymt', 1715807518, 'admin', 100.0, 'admin', NULL, NULL, 'Admin Account Test User - boo i can delete you account haha'),
	('01hxz91jcfwgkeywswrqckmv4g', 1715807518, 'test_user', 20.0, NULL, '#02060e', '#eeeeee', 'Test User Bio - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vehicula ipsum enim, et pellentesque elit egestas quis.')
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
	`games` (`game_id`, `title`, `description`, `price`)
VALUES
	( 1, 'DOOM Eternal', 'Experience the ultimate combination of speed and power with the next leap in push-forward, first-person combat.', 69.95),
	( 2, 'Sekiro: Shadows Die Twice', 'Carve your own clever path to vengeance in this critically acclaimed adventure from developer FromSoftware.', 99.95),
	( 3, 'Monster Hunter: World', 'Battle gigantic monsters in epic locales. As a hunter, you''ll take on quests to hunt monsters in a variety of habitats.', 48.96),
	( 4, 'Devil May Cry 5', 'The threat of demonic power has returned to menace the world once again in this action-packed game.', 15.16),
	( 5, 'Resident Evil Village', 'Experience survival horror like never before in the 8th major installment in the Resident Evil franchise.', 24.36),

	( 6, 'Football Manager 2022', 'Football isn''t just about being the best and winning. It''s about overcoming the odds, realizing your dreams, and earning your success.', 11.99),
	( 7, 'NBA 2K22', 'NBA 2K22 puts the entire basketball universe in your hands. Play now in real NBA and WNBA environments against authentic teams and players.', 99.95),
	( 8, 'EA Sports UFC 4', 'Shape your legend in the EA SPORTS UFC 4. In EA SPORTS UFC 4 the fighter you become is shaped by your fight style, achievements, and personality.', 92.65),
	( 9, 'Tony Hawk''s Pro Skater 1 + 2', 'Drop back in with the most iconic skateboarding games ever made. Play Tony Hawk''s Pro Skater & Tony Hawk''s Pro Skater 2 in one epic collection.', 36.50),
	(10, 'WWE 2K22', 'Get ripped out of the stands and hit with complete control of the WWE Universe. Throw down with the biggest and most realistic-looking WWE Superstars and Legends.', 98.65),

	(11, 'Sid Meier''s Civilization VI', 'Civilization VI offers new ways to interact with your world, expand your empire across the map, advance your culture, and compete against history''s greatest leaders.', 4.99),
	(12, 'Total War: Three Kingdoms', 'Three Kingdoms is the first in the award-winning series to recreate epic conflict across ancient China.', 99.99),
	(13, 'Age of Empires IV', 'One of the most beloved real-time strategy games returns to glory with Age of Empires IV, putting you at the center of epic historical battles.', 59.95),
	(14, 'Crusader Kings III', 'Your legacy awaits. Choose your noble house and lead your dynasty to greatness in a Middle Ages epic that will have you plotting, conquering, and sitting on the throne.', 79.99),
	(15, 'Stellaris', 'Explore a vast galaxy full of wonder! Paradox Development Studio brings you the grand strategy game with space exploration at its core.', 63.99),

	(16, 'The Witcher 3: Wild Hunt', 'As war rages on, you must take on the contract of your life and track down the Child of Prophecy, a key to saving or destroying this world.', 67.99),
	(17, 'Divinity: Original Sin 2', 'The Divine is dead. The Void approaches. And the powers lying dormant within you are soon to awaken. The battle for Divinity has begun.', 59.99),
	(18, 'Disco Elysium', 'Disco Elysium - The Final Cut is the definitive edition of the groundbreaking role-playing game. You''re a detective with a unique skill system at your disposal.', 12.49),
	(19, 'Pillars of Eternity II: Deadfire', 'Pursue a rogue god over land and sea in the sequel to the multi-award-winning RPG Pillars of Eternity. Captain your ship on a dangerous voyage of discovery.', 11.99),
	(20, 'GreedFall', 'Explore uncharted new lands as you set foot on a remote island seeping with magic, and filled with riches, lost secrets, and fantastic creatures.', 59.99),

	(21, 'Hades', 'Defy the god of the dead as you hack and slash out of the Underworld in this rogue-like dungeon crawler.', 35.99),
	(22, 'Stardew Valley', 'You''ve inherited your grandfather''s old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life.', 17.99),
	(23, 'Celeste', 'Help Madeline survive her inner demons on her journey to the top of Celeste Mountain, in this super-tight, hand-crafted platformer from the creators of TowerFall.', 28.99),
	(24, 'Undertale', 'The RPG game where you don''t have to destroy anyone. Each enemy can be “defeated” nonviolently.', 11.99),
	(25, 'Dead Cells', 'Dead Cells is a rogue-lite, metroidvania inspired, action-platformer. You''ll explore a sprawling, ever-changing castle...', 29.99)
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

-- Note to those who check, the content for `categories` and
-- `game_categories_link` was written by Halim 👍
INSERT INTO
	`categories` (`category_id`, `title`, `description`)
VALUES
    (1, 'Action', 'Games characterized by fast-paced gameplay, often emphasizing physical challenges, including hand-eye coordination and reaction-time.'),
    (2, 'Sports', 'Games that simulate the practice of sports.'),
    (3, 'Strategy', 'Games that emphasize strategic thinking and planning.'),
    (4, 'Role-playing', 'Games where players assume the roles of characters in a fictional setting.'),
    (5, 'Indie', 'Games developed by independent developers without the financial support of a publisher.')
;

INSERT INTO
	`game_categories_link` (`game_id`, `category_id`)
VALUES
    (1, 1), -- DOOM Eternal > Action
    (2, 1), -- Sekiro: Shadows Die Twice > Action
    (3, 1), -- Monster Hunter: World > Action
    (4, 1), -- Devil May Cry 5 > Action
    (5, 1), -- Resident Evil Village > Action
    (6, 2), -- Football Manager 2022 > Sports
    (7, 2), -- NBA 2K22 > Sports
    (8, 2), -- EA Sports UFC 4 > Sports
    (9, 2), -- Tony Hawk's Pro Skater 1 + 2 > Sports
    (10, 2), -- WWE 2K22 > Sports
    (11, 3), -- Sid Meier's Civilization VI > Strategy
    (12, 3), -- Total War: Three Kingdoms > Strategy
    (13, 3), -- Age of Empires IV > Strategy
    (14, 3), -- Crusader Kings III > Strategy
    (15, 3), -- Stellaris > Strategy
    (16, 4), -- The Witcher 3: Wild Hunt > Role-playing
    (17, 4), -- Divinity: Original Sin 2 > Role-playing
    (18, 4), -- Disco Elysium > Role-playing
    (19, 4), -- Pillars of Eternity II: Deadfire > Role-playing
    (20, 4), -- GreedFall > Role-playing
    (21, 5), -- Hades > Indie
    (22, 5), -- Stardew Valley > Indie
    (23, 5), -- Celeste > Indie
    (24, 5), -- Undertale > Indie
    (25, 5) -- Dead Cells > Indie
;

INSERT INTO
	`cart_items` (`game_id`, `user_id`)
VALUES
	(1, '01hxz91jcfwgkeywswrqckmv4g'), -- test user has DOOM: Eternal
	(5, '01hxz91jcfwgkeywswrqckmv4g') -- test user has Resident Evil: Village
;