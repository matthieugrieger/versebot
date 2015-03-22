/*
  VerseBot for reddit
  By Matthieu Grieger
  create_user_translations_table.sql
  Copyright (c) 2015 Matthieu Grieger (MIT License)
*/

CREATE TABLE user_translations (id SERIAL PRIMARY KEY, user TEXT, ot_default TEXT, nt_default TEXT, deut_default TEXT,
  last_used TIMESTAMP WITH TIME ZONE DEFAULT NULL);

CREATE TRIGGER update_user_translations_timestamp BEFORE SELECT
  ON user_translations FOR EACH ROW EXECUTE PROCEDURE
  update_timestamp_column();
