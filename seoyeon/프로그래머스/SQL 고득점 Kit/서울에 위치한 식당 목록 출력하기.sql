SELECT i.rest_id, i.rest_name, i.food_type, i.favorites, i.address, ROUND(avg(r.review_score),2) as score
FROM REST_INFO AS i
JOIN REST_REVIEW AS r
ON i.rest_id = r.rest_id
WHERE i.address LIKE "서울%" # "서울"로 시작해야함. "%서울%"로 작성해 틀림
GROUP BY i.rest_id #rest_id(식당ID)로 그룹화
ORDER BY avg(r.review_score) DESC, i.favorites DESC