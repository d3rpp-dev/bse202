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
    (1, 'DOOM Eternal', 'A fast-paced, first-person shooter where players combat demonic forces across various realms using a wide array of weapons and abilities.'),
    (2, 'Sekiro: Shadows Die Twice', 'An action-adventure game with a focus on stealth, exploration, and precise combat mechanics, set in a reimagined late 1500s Sengoku period Japan.'),
    (3, 'Monster Hunter: World', 'An action RPG where players hunt down colossal monsters in a beautiful, immersive world, either solo or with friends.'),
    (4, 'Devil May Cry 5', 'A stylish action game where players control demon hunters using a variety of weapons and combat techniques to defeat demonic enemies.'),
    (5, 'Resident Evil Village', 'A survival horror game that follows Ethan Winters as he searches for his kidnapped daughter in a village filled with mutant creatures.'),
    (6, 'Football Manager 2022', 'A detailed football management simulation where players take control of a football club and manage its tactics, transfers, and training.'),
    (7, 'NBA 2K22', 'A basketball simulation game that offers realistic graphics, player rosters, and gameplay modes, including MyCareer and MyTeam.'),
    (8, 'EA Sports UFC 4', 'A mixed martial arts fighting game that provides realistic fighter models, new arenas, and a career mode that lets players build their own fighter.'),
    (9, 'Tony Hawk\'s Pro Skater 1 + 2', 'Remastered versions of the classic skateboarding games with updated graphics and all the original levels, tricks, and modes.'),
    (10, 'WWE 2K22', 'A professional wrestling game featuring improved graphics, a redesigned gameplay engine, and a variety of modes including MyGM and Showcase.'),
    (11, 'Sid Meier\'s Civilization VI', 'A turn-based strategy game where players build and expand a civilization through time, developing cities, technology, and armies to dominate the world.'),
    (12, 'Total War: Three Kingdoms', 'A real-time strategy game set in ancient China during the Three Kingdoms period, combining turn-based empire management and real-time battles.'),
    (13, 'Age of Empires IV', 'A real-time strategy game that spans several historical eras, focusing on building empires, gathering resources, and commanding armies.'),
    (14, 'Crusader Kings III', 'A grand strategy game where players manage a medieval dynasty, focusing on politics, warfare, and intrigue to expand their realm.'),
    (15, 'Stellaris', 'A space grand strategy game where players manage an interstellar empire, exploring the galaxy, colonizing new worlds, and engaging in diplomacy and warfare.'),
    (16, 'The Witcher 3: Wild Hunt', 'An open-world RPG where players control Geralt of Rivia, a monster hunter searching for his adopted daughter in a richly detailed fantasy world.'),
    (17, 'Divinity: Original Sin 2', 'A critically acclaimed RPG with deep, tactical combat and an expansive world where players can choose their path and shape the story.'),
    (18, 'Disco Elysium', 'A narrative-driven RPG where players control a detective with a unique skill system, investigating a murder in a decaying city.'),
    (19, 'Pillars of Eternity II: Deadfire', 'A party-based RPG set in a rich fantasy world, focusing on exploration, complex quests, and deep role-playing mechanics.'),
    (20, 'GreedFall', 'An action RPG set in a 17th-century-inspired world where players explore an island filled with magic, secrets, and political intrigue.'),
    (21, 'Hades', 'A roguelike dungeon crawler where players attempt to escape the Underworld, battling mythological enemies and unlocking powerful abilities.'),
    (22, 'Stardew Valley', 'A farming simulation game where players grow crops, raise animals, mine, fish, and engage with the local community.'),
    (23, 'Celeste', 'A platformer with precise controls and a touching story about a young woman climbing a mountain, facing challenging levels and personal struggles.'),
    (24, 'Undertale', 'A unique RPG where players navigate a world of monsters, making choices that affect the story and combat, known for its humor and emotional depth.'),
    (25, 'Dead Cells', 'A roguelike metroidvania game with fast-paced combat, procedural generation, and permadeath, where players explore a constantly changing castle.')
;

INSERT INTO 
    `game_assets` (`asset_id`, `game_id`, `description`, `asset_type`)
VALUES
    (1, 1, 'DOOM Eternal Image', 'grid_banner'),
    (2, 2, 'Sekiro: Shadows Die Twice Image', 'grid_banner'),
    (3, 3, 'Monster Hunter: World Image', 'grid_banner'),
    (4, 4, 'Devil May Cry 5 Image', 'grid_banner'),
    (5, 5, 'Resident Evil Village Image', 'grid_banner'),
    (6, 6, 'Football Manager 2022 Image', 'grid_banner'),
    (7, 7, 'NBA 2K22 Image', 'grid_banner'),
    (8, 8, 'EA Sports UFC 4 Image', 'grid_banner'),
    (9, 9, 'Tony Hawk\'s Pro Skater 1 + 2 Image', 'grid_banner'),
    (10, 10, 'WWE 2K22 Image', 'grid_banner'),
    (11, 11, 'Sid Meier\'s Civilization VI Image', 'grid_banner'),
    (12, 12, 'Total War: Three Kingdoms Image', 'grid_banner'),
    (13, 13, 'Age of Empires IV Image', 'grid_banner'),
    (14, 14, 'Crusader Kings III Image', 'grid_banner'),
    (15, 15, 'Stellaris Image', 'grid_banner'),
    (16, 16, 'The Witcher 3: Wild Hunt Image', 'grid_banner'),
    (17, 17, 'Divinity: Original Sin 2 Image', 'grid_banner'),
    (18, 18, 'Disco Elysium Image', 'grid_banner'),
    (19, 19, 'Pillars of Eternity II: Deadfire Image', 'grid_banner'),
    (20, 20, 'GreedFall Image', 'grid_banner'),
    (21, 21, 'Hades Image', 'grid_banner'),
    (22, 22, 'Stardew Valley Image', 'grid_banner'),
    (23, 23, 'Celeste Image', 'grid_banner'),
    (24, 24, 'Undertale Image', 'grid_banner'),
    (25, 25, 'Dead Cells Image', 'grid_banner')
;

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