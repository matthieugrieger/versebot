/*
  VerseBot for reddit
  By Matthieu Grieger
  update_old_translation_table.sql
  Copyright (c) 2015 Matthieu Grieger (MIT License)
*/

ALTER TABLE translation_stats ALTER COLUMN name TYPE TEXT;
ALTER TABLE translation_stats ALTER COLUMN trans TYPE TEXT;
ALTER TABLE translation_stats ALTER COLUMN lang TYPE TEXT;

ALTER TABLE translation_stats ADD COLUMN has_ot BOOLEAN DEFAULT TRUE;
ALTER TABLE translation_stats ADD COLUMN has_nt BOOLEAN DEFAULT TRUE;
ALTER TABLE translation_stats ADD COLUMN has_deut BOOLEAN DEFAULT TRUE;
