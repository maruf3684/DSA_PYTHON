CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INT,
    card_number VARCHAR(20),
    merchant_id VARCHAR(20),
    amount NUMERIC(10, 2),
    status VARCHAR(20), -- e.g., 'SUCCESS', 'FAILED'
    txn_time TIMESTAMP
);


INSERT INTO transactions (user_id, card_number, merchant_id, amount, status, txn_time) VALUES
(1, '1234', 'AMZ', 100.00, 'SUCCESS', '2025-08-07 10:00:00'),
(1, '1234', 'AMZ', 100.00, 'SUCCESS', '2025-08-07 10:08:00'),
(1, '1234', 'AMZ', 150.00, 'FAILED',  '2025-08-07 11:00:00'),
(2, '5678', 'EBY', 200.00, 'SUCCESS', '2025-08-07 10:15:00'),
(2, '5678', 'EBY', 300.00, 'SUCCESS', '2025-08-07 10:18:00'),
(3, '9999', 'FLP', 250.00, 'FAILED',  '2025-08-07 12:00:00'),
(3, '9999', 'FLP', 250.00, 'FAILED',  '2025-08-07 12:04:00'),
(3, '9999', 'FLP', 250.00, 'FAILED',  '2025-08-07 12:06:00'),
(3, '9999', 'FLP', 250.00, 'SUCCESS', '2025-08-07 14:00:00'),
(4, '7777', 'OLX', 400.00, 'SUCCESS', '2025-08-07 09:00:00');



-- Running total of amounts per user
SELECT
  user_id,
  txn_time,
  amount,
  SUM(amount) OVER (PARTITION BY user_id ORDER BY txn_time) AS running_total
FROM transactions;

-- Time difference from previous txn (per user)
SELECT
  user_id,
  txn_time,
  LAG(txn_time) OVER (PARTITION BY user_id ORDER BY txn_time) AS prev_txn,
  txn_time - LAG(txn_time) OVER (PARTITION BY user_id ORDER BY txn_time) AS diff
FROM transactions;


-- Total, avg, min, max per user
SELECT
  user_id,
  COUNT(*) AS total_txns,
  SUM(amount) AS total_amount,
  AVG(amount) AS avg_amount,
  MAX(amount) AS max_amt
FROM transactions
GROUP BY user_id;


DO $$
DECLARE
  val NUMERIC;
BEGIN
  SELECT SUM(amount) INTO val FROM transactions WHERE user_id = 1;

  IF val > 200 THEN
    RAISE NOTICE 'User 1 has high transaction volume: %', val;
  ELSE
    RAISE NOTICE 'User 1 is under threshold: %', val;
  END IF;
END $$;


DO $$
DECLARE
  i INT := 1;
BEGIN
  WHILE i <= 5 LOOP
    RAISE NOTICE 'i = %', i;
    i := i + 1;
  END LOOP;
END $$;
