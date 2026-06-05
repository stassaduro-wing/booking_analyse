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
