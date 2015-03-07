/*
  VerseBot for reddit
  By Matthieu Grieger
  create_translation_table.sql
  Copyright (c) 2015 Matthieu Grieger (MIT License)
*/

CREATE TABLE translation_stats (id SERIAL PRIMARY KEY, name TEXT, trans TEXT, lang TEXT,
  count INTEGER DEFAULT 0, BOOLEAN has_ot DEFAULT TRUE, BOOLEAN has_nt DEFAULT TRUE, BOOLEAN has_deut DEFAULT FALSE,
  last_used TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW());

CREATE TRIGGER update_translation_stats_timestamp BEFORE UPDATE
  ON translation_stats FOR EACH ROW EXECUTE PROCEDURE
  update_timestamp_column();
