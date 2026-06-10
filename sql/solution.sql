--1

SELECT 

ROUND(COUNT(*) FILTER (WHERE search_mode = 'ai')*100.0/COUNT(*), 2) AS percent_ai_srch,

ROUND(COUNT(*) FILTER (WHERE search_mode = 'ai' AND booking_id != 0)*100.0/COUNT(*), 2) AS percent_success_ai_srch,
ROUND(COUNT(*) FILTER (WHERE search_mode != 'ai' AND booking_id != 0)*100.0/COUNT(*), 2) AS percent_success_man_srch,
ROUND(
(COUNT(*) FILTER (WHERE search_mode = 'ai' AND booking_id != 0)*100.0/COUNT(*))
/
(COUNT(*) FILTER (WHERE search_mode != 'ai' AND booking_id != 0)*100.0/COUNT(*)) 
,2) AS success_ai_vs_man,

AVG(closed_at-created_at) FILTER (WHERE search_mode = 'ai' AND booking_id IS NOT NULL) AS avg_duration_ai,
AVG(closed_at-created_at) FILTER (WHERE search_mode != 'ai' AND booking_id IS NOT NULL) AS avg_duration_man,
ROUND(

EXTRACT(EPOCH FROM (AVG(closed_at-created_at) FILTER (WHERE search_mode != 'ai' AND booking_id IS NOT NULL)))
/
EXTRACT(EPOCH FROM AVG(closed_at-created_at) FILTER (WHERE search_mode = 'ai' AND booking_id IS NOT NULL))

, 2) AS avg_ai_vs_avg_man

FROM events

--2 

WITH user_orders AS (
	SELECT 
		user_id,
		COUNT(*) FILTER (WHERE booking_id IS NOT NULL) AS orders_count
	FROM events
	GROUP BY user_id
)
SELECT
	ROUND(
		COUNT(*) FILTER (WHERE orders_count > 1)*100.0/COUNT(*),
	2) AS percent_loyal_users
FROM user_orders

--3.1

SELECT city_of_booking,
COUNT(*)
FROM events
GROUP BY city_of_booking

--3.2

SELECT
	(end_date-start_date) AS count_days,
	COUNT(*) AS raito
FROM events
GROUP BY count_days
ORDER BY raito DESC

--3.3

WITH total_events AS (
    SELECT COUNT(*)::float AS total_count FROM events
),
unnested_filters AS (
    SELECT unnest(string_to_array(meals, ', ')) AS filter_name, 'meals' AS category FROM events WHERE meals IS NOT NULL
    UNION ALL
    SELECT unnest(string_to_array(pets, ', ')) AS filter_name, 'pets' AS category FROM events WHERE pets IS NOT NULL
    UNION ALL
    SELECT unnest(string_to_array(parking, ', ')) AS filter_name, 'parking' AS category FROM events WHERE parking IS NOT NULL
    UNION ALL
    SELECT unnest(string_to_array(accessibility, ', ')) AS filter_name, 'accessibility' AS category FROM events WHERE accessibility IS NOT NULL
    UNION ALL
    SELECT unnest(string_to_array(facilities, ', ')) AS filter_name, 'facilities' AS category FROM events WHERE facilities IS NOT NULL
    UNION ALL
    SELECT unnest(string_to_array(kids, ', ')) AS filter_name, 'kids' AS category FROM events WHERE kids IS NOT NULL
    UNION ALL
    SELECT unnest(string_to_array(pool_n_beach, ', ')) AS filter_name, 'pool_n_beach' AS category FROM events WHERE pool_n_beach IS NOT NULL
    UNION ALL
    SELECT unnest(string_to_array(sport, ', ')) AS filter_name, 'sport' AS category FROM events WHERE sport IS NOT NULL
    UNION ALL
    SELECT unnest(string_to_array(transfer, ', ')) AS filter_name, 'transfer' AS category FROM events WHERE transfer IS NOT NULL
    UNION ALL
    SELECT unnest(string_to_array(business, ', ')) AS filter_name, 'business' AS category FROM events WHERE business IS NOT NULL
    UNION ALL
    SELECT unnest(string_to_array(other, ', ')) AS filter_name, 'other' AS category FROM events WHERE other IS NOT NULL
)
SELECT 
    f.filter_name,
    f.category,
    ROUND(
        (COUNT(*) * 100.0 / t.total_count)::numeric, 
        2
    ) AS percent_of_total_searches
FROM unnested_filters f
CROSS JOIN total_events t 
WHERE f.filter_name IS NOT NULL
GROUP BY f.filter_name, f.category, t.total_count
ORDER BY percent_of_total_searches DESC
LIMIT 10;
