-- this script will list scores with their numbers
-- with descending format
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
