SELECT SCORE,DENSE_RANK() OVER (ORDER BY SCORE DESC) AS RANK FROM SCORES;
-- Check again, not done properly. Read the documentation for DENSE_RANK() 