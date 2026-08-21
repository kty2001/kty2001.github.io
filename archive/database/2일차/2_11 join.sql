SELECT 
    menu_code AS 'code',
    menu_name AS name,
    menu_price 'price'
FROM
    tbl_menu
ORDER BY price;

SELECT
    a.category_code,
    a.menu_name
FROM
    -- tbl_menu AS a
    tbl_menu a
ORDER BY 
    a.category_code,
    a.menu_name;

SELECT 
    *
FROM 
    tbl_menu a
-- INNER JOIN tbl_category b ON a.category_code = b.category_code;
JOIN tbl_category b ON a.category_code = b.category_code;

SELECT 
    a.menu_name,
    b.category_name
FROM 
    tbl_menu a
INNER JOIN tbl_category b USING (category_code);

SELECT 
    a.category_name,
    b.menu_name
FROM 
    tbl_category a
LEFT JOIN tbl_menu b ON a.category_code = b.category_code;

SELECT 
    a.menu_name,
    b.category_name
FROM 
    tbl_menu a
RIGHT JOIN tbl_category b ON a.category_code = b.category_code;

SELECT 
    a.menu_name,
    b.category_name
FROM 
    tbl_menu a
CROSS JOIN tbl_category b;

SELECT
    a.category_name,
    b.category_name
FROM 
    tbl_category a
JOIN tbl_category b ON a.ref_category_code = b.category_code
WHERE a.ref_category_code IS NOT NULL;

SELECT /*+ NO_HASH_JOIN(a) */
    a.menu_name,
    b.category_name
FROM 
    tbl_menu a
JOIN tbl_category b ON a.category_code = b.category_code;

SELECT /*+ HASH_JOIN(a) */
    a.menu_name,
    b.category_name
FROM
    tbl_menu a
JOIN tbl_category b ON a.category_code = b.category_code;