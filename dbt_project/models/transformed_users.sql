-- models/transformed_users.sql
SELECT *
FROM {{ ref('users_data') }}
