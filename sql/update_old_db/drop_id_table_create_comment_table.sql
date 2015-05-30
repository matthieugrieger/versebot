/*
  VerseBot for reddit
  By Matthieu Grieger
  drop_id_table_create_comment_table.sql
  Copyright (c) 2015 Matthieu Grieger (MIT License)
*/

CREATE TABLE comment_count (id SERIAL PRIMARY KEY, count INTEGER DEFAULT 0, last_used TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW());

INSERT INTO comment_count (count) SELECT id FROM comment_ids WHERE id = (SELECT max(id) FROM comment_ids);

DROP TABLE comment_ids;
