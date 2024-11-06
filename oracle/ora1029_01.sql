create table member(
no number(4),
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20),
mdate date
);

insert into member values(
1,'aaa','1111','홍길동','010-1111-1111','2024-10-29'
);

insert into member values(
2,'aaa','2222','유관순','010-1111-1111','2024-10-29'
);

select * from member;

commit;
rollback;

delete member where no=2;

update member set name='홍길자' where no=1;

create table students (
stuno number(4),
name varchar2(20),
kor number(3),
eng number(3),
total number(3),
sdate date
);

insert into students values(
1,'홍길동',100,100,100+100,sysdate
);
-- 특정컬럼만 입력하면 컬럼입력
insert into students (stuno,name) values(
2,'유관순'
);
select * from students;

select * from employees;

create table emp2 as select * from employees;

drop table students;

create table emp3 as select * from employees where 1=2;

select * from emp3;

select count(*) from emp2;

create table member2 as select * from member where 1=2;
insert into member2 select * from member;
select * from member2;
commit;


desc member;

update member set no='';
commit;
alter table member modify no varchar2(10);
select * from member;
-- 칼럼의 이름 변경
alter table member rename column no to memberno;


select employee_id, emp_name, hire_date from employees;
create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);
select * from students;


create table students (
	no number(4),
	name VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(3),
	avg number,
	rank number(3),
	sdate DATE
);
select kor,eng,kor-eng from students;

select concat(employee_id,emp_name) from employees;
select to_char(salary*1384,'999,999,999') from employees;

select emp_name,salary,salary*1384 from employees;

create table stu(
no number(4), name varchar2(20), kor number(3)
);
insert into stu values(1,'홍길동',100);
insert into stu values(2,'유관순',99);

commit;
insert into stu values(3,'',0);
insert into stu values(4,null,null);

select * from stu;
select * from stu where name is not null;
select no,name,kor,kor+100 from stu;
select no,name,kor,nv1(kor,0)+100 from stu;
select salary,salary*12,salary*12+(salary*12)*commision_pct*0.01 from employees;


--as 특수문자, 사이공간까지 컬럼명으로 사용가능

drop table students;
create table students(
no number(3), name varchar2(20), kor number(3), eng number(3), math number(3),
total number(3), avg number(6,2), rank number(3), sdate date
);
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (1, '홍길동', 77, 70, 92, 239, 79.6666666667, 0, '2023-12-02');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (2, '유관순', 89, 69, 55, 213, 71, 0, '2024-01-19');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (3, '이순신', 75, 89, 53, 217, 72.3333333333, 0, '2024-04-16');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (4, '강감찬', 85, 91, 81, 257, 85.6666666667, 0, '2023-11-23');
insert into students (no, name, kor, eng, math, total, avg, rank, sdate) values (5, '김구', 62, 71, 54, 187, 62.3333333333, 0, '2024-09-09');


select no as 번호, name as 이름, kor as 국어, eng as 영어, math as 수학, total as 합계, avg as 평균, rank as 등수,
sdate as 등록일 from students;
 
 select * from students;
 
select department_id from employees;
select distinct department_id from employees;
select distinct department_id from employees order by department_id Desc;

select distinct job_id from employees;
select substr(job_id,0,2) from employees;
select distinct substr(job_id,4) from employees;

select * from employees where manager_id=124;
select * from employees where job_id='SH_CLERK';


select * from students where total>250;
select * from students where total>250 and kor>90 order by kor desc;
select * from students where eng>=70 and eng<=90;

select * from employees where salary>=5000 and salary <= 8000;
select * from employees where salary !=7000;

select count(*) from employees where department_id != 50;

select * from employees where department_id!=50;

select count(*) from employees where department_id is null;

select employee_id,emp_name,salary from employees where salary<=4000;
select employee_id as 사원번호, emp_name as 이름, salary as 급여 from employees where salary<=4000;

select * from employees where hire_date <='1999/12/31';

select count(*) from students where kor>=90 or eng >= 90;

select * from students;
select * from employees where department_id=80 and substr(job_id,4)='MAN';

select commission_pct from employees where commission_pct=0.2 or commission_pct=0.3  or commission_pct=0.5;

select * from employees where employee_id=110 or employee_id=120 or  employee_id=130;

select * from employees where hire_date between '2002/06/17' and '2004/12/31';
select * from employees where hire_date in('2004/12/31','2002/06/17');
select * from employees where substr(jod_id,4) ='MAN';

select * from employees where job_id like '%MAN';
select * from employees where job_id like 'ST%';
select * from employees where emp_name like '%a%';

select * from employees where emp_name like '_t%';
select * from employees where emp_name like'___v%';
select * from employees where emp_name like'%l_';
select * from employees where emp_name like'D%';

select * from employees where employee_id>=120;


select salary from employees order by salary desc;