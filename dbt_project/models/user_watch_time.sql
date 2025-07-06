SELECT
    u.user_id,
    u.name,
    SUM(c.duration_minutes) AS total_watch_time_minutes
FROM {{ ref('watch_history') }} wh
JOIN {{ ref('users_data') }} u ON wh.user_id = u.user_id
JOIN {{ ref('content') }} c ON wh.content_id = c.content_id
GROUP BY u.user_id, u.name
