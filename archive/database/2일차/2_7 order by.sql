SELECT
    menu_code,
    menu_name,
    menu_price
FROM
    tbl_menu
ORDER BY
--     menu_price ASC;    -- ASC는 오름차순
    menu_price;

SELECT
    menu_code,
    menu_name,
    menu_price
FROM
    tbl_menu
ORDER BY
    menu_price DESC;    -- DESC는 내림차순
    
SELECT 
    menu_code,
    menu_name,
    menu_price
FROM
    tbl_menu
ORDER BY 
    menu_price DESC,
    menu_name ASC;

SELECT 
    menu_code, 
    menu_price, 
    menu_code * menu_price
FROM
    tbl_menu
ORDER BY 
    menu_code * menu_price DESC;

SELECT FIELD('A', 'A', 'B', 'C');
SELECT FIELD('B', 'A', 'B', 'C');

SELECT 
    FIELD(orderable_status, 'N', 'Y')-1 as orderable
FROM 
    tbl_menu;

SELECT 
    menu_name, 
    orderable_status
FROM
    tbl_menu
ORDER BY FIELD(orderable_status, 'N', 'Y');

SELECT 
    category_code,
    category_name,
    ref_category_code
FROM
    tbl_category
ORDER BY 
--     ref_category_code ASC;
    ref_category_code;    -- ASC 생략 가능
    
    SELECT 
    category_code,
    category_name,
    ref_category_code
FROM
    tbl_category
ORDER BY 
--     ref_category_code IS NULL ASC;
    ref_category_code IS NULL;    -- ASC 생략 가능
    
