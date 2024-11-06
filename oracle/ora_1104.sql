create table emp02(
empno number(4) unique, --unique 중복 안됨, not null- null 사용 불가
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02 values(
1,'홍길동','clerk',2
);
insert into emp02 values(
2,'유관순',null,null
);
insert into emp02 values(
2,'김구',null,null
);
select * from emp02;

drop table emp02;
delete emp02 where empno is null;
commit;
alter table emp02 modify emp02 number(4) not null;

create table men(
id varchar2(30),
pw varchar2(30) not null,
name varchar2(10) default '무명',
gender varchar2(6) check(gender in('Male','Female')) --- male, female MALE FEMALE));
);

insert into men values(
'aaa','1111','홍길동','Male'
);

insert into men values(
'bbb','1111','유관순','Female'
);

commit;

create table board2 (
bno number(4) primary key,
btitle varchar2(1000) not null,
id varchar2(30),
constraint fk_board2_id foreign key(id) references mem(id)
);
select * from mem;
delete mem where id='aaa';
-- 외래키로 등록시 부모키에 해당 값이 없을시 에러
insert into board2 values(
4,'제목4','bbb'
);
-- 외래키 삭제
alter table board2 drop constraint fk_board2_id;
-- 부모키 삭제시, 외래키로 등록된 값들을 모두 삭제
alter table board2
add constraint fk_board2_id foreign key (id)
references mem(id) on delete cascade;  -- on delete set null
-- default : on delete restricted : 부모키 삭제시, 외래키에 등록된 값이 있으면, 삭제가 되지 않음.
-- on delete set null : 부모키 삭제시, 외래키로 등록된 값을 삭제는 하지 않고, 해당되는 컬럼값만 null 처리
-- 부모테이블의 aaa삭제시, 자식테이블의 aaa글이 모두 삭제
delete mem where id='aaa';
select * from mem;
select * from board2;

select id,pw,name,deptno, decode (deptno, 10,'총무부',20,'인사부',30,'마케팅');


select * from employees;

select job_id from employees;

select substr(job_id,4) j_id from employees where substr(job_id,4) = 'CLERK';
select substr(job_id,4) j_id from employees where substr(job_id,4) in ('CLERK','REP','MAN');

select substr(job_id,4) j_id , salary,
decode (substr(job_id,4),
'CLERK',salary*1.05,
'REP', salary*1.1,
'MAN',salary*1.15
) sal
from employees
where substr(job_id,4) in ('CLERK','REP','MAN')
;



create table lavel_data (
	id VARCHAR2(50) primary key,
	lavel number(1) not null
);
insert into lavel_data (id, lavel) values ('Arlen', 4);
insert into lavel_data (id, lavel) values ('Catie', 4);
insert into lavel_data (id, lavel) values ('Adoree', 5);
insert into lavel_data (id, lavel) values ('Cher', 4);
insert into lavel_data (id, lavel) values ('Dorita', 5);
insert into lavel_data (id, lavel) values ('Zulema', 1);
insert into lavel_data (id, lavel) values ('Richy', 4);
insert into lavel_data (id, lavel) values ('James', 5);
insert into lavel_data (id, lavel) values ('Aeriel', 5);
insert into lavel_data (id, lavel) values ('Reinald', 3);
insert into lavel_data (id, lavel) values ('Bernardina', 1);
insert into lavel_data (id, lavel) values ('Tiertza', 2);
insert into lavel_data (id, lavel) values ('Carolyne', 5);
insert into lavel_data (id, lavel) values ('Jonis', 1);
insert into lavel_data (id, lavel) values ('Abigael', 5);
insert into lavel_data (id, lavel) values ('Pauli', 4);
insert into lavel_data (id, lavel) values ('Sheffie', 2);
insert into lavel_data (id, lavel) values ('Tully', 2);
insert into lavel_data (id, lavel) values ('Ricard', 5);
insert into lavel_data (id, lavel) values ('Jameson', 3);
insert into lavel_data (id, lavel) values ('Thorstein', 1);
insert into lavel_data (id, lavel) values ('Arlyne', 5);
insert into lavel_data (id, lavel) values ('Mela', 5);
insert into lavel_data (id, lavel) values ('Yetta', 3);
insert into lavel_data (id, lavel) values ('Corilla', 4);
insert into lavel_data (id, lavel) values ('Adoree', 1);
insert into lavel_data (id, lavel) values ('Sabine', 3);
insert into lavel_data (id, lavel) values ('Nelson', 3);
insert into lavel_data (id, lavel) values ('Isahella', 5);
insert into lavel_data (id, lavel) values ('Mandel', 5);
insert into lavel_data (id, lavel) values ('Sasha', 4);
insert into lavel_data (id, lavel) values ('Deanne', 1);
insert into lavel_data (id, lavel) values ('Thorny', 1);
insert into lavel_data (id, lavel) values ('Jacki', 3);
insert into lavel_data (id, lavel) values ('Sibby', 2);
insert into lavel_data (id, lavel) values ('Jack', 2);
insert into lavel_data (id, lavel) values ('Chandra', 2);
insert into lavel_data (id, lavel) values ('Cecilla', 5);
insert into lavel_data (id, lavel) values ('Saunder', 1);
insert into lavel_data (id, lavel) values ('Way', 4);
insert into lavel_data (id, lavel) values ('Velma', 3);
insert into lavel_data (id, lavel) values ('Keelia', 1);
insert into lavel_data (id, lavel) values ('Clay', 4);
insert into lavel_data (id, lavel) values ('Grace', 2);
insert into lavel_data (id, lavel) values ('Maura', 5);
insert into lavel_data (id, lavel) values ('Karolina', 4);
insert into lavel_data (id, lavel) values ('Mal', 5);
insert into lavel_data (id, lavel) values ('Annette', 4);
insert into lavel_data (id, lavel) values ('Issy', 2);
insert into lavel_data (id, lavel) values ('Reid', 2);
insert into lavel_data (id, lavel) values ('Dall', 4);
insert into lavel_data (id, lavel) values ('Sukey', 2);
insert into lavel_data (id, lavel) values ('Etty', 5);
insert into lavel_data (id, lavel) values ('Kendall', 5);
insert into lavel_data (id, lavel) values ('Gibby', 4);
insert into lavel_data (id, lavel) values ('Kylila', 2);
insert into lavel_data (id, lavel) values ('Orelia', 2);
insert into lavel_data (id, lavel) values ('Alexei', 4);
insert into lavel_data (id, lavel) values ('Iorgo', 1);
insert into lavel_data (id, lavel) values ('Clive', 1);
insert into lavel_data (id, lavel) values ('Roger', 1);
insert into lavel_data (id, lavel) values ('Halette', 3);
insert into lavel_data (id, lavel) values ('Clyve', 3);
insert into lavel_data (id, lavel) values ('Peadar', 1);
insert into lavel_data (id, lavel) values ('Mose', 4);
insert into lavel_data (id, lavel) values ('Raimundo', 3);
insert into lavel_data (id, lavel) values ('Glori', 1);
insert into lavel_data (id, lavel) values ('Merrel', 2);
insert into lavel_data (id, lavel) values ('Ulberto', 2);
insert into lavel_data (id, lavel) values ('Bren', 4);
insert into lavel_data (id, lavel) values ('Ker', 2);
insert into lavel_data (id, lavel) values ('Rosalinda', 1);
insert into lavel_data (id, lavel) values ('Delphinia', 5);
insert into lavel_data (id, lavel) values ('Johnette', 3);
insert into lavel_data (id, lavel) values ('Marilyn', 3);
insert into lavel_data (id, lavel) values ('Paddy', 2);
insert into lavel_data (id, lavel) values ('Antony', 3);
insert into lavel_data (id, lavel) values ('Kinna', 5);
insert into lavel_data (id, lavel) values ('Rogers', 5);
insert into lavel_data (id, lavel) values ('Zolly', 5);
insert into lavel_data (id, lavel) values ('Lance', 1);
insert into lavel_data (id, lavel) values ('Carroll', 2);
insert into lavel_data (id, lavel) values ('Geralda', 2);
insert into lavel_data (id, lavel) values ('Riobard', 2);
insert into lavel_data (id, lavel) values ('Sunshine', 4);
insert into lavel_data (id, lavel) values ('Betteanne', 2);
insert into lavel_data (id, lavel) values ('Andrea', 1);
insert into lavel_data (id, lavel) values ('Theresina', 3);
insert into lavel_data (id, lavel) values ('Koenraad', 4);
insert into lavel_data (id, lavel) values ('Eydie', 1);
insert into lavel_data (id, lavel) values ('Karolina', 2);
insert into lavel_data (id, lavel) values ('Sutton', 5);
insert into lavel_data (id, lavel) values ('Ikey', 5);
insert into lavel_data (id, lavel) values ('Ugo', 1);
insert into lavel_data (id, lavel) values ('Mallory', 4);
insert into lavel_data (id, lavel) values ('Mariska', 2);
insert into lavel_data (id, lavel) values ('Edmund', 3);
insert into lavel_data (id, lavel) values ('Twyla', 5);
insert into lavel_data (id, lavel) values ('Laney', 5);
insert into lavel_data (id, lavel) values ('Onida', 4);
commit;
select * from lavel_data;

--1 : 100포인트 , 2:1000포인트 3:5000포인트 4ㅣ10000포인트 5, 20000포인트
--point decode 이용
select id, lavel,
decode ( lavel,
1,100,
2,1000,
3,5000,
4,10000,
5,20000) point 
from lavel_data ;
--1 : 100포인트 , 2:3:5000포인트 4ㅣ 5, 20000포인트
--point case 이용
select id,lavel,
case 
when lavel=1 then '100p'
when lavel=2 or lavel=3 then '5000p'
when lavel>=4 then '20000p'
end as point
from lavel_data;


--avg 90이상 A 80B ------

--컬럼 추가
select * from stu;
alter table stu add result varchar2(2);

select 
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
when avg<60 then 'F'
end as result
from stu;

update stu set result = (
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
when avg<60 then 'F'
end
);

select * from stu;
--rank() over : 중복개수만큼 다음 순위 증가
select name,total, rank() over(order by total) from stu order by no;
--dense_over : 중복이 존재해도 순차적으로 표시
select no, name, total, dense_rank() over (order by total desc) from stu;

update stu set rank = (
select dense_rank() over (order by total desc) from stu
);

select ranks from (
select rank() over(order by total desc) from stu b
);

update stu a set ranks = (
select ranks from (
select no,rank() over (order by total desc) as ranks from stu) b
where a.no=b.no
);

--salayu 5000이하 *15 5000~8000 *10 8000이상5%
select * from employees;
select emp_name, salary, 
case
when salary<=5000 then salary + salary*15/100
when salary>5000 and salary <=8000 then salary + salary*10/100
when salary>8000 then salary + salary*5/100
end as up_sal
from employees;

select emp_name from employees where emp_name like '%M%';

select emp_name, 
case 
when emp_name like '%D%' then salary + salary * 10/100
when emp_name like '%M%' then salary + salary * 5/100
else salary
end as up_sal
from employees;
select * from employees;
select count(*) from employees where commission_pct is not null;
select department_id, count(*) from employees group by department_id order by department_id;

select department_id, avg(salary),count(salary) from employees group by department_id;

select department_id,avg(salary),count(salary) from employees
group by department_id having  < avg(salary);

select avg(salary) from employees;

select department_id, count(salary) from employees group by department_id having avg(salary) >6000;

select department_id, count(salary) from employees group by department_id;

select department_id,emp_name,salary from employees where department_id=30;
select avg(salary) from employees where department_id ;

select department_id, max(salary), min(salary) from employees group by department_id having max(salary)>=5000
order by department_id desc;

select emp_name, department_id from employees where emp_name='Donald OConnell';
select department_name from departments where department_id=50;
--join  사용법
--cross join : 특별한 키워드 없이 두개의 테이블 검색
select * from employees ;
select * from departments;
select * from employees,departments where employees.department_id = departments.department_id;
select count(*) from employees,departments where employees.department_id = departments.department_id(+); -- output join
select count(*) from employees,departments where employees.department_id = departments.department_id;

select * from member;
select * from board;
select bno,btitle,bcontent,id from board;

select bno,btitle,bcontent,email,phone from member a ,board b
where a.id=b.id;

select * from jobs;
select * from employees;
select * from departments;
select employee_id,emp_name,job_title,a.job_id from jobs a, employees b
where a.job_id=b.job_id;

select employee_id,emp_name,b.department_id,department_name,b.job_id,job_title from jobs a, employees b, departments c
where a.job_id= b.job_id and b.department_id = c.department_id;
select * from board;
select bno,btitle, bgroup,bstep,bindent,bint,bdate from board a, member b
where a.id=b.id;

select employee_id,emp_name, salary, a.department_id,department_name from  employees a, departments b
where a.department_id=b.department_id and salary < (select avg(salary) from employees);

select employee_id, emp_name,salary,a.department_id,department_name from employees a, departments b
where a.department_id = b.department_id and 
salary < (
select salarys from (department_id, avg(salary) salarys from employees group by department_id) c
where a.department_id = c.department_id);

select employee_id,emp_name,department_name,a.department_id,job_id from employees a, departments b
where a.department_id = b.department_id and substr(job_id,4)='CLERK';

create table stu_grade(
grade varchar2(20),
loavg number(5.2),
hiavg number(5.2)
);
drop table stu_grade;
commit;
insert into stu_grade values('F',0,59.99);
insert into stu_grade values('D',60,69.99);
insert into stu_grade values('C',70,79.99);
insert into stu_grade values('B',80,89.99);
insert into stu_grade values('A',90,100);

select * from stu;
select * from stu_grade;
select name,total,avg,grade from students,stu_grade where avg between loavg and hiavg;

select name,total,rank() over (order by total desc) from stu_grade, stu where result between loavg and hiavg;

select a.employee_id,a.emp_name,manager_id from employees where employee_id=124;
select a.employee_id,a.emp_name,a.manager_id,b.emp_name from employees a, employees b
where a.manager_id = b.employee_id and a.manager_id=124;


