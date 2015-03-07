/*
  VerseBot for reddit
  By Matthieu Grieger
  update_old_book_table.sql
  Copyright (c) 2015 Matthieu Grieger (MIT License)
*/

ALTER TABLE book_stats ALTER COLUMN book TYPE TEXT;
