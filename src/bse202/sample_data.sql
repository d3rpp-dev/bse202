INSERT INTO 
	`users` (`user_id`, `created_at`, `username`, `account_type`) 
VALUES 
	--- this is the only account with admin privileges
	('01HXZ1G3CWZADWKVWEWZ0TAYMT', 1715807518, 'admin', 'admin')
;

INSERT INTO 
	`password_hashes` (`user_id`, `password_hash`)
VALUES
	-- this is the admin password, it is `admin_password`
	('01HXZ1G3CWZADWKVWEWZ0TAYMT', '$argon2id$v=19$m=16,t=2,p=1$MDFIWFoxRzNDV1pBRFdLVldFV1owVEFZTVQ$O8+EtclWefuxQv14bRjAhw')
;