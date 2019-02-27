CREATE DATABASE tejas;
\connect tejas;


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


--Question 1

select distinct s.sid,s.sname, b.bookno, b.title from student s cross join book b inner join buys t on ((s.sname = 'Eric' or s.sname = 'Anna') and s.sid = t.sid and b.price > 20 and t.bookno = b.bookno);

--Moving Down Conditions

select distinct s.sid,s.sname, b.bookno, b.title from (select * from student where sname = 'Eric' or sname = 'Anna') s cross join (select * from book where price>20) b inner join buys t on (s.sid = t.sid and t.bookno = b.bookno);

--Moving down Projections

select distinct s.sid,s.sname, b.bookno, b.title from (select sid,sname from student where sname = 'Eric' or sname = 'Anna') s cross join (select bookno,title from book where price>20) b inner join buys t on (s.sid = t.sid and t.bookno = b.bookno);


--Question 2

select distinct s.sid from student s cross join book b inner join buys t on ((s.sname = 'Eric' or s.sname = 'Anna') and s.sid = t.sid and b.price > 20 and t.bookno = b.bookno);

--Moving down Conditions

select distinct s.sid from (select * from student where sname = 'Eric' or sname = 'Anna') s cross join (select * from book where price>20) b inner join buys t on (s.sid = t.sid and t.bookno = b.bookno);

--Moving down Projections and removing extra atrributes

select distinct s.sid from (select sid from student where sname = 'Eric' or sname = 'Anna') s cross join (select bookno from book where price>20) b inner join buys t on (s.sid = t.sid and t.bookno = b.bookno);

--Question 3

select distinct s.sid, b1.price as b1_price, b2.price as b2_price
from (select s.sid from student s where s.sname <> 'Eric') s
cross join book b2
inner join book b1 on (b1.bookno <> b2.bookno and b1.price > 60 and b2.price >= 50)
inner join buys t1 on (t1.bookno = b1.bookno and t1.sid = s.sid)
inner join buys t2 on (t2.bookno = b2.bookno and t2.sid = s.sid);

--Pushing Down all innerjoins and re-arranging

select distinct test1.sid,test1.price,test2.price from (select s.sid,test.bookno,test.price from (select s.sid from student s where s.sname <> 'Eric') s inner join (select b2.bookno,b2.price,t2.sid from (buys t2 inner join book b2 on (t2.bookno = b2.bookno and b2.price >=50))) test on (test.sid = s.sid)) test1 inner join (select b1.bookno,b1.price,t1.sid from (buys t1 inner join book b1 on (t1.bookno = b1.bookno and b1.price > 60))) test2 on (test1.bookno != test2.bookno and test2.sid = test1.sid);

--Question 4

select q.sid from 
(select s.sid, s.sname from student s
except
select s.sid, s.sname from student s
inner join buys t on (s.sid = t.sid)
inner join book b on (t.bookno = b.bookno and b.price > 50)) q;

--Pushing down condition 

select q.sid from 
(select s.sid, s.sname from student s
except
select s.sid, s.sname from student s
inner join buys t on (s.sid = t.sid)
inner join (select * from book where price>50) b on (t.bookno = b.bookno)) q;

--Removing reduntant attributes 

select q.sid from 
(select s.sid from student s
except
select s.sid from student s
inner join buys t on (s.sid = t.sid)
inner join (select bookno from book where price>50) b on (t.bookno = b.bookno)) q;


--Question 5

select q.sid,q.sname
from (select s.sid, s.sname, 2007 as bookno
from student s
cross join book b
intersect
select s.sid, s.sname, b.bookno from student s
cross join book b
inner join buys t on (s.sid = t.sid and t.bookno = b.bookno and b.price <25)) q;


--Pushing Down conditions

select q.sid,q.sname
from (select s.sid, s.sname, 2007 as bookno
from student s
cross join book b
intersect
select s.sid, s.sname, test.bookno from student s
inner join (select b.bookno,t.sid from (buys t inner join (select * from book where price<25) b on (t.bookno = b.bookno))) test on (test.sid = s.sid)) q;


--Removing Reduntant Intersection and instead pushing condition down

select q.sid,q.sname
from (select s.sid, s.sname from student s
inner join (select b.bookno,t.sid from (buys t inner join (select * from book where price<25) b on (t.bookno = b.bookno))) test on (test.sid = s.sid and test.bookno = 2007)) q;



--Question 6

select distinct q.bookno
from (select s.sid, s.sname, b.bookno, b.title
from student s
cross join book b
except
select s.sid, s.sname, b.bookno, b.title
from student s
cross join book b
inner join buys t on (s.sid = t.sid and t.bookno = b.bookno and b.price <20)) q;

--Pushing Down conditions


select distinct q.bookno
from (select s.sid, s.sname, b.bookno, b.title
from student s
cross join book b
except
select s.sid, s.sname, test.bookno,test.title from student s
inner join (select b.bookno,t.sid,b.title from (buys t inner join (select * from book where price<20) b on (t.bookno = b.bookno))) test on (test.sid = s.sid)) q;


--Removing Redantant attributes

select distinct q.bookno
from (select b.bookno,s.sid
from student s
cross join book b
except
select test.bookno,s.sid from student s
inner join (select b.bookno,t.sid,b.title from (buys t inner join (select * from book where price<20) b on (t.bookno = b.bookno))) test on (test.sid = s.sid)) q;

--Question 7

select s.sid
from student s
except
(select s1.sid
from student s1
inner join student s2 on (s1.sid <> s2.sid)
inner join buys t1 on (s1.sid = t1.sid)
union
select s1.sid
from student s1
inner join student s2 on (s1.sid <> s2.sid)
inner join buys t1 on (s1.sid = t1.sid)
inner join buys t2 on (t1.bookno = t2.bookno and t2.sid = s2.sid)
inner join book b on (t2.bookno = b.bookno and b.price = 80));

--Removing Union as subgroup present

select s.sid
from student s
except
(select s1.sid
from student s1
inner join student s2 on (s1.sid <> s2.sid)
inner join buys t1 on (s1.sid = t1.sid));

--Removing inner joins that are not necessary as selection is on single collumn

select s.sid
from student s
except
(select s1.sid
from student s1
inner join buys t1 on (s1.sid = t1.sid));


\connect postgres;
DROP DATABASE tejas;


