-- Top states by transaction amount
SELECT state, SUM(amount) as total_amount
FROM transactions
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;

-- Year-wise growth
SELECT year, SUM(amount) as total_amount
FROM transactions
GROUP BY year;