create database employee

create table student1(
id int PRIMARY KEY ,
name varchar(20),
dept varchar(20)
);

insert into student1(id,name,dept)
VALUES
(1,'mythili','maths'),
(2,'priya','Hr'),
(4,'aruna','eng');

 select * from student1;

 delete student where id=1;					--delete particular row
 select * from student;

 truncate table student;					--delete values
  select * from student;

  drop table student;                       --delete whole tables

  select * from students;

 EXEC sp_rename 'student','students';	   --Rename - add, modify, rename, drop

ALTER TABLE students RENAME  TO studentss;

ALTER TABLE students ADD age INT;

ALTER TABLE students DROP COLUMN age;

BEGIN TRANSACTION

update students SET name='anu'		 		
WHERE id=1;

rollback;

commit;
create table account2(
id int,
foreign key(id) REFERENCES students(id),
name varchar(20),
dept varchar(20)
);
insert into account2(id,name,dept)
VALUES
(1,'sunil','maths'),
(2,'priu','tamil'),
(3,'shalu','science');

  select * from account2;

  create view stu_acc
  as
  select student1.id, student1.name AS student_name, student1.dept AS student_dept, 
       account2.name AS account_name, account2.dept AS account_dept
FROM student1
INNER JOIN account2
ON student1.id = account2.id;
 
 select * from stu_acc;

