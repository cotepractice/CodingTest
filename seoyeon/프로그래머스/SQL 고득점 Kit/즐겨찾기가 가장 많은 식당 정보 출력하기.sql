SELECT r.food_type, r.rest_id, r.rest_name, r.favorites
FROM REST_INFO AS r
WHERE r.favorites in (
    select max(r.favorites)
    from REST_INFO AS r
    group by r.food_type
)
GROUP BY r.food_type
ORDER BY FOOD_TYPE DESC