/*
  VerseBot for reddit
  By Matthieu Grieger
  create_comment_count_table.sql
  Copyright (c) 2015 Matthieu Grieger (MIT License)
*/

CREATE TABLE comment_count (id SERIAL PRIMARY KEY, count INTEGER DEFAULT 0, last_used TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW());

CREATE TRIGGER update_comment_count_timestamp BEFORE UPDATE
  ON comment_count FOR EACH ROW EXECUTE PROCEDURE
  update_timestamp_column();
