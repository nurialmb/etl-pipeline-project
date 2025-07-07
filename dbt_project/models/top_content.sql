SELECT
  c.content_id,
  c.title,
  c.genre,
  SUM(w.duration_minutes) AS total_watch_time
FROM {{ ref('watch_history') }} w
JOIN {{ ref('content') }} c ON w.content_id = c.content_id
GROUP BY c.content_id, c.title, c.genre
ORDER BY total_watch_time DESC
LIMIT 10
