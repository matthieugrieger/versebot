/*
  VerseBot for reddit
  By Matthieu Grieger
  create_subreddit_translations_table.sql
  Copyright (c) 2015 Matthieu Grieger (MIT License)
*/

CREATE TABLE subreddit_translations (id SERIAL PRIMARY KEY, sub TEXT, ot_default TEXT, nt_default TEXT, deut_default TEXT,
  last_used TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW());

CREATE TRIGGER update_subreddit_translations_timestamp BEFORE SELECT
  ON subreddit_translations FOR EACH ROW EXECUTE PROCEDURE
  update_timestamp_column();
