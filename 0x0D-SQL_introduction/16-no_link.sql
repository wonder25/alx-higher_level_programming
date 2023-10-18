-- lists all records of the table
-- don't list rows without a name value
-- lists records in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
