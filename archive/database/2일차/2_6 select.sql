use menudb;

SELECT menu_code, menu_name, menu_price FROM tbl_menu;

SELECT 
    * 
FROM 
    tbl_menu;

SELECT 6 + 3;   
SELECT 6 * 3;
SELECT 6 % 3;

select now();
SELECT CONCAT('홍.',' ','길동');

SELECT CONCAT('홍',' ','길동') AS name;
SELECT CONCAT('홍',' ','길동') AS 'Full name';

select concat('진짜 맛있는 ', menu_name, ' 빨리 먹어') as '메뉴' from tbl_menu;

select concat('진짜 맛있는 ', menu_name, ' 빨리 먹어') as '메뉴',
now() as cur_time from tbl_menu;

desc tbl_menu;
select * from tbl_menu;

select
	menu_name,
	menu_price,
	orderable_status
from tbl_menu where orderable_status = 'Y';

select
	menu_name,
	menu_price,
	orderable_status
from tbl_menu where menu_price = 13000;

select
	menu_name,
	menu_price,
	orderable_status
from tbl_menu where orderable_status != 'Y';

select
	menu_name,
	menu_price,
	orderable_status
from tbl_menu where menu_price > 20000;

select
	menu_name,
	menu_price,
	orderable_status
from tbl_menu where (menu_price > 10000 and menu_price < 20000) or menu_price  > 30000;

SELECT 1 AND 1;
SELECT 1 AND 0, 0 AND 1, 0 AND 0, 0 AND NULL;
SELECT 1 AND NULL, NULL AND NULL;

insert into tb1
values (2, 1, null);

select
	menu_name,
	menu_price,
	orderable_status
from tbl_menu where orderable_status = 'Y' and category_code = 10;

select
	menu_name,
	menu_price,
	orderable_status
	category_code,
	orderable_status
from tbl_menu where menu_price > 5000 and category_code = 10;

SELECT 1 OR 1, 1 OR 0, 0 OR 1;
SELECT 0 OR 0;
SELECT 1 OR NULL, 0 OR NULL, NULL or NULL;

SELECT 
    menu_name, 
    menu_price, 
    category_code,
    orderable_status
FROM
    tbl_menu
WHERE
    orderable_status = 'Y' OR
    category_code = 10
ORDER BY 
    category_code;

SELECT 
    menu_code, 
    menu_name, 
    menu_price,
    category_code,
    orderable_status
FROM
    tbl_menu
WHERE
    category_code = 4 OR
    menu_price = 9000 AND
    menu_code > 10;

SELECT 
    menu_name, 
    menu_price
FROM
    tbl_menu
WHERE
    menu_name LIKE '%마늘%'
ORDER BY 
    menu_name;

SELECT 
    menu_code, 
    menu_name, 
    menu_price,
    category_code,
    orderable_status
FROM
    tbl_menu
WHERE
    menu_price > 5000 AND 
    category_code = 10 AND
    menu_name LIKE '%갈치%';

SELECT 
    menu_name, 
    menu_price
FROM
    tbl_menu
WHERE
    menu_name NOT LIKE '%마늘%'
ORDER BY 
    menu_name;

SELECT 
    menu_name,
    category_code
FROM
    tbl_menu
WHERE
    category_code IN (4, 5, 6)
ORDER BY 
    category_code;

SELECT 
    category_code, 
    category_name, 
    ref_category_code
FROM
    tbl_category
WHERE
    ref_category_code is not NULL;


-- 문제 1
-- 상위 카테고리 코드가 null이 아닌 카테고리의 카테고리 코드와 카테고리명을 출력하세요.
-- 단, 카테고리명을 기준으로 내림차순 정렬하여 출력하세요.
select category_code, category_name from tbl_category where category_code is not null order by category_name desc;

--  Q2.
-- 메뉴명에 '밥'이 포함되고, 가격이 20,000원 이상 30,000원 이하인 메뉴의 메뉴명과 가격을 출력하세요.
select menu_name, menu_price from tbl_menu
where menu_name like '%밥%' and menu_price between 20000 and 30000;


--  Q3.
-- 가격이 10,000원 미만이거나, 메뉴명에 김치가 포함되는 메뉴의 모든 컬럼을 출력하세요.
-- 단, 가격을 기준으로 오름차순 정렬하고, 추가로 메뉴명을 기준으로 내림차순 정렬하여 출력하세요.
select * from tbl_menu
where menu_price < 10000 or menu_name like '%김치%'
order by menu_price , menu_name desc;

--  Q4.
-- Q1에서 출력한 카테고리명 결과를 참고하여, 카테고리가 기타, 쥬스, 커피에 해당하지 않는 메뉴 중 메뉴 가격이 13,000원인 메뉴의 모든 컬럼을 출력하세요.
-- 단, 주문이 불가능한 상품은 출력하지 않습니다.
select tbl_menu.* from tbl_category, tbl_menu
where tbl_category.category_name not in ('기타', '쥬스', '커피') and menu_price = 13000 and orderable_status != 'N';

-- - 참고 1. Q1 에서 출력한 결과
-- - 참고 2. orderable_status의 컬럼값이 N이면 주문 불가