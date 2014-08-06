CREATE TABLE subreddit_stats (id SERIAL PRIMARY KEY, sub VARCHAR(30), count INTEGER DEFAULT 0, last_used TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW());

CREATE TRIGGER update_subreddit_stats_timestamp BEFORE UPDATE
    ON subreddit_stats FOR EACH ROW EXECUTE PROCEDURE 
    update_timestamp_column();
