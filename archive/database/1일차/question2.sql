use employeedb;

--   `EMP_ID` varchar(3) NOT NULL COMMENT '사원번호',
--   `EMP_NAME` varchar(20) NOT NULL COMMENT '직원명',
--   `EMP_NO` char(14) NOT NULL COMMENT '주민등록번호',
--   `EMAIL` varchar(35) DEFAULT NULL COMMENT '이메일',
--   `PHONE` varchar(12) DEFAULT NULL COMMENT '전화번호',
--   `DEPT_CODE` char(2) DEFAULT NULL COMMENT '부서코드',
--   `JOB_CODE` char(2) NOT NULL COMMENT '직급코드',
--   `SAL_LEVEL` char(2) NOT NULL COMMENT '급여등급',
--   `SALARY` decimal(10,0) DEFAULT NULL COMMENT '급여',
--   `BONUS` float DEFAULT NULL COMMENT '보너스율',
--   `MANAGER_ID` varchar(3) DEFAULT NULL COMMENT '관리자사번',
--   `HIRE_DATE` date DEFAULT NULL COMMENT '입사일',
--   `ENT_DATE` date DEFAULT NULL COMMENT '퇴사일',
--   `ENT_YN` char(1) DEFAULT 'N' COMMENT '퇴직여부',

-- Q1
select emp_id, emp_name, phone, hire_date, ent_yn from employee e
where e.ENT_YN = 'N' and e.PHONE like '%2'
order by hire_date 
limit 3

-- Q2
select e.EMP_NAME, j.JOB_NAME, e.SALARY, e.EMP_ID, e.EMAIL, e.PHONE, e.HIRE_DATE
from employee e join job j on j.JOB_CODE = e.JOB_CODE 
where j.JOB_NAME = '대리' and e.ENT_YN = 'N'
order by e.SALARY desc;

-- Q3
select e.DEPT_CODE as 부서명, count(*) as 인원, sum(e.SALARY) as 급여합계, avg(e.SALARY) as 급여평균
from employee e
where e.ENT_YN = 'N'
group by e.DEPT_CODE
with rollup;

-- Q4
select e.EMP_NAME, e.EMP_NO, e.PHONE, j.JOB_NAME 
from employee e join job j on e.JOB_CODE = j.JOB_CODE
order by e.HIRE_DATE asc;

-- Q5
select count(*)
from employee e
where e.MANAGER_ID is not null;

select count(*)
from employee e
where e.MANAGER_ID in (select e2.EMP_ID from employee e2);
select count(*)
from employee e join employee e2 on e.MANAGER_ID = e2.EMP_ID;

select e.EMP_NAME, e.MANAGER_ID
from employee e;

select e.EMP_NAME, e.MANAGER_ID
from employee e join employee e2 on e.MANAGER_ID = e2.EMP_ID;
