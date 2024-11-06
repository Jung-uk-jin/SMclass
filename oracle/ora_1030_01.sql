select * from students order by total desc;
select * from employees order by hire_date asc;
select * from students order by kor desc, eng desc;
select * from employees order by hire_date asc, emp_name desc;

select -10 val, abs(-10) as abc from dual;

select kor,kor-eng,abs(kor-eng) from students; -- abs = 절대값
select 3.141592, floor(3.141592) from dual; --float = 소수점 버림
select 34.5678, round(34.5678) from dual; --round = 소수점 첫재짜리 반올림
select 34.5678, round(34.5678,2) from dual; --round(n,m) n의 소수점 m+1짜리에서 반올림
select 34.5678, trunc(34.5678,2) from dual; --trunc(n,m) n의 소수점 m+1짜리에서 버림
select ceil(34.5678) from dual; --ceil 올림
select 27/2, mod(27,2) from dual; -- mod 나머지
select  * from employees;
select * from employees where mod(employee_id,2)=1 order by employee_id asc;
select commission_pct from employees where commission_pct is not null;
select emp_name,trunc(salary*12+(salary*12)*commission_pct*1381.86795,1) as trunc from employees order by salary desc;

--시퀀스 ㅣ 자동으로 번호 부여
create sequence stu_seq
start with 1
increment by 1
minvalue 1
maxvalue 9999
nocycle
nocache;

select stu_seq.nextval from dual;

select stu_seq.currval from dual;
--게시판 만들기
create table board(
bno number(4), btitle varchar2(100), bcontent varchar2(4000), id varchar2(30),
bhit number(10), bdate date
);
insert into board values(
1,'제목입니다','내용입니다','aaa',1,sysdate
);
insert into board values(
stu_seq.nextval,'제목입니다2','내용입니다2','aaa',2,sysdate
);


select * from board;
commit;

create sequence board_seq
start with 14 --시작번호
increment by 1--증감 숫자
minvalue 1 -- 최소값
maxvalue 9999 -- 최대값
nocycle -- 1~9999d이상이 되면 다시 1시작
nocache -- 메모리에 시퀀스값을 미리 할당
;

insert into board values(
board_seq.nextval,'제목14','내용14','aaa',1,sysdate
);

drop table board;

create table board(
bno number(4), btitle varchar2(100), bcontent clob, -- 대용량 글자 타입
id varchar2(20),bgroup number(4) -- 답변달기 그룹팡
,bstep number(4), bindent number(4), bint number(10), bdate date
--답변 순서정의, 들여쓰기, 조회수, 등록일
);
insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,1,sysdate
);

select no,name,round(avg,2) from students where no>=100;
commit;
insert into students values(
student_seq.nextval,'홍길순',99,99,90,99+99+90,288/3,0,sysdate
);

delete from students where no=101;

select dept_seq.nextval from dual;

select '홀길동' from dual;
select length('홍길동') from dual; -- 문자길이
select lengthb('홍길동') from dual; -- byte 크기

select name,length(name) n from students order by n desc;
select * from students where total>=200 and no>=10 and no<=50 and name like '_e%';

select * from (select * from students where total>=200) where name like '_e%' and no >=30;

select no,name,total,rank() over(order by total desc) from students;

select * from students order by rank;

update students a 
set rank=(select ranks from (select no,rank() over(order by total desc) ranks from students)b
where a.no = b.no);
rollback;
delete from students where no = 103;

select no,name,rank() over(order by total desc) as ranks from students;

update students set rank=1 where no=102;
update students set rank=2 where no=96;
update students set rank=2 where no = 64;
update students set rank=4 where no = 49;
update students set rank=5 where no = 14;
select * from students order by total desc;

select no,name,rank() over(order by no desc) from students;
create table emp2 as select * from employees;
select * from emp2;


select rank() over(order by no desc) from students;

alter table emp2 add rank number(4); -- 테이블 컬럼 추가
desc emp2;
-- 숨김 visible 숨김 헤제
alter table emp2 modify email invisible;
alter table emp2 modify employee_id invisible;
alter table emp2 modify emp_name invisible;
alter table emp2 modify phone_number invisible;
alter table emp2 modify hire_date invisible;
alter table emp2 modify salary invisible;
alter table emp2 modify manager_id invisible;
alter table emp2 modify commission_pct invisible;
alter table emp2 modify retire_date invisible;
alter table emp2 modify department_id invisible;
alter table emp2 modify job_id invisible;
alter table emp2 modify create_date invisible;
alter table emp2 modify update_date invisible;
alter table emp2 modify rank invisible;
select * from emp2;
--컬럼 삭제
alter table emp2 drop column email;
alter table emp2 drop column phone_number;
alter table emp2 drop column hire_date;
alter table emp2 drop column retire_date;
alter table emp2 drop column create_date;
alter table emp2 drop column update_date;
alter table emp2 drop column commission_pct;
alter table emp2 drop column salary;
--컬럼 추가
alter table emp2 add department_name varchar2(80);
select * from departments;
select * from emp2;
update emp2 e set e.department_name = (select d 
from(select departmend_id,department_name d from departments) e2
where e.department_id = e2.department_id);

select department_id, department_name from emp2;
select * from stu;
create table stu as select * from students;
drop table stu;
commit;
alter table stu add total number(3);
alter table stu add avg number;
alter table stu add rank number(3);

select * from stu order by total desc;
desc stu;
update stu a set rank = (select ranks from (select no,rank() over (order by total desc)
ranks from students) b where a.no=b.no);

--날짜 함수
select sysdate from dual;
select sysdate-1 from dual;
select sysdate+30 from dual;
create table dateable(
no number(4), predate date, today date, nextdate date
);
insert into dateable values(
1,sysdate-30,sysdate,sysdate+180
);
select no,predate,today 가입일, nextdate 만기일 from dateable;

select * from employees;
select id,name,mdate,round(sysdate-mdate) from member where sysdate>=  mdate+180;

select emp_name,round(sysdate-hire_date) from employees;
--입사일 현재일 사이의 개월 수 
select hire_date,sysdate,months_between(sysdate,hire_date)from employees;

select hire_date, add_months(hire_date,3) from employees;
select sysdate,next_day(sysdate,'수요일') from dual; -- 다음주 
select hire_date, last_day(hire_date) from employees; --마지막날
select sysdate, last_day(sysdate)from dual;

--형변환 함수
select to_char(sysdate,'yyyy-mm-dd')from dual;
select to_char('2024/01/01','yyyy-mm-dd')from dual;

select * from member where id='aaa' and pw='1111';
select * from member;
update member set id='abc',pw='1111', name='정욱진', email='ukjin32@naver.com' where id='Trineman';
commit;

select * from member where id='eee';