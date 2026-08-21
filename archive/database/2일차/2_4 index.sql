use menudb;

CREATE TABLE phone (
    phone_code INT PRIMARY KEY,
    phone_name VARCHAR(100),
    phone_price DECIMAL(10, 2)
);

INSERT INTO phone (phone_code , phone_name , phone_price )
VALUES (1, 'galaxyS23', 1200000),
       (2, 'iPhone14pro', 1433000),
       (3, 'galaxyZfold3', 1730000);

SELECT * FROM phone;

-- 실행계획 확인 (type = all: 모든 rows 검색)
explain select * from phone where phone_name = 'galaxy23';
-- 실행계획 확인 (type = const: 해당 rows 검색 = 1)
explain select * from phone where phone_code = 1;

create index idx_name on phone (phone_name);

show index from phone;

-- index를 활용한 검색 (row 1)
explain select * from phone where phone_name = 'galaxyS23' and phone_price = 1200000;

show index from phone;

drop index idx_name on phone;

show index from phone;


