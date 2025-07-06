-- models/user_watch_time.sql
SELECT
    u.user_id,
    u.name,
    SUM(wh.duration_minutes) AS total_watch_time
FROM {{ ref('watch_history') }} wh
JOIN {{ ref('transformed_users') }} u ON u.user_id = wh.user_id
GROUP BY u.user_id, u.name
