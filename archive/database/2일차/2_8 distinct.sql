SELECT 
    category_code
FROM
    tbl_menu
ORDER BY 
    category_code;

SELECT 
    DISTINCT category_code
FROM
    tbl_menu
ORDER BY 
    category_code;

SELECT
	ref_category_code
FROM 
	tbl_category;

SELECT
	DISTINCT ref_category_code
FROM 
	tbl_category;

SELECT 
    category_code, 
    orderable_status
FROM
    tbl_menu;

SELECT DISTINCT
    category_code, 
    orderable_status
FROM
    tbl_menu;