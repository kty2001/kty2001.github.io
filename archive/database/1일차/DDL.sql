USE menudb;

-- tb1 테이블 생성
create table if not exists TB1 (
	pk INT primary key,
	fk INT,
	col1 varchar(255),
	check(col1 in ('Y', 'N'))
) engine = INNODB;

-- 테이블 컬럼 확인
describe tb1;

-- 테이블 값 추가
insert into tb1 values (1, 10, 'Y');

-- tb1 데이터 확인
select * from tb1;

-- tb2 생성
CREATE TABLE IF NOT EXISTS tb2 (
    pk INT AUTO_INCREMENT PRIMARY KEY,
    fk INT,
    col1 VARCHAR(255),
    CHECK(col1 IN ('Y', 'N'))
) ENGINE=INNODB;

INSERT INTO tb2 VALUES (null, 10, 'Y');
INSERT INTO tb2 VALUES (null, 20, 'Y');
SELECT * FROM tb2;

describe tb2;

alter table tb2 add col2 int not null;

describe tb2;

-- col2 not null 오류 발생
INSERT INTO tb2 VALUES (null, 20, 'Y', null);

alter table tb2 change column fk change_fk int not null;

describe tb2;

alter table tb2 drop primary key;

alter table tb2 modify pk int;

describe tb2;

alter table tb2 drop primary key;

describe tb2;

alter table tb2 add primary key(pk);

describe tb2;

alter table tb2 add col3 date not null, add col4 tinyint not null;

alter table tb2 add col3 date not null;

-- MySQL db 서버 전역 sql 모드 설정
select @@global.sql_mode;

-- 0으로 채워진 DATE 컬럼 제약조건 삭제
set global sql_mode = '';

alter table tb2 add col3 date not null, add col4 tinyint not null;

describe tb2;

-- tb6 테이블 생성
CREATE TABLE IF NOT EXISTS tb6 (
  pk INT AUTO_INCREMENT PRIMARY KEY,
  fk INT,
  col1 VARCHAR(255),
  CHECK(col1 IN ('Y', 'N'))
) ENGINE=INNODB;

-- 4개 행 데이터 INSERT
INSERT INTO tb6 VALUES (null, 10, 'Y');
INSERT INTO tb6 VALUES (null, 20, 'Y');
INSERT INTO tb6 VALUES (null, 30, 'Y');
INSERT INTO tb6 VALUES (null, 40, 'Y');

-- 제대로 INSERT 되었는지 확인
SELECT * FROM tb6;

-- 테이블 초기화 하기
-- TRUNCATE TABLE tb6;
TRUNCATE tb6;    -- TABLE 키워드 생략 가능

SELECT * FROM tb6;

-- 문제 풀다 만 거
-- create table if not exists member_info (
-- 	team_code int primary key,
-- 	team_name varchar(100),
-- 	team_detail varchar(500),
-- 	use_yn char(2)
-- ) engine=INNODB;
-- 
-- create table if not exists team_info (
-- 	team_code int primary key,
-- 	team_name varchar(100),
-- 	team_detail varchar(500),
-- 	use_yn char(2)
-- ) engine=INNODB;

