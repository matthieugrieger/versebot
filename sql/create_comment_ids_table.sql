CREATE TABLE comment_ids (id SERIAL PRIMARY KEY, comment_id VARCHAR(7), timestamp TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW());