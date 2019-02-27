CREATE DATABASE tejas;
\connect tejas;

--Question 1 

CREATE OR REPLACE FUNCTION setUnion (A anyarray, B anyarray) RETURNS anyarray AS
$$
SELECT ARRAY( SELECT * FROM UNNEST(A)
UNION
SELECT * FROM UNNEST(B));
$$ LANGUAGE SQL;

SELECT setUnion( '{1,2,3}'::int[], '{2,3,3,5}'::int[] );

CREATE OR REPLACE FUNCTION setIntersection (A anyarray, B anyarray) RETURNS anyarray AS
$$
SELECT ARRAY( SELECT * FROM UNNEST(A)
INTERSECT 
SELECT * FROM UNNEST(B));
$$ LANGUAGE SQL;

SELECT setIntersection( '{1,2,3}'::int[], '{2,3,3,5}'::int[] );

CREATE OR REPLACE FUNCTION setDifference (A anyarray, B anyarray) RETURNS anyarray AS
$$
SELECT ARRAY( SELECT * FROM UNNEST(A)
EXCEPT  
SELECT * FROM UNNEST(B));
$$ LANGUAGE SQL;

SELECT setDifference( '{1,2,3}'::int[], '{2,3,3,5}'::int[] );

create or replace function memberof(x anyelement, A anyarray) returns boolean as
$$
select x = SOME(A);
$$ language sql;

CREATE table Student(Sid integer primary key,Sname Varchar(15));

CREATE table Major(Sid integer ,Major Varchar(15) ,foreign key (Sid) references Student (Sid));

CREATE table Book(BookNo integer primary key,Title Varchar(30),Price integer);

CREATE table Cites(BookNo integer,CitedBookNo integer,foreign key (BookNo) references Book (BookNo),foreign key (CitedBookNo) references Book (BookNo));

CREATE table Buys(Sid integer,BookNo integer,foreign key (Sid) references Student (Sid),foreign key (BookNo) references Book (BookNo));

insert into Student (Sid, Sname) values  (1001, 'Jean'),	(1002, 'Maria'),(1003, 'Anna'),(1004, 'Chin'),(1005, 'John'),(1006, 'Ryan'),(1007, 'Catherine'),(1008, 'Emma'),(1009, 'Jan'),(1010, 'Linda'),(1011, 'Nick'),(1012, 'Eric'),	(1013, 'Lisa'),(1014, 'Filip'),(1015, 'Dirk'),	(1016, 'Mary'),	(1017, 'Ellen'),	(1020, 'Greg'),	(1022, 'Qin'),(1023, 'Melanie'),	(1040, 'Pam') ;

insert into Major (Sid, Major) values (1001,  'Math'),(1001, 'Physics'),(1002,  'CS'),		(1002,  'Math'),		(1003,  'Math'),	(1004,  'CS'),	(1006,  'CS'),(1007,  'CS')	,(1007,  'Physics'),		(1008,  'Physics'),	(1009,  'Biology'),		(1010,  'Biology'),	(1011,  'CS'),	(1011,  'Math'),		(1012,  'CS'),(1013,  'CS'),		(1013,  'Psychology'),		(1014,  'Theater'),		(1017,  'Anthropology'),		(1022,  'CS'),	(1015,  'Chemistry');

insert into Book (BookNo, Title, Price) values	(2001 , 'Databases',  40),	(2002 , 'OperatingSystems', 25),	(2003 , 'Networks',   20),	(2004 , 'AI',    45),	(2005 , 'DiscreteMathematics',    20),	(2006 , 'SQL',   25),	(2007 , 'ProgrammingLanguages',   15),	(2008 , 'DataScience', 50),	(2009 , 'Calculus',   10),	(2010 , 'Philosophy', 25),	(2012 , 'Geometry',   80),	(2013 , 'RealAnalysis ',    35),	(2011 , 'Anthropology',     50),	(2014 , 'Topology',   70);

insert into Buys (Sid,BookNo) values (1023 ,	2012), (1023 ,	2014), (1040,	2002), (1001,	2002),(1001,	2007),(1001,	2009),(1001,	2011),(1001,	2013),(1002,	2001),(1002,	2002),(1002,	2007),	(1002,	2011),(1002,	2012),(1002,	2013),(1003,	2002),	(1003,	2007),	(1003,	2011),	(1003,	2012),(1003,	2013),	(1004,	2006),	(1004,	2007),	(1004,	2008),	(1004,	2011),	(1004,	2012),(1004,	2013),	(1005,	2007),	(1005,	2011),	(1005,	2012),	(1005,	2013),(1006,	2006),	(1006,	2007),	(1006,	2008),	(1006,	2011),	(1006,	2012),	(1006,	2013),	(1007,	2001),	(1007,	2002),	(1007,	2003),	(1007,	2007),	(1007,	2008),	(1007,	2009),	(1007,	2010),	(1007,	2011),	(1007,	2012),	(1007,	2013),	(1008,	2007),	(1008,	2011),	(1008,	2012),	(1008,	2013),	(1009,	2001),	(1009,	2002),	(1009,	2011),	(1009,	2012),	(1009,	2013),	(1010,	2001),	(1010,	2002),	(1010,	2003),	(1010,	2011),	(1010,	2012),	(1010,	2013),	(1011,	2002),	(1011,	2011),	(1011,	2012),	(1012,	2011),	(1012,	2012),	(1013,	2001),	(1013,	2011),	(1013,	2012),	(1014,	2008),	(1014,	2011),	(1014,	2012),	(1017,	2001),	(1017,	2002),	(1017,	2003),	(1017,	2008),	(1017,	2012),	(1020,	2001),	(1020,	2012),	(1022,	2014);

insert into Cites (BookNo,CitedBookNo) values (2012,  2001),(2008,  2011),(2008,  2012),(2001,  2002),(2001,  2007),(2002,  2003),(2003,  2001),(2003,  2004),(2003,  2002),(2010,  2001),(2010,  2002),(2010,  2003),(2010,  2004),(2010,  2005),(2010,  2006),(2010,  2007),(2010,  2008),(2010,  2009),(2010,  2011),(2010,  2013),(2010,  2014);

--Question 2

create or replace view student_books as 
select s.sid as sid, array(select t.bookno from   buys t where  t.sid = s.sid order by bookno) as books 
from   student s 
order by sid;

SELECT * FROM student_books;

create or replace view book_students as
select s.bookno as bookno, array(select t.sid from buys t where t.bookno = s.bookno order by sid) as student
from book s
order by bookno;

SELECT * FROM book_students;

create or replace view book_citedbooks as
select s.bookno as bookno, array(select t.CitedBookNo from Cites t where t.bookno = s.bookno order by CitedBookNo) as citedbooks
from book s
order by bookno;

SELECT * FROM book_citedbooks;

create or replace view book_citingbooks as
select s.bookno as bookno, array(select t.BookNo from Cites t where t.CitedBookNo = s.bookno order by BookNo) as booksitcites
from book s
order by bookno;

SELECT * FROM book_citingbooks;


create or replace view major_students as
select distinct s.Major as Major, array(select t.Sid from Major t where t.Major = s.Major order by Sid) as students
from Major s
order by Major;

SELECT * FROM major_students;

create or replace view student_majors as
select distinct s.Sid as Sid, array(select t.Major from Major t where t.Sid = s.Sid order by Major) as majors
from Student s
order by Sid;

SELECT * FROM student_majors;

--Question 3

--a
select x.sid from student_books x where
cardinality(x.books) = 2;

--b
select x2.sid from student_books x1,student_books x2 where
x1.sid = 1001 and x1.books <@ x2.books;

--c
select x.bookno from book_citedbooks x where 
(select count(*) from (select p1.bookno,UNNEST(p1.citedbooks) as cited from book_citedbooks p1) p,book s 
	where p.bookno = x.bookno and p.cited = s.bookno and s.price > 30) < 2;

--d

select bs.bookno from book_students bs where NOT(bs.student && (select setIntersection((select ms1.students from major_students ms1 where major = 'CS'),(select ms1.students from major_students ms1 where major = 'Math'))));

--e

with E as (select distinct bc1.bookno from (select bc.bookno,UNNEST(bc.booksitcites) as citingbooks from book_citingbooks bc) bc1 where (select count(*) from (select bc.bookno,UNNEST(bc.booksitcites) as citingbooks from book_citingbooks bc) bc2,book b where bc2.bookno = bc1.bookno and bc2.bookno = b.bookno and b.price<50) >= 2) 

select unnest(bs.student) as sid, bs.bookno  from book_students bs inner join E e on (e.bookno=bs.bookno) group by(bs.student,bs.bookno) order by bs.student, bs.bookno;

--f
select distinct array_agg(sb.sid) as students  from student_books sb inner join student_majors sm on ('{"CS","Math"}' <@ sm.majors and sm.sid=sb.sid);

--g
select distinct sb2.sid ,sm.majors from student_books sb1, student_books sb2, student_majors sm where not(sb1.books && sb2.books) and sb1.sid=1001 and sm.sid=sb2.sid order by sb2.sid;

--h
select distinct array(select distinct unnest (sb.books) as books  from student_books sb inner join student_majors sm1 on('CS'=Some(sm1.majors)  and sm1.sid=sb.sid)) as books from student_books,student_majors as books;

--i
select distinct array (select distinct sb.sid as students from student_books sb, book_citedbooks bc where sb.books && (select array_agg(bc.bookno) from book_citedbooks bc where cardinality(bc.citedbooks) >=2)) from student_books , book_citedbooks ;

--j
with E as (select distinct unnest(sb.books) as books ,  sb.sid from student_books sb inner join student_majors sm1 on('CS'=Some(sm1.majors)  and sm1.sid=sb.sid)   group by(sb.books,sb.sid))

select distinct e1.books as books, array(select distinct e.sid from E e where e.books=e1.books) as students from E e1 ;

--k
select distinct sb1.sid from student_books sb1,student_books sb2 
where memberof(sb1.sid , (select students from major_students where major = 'CS')) and 
NOT((sb1.books && (select sb2.books where memberof(sb2.sid,(select students from major_students where major = 'Math')))));

--l
select distinct bs1.bookno, bs2.bookno from book_students bs1 , book_students bs2 where bs1.student<@bs2.student and bs2.student<@bs1.student and bs1.bookno<>bs2.bookno;

--m

select distinct bs1.bookno,bs2.bookno from book_students bs1,book_students bs2 where cardinality(setIntersection((select array((select t1.sno from (select ms.major,UNNEST(ms.students) as sno from major_students ms where major = 'Math') t1))),bs1.student)) < 
cardinality(setIntersection((select array((select t1.sno from (select ms.major,UNNEST(ms.students) as sno from major_students ms where major = 'CS') t1))),bs2.student)) and bs1.bookno != bs2.bookno;

--n
select sb1.sid from student_books sb1 where cardinality(setIntersection(array(select distinct x.bookid from (select sb2.sid,UNNEST(sb2.books) as bookid from student_books sb2) x,book b where x.bookid = b.bookno and b.price > 50),sb1.books)) = 1;



\connect postgres;
DROP DATABASE tejas;








