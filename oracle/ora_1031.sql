select * from member;

select hire_date,round(hire_date,'Month')from employees;
select hire_date,trunc(hire_date,'Month')from employees;
select add_months(trunc(sysdate,'Month'),1)from dual;

select hire_date,add_months(trunc(hire_date,'month'),1)from employees;

select hire_date,add_months(hire_date,12),last_day(add_months(hire_date,12))from employees;

select name,sdate,last_day(add_months(sdate,12)) from students 
where last_day(add_months(sdate,12)) in ('24/08/31','24/11/30','24/09/30') ;
--년 월 일
select extract(month from sysdate) from dual;
select extract(year from sysdate) from dual;
select extract(day from sysdate) from dual;
---년 유ㅝㄹ 일 시 분초
select extract(minute from systimestamp) from dual;
select extract(hour from systimestamp) from dual;
select extract(second from systimestamp) from dual;
--substr : 문자에서 시작위치, 가져올 개수
select sysdate,substr(sysdate,4.10)from dual;

--날짜 형변환
select sysdate,to_char(sysdate,'yyyy-mm-dd')from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss day')from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd hh24:mi:ss dy')from dual;

select name,sdate,to_char(sdate,'yyyy/mm/dd')from students;

select kor from students where kor=70;
-- 뒤에 자리수 채우기 9: 빈공백 0 : 0으로 채움
select to_char(salary*1382.86*12,'000,000,999,999')from employees;

create table chartable2(
no number(4), kor number(10), kor_char varchar2(10), kor_mark varchar2(10)
);

insert into chartable values(
1,10000,to_char(10000,'00000000'),to_char(10000,'0,000,000')
);
insert into chartable2 values(
3,3000000,3000000,3000000
);
commit;
select * from chartable;

select '20241031',to_date('20241031')+2,sysdate+2 from dual;

delete chartable;
commit;

insert into chartable values(
3,30000,'0030000','3,000,000'
);

select * from chartable;

-- 날짜 -> 문자 to_char     ## 날짜포맷
-- 문자 -> 날짜 to_date     ## 날짜 사칙연산
-- 숫자 -> 문자 to_char     ## 천단위, 숫자앞에 0 을표시, 통화표시
-- 문자 -> 숫자 to_number ## 천단위 표시 , 천단위 삭제해서 사칙연산

select department_id from employees where department_id is null;
select emp_name,salary*commission_pct from employees;
select nvl(department_id,0) from employees ;
select nvl(to_char(department_id),ceo) from employees;
select sum(salary) from employees;
select round(avg(salary),2) from employees;

select sum(salary),round(avg(salary),2),max(salary),min(salary),median(salary) 
from employees where department_id=50;
select department_id,avg(salary) from employees group by department_id order by department_id desc;

select count(salary) from employees where salary> (select avg(salary) from employees);

select power(3,3) from dual;

select sysdate,to_char(sysdate,'YYYY"년"mm"월"dd"일"day') from dual;

select emp_name from employees;

select * from member where upper(name) = 'bryan';
--lpad: 왼쪽자리 채우기
--rpad: 오른쪽자리 채우기
--trin: 앞 ,뒤 공백 없애기 ltrin : 왼쪽 없애기 rtrin : 오른쪽 없애기
select 'john',lpad('jhon',10,'#'),rpad('jhon',10,'#') from dual;
select length('      aaa  '),length(trin('      aaa  ')),length(ltrin('      aaa  '))
,length(rtrin('      aaa  ')) from dual;
select * from employees;
select emp_name,hire_date,substr(hire_date,4.2) from employees where substr(hire_date,4.2)> 7;

SELECT emp_name, hire_date, TO_CHAR(hire_date, 'MM') AS month
FROM employees
WHERE TO_CHAR(hire_date, 'MM') > '07';

--replace 치환 translate 치환
select 'axyz', translate('jndlkasjkk','jk','ab')from dual;
select 'axyz', replace('jndlkasjkk','jk','ab')from dual;

select name,length(name) from students where length(name) >= 5;

select sum(salary), round(avg(salary),2) from employees;

select sum(eng), avg(eng), max(eng),min(eng) from students;

select name, to_char(sdate,'"등록일 : "YYYY"년"mm"월"dd"일"') from students;