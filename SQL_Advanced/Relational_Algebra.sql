create database tejas1;
\c tejas1;



CREATE TABLE W(a INTEGER, b VARCHAR(5));
INSERT INTO W values(1, 'John');
INSERT INTO W values(2, 'Ellen');
INSERT INTO W values(3, 'Ann');
INSERT INTO W values(2, 'Linda');
INSERT INTO W values(4, 'Nick');
INSERT INTO W values(4, 'Ann');
INSERT INTO W values(4, 'Vince');
INSERT INTO W values(4, 'Lisa');


CREATE TABLE student(sid INTEGER, sname VARCHAR(15));
CREATE TABLE major(sid INTEGER, major VARCHAR(15));
CREATE TABLE book(bookNo INTEGER, title VARCHAR(30), price INTEGER);
CREATE TABLE cites(bookNo INTEGER, citedBookNo INTEGER);
CREATE TABLE buys(sid INTEGER, bookNo INTEGER);



insert into Student (Sid, Sname) values 
   (1001, 'Jean'),
  (1002, 'Maria'),
  (1003, 'Anna'),
  (1004, 'Chin'),
  (1005, 'John'),
  (1006, 'Ryan'),
  (1007, 'Catherine'),
  (1008, 'Emma'),
  (1009, 'Jan'),
  (1010, 'Linda'),
  (1011, 'Nick'),
  (1012, 'Eric'),
  (1013, 'Lisa'),
  (1014, 'Filip'),
  (1015, 'Dirk'),
  (1016, 'Mary'),
  (1017, 'Ellen'),
  (1020, 'Greg'),
  (1022, 'Qin'),
  (1023, 'Melanie'),
  (1040, 'Pam') ;

insert into Major (Sid, Major) values
    (1001,  'Math'),
    (1001, 'Physics'),
    (1002,  'CS'),
    (1002,  'Math'),
    (1003,  'Math'),
    (1004,  'CS'),
    (1006,  'CS'),
    (1007,  'CS'),
    (1007,  'Physics'),
    (1008,  'Physics'),
    (1009,  'Biology'),
    (1010,  'Biology'),
    (1011,  'CS'),
    (1011,  'Math'),
    (1012,  'CS'),
    (1013,  'CS'),
    (1013,  'Psychology'),
    (1014,  'Theater'),
    (1017,  'Anthropology'),
    (1022,  'CS'),
    (1015,  'Chemistry');

insert into Book (BookNo, Title, Price) values
  (2001 , 'Databases',  40),
  (2002 , 'OperatingSystems', 25),
  (2003 , 'Networks',   20),
  (2004 , 'AI',    45),
  (2005 , 'DiscreteMathematics',    20),
  (2006 , 'SQL',   25),
  (2007 , 'ProgrammingLanguages',   15),
  (2008 , 'DataScience', 50),
  (2009 , 'Calculus',   10),
  (2010 , 'Philosophy', 25),
  (2012 , 'Geometry',   80),
  (2013 , 'RealAnalysis ',    35),
  (2011 , 'Anthropology',     50),
  (2014 , 'Topology',   70);


insert into Buys (Sid,BookNo) values
  (1023 , 2012),
  (1023 , 2014),
  (1040,  2002),
  (1001,  2002),
  (1001,  2007),
  (1001,  2009),
  (1001,  2011),
  (1001,  2013),
  (1002,  2001),
  (1002,  2002),
  (1002,  2007),
  (1002,  2011),
  (1002,  2012),
  (1002,  2013),
  (1003,  2002),
  (1003,  2007),
  (1003,  2011),
  (1003,  2012),
  (1003,  2013),
  (1004,  2006),
  (1004,  2007),
  (1004,  2008),
  (1004,  2011),
  (1004,  2012),
  (1004,  2013),
  (1005,  2007),
  (1005,  2011),
  (1005,  2012),
  (1005,  2013),
  (1006,  2006),
  (1006,  2007),
  (1006,  2008),
  (1006,  2011),
  (1006,  2012),
  (1006,  2013),
  (1007,  2001),
  (1007,  2002),
  (1007,  2003),
  (1007,  2007),
  (1007,  2008),
  (1007,  2009),
  (1007,  2010),
  (1007,  2011),
  (1007,  2012),
  (1007,  2013),
  (1008,  2007),
  (1008,  2011),
  (1008,  2012),
  (1008,  2013),
  (1009,  2001),
  (1009,  2002),
  (1009,  2011),
  (1009,  2012),
  (1009,  2013),
  (1010,  2001),
  (1010,  2002),
  (1010,  2003),
  (1010,  2011),
  (1010,  2012),
  (1010,  2013),
  (1011,  2002),
  (1011,  2011),
  (1011,  2012),
  (1012,  2011),
  (1012,  2012),
  (1013,  2001),
  (1013,  2011),
  (1013,  2012),
  (1014,  2008),
  (1014,  2011),
  (1014,  2012),
  (1017,  2001),
  (1017,  2002),
  (1017,  2003),
  (1017,  2008),
  (1017,  2012),
  (1020,  2001),
  (1020,  2012),
  (1022,  2014);

insert into Cites (BookNo,CitedBookNo) values
  (2012,  2001),
  (2008,  2011),
  (2008,  2012),
  (2001,  2002),
  (2001,  2007),
  (2002,  2003),
  (2003,  2001),
  (2003,  2004),
  (2003,  2002),
  (2010,  2001),
  (2010,  2002),
  (2010,  2003),
  (2010,  2004),
  (2010,  2005),
  (2010,  2006),
  (2010,  2007),
  (2010,  2008),
  (2010,  2009),
  (2010,  2011),
  (2010,  2013),
  (2010,  2014);

--------- Question 1

WITH violations AS (SELECT DISTINCT test.A FROM (SELECT W1.A,W2.B FROM W AS W1,W AS W2 WHERE W1.A = W2.A AND W1.B != W2.B) as test)                                                                  
SELECT A FROM violations UNION (SELECT test.A from (SELECT A FROM W) AS test EXCEPT (SELECT t1.A FROM W t1,violations t2));


--------- Question 2

-- 2A

SELECT DISTINCT D.sid,D.sname FROM (SELECT Sid FROM Buys A,Cites B where A.BookNo = B.BookNo) As C,(SELECT Sid,Sname FROM Student) AS D WHERE C.Sid = D.Sid;

--2B

SELECT DISTINCT D.Sid,D.Sname FROM (SELECT A.Sid FROM Major A,Major B WHERE A.Sid = B.Sid and A.Major != B.Major) AS C,(SELECT Sid,Sname FROM Student) AS D WHERE C.Sid = D.Sid;

--2C

SELECT Sid FROM Buys EXCEPT SELECT test.Sid FROM (SELECT A.Sid FROM Buys A,Buys B WHERE A.Sid = B.Sid AND A.BookNo != B.BookNo) As test;

--2D

WITH without_min AS (SELECT DISTINCT test.BookNo,test.Price,test.Title FROM (SELECT BookNo,Price,Title FROM Book EXCEPT (SELECT test1.BookNo,test1.Price,test1.Title FROM ((SELECT DISTINCT b1.BookNo,b1.Price,b1.Title FROM Book b1,Book b2) EXCEPT (SELECT DISTINCT b2.BookNo,b2.Price,b2.Title FROM Book b1,Book b2 WHERE b1.Price < b2.Price)) AS test1)) As test)
SELECT test1.BookNo,test1.Title FROM ((SELECT DISTINCT b1.BookNo,b1.Title FROM without_min b1,without_min b2) EXCEPT (SELECT DISTINCT b2.BookNo,b2.Title FROM without_min b1,without_min b2 WHERE b1.Price < b2.Price)) AS test1;


--2E

WITH 
TW as (select Bookno , title from Book except select * from (select * from (select b.bookno,b.title from book b, buys t where t.bookno=b.bookno and t.sid<>1001) AS test2 except select * from (select b.bookno,b.title from book b, buys t where t.bookno=b.bookno and t.sid=1001) AS test3) AS test1)

select Bookno , title from TW except select test.bookno, test.title from (select b.bookno,b.title from book b, buys t where t.bookno=b.bookno) test;

--2F

SELECT DISTINCT A.Sid,A.Sname from Student A,Buys B,Buys C,Book D,Book E WHERE B.Sid = C.Sid AND B.BookNo != C.BookNo AND A.sid = B.Sid AND B.BookNo = D.BookNo 
AND C.BookNo = E.BookNo and D.Price < 50 and E.Price < 50;


--2G

WITH
E1 as (select m.sid as sid from major m where m.major = 'CS'),
E2 as (select b.bookno 
	from book b 
	where not exists (select s.sid 
			from E1 s 
			where not exists (select T.bookno 
					from buys T 
					where  s.sid = T.sid and b.bookno = T.bookNo)))

select b.bookNo from book b where  not exists (select bookNo from E2 where b.bookNo = bookNo);

--2H

WITH
E1 as (select b.bookNo from book b where b.price > 50),
E2 as (select distinct b1.bookNo 
	from book b1 
	where Not exists (select *
			 from ((select c.bookNo from cites c where c.citedBookNo = b1.bookNo)
					INTERSECT
				(select * from E1)) q))
select * from E2;

--2I

SELECT A.Sid FROM Buys A,Book B WHERE A.BookNo = B.BookNo AND B.Price > 30
EXCEPT 
SELECT A.Sid FROM Buys A,Book B WHERE A.BookNo = B.BookNo AND B.Price < 30;

--2J

select distinct t.sid , t.bookno from buys t, cites c where t.bookno not  in  ( select c2.citedBookNo from cites c2 where c2.citedBookNo=c2.bookno );

--2K

with 
temp1 as (select m.sid,t.bookno from buys t, major m where m.major = 'CS' and m.sid=t.sid),
temp2 as (select m.sid,t.bookno from buys t, major m where m.major = 'CS' and m.sid=t.sid)

select distinct  B.bookno as b1, X.bookno as b2 from temp1 B , temp2 X where B.bookno<>X.bookno and B.sid=X.sid;

--2L

SELECT * FROM (select distinct s1.sid, s2.sid
	from student s1, student s2, book b
	where s1.sid<>s2.sid and not exists
	(
	 (select bookNo from buys t where t.sid = s1.sid)
	 EXCEPT
	 (select bookNo from buys t where t.sid = s2.sid)
	)
     ) AS foo;

--2M


--3A

select distinct  m.* from major m inner join buys t on (m.sid=t.sid) inner join book b on ( t.bookno=b.bookno and b.price<20);

--3B

select distinct q.sid, q.bookno from (select t.sid, b.bookno from buys t, book b
      except 
      select t.sid, b.bookno from buys t, book b, buys t1, book b1 where t1.bookno=b1.bookno and t1.sid=t.sid and not b.price<=b1.price) q;

--3C

select distinct b.bookno, b.title from book b inner join cites c on (b.bookno=c.citedbookno and 20 <= b.price and b.price <= 40);

--3D

select distinct s.sid , s.sname 
from (student s inner join major m on (s.sid=m.sid and m.major ='CS') inner join buys t on (s.sid=t.sid) inner join cites c on (t.bookno=c.citedBookNo ) inner join book b1 on (c.citedbookno=b1.bookno) inner join book b2 on (c.bookno=b2.bookno and b1.price> b2.price));


--3E

select b.bookno, b.title
   from   book b
   where  exists (select m.sid
                  from   major m
                  where  m.major = 'CS' and
                         m.sid not in(select t.sid
                                      from   buys t
                                      where  t.bookno = b.bookno));


select DISTINCT b.bookno, b.title
   from   book b,(SELECT m.sid,m.Major FROM Major m WHERE m.Major = 'CS') m
        WHERE m.sid not in(select t.sid
                from   buys t
                        where  t.bookno = b.bookno);

SELECT test.BookNo,test.Title FROM
((select DISTINCT b.bookno, b.title
   from   book b,(SELECT m.sid,m.Major FROM Major m WHERE m.Major = 'CS') m) 
EXCEPT
(select DISTINCT b.bookno, b.title
   from   book b,(SELECT m.sid,m.Major FROM Major m WHERE m.Major = 'CS') m,Buys t WHERE t.BookNo = b.BookNo AND m.sid = t.sid)) AS test;



--3F

select b.bookno, b.title from book b where not exists (select s.sid from  student s where s.sid in (select m.sid from major m where m.major = 'CS') and s.sid in (select m.sid from major m where m.major = 'Math') and s.sid not in (select t.sid from   buys t where  t.bookno = b.bookno));




\c postgres;
drop database tejas1;




 



