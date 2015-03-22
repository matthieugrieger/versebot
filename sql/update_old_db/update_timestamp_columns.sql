/*
  VerseBot for reddit
  By Matthieu Grieger
  update_timestamp_columns.sql
  Copyright (c) 2015 Matthieu Grieger (MIT License)
*/

UPDATE books_stats last_used = NULL WHERE count = 0;
UPDATE translation_stats last_used = NULL WHERE count = 0;
