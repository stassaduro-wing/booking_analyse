-- booking_activity_dataset Schema Reconstruction
-- Database Engine: PostgreSQL
-- event table

CREATE TABLE events (
	id BIGINT PRIMARY KEY,
	user_id BIGINT,
	created_at TIMESTAMP,
	closed_at TIMESTAMP,
	city_of_booking VARCHAR(100),
	start_date DATE,
 	end_date DATE,
	cnt_of_person INT,
	min_price INT,
	max_price INT,
	booking_id BIGINT,
	rules TEXT,
	meals TEXT,
	pets TEXT,
	parking TEXT,
	accessibility TEXT,
	facilities TEXT,
	search_settings TEXT,
	room_size INT,
	kids TEXT,
 	pool_N_beach TEXT,
 	sport TEXT,
	transfer TEXT,
	business TEXT,
	rating INT,
	score INT,
	other TEXT,
	search_mode VARCHAR(20),
	ai_chat_id BIGINT,


	CONSTRAINT check_booking_dates CHECK (end_date > start_date),
	CONSTRAINT check_price CHECK (max_price > min_price)
);
