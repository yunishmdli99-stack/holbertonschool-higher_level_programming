-- this script will list scores with their numbers
-- with descending format
SELECT score FROM second_table GROUP BY score AS number ORDER BY DESC;
