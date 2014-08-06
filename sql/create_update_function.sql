CREATE OR REPLACE FUNCTION update_timestamp_column()
	RETURNS TRIGGER AS $$
	BEGIN
		NEW.last_used = now(); 
	RETURN NEW;
END;
$$ language 'plpgsql';
