/*
  VerseBot for reddit
  By Matthieu Grieger
  update_old_subreddit_table.sql
  Copyright (c) 2015 Matthieu Grieger (MIT License)
*/

ALTER TABLE subreddit_stats ALTER COLUMN sub TYPE TEXT;
