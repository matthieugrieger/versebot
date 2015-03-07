/*
  VerseBot for reddit
  By Matthieu Grieger
  create_update_function.sql
  Copyright (c) 2015 Matthieu Grieger (MIT License)
*/

CREATE OR REPLACE FUNCTION update_timestamp_column()
	RETURNS TRIGGER AS $$
	BEGIN
		NEW.last_used = now();
	RETURN NEW;
END;
$$ language 'plpgsql';
