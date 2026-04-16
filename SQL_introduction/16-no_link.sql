-- this script will list students in descending format
-- but not without any value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
