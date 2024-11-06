--select * from employees;
--테이블 생성
create table students(
no number(4), name varchar2(20),kor number(3), eng number(3), math number(3),
total number(3), avg number(5), rank number(4)
);
--데이터 입력
insert into students (no,name,kor,eng,math,total,avg,rank) values(
1,'홍길동',100,100,99,299,(299/3),1
);
insert into students (no,name,kor,eng,math,total,avg,rank) values(
2,'유관순',100,90,99,289,(289/3),1
);

--검색
select no,name,kor,eng,math,total,avg,rank from students;


select * from students;
--테이블 삭제
drop table students;

create table member(
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);
insert into member (id, pw, name, phone) values(
'aaa',1111,'홍길동','010-1111-1111'
);
insert into member values(
'bbb',2222,'유관순','010-2222-2222'
);
select *from member;
commit;
insert into member (id, name) values(
'ccc','이순신'
);

--데이터 확정 : commit, rollback
commit;

select emp_name, salary from employees;

update member set name = '홍길자' where id='aaa';

delete member where id = 'ccc';