-- 코드를 입력하세요
SELECT A.REST_ID, B.REST_NAME, B.FOOD_TYPE, B.FAVORITES, B.ADDRESS, ROUND(AVG(A.REVIEW_SCORE),2) AS SCORE
FROM REST_REVIEW A
JOIN REST_INFO B ON A.REST_ID = B.REST_ID
GROUP BY A.REST_ID
HAVING B.ADDRESS like "서울%"
ORDER BY SCORE DESC, B.FAVORITES DESC