/*
  VerseBot for reddit
  By Matthieu Grieger
  update_timestamp_columns.sql
  Copyright (c) 2015 Matthieu Grieger (MIT License)
*/

ALTER TABLE book_stats DISABLE TRIGGER update_book_stats_timestamp;
ALTER TABLE translation_stats DISABLE TRIGGER update_translation_stats_timestamp;

UPDATE book_stats SET last_used = NULL WHERE count = 0;
UPDATE translation_stats SET last_used = NULL WHERE count = 0;

ALTER TABLE book_stats ENABLE TRIGGER update_book_stats_timestamp;
ALTER TABLE translation_stats ENABLE TRIGGER update_translation_stats_timestamp;
