--join 
--inner join equl join non equl join self join outer join
select * from employees a,departments b where a.department_id = b.department_id;

create table stu_grade(
grade varchar2(20),
loavg number(5,2),
hiavg number(5,2)
);
insert into stu_grade values(
'F',0,59.99
);
insert into stu_grade values(
'D',60,69.99
);
insert into stu_grade values(
'C',70,79.99
);
insert into stu_grade values(
'B',80,89.99
);
insert into stu_grade values(
'A',90,100
);
commit;
select name,avg,grade from students, stu_grade
where avg between loavg and hiavg;

select a.employee_id, a.emp_name, a.manager_id, b.emp_name from employees a, employees b
where a.manager_id = b.employee_id;

select * from stu_grade;
alter table stu drop column result;
alter table stu add result varchar2(10);

select name, avg,result,grade from stu, stu_grade
where avg between loavg and hiavg;
select * from stu;
update stu set result = (select grade from stu_grade where avg between loavg and hiavg);
-- non-equi join update구문
update stu a set result = (
select grades from (
select no,grade as grades
from stu,stu_grade
where avg between loavg and hiavg
) b
where a.no = b.no
);
select * from stu;
update stu set rank=0;
select no,name,avg,rank,rank() over(order by avg desc) as ranks from stu;
update stu a set rank = (select rank from(select no,rank() over(order by avg desc) from stu)b where a.no=b.no) ;

select employee_id,emp_name, manager_id from employees;

select count(manager_id) from employees where manager_id is not null;

select nvl(manager_id,0) from employees;
select nvl(to_char(manager_id),'CEO') from employees;

select a.employee_id,a.emp_name,a.manager_id,b.emp_name,a.salary
from employees a, employees b
where a.manager_id = b.employee_id(+);

--부서번호, 부서명 사원번호 사원명
select employee_id,emp_name,a.department_id, department_name from employees a, departments b
where a.department_id(+) = b.department_id;

select department_id,department_name from employees natural join departments;

select employee_id,emp_name,a.department_id, department_name from employees a left outer join departments b
on a.department_id=b.department_id;

--union : 두개의 검색 결과를 합치는것 중복제외
select * from students where total >=250 union all
select * from students where name like '%a%';

select employee_id,emp_name from employees union select no,name from students;
select * from employees;
select emp_name,department_id from employees where department_id=50 union
select department_id, department_name from departments; 

select department_id, department_name from departments a where not exists(select 1 from employees b 
where a.department_id = b.department_id);
select distinct department_id from employees;


select name,mdate from member union
select name,sdate from students;


create table board2 (
	bno number(4),
	btitle VARCHAR2(50),
	bcontent VARCHAR2(50),
	id VARCHAR2(50),
	bgroup number(4),
	bstep number(4),
	bindent number(4),
	bhit number(4),
	bfile VARCHAR2(50)
);

insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (1, 'Netaji Subhash Chandra Bose International Airport', 'Staff Scientist', 'aaa', 1, 0, 0, 0, 'Dimanche');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (2, 'Pala Airport', 'Human Resources Assistant III', 'bbb', 2, 0, 0, 0, 'Doleman');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (3, 'Barriles Airport', 'Marketing Assistant', 'ccc', 3, 0, 0, 0, 'Tatum');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (4, 'Kristiansund Airport (Kvernberget)', 'Senior Editor', 'ddd', 4, 0, 0, 0, 'Himpson');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (5, 'Hawke''s Bay Airport', 'Statistician III', 'eee', 5, 0, 0, 0, 'Fennelly');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (6, 'Bozoum Airport', 'Web Designer I', 'abc', 6, 0, 0, 0, 'Velde');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (7, 'Baitadi Airport', 'Engineer II', 'Faustina', 7, 0, 0, 0, 'Scimone');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (8, 'Rurenabaque Airport', 'Safety Technician I', 'Gilly', 8, 0, 0, 0, 'Greystoke');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (9, 'Industrial Airpark', 'Editor', 'Godart', 9, 0, 0, 0, 'Springthorpe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (10, 'Barreirinhas Airport', 'Account Coordinator', 'Cole', 10, 0, 0, 0, 'Jerram');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (11, 'Toledo Airport', 'Safety Technician IV', 'Mannie', 11, 0, 0, 0, 'Longden');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (12, 'Tamale Airport', 'Occupational Therapist', 'Sofie', 12, 0, 0, 0, 'Cheeld');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (13, 'Budapest Liszt Ferenc International Airport', 'Dental Hygienist', 'Danyette', 13, 0, 0, 0, 'Grigolli');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (14, 'Juan Pablo Pérez Alfonso Airport', 'Systems Administrator I', 'Irv', 14, 0, 0, 0, 'Lyster');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (15, 'Kangaatsiaq Heliport', 'Product Engineer', 'Maggi', 15, 0, 0, 0, 'O''Ferris');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (16, 'Dabo Airport', 'Environmental Specialist', 'Theo', 16, 0, 0, 0, 'Sothcott');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (17, 'Rivers Airport', 'Mechanical Systems Engineer', 'Svend', 17, 0, 0, 0, 'Lidgley');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (18, 'Fitzroy Crossing Airport', 'Project Manager', 'Harp', 18, 0, 0, 0, 'Wallworke');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (19, 'Minnipa Airport', 'Environmental Specialist', 'Dorelle', 19, 0, 0, 0, 'Farmar');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (20, 'Arboletes Airport', 'General Manager', 'Caresse', 20, 0, 0, 0, 'Camacke');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (21, 'Yakutat Airport', 'Teacher', 'Bibby', 21, 0, 0, 0, 'Gai');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (22, 'Zahedan International Airport', 'Actuary', 'Viv', 22, 0, 0, 0, 'Penrice');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (23, 'Xingyi Airport', 'VP Marketing', 'Gris', 23, 0, 0, 0, 'Liddicoat');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (24, 'La Chorrera Airport', 'Assistant Manager', 'Rouvin', 24, 0, 0, 0, 'Brassington');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (25, 'Peretola Airport', 'Research Assistant III', 'Thane', 25, 0, 0, 0, 'Pittel');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (26, 'Flughafen München-Riem', 'Account Representative II', 'Dore', 26, 0, 0, 0, 'Newcom');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (27, 'Merritt Island Airport', 'Analyst Programmer', 'Jacobo', 27, 0, 0, 0, 'Bragginton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (28, 'Anaco Airport', 'Electrical Engineer', 'Stanislaus', 28, 0, 0, 0, 'Eppson');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (29, 'Barinas Airport', 'Operator', 'Ariana', 29, 0, 0, 0, 'Duchart');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (30, 'Araxos Airport', 'Senior Editor', 'Delphinia', 30, 0, 0, 0, 'Wheway');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (31, 'Kamloops Airport', 'Research Associate', 'Gannon', 31, 0, 0, 0, 'Matches');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (32, 'Tzaneen Airport', 'Quality Control Specialist', 'Dorree', 32, 0, 0, 0, 'Frondt');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (33, 'Mayajigua Airport', 'VP Accounting', 'Kellia', 33, 0, 0, 0, 'Miettinen');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (34, 'Kadugli Airport', 'Help Desk Technician', 'Magdaia', 34, 0, 0, 0, 'MacTeague');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (35, 'Miyazaki Airport', 'Software Consultant', 'Brenda', 35, 0, 0, 0, 'Pentony');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (36, 'Escuela Mariscal Sucre Airport', 'Data Coordinator', 'Arman', 36, 0, 0, 0, 'Jarvie');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (37, 'Arua Airport', 'Research Associate', 'Alexandro', 37, 0, 0, 0, 'Lecointe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (38, 'Lagunillas Airport', 'Account Representative I', 'Christye', 38, 0, 0, 0, 'Smitham');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (39, 'Buzzards Point Seaplane Base', 'Operator', 'Nedda', 39, 0, 0, 0, 'Cardoe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (40, 'Paraparaumu Airport', 'Assistant Professor', 'Linnet', 40, 0, 0, 0, 'Swane');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (41, 'Wudalianchi Dedu Airport', 'Analog Circuit Design manager', 'Guenna', 41, 0, 0, 0, 'Pillinger');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (42, 'D. Casimiro Szlapelis Airport', 'Payment Adjustment Coordinator', 'Ozzy', 42, 0, 0, 0, 'Ogbourne');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (43, 'Pondicherry Airport', 'Media Manager III', 'Lev', 43, 0, 0, 0, 'Marritt');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (44, 'Tonghua Sanyuanpu Airport', 'Statistician IV', 'Franni', 44, 0, 0, 0, 'Saldler');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (45, 'Fort Albany Airport', 'Professor', 'Katerina', 45, 0, 0, 0, 'Golland');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (46, 'Žilina Airport', 'Accounting Assistant I', 'Whittaker', 46, 0, 0, 0, 'Owbridge');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (47, 'Soekarno-Hatta International Airport', 'Project Manager', 'Rosemaria', 47, 0, 0, 0, 'Pohl');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (48, 'Sebba Airport', 'Actuary', 'Keelby', 48, 0, 0, 0, 'Palatini');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (49, 'Rundu Airport', 'Health Coach I', 'Bonni', 49, 0, 0, 0, 'Boniface');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (50, 'London Stansted Airport', 'Paralegal', 'Martin', 50, 0, 0, 0, 'Pentlow');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (51, 'Rustaq Airport', 'Chemical Engineer', 'Karlen', 51, 0, 0, 0, 'Dell Casa');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (52, 'Ratnagiri Airport', 'Pharmacist', 'Constantin', 52, 0, 0, 0, 'Trees');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (53, 'Cooinda Airport', 'Database Administrator III', 'Lauretta', 53, 0, 0, 0, 'Hubball');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (54, 'Lisala Airport', 'Project Manager', 'Merrili', 54, 0, 0, 0, 'Cady');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (55, 'Accomack County Airport', 'Geologist II', 'Honor', 55, 0, 0, 0, 'Amber');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (56, 'Municipal de Linares Airport', 'Research Nurse', 'Ashby', 56, 0, 0, 0, 'Larmuth');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (57, 'Wrangell Airport', 'Professor', 'Sydel', 57, 0, 0, 0, 'Tuer');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (58, 'Querétaro Intercontinental Airport', 'Senior Developer', 'Paige', 58, 0, 0, 0, 'Kann');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (59, 'Ruhengeri Airport', 'Food Chemist', 'Mathe', 59, 0, 0, 0, 'Mapston');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (60, 'Berbérati Airport', 'Research Associate', 'Mandi', 60, 0, 0, 0, 'Lacroutz');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (61, 'Aratika Nord Airport', 'Web Developer IV', 'Dinny', 61, 0, 0, 0, 'Rolley');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (62, 'Kuusamo Airport', 'Legal Assistant', 'Brody', 62, 0, 0, 0, 'Charrett');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (63, 'Vila Bela da Santíssima Trindade Airport', 'Programmer Analyst IV', 'Berget', 63, 0, 0, 0, 'MacComiskey');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (64, 'Lai Airport', 'Financial Advisor', 'Suzy', 64, 0, 0, 0, 'Pellman');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (65, 'Maintirano Airport', 'Paralegal', 'Creight', 65, 0, 0, 0, 'D''Alesio');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (66, 'Curitibanos Airport', 'Staff Accountant IV', 'Bale', 66, 0, 0, 0, 'Jessop');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (67, 'Huahine-Fare Airport', 'Senior Editor', 'Melinda', 67, 0, 0, 0, 'Baskerfield');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (68, 'Solano Airport', 'Tax Accountant', 'Nowell', 68, 0, 0, 0, 'Wrightim');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (69, 'Nikunau Airport', 'Legal Assistant', 'Hi', 69, 0, 0, 0, 'Clamp');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (70, 'Merced Regional Macready Field', 'Senior Editor', 'Kelbee', 70, 0, 0, 0, 'Shervil');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (71, 'Humberto Delgado Airport (Lisbon Portela Airport)', 'Dental Hygienist', 'Sharai', 71, 0, 0, 0, 'McAteer');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (72, 'La Grande Rivière Airport', 'Editor', 'Oralie', 72, 0, 0, 0, 'Klemz');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (73, 'Sidney Municipal-Lloyd W Carr Field', 'Recruiting Manager', 'Gabbie', 73, 0, 0, 0, 'Bunten');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (74, 'Pathankot Airport', 'Safety Technician III', 'Kyle', 74, 0, 0, 0, 'Springell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (75, 'Half Moon Bay Airport', 'Project Manager', 'Gamaliel', 75, 0, 0, 0, 'Emms');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (76, 'Lübeck Blankensee Airport', 'Automation Specialist I', 'Wilbert', 76, 0, 0, 0, 'Morgans');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (77, 'Purdue University Airport', 'Data Coordinator', 'Xenia', 77, 0, 0, 0, 'Boxe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (78, 'Sui Airport', 'Registered Nurse', 'Gertrudis', 78, 0, 0, 0, 'Durbridge');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (79, 'Talkeetna Airport', 'VP Quality Control', 'Tamra', 79, 0, 0, 0, 'Mowsdale');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (80, 'Chacalluta Airport', 'Safety Technician IV', 'Blair', 80, 0, 0, 0, 'Thurlow');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (81, 'N''Délé Airport', 'Engineer III', 'Heidie', 81, 0, 0, 0, 'Maw');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (82, 'Nanuque Airport', 'Database Administrator IV', 'Fanni', 82, 0, 0, 0, 'Bessell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (83, 'Nipa Airport', 'Environmental Specialist', 'Arlan', 83, 0, 0, 0, 'Clitheroe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (84, 'Soldotna Airport', 'Assistant Media Planner', 'Gerta', 84, 0, 0, 0, 'Merriton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (85, 'Proserpine Whitsunday Coast Airport', 'Clinical Specialist', 'Maryellen', 85, 0, 0, 0, 'Ouldcott');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (86, 'Dubai International Airport', 'General Manager', 'Travis', 86, 0, 0, 0, 'Bogace');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (87, 'Dalton Municipal Airport', 'Human Resources Assistant I', 'Jeanie', 87, 0, 0, 0, 'Pitson');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (88, 'Salem Airport', 'Help Desk Technician', 'Nanete', 88, 0, 0, 0, 'Braxton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (89, 'Warren "Bud" Woods Palmer Municipal Airport', 'Food Chemist', 'Claudia', 89, 0, 0, 0, 'Bernardotte');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (90, 'Palm Beach International Airport', 'Financial Analyst', 'Allard', 90, 0, 0, 0, 'Fillgate');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (91, 'Marinduque Airport', 'Mechanical Systems Engineer', 'Lars', 91, 0, 0, 0, 'Timoney');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (92, 'Cape Cod Coast Guard Air Station', 'Product Engineer', 'Dante', 92, 0, 0, 0, 'Kaubisch');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (93, 'Capitán Av. German Quiroga G. Airport', 'VP Sales', 'Kory', 93, 0, 0, 0, 'Quail');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (94, 'Nyagan Airport', 'Food Chemist', 'Cristionna', 94, 0, 0, 0, 'Betser');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (95, 'Tynda Airport', 'Professor', 'Inessa', 95, 0, 0, 0, 'Wratten');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (96, 'Mumias Airport', 'Assistant Media Planner', 'Vally', 96, 0, 0, 0, 'Dumigan');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (97, 'Qikiqtarjuaq Airport', 'Programmer II', 'Elmer', 97, 0, 0, 0, 'Pashenkov');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (98, 'McGhee Tyson Airport', 'Project Manager', 'Leda', 98, 0, 0, 0, 'Swales');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (99, 'Awar Airport', 'Engineer II', 'Dyanna', 99, 0, 0, 0, 'Popplewell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bfile) values (100, 'Barnaul Airport', 'Software Engineer III', 'Dulsea', 100, 0, 0, 0, 'Mothersole');


select * from board2;
commit;
delete board2 where bno=98;
select * from board2 where bno between 1 and 20;
select rownum,bno,btitle from board2; --rownum 번호를 새롭게 부여
select rownum,bno,btitle from board2 order by btitle;
commit;
drop table board2;
create table board2 (
	bno number(4),
	btitle VARCHAR2(1000),
	bcontent clob,
	id VARCHAR2(30),
	bgroup number(4),
	bstep number(4),
	bindent number(4),
	bhit number(4),
	bdate DATE,
	bfile VARCHAR2(100)
);

insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (1, 'Maury County Airport', 'Software Engineer IV', 'Dex', 1, 0, 0, 0, '2024-07-31', 'Garth');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (2, 'Ras Al Khaimah International Airport', 'Electrical Engineer', 'Thorstein', 2, 0, 0, 0, '2024-11-03', 'Carnoghan');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (3, 'Miller Field', 'Senior Sales Associate', 'Killian', 3, 0, 0, 0, '2023-12-10', 'Soughton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (4, 'Garowe Airport', 'Physical Therapy Assistant', 'Marleah', 4, 0, 0, 0, '2024-01-14', 'Naisey');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (5, 'Kiryat Shmona Airport', 'Junior Executive', 'Boothe', 5, 0, 0, 0, '2024-01-13', 'Bassano');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (6, 'Playa Baracoa Airport', 'Software Consultant', 'Alfred', 6, 0, 0, 0, '2024-09-22', 'Houston');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (7, 'Southampton Airport', 'Media Manager IV', 'Goddard', 7, 0, 0, 0, '2024-05-21', 'Stroton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (8, 'Nushki Airport', 'Account Representative I', 'Jehu', 8, 0, 0, 0, '2024-07-27', 'Ginsie');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (9, 'Kashan Airport', 'Safety Technician IV', 'Reggie', 9, 0, 0, 0, '2024-01-02', 'Gillingham');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (10, 'Land''s End Airport', 'Teacher', 'Grace', 10, 0, 0, 0, '2024-07-02', 'Dinnington');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (11, 'Marau Airport', 'Senior Sales Associate', 'Carrissa', 11, 0, 0, 0, '2024-09-26', 'Vannucci');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (12, 'Paros National Airport', 'Computer Systems Analyst IV', 'Charline', 12, 0, 0, 0, '2024-08-30', 'Pearn');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (13, 'Kazan International Airport', 'Web Designer IV', 'Petra', 13, 0, 0, 0, '2024-05-25', 'Tench');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (14, 'Abadan Airport', 'Social Worker', 'Guenevere', 14, 0, 0, 0, '2023-12-25', 'Whatford');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (15, 'Alerta Airport', 'Human Resources Manager', 'Rainer', 15, 0, 0, 0, '2023-12-13', 'Kagan');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (16, 'Ambatolhy Airport', 'Statistician II', 'Clemence', 16, 0, 0, 0, '2024-07-25', 'Abelovitz');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (17, 'Antrim County Airport', 'Graphic Designer', 'Atlanta', 17, 0, 0, 0, '2024-01-24', 'Puvia');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (18, 'Dayton-Wright Brothers Airport', 'Financial Analyst', 'Meriel', 18, 0, 0, 0, '2024-06-24', 'Towl');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (19, 'Caransebeş Airport', 'Media Manager III', 'Eada', 19, 0, 0, 0, '2023-11-12', 'Foresight');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (20, 'Kédougou Airport', 'Mechanical Systems Engineer', 'Franky', 20, 0, 0, 0, '2024-06-26', 'Connell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (21, 'Hosea Kutako International Airport', 'Operator', 'Aleta', 21, 0, 0, 0, '2024-06-04', 'O''Shields');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (22, 'Norsup Airport', 'Accountant I', 'Lucky', 22, 0, 0, 0, '2024-04-08', 'Peatman');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (23, 'Kota Kinabalu International Airport', 'Business Systems Development Analyst', 'Wolf', 23, 0, 0, 0, '2024-11-03', 'Whymark');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (24, 'Yeva Airport', 'Systems Administrator I', 'Germain', 24, 0, 0, 0, '2024-06-13', 'Burril');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (25, 'Ampara Airport', 'Software Consultant', 'Costanza', 25, 0, 0, 0, '2024-01-11', 'De Giorgis');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (26, 'Madeira Airport', 'Executive Secretary', 'Jeane', 26, 0, 0, 0, '2024-05-01', 'Northedge');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (27, 'Manang Airport', 'Electrical Engineer', 'Ramona', 27, 0, 0, 0, '2024-10-30', 'Camellini');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (28, 'Dirranbandi Airport', 'Teacher', 'Evelyn', 28, 0, 0, 0, '2024-10-22', 'Smitherham');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (29, 'Chevak Airport', 'Senior Editor', 'Alfi', 29, 0, 0, 0, '2024-08-05', 'Skiggs');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (30, 'Along Airport', 'Legal Assistant', 'Sinclare', 30, 0, 0, 0, '2024-08-31', 'Jay');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (31, 'Tongliao Airport', 'Graphic Designer', 'Randi', 31, 0, 0, 0, '2024-06-01', 'Nias');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (32, 'Videira Airport', 'Social Worker', 'Alfi', 32, 0, 0, 0, '2024-06-27', 'Rodge');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (33, 'Lawrenceville Vincennes International Airport', 'Product Engineer', 'Ortensia', 33, 0, 0, 0, '2024-10-19', 'Cornew');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (34, 'St Marys Municipal Airport', 'Health Coach III', 'Edik', 34, 0, 0, 0, '2024-07-31', 'Greenway');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (35, 'Pimaga Airport', 'Nuclear Power Engineer', 'Melantha', 35, 0, 0, 0, '2024-06-07', 'Eixenberger');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (36, 'Sand Point Airport', 'Automation Specialist II', 'Mario', 36, 0, 0, 0, '2024-10-07', 'Szanto');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (37, 'Syangboche Airport', 'Tax Accountant', 'Goran', 37, 0, 0, 0, '2024-06-27', 'Height');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (38, 'Healy Lake Airport', 'Librarian', 'Mela', 38, 0, 0, 0, '2024-06-02', 'Collough');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (39, 'Midgard Airport', 'Database Administrator III', 'Bambie', 39, 0, 0, 0, '2024-05-09', 'Verduin');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (40, 'Heglig Airport', 'Programmer IV', 'Bernelle', 40, 0, 0, 0, '2024-07-04', 'Sidry');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (41, 'Mossel Bay Airport', 'Health Coach IV', 'Perice', 41, 0, 0, 0, '2024-06-29', 'Moye');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (42, 'Siwo Airport', 'VP Marketing', 'Dallis', 42, 0, 0, 0, '2024-02-04', 'McGiff');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (43, 'Danilo Atienza Air Base', 'Speech Pathologist', 'Thaine', 43, 0, 0, 0, '2024-01-19', 'Tribbeck');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (44, 'Shelby Airport', 'Assistant Media Planner', 'Francyne', 44, 0, 0, 0, '2023-12-13', 'Crookshanks');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (45, 'Gage Airport', 'GIS Technical Architect', 'Hyacintha', 45, 0, 0, 0, '2023-12-23', 'Hearnes');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (46, 'Gelephu Airport', 'Internal Auditor', 'Hanny', 46, 0, 0, 0, '2024-09-12', 'McJerrow');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (47, 'Sugraly Airport', 'Chemical Engineer', 'Quentin', 47, 0, 0, 0, '2023-11-11', 'Brydell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (48, 'Myrtle Beach International Airport', 'Senior Developer', 'Karrah', 48, 0, 0, 0, '2024-03-16', 'McKue');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (49, 'Rustaq Airport', 'Accounting Assistant IV', 'Stepha', 49, 0, 0, 0, '2024-10-10', 'Charity');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (50, 'Southwest Oregon Regional Airport', 'Design Engineer', 'Marcille', 50, 0, 0, 0, '2024-08-16', 'Philbin');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (51, 'New Stuyahok Airport', 'Data Coordinator', 'Armand', 51, 0, 0, 0, '2024-04-10', 'Bianco');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (52, 'Rabil Airport', 'Clinical Specialist', 'Abelard', 52, 0, 0, 0, '2024-03-23', 'D''eathe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (53, 'Walvis Bay Airport', 'Food Chemist', 'Janine', 53, 0, 0, 0, '2024-01-23', 'Klousner');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (54, 'Willow Airport', 'Executive Secretary', 'Tamar', 54, 0, 0, 0, '2024-02-10', 'Nanuccioi');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (55, 'Maquinchao Airport', 'Staff Scientist', 'Jobina', 55, 0, 0, 0, '2024-03-27', 'Danshin');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (56, 'Smithton Airport', 'Structural Analysis Engineer', 'Pablo', 56, 0, 0, 0, '2024-03-20', 'Dulwitch');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (57, 'Los Menucos Airport', 'Health Coach IV', 'Ashlin', 57, 0, 0, 0, '2023-12-06', 'Serot');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (58, 'Jersey Airport', 'Occupational Therapist', 'Sarene', 58, 0, 0, 0, '2024-02-27', 'Fullard');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (59, 'Mikkeli Airport', 'Research Associate', 'Juana', 59, 0, 0, 0, '2024-08-11', 'Wolver');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (60, 'Granville Airport', 'Computer Systems Analyst II', 'Perl', 60, 0, 0, 0, '2024-05-14', 'Barkess');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (61, 'Mont Joli Airport', 'Sales Associate', 'Bradley', 61, 0, 0, 0, '2024-01-08', 'Crosi');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (62, 'Moabi Airport', 'Marketing Manager', 'Kiah', 62, 0, 0, 0, '2024-01-04', 'Wardel');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (63, 'Provo Municipal Airport', 'Paralegal', 'Mallory', 63, 0, 0, 0, '2024-03-26', 'Nashe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (64, 'Belgorod International Airport', 'Programmer III', 'Lory', 64, 0, 0, 0, '2024-04-24', 'Bowdrey');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (65, 'Northern Peninsula Airport', 'Professor', 'Augustin', 65, 0, 0, 0, '2023-12-01', 'Mantrip');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (66, 'Makemo Airport', 'Chief Design Engineer', 'Karia', 66, 0, 0, 0, '2024-07-06', 'Leppingwell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (67, 'Croker Island Airport', 'Software Test Engineer III', 'Baily', 67, 0, 0, 0, '2024-07-07', 'Vader');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (68, 'Vestmannaeyjar Airport', 'Electrical Engineer', 'Whit', 68, 0, 0, 0, '2024-03-28', 'Gill');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (69, 'Buri Ram Airport', 'Executive Secretary', 'Renato', 69, 0, 0, 0, '2023-11-07', 'Krug');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (70, 'Brochet Airport', 'Research Nurse', 'Dyanna', 70, 0, 0, 0, '2024-04-29', 'Milbourn');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (71, 'Mbarara Airport', 'Structural Analysis Engineer', 'Sydney', 71, 0, 0, 0, '2024-05-07', 'Rendell');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (72, 'Manchester-Boston Regional Airport', 'Teacher', 'Jose', 72, 0, 0, 0, '2024-10-29', 'Northover');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (73, 'Kushiro Airport', 'Financial Advisor', 'Lyle', 73, 0, 0, 0, '2024-07-16', 'Lockyer');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (74, 'Ulusaba Airport', 'Chemical Engineer', 'Marti', 74, 0, 0, 0, '2023-12-06', 'Readman');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (75, 'Corvallis Municipal Airport', 'Software Engineer II', 'Terrill', 75, 0, 0, 0, '2024-07-21', 'Ianno');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (76, 'Anshan Air Base', 'Physical Therapy Assistant', 'Coleen', 76, 0, 0, 0, '2024-09-09', 'Philpot');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (77, 'Longdongbao Airport', 'Software Engineer I', 'Filberto', 77, 0, 0, 0, '2024-07-01', 'Simunek');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (78, 'Apple Valley Airport', 'Editor', 'Joycelin', 78, 0, 0, 0, '2023-11-22', 'Clampin');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (79, 'Arthur N Neu Airport', 'Financial Advisor', 'El', 79, 0, 0, 0, '2024-06-18', 'Foggo');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (80, 'Inukjuak Airport', 'Nurse Practicioner', 'Dylan', 80, 0, 0, 0, '2024-09-07', 'Buzza');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (81, 'Rochester International Airport', 'Registered Nurse', 'Lindsay', 81, 0, 0, 0, '2023-11-10', 'O''Kenny');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (82, 'Prado Airport', 'Electrical Engineer', 'Fiorenze', 82, 0, 0, 0, '2024-04-18', 'Benterman');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (83, 'Craig Seaplane Base', 'Health Coach I', 'Michaella', 83, 0, 0, 0, '2023-12-06', 'Gibbons');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (84, 'Fayetteville Municipal Airport', 'Software Engineer III', 'Alfredo', 84, 0, 0, 0, '2024-05-11', 'Karczinski');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (85, 'Whiting Field Naval Air Station - North', 'Research Associate', 'Randie', 85, 0, 0, 0, '2024-10-13', 'Holdworth');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (86, 'Harry P Williams Memorial Airport', 'Human Resources Assistant III', 'Shane', 86, 0, 0, 0, '2024-07-07', 'Longbone');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (87, 'Geilenkirchen Air Base', 'Programmer Analyst I', 'Margarita', 87, 0, 0, 0, '2024-01-26', 'Bryce');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (88, 'Cornélio Procópio Airport', 'Programmer IV', 'Arlene', 88, 0, 0, 0, '2024-03-11', 'Ranns');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (89, 'Witu Airport', 'Paralegal', 'Shawn', 89, 0, 0, 0, '2024-10-30', 'Hamblington');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (90, 'Milyakburra Airport', 'Social Worker', 'Marion', 90, 0, 0, 0, '2024-02-22', 'Gillies');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (91, 'Monkey Bay Airport', 'Executive Secretary', 'Nedi', 91, 0, 0, 0, '2024-02-07', 'Tatterton');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (92, 'Aeroclube de Bento Gonçalves Airport', 'Human Resources Manager', 'Lucila', 92, 0, 0, 0, '2024-10-20', 'Fust');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (93, 'Gregory Downs Airport', 'Marketing Assistant', 'Toddie', 93, 0, 0, 0, '2024-01-07', 'Dancer');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (94, 'Bunyu Airport', 'Pharmacist', 'Francisco', 94, 0, 0, 0, '2024-02-08', 'Bordis');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (95, 'Lake Macquarie Airport', 'Financial Advisor', 'Georgi', 95, 0, 0, 0, '2024-09-02', 'Sparhawk');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (96, 'Nain Airport', 'Senior Quality Engineer', 'Carolan', 96, 0, 0, 0, '2024-02-20', 'O''Cuddie');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (97, 'Touggourt Sidi Madhi Airport', 'Civil Engineer', 'Roma', 97, 0, 0, 0, '2024-07-18', 'Berrington');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (98, 'Lae Island Airport', 'Quality Control Specialist', 'Edin', 98, 0, 0, 0, '2024-06-21', 'Walewski');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (99, 'Chipinge Airport', 'Nurse', 'Hubie', 99, 0, 0, 0, '2023-11-08', 'Bristoe');
insert into board2 (bno, btitle, bcontent, id, bgroup, bstep, bindent, bhit, bdate, bfile) values (100, 'Tapini Airport', 'Product Engineer', 'Katine', 100, 0, 0, 0, '2024-01-13', 'Scrine');


-- 8, 11,12,16, 21,22,25,29,35,38,44,46,57,61,66,74,88,95,96,98
delete board2 where bno=98;
commit;
select * from board2;
select rownum,bno,btitle,bdate from board2 order by bdate desc;

select rnum, bno,btitle,bdate from(select row_number() over (order by bdate desc) rnum,bno,btitle, bdate from board2) 
where rnum between 11 and 20;

select * from (select rownum from board2) where rownum between 11 and 20;
select * from board2;

select * from(select rownum rnum, a.* from (select * from board2 order by bdate desc)a) where rnum between 1 and 20;

select no,name,avg,rank() over (order by avg desc) from students;

select * from(select rownum rnum,a.*from (select no,name,avg,rank() over (order by avg desc)
from students) a) where rnum between 11 and 20;

select * from(select row_number() over (order by avg desc)rnum,rank() over(order by avg desc),a,*from students a)
where rnum between 11 and 20;
select * from students;
select no,name,avg,rank() over (order by avg desc) from students;
commit;
update students a set rank = (select rank from(select no,rank() over (order by avg desc) from students )b where a.no=b.no);


--veiw 
--상담원 : 전화번호 마케팅
--직원가 100만원 90% 10만원 
create or replace view employees_view as select employee_id,emp_name, email,phone_number,hire_date from employees;
select * from employees_view;

create or replace view emp_view as
select employee_id,emp_name,email,phone_number,hire_date,a.department_id,department_name
from employees a, departments b where a.department_id = b.department_id;
select * from emp_view;

--view 컬럼 추가
comment on column employees_view.employee_id is '사원 번호에 해당';

select * from emp2;
drop table emp2;
commit;
create table emp02(
employee_id number(6),
emp_name varchar2(80),
hire_date date,
salary number(8,2),
department_id number(6)
);
desc emp02;
insert into emp02(employee_id,emp_name,hire_date,salary,department_id)
select employee_id,emp_name,hire_date,salary,department_id from employees;
select * from emp02;
create or replace view emp02_view
as select employee_id,emp_name,hire_date from emp02;
select * from emp02_view order by employee_id;
--100번 이름 홍길동으로 변경
update emp02_view set emp_name='홍길동'
where employee_id = 101;
commit;
select * from emp02_view;

--단순 view 한개의 테이블로 구성
--insert update delete가능 not null이면 insert가 불가
--복합 view 2개이상일때는 불가능

insert into emp02_view values(
207,'유관순',sysdate
);
select * from emp02_view order by employee_id;
select * from emp02;
delete emp02 where employee_id=207;
commit;

select * from students;
--no :seq
--total avg rank sdate 오라클에서 입력
--입력받을 데이터 name,kor,eng,math
insert into students values(students_seq.nextval,name,kor,eng,math,kor+eng+math
,(kor+eng+math)/3,sysdate;

select * from students;

select * from students order by total;
select name,rank() over (order by avg desc) from students;

update students set rank =(select rank() over (order by avg desc) from students a where a.name = studetnts.name);