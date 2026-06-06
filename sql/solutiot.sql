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

AVG(closed_at-created_at) FILTER (WHERE search_mode = 'ai' AND booking_id != 0) AS avg_duration_man,
AVG(closed_at-created_at) FILTER (WHERE search_mode != 'ai' AND booking_id != 0) AS avg_duration_ai,
ROUND(

EXTRACT(EPOCH FROM (AVG(closed_at-created_at) FILTER (WHERE search_mode != 'ai' AND booking_id != 0)))
/
EXTRACT(EPOCH FROM AVG(closed_at-created_at) FILTER (WHERE search_mode = 'ai' AND booking_id != 0))

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
		COUNT(*) FILTER (WHERE orders_count > 1)*100/COUNT(*),
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

