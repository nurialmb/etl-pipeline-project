SELECT
  strftime('%Y-%m', watch_date) AS month,
  COUNT(DISTINCT user_id) AS active_users
FROM {{ ref('watch_history') }}
GROUP BY month
ORDER BY month
