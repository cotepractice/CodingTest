SELECT r.food_type, r.rest_id, r.rest_name, r.favorites
FROM REST_INFO AS r
WHERE r.favorites in (
    select max(r.favorites)
    from REST_INFO AS r
    group by r.food_type
)
GROUP BY r.food_type
ORDER BY FOOD_TYPE DESC

-- 아래와 같이 작성하는게 더 정확 --
-- 위 코드는 한식의 최대 즐겨찾기 수가 50일 때 일식에 50이 있는 경우 함께 출력 -- s
SELECT r.food_type, r.rest_id, r.rest_name, r.favorites
FROM REST_INFO AS r
WHERE (r.food_type, r.favorites) in (
    select r.food_type, max(r.favorites)
    from REST_INFO AS r
    group by r.food_type
)
#GROUP BY r.food_type
ORDER BY FOOD_TYPE DESC