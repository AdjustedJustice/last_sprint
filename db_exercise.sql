--Задание 1

 SELECT
    c.login AS courier_login,
    COUNT(o.id) AS in_delivery_count
FROM "Couriers" AS c
JOIN "Orders" AS o ON o."courierId" = c.id
WHERE o."inDelivery" = TRUE
GROUP BY c.login
ORDER BY courier_login;

--Задание 2

SELECT
    tracker,
    CASE
        WHEN finished = TRUE THEN 2
        WHEN cancelled = TRUE THEN -1
        WHEN inDelivery = TRUE THEN 1
        ELSE 0
    END AS status
FROM "Orders"