
--Question 1

CREATE TABLE A (M INTEGER);
INSERT INTO  A VALUES (1);
INSERT INTO  A VALUES (2);
INSERT INTO  A VALUES (3);
INSERT INTO  A VALUES (4);
INSERT INTO  A VALUES (5);
SELECT b.M AS x,SQRT(b.M) AS square_root_x,b.M*b.M AS x_squared,POWER(2,b.M) AS two_to_the_power_x,b.M ! AS x_factorial,LOG(2.71828,b.M) AS logarithm_x FROM A b;

--Question 2

CREATE TABLE A (M INTEGER);
CREATE TABLE B (M INTEGER);
INSERT INTO  A VALUES (1);
INSERT INTO  A VALUES (2);
INSERT INTO  B VALUES (1);
INSERT INTO  B VALUES (2);


SELECT
(SELECT 
CASE WHEN COUNT( * ) > 0 THEN 
     CAST( 'True' AS VARCHAR(20)) 
ELSE 
      CAST( 'False' AS VARCHAR(20))  
END As empty_a_minus_b
FROM (SELECT M FROM A EXCEPT SELECT M FROM B) AS x),
(SELECT 
CASE WHEN COUNT( * ) > 0 THEN 
     CAST( 'True' AS VARCHAR(20)) 
ELSE 
      CAST( 'False' AS VARCHAR(20))  
END As not_empty_symetric_difference
FROM ((SELECT M FROM A EXCEPT SELECT M FROM B) UNION (SELECT M FROM B EXCEPT SELECT M FROM B)) AS x),
(SELECT 
CASE WHEN COUNT( * ) > 0 THEN 
     CAST( 'True' AS VARCHAR(20)) 
ELSE 
      CAST( 'False' AS VARCHAR(20))  
END As empty_a_intersection_b
FROM (SELECT M FROM A INTERSECT SELECT M FROM B) AS x);

--Question 3

CREATE TABLE Pair (M INTEGER,N INTEGER);
INSERT INTO  Pair VALUES (1,2);
INSERT INTO  Pair VALUES (2,3);
INSERT INTO  Pair VALUES (3,4);
INSERT INTO  Pair VALUES (4,5);
INSERT INTO  Pair VALUES (5,6);
INSERT INTO  Pair VALUES (11,1);

SELECT tb1.M AS x1,tb2.N AS x2,tb3.M AS x3,tb4.N AS x4 FROM Pair tb1,Pair tb2,Pair tb3,Pair tb4 WHERE tb1.M != tb3.M AND tb2.N != tb4.N AND tb1.M + tb2.N = tb3.M + tb4.N;

--Question 4

CREATE TABLE P (M BOOLEAN);
CREATE TABLE Q (N BOOLEAN);
CREATE TABLE R (O BOOLEAN);
INSERT INTO  P VALUES (true);
INSERT INTO  Q VALUES (false);
INSERT INTO  R VALUES (true);
INSERT INTO  P VALUES (true);
INSERT INTO  Q VALUES (true);
INSERT INTO  R VALUES (true);

SELECT DISTINCT tb1.M AS p,tb2.N AS q,tb3.O AS r,((NOT((NOT tb1.M) OR tb2.N)) OR tb3.O) AS Result FROM P tb1,Q tb2,R tb3; 

--Question 5

CREATE TABLE A (M INTEGER);
CREATE TABLE B (M INTEGER);
CREATE TABLE C (M INTEGER);
INSERT INTO  A VALUES (1);
INSERT INTO  A VALUES (2);
INSERT INTO  B VALUES (1);
INSERT INTO  B VALUES (2);
INSERT INTO  C VALUES (1);
INSERT INTO  C VALUES (2);

--5a

SELECT EXISTS (SELECT * FROM A INTERSECT SELECT * FROM B) AS answer;

SELECT EXISTS (SELECT tb1.M FROM A tb1 WHERE tb1.M IN (SELECT tb2.M FROM B tb2)) AS answer;

--5b

SELECT NOT EXISTS (SELECT tb1.M FROM A tb1 WHERE tb1.M NOT IN (SELECT tb2.M FROM B tb2)) AS answer;

SELECT NOT EXISTS (SELECT tb1.M FROM A tb1 EXCEPT (SELECT tb2.M FROM B tb2)) AS answer;

--5c

SELECT NOT EXISTS ((SELECT tb1.M FROM A tb1 INTERSECT SELECT tb2.M FROM B tb2) EXCEPT (SELECT tb3.M FROM B tb3)) AS answer;

SELECT NOT EXISTS ((SELECT tb1.M FROM A tb1 WHERE tb1.M IN (SELECT tb2.M FROM B tb2) AND tb1.M NOT IN (SELECT tb3.M FROM B tb3))) AS answer;

--5d

SELECT EXISTS (SELECT tb1.M FROM A tb1 WHERE tb1.M != ALL (SELECT tb2.M FROM B tb2)) AS answer;

SELECT NOT EXISTS (SELECT * FROM A INTERSECT SELECT * FROM B) OR EXISTS (SELECT tb1.M FROM A tb1 EXCEPT (SELECT tb2.M FROM B tb2)) OR EXISTS (SELECT tb1.M FROM B tb1 EXCEPT (SELECT tb2.M FROM A tb2)) AS answer;

--5e

SELECT EXISTS (SELECT tf1.M,tf2.M FROM (SELECT tb1.M FROM A tb1 WHERE tb1.M IN (SELECT tb2.M FROM B tb2)) tf1,(SELECT tb1.M FROM A tb1 WHERE tb1.M IN (SELECT tb2.M FROM B tb2)) tf2 WHERE tf1.M != tf2.M);                   

SELECT EXISTS (SELECT tf1.M,tf2.M FROM (SELECT * FROM A INTERSECT SELECT * FROM B) tf1,(SELECT * FROM A INTERSECT SELECT * FROM B) tf2 WHERE tf1.M != tf2.M);                   

--5f

SELECT NOT EXISTS (SELECT tb1.M,tb3.M FROM A tb1,B tb3 WHERE tb1.M NOT IN (SELECT tb2.M FROM C tb2) AND tb3.M NOT IN (SELECT tb2.M FROM C tb2)) AS answer;

SELECT ((SELECT NOT EXISTS (SELECT tb1.M FROM A tb1 EXCEPT (SELECT tb2.M FROM C tb2))) AND (SELECT NOT EXISTS (SELECT tb3.M FROM B tb3 EXCEPT (SELECT tb2.M FROM C tb2)))) AS answer;


--5g

SELECT EXISTS (SELECT tf1.M,tf2.M FROM (SELECT tb1.M FROM A tb1 WHERE tb1.M NOT IN (SELECT tb2.M FROM B tb2)) tf1,(SELECT tb3.M FROM B tb3 WHERE tb3.M NOT IN (SELECT tb4.M FROM C tb4)) tf2 WHERE tf1.M = tf2.M AND NOT EXISTS (SELECT tb5.M FROM A tb5 WHERE tb5.M NOT IN (SELECT tb6.M FROM B tb6) AND tb5.M = tf1.M) AND NOT EXISTS (SELECT tb6.M FROM B tb6 WHERE tb6.M NOT IN (SELECT tb7.M FROM C tb7) AND tb6.M = tf2.M)) AS answer;

SELECT EXISTS (SELECT tf1.M,tf2.M FROM (SELECT tb1.M FROM A tb1 EXCEPT (SELECT tb2.M FROM B tb2)) tf1,(SELECT tb3.M FROM B tb3 EXCEPT (SELECT tb4.M FROM C tb4)) tf2 WHERE tf1.M = tf2.M AND NOT EXISTS (SELECT tb5.M FROM A tb5 EXCEPT (SELECT tb6.M FROM B tb6) AND tb5.M = tf1.M) AND NOT EXISTS (SELECT tb6.M FROM B tb6 EXCEPT (SELECT tb7.M FROM C tb7) AND tb6.M = tf2.M)) AS answer;


--Question 6

--6a

SELECT
(SELECT 
CASE WHEN COUNT( * ) > 0 THEN 
     CAST( 'True' AS VARCHAR(20)) 
ELSE 
      CAST( 'False' AS VARCHAR(20))  
END As answer
FROM (SELECT * FROM A INTERSECT SELECT * FROM B) AS x);

--6b

SELECT
(SELECT 
CASE WHEN COUNT( * ) > 0 THEN 
     CAST( 'False' AS VARCHAR(20)) 
ELSE 
      CAST( 'True' AS VARCHAR(20))  
END As answer
FROM (SELECT tb1.M FROM A tb1 EXCEPT (SELECT tb2.M FROM B tb2)) AS x);

--6c

SELECT
(SELECT 
CASE WHEN COUNT( * ) > 0 THEN 
     CAST( 'False' AS VARCHAR(20)) 
ELSE 
      CAST( 'True' AS VARCHAR(20))  
END As answer
FROM ((SELECT tb1.M FROM A tb1 INTERSECT SELECT tb2.M FROM B tb2) EXCEPT (SELECT tb3.M FROM B tb3)) AS x);

--6d

SELECT
(SELECT 
CASE WHEN COUNT( * ) > 0 THEN 
     CAST( 'True' AS VARCHAR(20)) 
ELSE 
      CAST( 'False' AS VARCHAR(20))  
END As answer
FROM (SELECT tb1.M FROM A tb1 WHERE tb1.M != ALL (SELECT tb2.M FROM B tb2)) AS x);

--6e

SELECT
(SELECT 
CASE WHEN COUNT( * ) > 0 THEN 
     CAST( 'True' AS VARCHAR(20)) 
ELSE 
      CAST( 'False' AS VARCHAR(20))  
END As answer
FROM (SELECT tf1.M,tf2.M FROM (SELECT * FROM A INTERSECT SELECT * FROM B) tf1,(SELECT * FROM A INTERSECT SELECT * FROM B) tf2 WHERE tf1.M != tf2.M) AS x);

--6f

SELECT
(SELECT 
CASE WHEN COUNT( * ) > 0 THEN 
     CAST( 'False' AS VARCHAR(20)) 
ELSE 
      CAST( 'True' AS VARCHAR(20))  
END As answer
FROM (SELECT tb1.M,tb3.M FROM A tb1,B tb3 WHERE tb1.M NOT IN (SELECT tb2.M FROM C tb2) AND tb3.M NOT IN (SELECT tb2.M FROM C tb2)) AS x);

--6g

SELECT
(SELECT 
CASE WHEN COUNT( * ) > 0 THEN 
     CAST( 'True' AS VARCHAR(20)) 
ELSE 
      CAST( 'False' AS VARCHAR(20))  
END As answer
FROM (SELECT tf1.M,tf2.M FROM (SELECT tb1.M FROM A tb1 WHERE tb1.M NOT IN (SELECT tb2.M FROM B tb2)) tf1,(SELECT tb3.M FROM B tb3 WHERE tb3.M NOT IN (SELECT tb4.M FROM C tb4)) tf2 WHERE tf1.M = tf2.M AND NOT EXISTS (SELECT tb5.M FROM A tb5 WHERE tb5.M NOT IN (SELECT tb6.M FROM B tb6) AND tb5.M = tf1.M) AND NOT EXISTS (SELECT tb6.M FROM B tb6 WHERE tb6.M NOT IN (SELECT tb7.M FROM C tb7) AND tb6.M = tf2.M)) AS x);

--Question 7

CREATE TABLE W(A INTEGER,B VARCHAR(5));
INSERT INTO  W VALUES(1,'John');
INSERT INTO  W VALUES(2,'Ellen');
INSERT INTO  W VALUES(3,'Ann');


(SELECT tb5.A FROM W tb5 WHERE ((SELECT COUNT( * ) FROM W tb1 ) - (SELECT COUNT( DISTINCT tb2.A ) FROM W tb2)) = 0)
UNION ALL
(SELECT tf1.A FROM
(SELECT tb3.A, COUNT(*)
FROM W tb3
WHERE ((SELECT COUNT( * ) FROM W tb1 ) - (SELECT COUNT( DISTINCT tb2.A ) FROM W tb2)) > 0
GROUP BY tb3.A
HAVING COUNT(*) > 1) tf1);

--Question 8

CREATE TABLE Student(Sid INTEGER,Sname VARCHAR(15));
CREATE TABLE Major(Sid INTEGER,Major VARCHAR(15));
CREATE TABLE Book(BookNo INTEGER,Title VARCHAR(30),Price INTEGER);
CREATE TABLE Buys(Sid INTEGER,BookNo INTEGER);

insert into Student (Sid, Sname) values  (1001, 'Jean'),	(1002, 'Maria'),(1003, 'Anna'),(1004, 'Chin'),(1005, 'John'),(1006, 'Ryan'),(1007, 'Catherine'),(1008, 'Emma'),(1009, 'Jan'),(1010, 'Linda'),(1011, 'Nick'),(1012, 'Eric'),	(1013, 'Lisa'),(1014, 'Filip'),(1015, 'Dirk'),	(1016, 'Mary'),	(1017, 'Ellen'),	(1020, 'Greg'),	(1022, 'Qin'),(1023, 'Melanie'),	(1040, 'Pam') ;

insert into Major (Sid, Major) values (1001,  'Math'),(1001, 'Physics'),(1002,  'CS'),		(1002,  'Math'),		(1003,  'Math'),	(1004,  'CS'),	(1006,  'CS'),(1007,  'CS')	,(1007,  'Physics'),		(1008,  'Physics'),	(1009,  'Biology'),		(1010,  'Biology'),	(1011,  'CS'),	(1011,  'Math'),		(1012,  'CS'),(1013,  'CS'),		(1013,  'Psychology'),		(1014,  'Theater'),		(1017,  'Anthropology'),		(1022,  'CS'),	(1015,  'Chemistry');

insert into Book (BookNo, Title, Price) values	(2001 , 'Databases',  40),	(2002 , 'OperatingSystems', 25),	(2003 , 'Networks',   20),	(2004 , 'AI',    45),	(2005 , 'DiscreteMathematics',    20),	(2006 , 'SQL',   25),	(2007 , 'ProgrammingLanguages',   15),	(2008 , 'DataScience', 50),	(2009 , 'Calculus',   10),	(2010 , 'Philosophy', 25),	(2012 , 'Geometry',   80),	(2013 , 'RealAnalysis ',    35),	(2011 , 'Anthropology',     50),	(2014 , 'Topology',   70);

insert into Buys (Sid,BookNo) values (1023 ,	2012), (1023 ,	2014), (1040,	2002), (1001,	2002),(1001,	2007),(1001,	2009),(1001,	2011),(1001,	2013),(1002,	2001),(1002,	2002),(1002,	2007),	(1002,	2011),(1002,	2012),(1002,	2013),(1003,	2002),	(1003,	2007),	(1003,	2011),	(1003,	2012),(1003,	2013),	(1004,	2006),	(1004,	2007),	(1004,	2008),	(1004,	2011),	(1004,	2012),(1004,	2013),	(1005,	2007),	(1005,	2011),	(1005,	2012),	(1005,	2013),(1006,	2006),	(1006,	2007),	(1006,	2008),	(1006,	2011),	(1006,	2012),	(1006,	2013),	(1007,	2001),	(1007,	2002),	(1007,	2003),	(1007,	2007),	(1007,	2008),	(1007,	2009),	(1007,	2010),	(1007,	2011),	(1007,	2012),	(1007,	2013),	(1008,	2007),	(1008,	2011),	(1008,	2012),	(1008,	2013),	(1009,	2001),	(1009,	2002),	(1009,	2011),	(1009,	2012),	(1009,	2013),	(1010,	2001),	(1010,	2002),	(1010,	2003),	(1010,	2011),	(1010,	2012),	(1010,	2013),	(1011,	2002),	(1011,	2011),	(1011,	2012),	(1012,	2011),	(1012,	2012),	(1013,	2001),	(1013,	2011),	(1013,	2012),	(1014,	2008),	(1014,	2011),	(1014,	2012),	(1017,	2001),	(1017,	2002),	(1017,	2003),	(1017,	2008),	(1017,	2012),	(1020,	2001),	(1020,	2012),	(1022,	2014);

--8a i

CREATE FUNCTION booksBoughtbyStudent9(snumber INT)
RETURNS TABLE(bookno int, title VARCHAR(30), price int)
AS 
$$
SELECT tb3.BookNo,tb3.Title,tb3.Price FROM Book tb3 WHERE tb3.BookNo IN (SELECT BookNo FROM Buys M WHERE M.Sid = snumber);
$$ LANGUAGE SQL;


--8a ii

SELECT bookno,title,price FROM booksBoughtbyStudent(1001);
SELECT bookno,title,price FROM booksBoughtbyStudent(1015);

--8a iii

SELECT Sid,Sname FROM Student tb1 WHERE (SELECT COUNT(*) FROM booksBoughtbyStudent9(tb1.Sid) tb2 WHERE tb2.price < 50) = 1;

SELECT tb1.Sid,tb2.Sid FROM Student tb1,Student tb2 WHERE (SELECT COUNT(*) FROM (SELECT * FROM booksBoughtbyStudent9(tb1.Sid) INTERSECT SELECT * FROM booksBoughtbyStudent9(tb2.Sid)) AS x) = (SELECT COUNT(*) FROM booksBoughtbyStudent9(tb1.Sid)) AND (SELECT COUNT(*) FROM (SELECT * FROM booksBoughtbyStudent9(tb1.Sid) INTERSECTSELECT * FROM booksBoughtbyStudent9(tb2.Sid)) AS x) = (SELECT COUNT(*) FROM booksBoughtbyStudent9(tb2.Sid)) AND tb1.Sid != tb2.Sid;

--8b i

CREATE FUNCTION studentsWhoBoughtBook(sbookno INT)
RETURNS TABLE(sid INT, sname VARCHAR(15))
AS
$$
SELECT tb1.Sid,tb1.Sname FROM Student tb1 WHERE tb1.Sid IN (SELECT tb2.Sid FROM Buys tb2 WHERE tb2.BookNo IN (SELECT tb3.BookNo FROM Book tb3 WHERE tb3.BookNo = sbookno));
$$ LANGUAGE SQL;

--8b ii

SELECT * FROM studentsWhoBoughtBook(2001);
SELECT * FROM studentsWhoBoughtBook(2010);

--8b iii

SELECT tb1.BookNo FROM Book tb1 WHERE (SELECT COUNT(*) FROM studentsWhoBoughtBook(tb1.BookNo) tb2 WHERE tb2.sid IN (SELECT tb3.Sid FROM Major tb3 WHERE Major = 'CS' AND tb3.Sid IN (SELECT tb4.Sid FROM Buys tb4 WHERE tb4.BookNo IN (SELECT BookNo From Book WHERE Price>30)))) >= 2;

--8c (Refrence Taken for Solutions in Assignment 2)

--i

CREATE FUNCTION booksBoughtbyStudent9(snumber INT)
RETURNS TABLE(bookno int, title VARCHAR(30), price int)
AS 
$$
SELECT tb3.BookNo,tb3.Title,tb3.Price FROM Book tb3 WHERE tb3.BookNo IN (SELECT BookNo FROM Buys M WHERE M.Sid = snumber);
$$ LANGUAGE SQL;

SELECT tb1.Sid,tb2.Major FROM Student tb1,Major tb2 WHERE tb1.Sid = tb2.Sid AND (SELECT COUNT(*) FROM booksBoughtbyStudent9(tb1.Sid) tb3 WHERE tb3.price > 30) >= 4;

--ii

CREATE FUNCTION booksBoughtbyStudent9(snumber INT)
RETURNS TABLE(bookno int, title VARCHAR(30), price int)
AS 
$$
SELECT tb3.BookNo,tb3.Title,tb3.Price FROM Book tb3 WHERE tb3.BookNo IN (SELECT BookNo FROM Buys M WHERE M.Sid = snumber);
$$ LANGUAGE SQL;
SELECT tb1.Sid,tb2.Sid FROM Student tb1,Student tb2 WHERE (SELECT SUM(tb3.Price) FROM booksBoughtbyStudent9(tb1.Sid) tb3) = (SELECT SUM(tb4.Price) FROM booksBoughtbyStudent9(tb2.Sid) tb4) AND tb1.Sid != tb2.Sid;

--iii

SELECT tb1.Sid,tb1.Sname FROM Student tb1 WHERE ((SELECT SUM(tb2.price) FROM booksBoughtbyStudent9(tb1.Sid) tb2) > ALL (SELECT AVG(b.Price) FROM Book b,Buys t WHERE b.BookNo = t.BookNo AND EXISTS(SELECT m.Major from Major m WHERE m.Major = 'CS'))) AND EXISTS(SELECT Major FROM Major WHERE Major.Sid = tb1.Sid and Major = 'CS') ;

--iv

SELECT tb2.BookNo,tb2.Title FROM Book tb2 WHERE tb2.Price = (SELECT tb1.Price FROM Book tb1 ORDER BY tb1.Price DESC LIMIT 1 OFFSET 2);

--v

select b.bookno,b.Title
from   book b
where  (select count(1)
                   from   buys t 
                   where  t.bookno = b.bookno 
                   except2
                   select m.sid
                   from   major m
                   where  m.major = 'CS') = 0 order by bookno;

--vi

select s.sid, s.sname
from   student s
where  (select count(1)
               from   buys t
               where  t.sid = s.sid and
                      t.bookno not in (select t1.bookno
                                       from   buys t1, buys t2
                                       where  t1.bookno = t2.bookno and
                                              t1.sid <> t2.sid and
                                              t1.sid in (select m.sid
                                                         from   major m
                                                         where  m.major = 'CS') and
                                              t2.sid in (select m.sid
                                                         from   major m
                                                         where  m.major = 'CS'))) >=1 order by sid, sname;
--vii

select x1.sid, b1.bookno from buys x1, book b1
where x1.bookno = b1.bookno and b1.price < all (
    select avg(b2.price) from book b2, buys x2
    where b2.bookno = x2.bookno and x2.sid = x1.sid) order by x1.sid,b1.bookno;



--viii

CREATE FUNCTION booksBoughtbyStudent9(snumber INT)
RETURNS TABLE(bookno int, title VARCHAR(30), price int)
AS 
$$
SELECT tb3.BookNo,tb3.Title,tb3.Price FROM Book tb3 WHERE tb3.BookNo IN (SELECT BookNo FROM Buys M WHERE M.Sid = snumber);
$$ LANGUAGE SQL;


SELECT tb1.Sid,tb2.Sid FROM Student tb1,Student tb2 WHERE (SELECT COUNT(*) FROM booksBoughtbyStudent9(tb1.Sid)) = (SELECT COUNT(*) FROM booksBoughtbyStudent9(tb2.Sid)) and tb1.Sid != tb2.Sid and (SELECT COUNT(*) FROM ((SELECT Major From Major WHERE Sid = tb1.Sid) INTERSECT (SELECT Major FROM Major WHERE Sid = tb2.Sid)) AS x) >= 1;

--ix

SELECT tb1.Sid,tb2.Sid,(SELECT COUNT(*) FROM (SELECT tb3.bookno FROM booksBoughtbyStudent9(tb1.Sid) tb3 WHERE tb3.bookno NOT IN( SELECT tb4.bookno FROM booksBoughtbyStudent9(tb2.Sid) tb4) ) AS x) FROM Student tb1,Student tb2 WHERE (SELECT COUNT(*) FROM ((SELECT Major From Major WHERE Sid = tb1.Sid) INTERSECT (SELECT Major FROM Major WHERE Sid = tb2.Sid)) AS x) >= 1 AND tb1.Sid != tb2.Sid;

--x

select b.bookno 
from   book b 
where  (select count(1) 
				from   major m 
				where  m.major = 'CS' and m.sid not in (select t.sid 
														from   buys t 
														where  t.bookno = b.bookno)) >=1 and 
														 (select count(1) from major m1, major m2 where m1.major = 'CS' and m2.major = 'CS' and m1.sid <> m2.sid and m1.sid not in (select t.sid
																																														from   buys t 
																																														where t.bookno = b.bookno) and m2.sid not in (select t.sid from   buys t where  t.bookno = b.bookno)) = 0 order by bookno;


--Question 9

CREATE TABLE Student(sid INTEGER PRIMARY KEY,sname text);
CREATE TABLE Course(cno INTEGER PRIMARY KEY, cname text, total INTEGER, max INTEGER);
CREATE TABLE Prerequisite(cno INTEGER, prereq INTEGER,FOREIGN KEY (cno) REFERENCES Course(cno),FOREIGN KEY (prereq) REFERENCES Course(cno));
CREATE TABLE HasTaken(sid INTEGER,cno INTEGER,FOREIGN KEY (cno) REFERENCES Course(cno),FOREIGN KEY (sid) REFERENCES Student(sid));
CREATE TABLE Enroll(sid INTEGER,cno INTEGER,FOREIGN KEY (cno) REFERENCES Course(cno),FOREIGN KEY (sid) REFERENCES Student(sid));
CREATE TABLE Waitlist(sid INTEGER,cno INTEGER, position INTEGER,FOREIGN KEY (sid) REFERENCES Student(sid),FOREIGN KEY (cno) REFERENCES Course(cno));

INSERT INTO Course VALUES(201,'Programming',0,3);
INSERT INTO Course VALUES(202,'Calculus',0,3);
INSERT INTO Course VALUES(203,'Probability',0,3);
INSERT INTO Course VALUES(204,'AI',0,2);
INSERT INTO Course VALUES (301,'DiscreteMathematics',0,2);
INSERT INTO Course VALUES (302,'OS',0,2);
INSERT INTO Course VALUES (303,'Databases',0,2);
INSERT INTO Course VALUES (401,'DataScience',0,2);
INSERT INTO Course VALUES (402,'Networks',0,2);
INSERT INTO Course VALUES (403,'Philosophy',0,2);

INSERT INTO Prerequisite VALUES (301,201);
INSERT INTO Prerequisite VALUES (301,202);
INSERT INTO Prerequisite VALUES (302,201);
INSERT INTO Prerequisite VALUES (302,202);
INSERT INTO Prerequisite VALUES (302,203);
INSERT INTO Prerequisite VALUES (401,301);
INSERT INTO Prerequisite VALUES (401,204);
INSERT INTO Prerequisite VALUES (402,302);

INSERT INTO Student VALUES (1,'Jean');
INSERT INTO Student VALUES (2,'Eric');
INSERT INTO Student VALUES (3,'Ahmed');
INSERT INTO Student VALUES (4,'Qin');
INSERT INTO Student VALUES (5,'Filip');
INSERT INTO Student VALUES (6,'Pam');
INSERT INTO Student VALUES (7,'Lisa');

INSERT INTO Hastaken VALUES (1,201);
INSERT INTO Hastaken VALUES (1,202);
INSERT INTO Hastaken VALUES (1,301);
INSERT INTO Hastaken VALUES (2,201);
INSERT INTO Hastaken VALUES (2,202);
INSERT INTO Hastaken VALUES (3,201);
INSERT INTO Hastaken VALUES (4,201);
INSERT INTO Hastaken VALUES (4,202);
INSERT INTO Hastaken VALUES (4,203);
INSERT INTO Hastaken VALUES (4,204);
INSERT INTO Hastaken VALUES (5,201);
INSERT INTO Hastaken VALUES (5,202);
INSERT INTO Hastaken VALUES (5,301);
INSERT INTO Hastaken VALUES (5,204);



CREATE VIEW Enroll_view AS 
SELECT sid,cno FROM Enroll;


CREATE OR REPLACE FUNCTION insert_enroll() RETURNS TRIGGER AS
$$
DECLARE
test BOOLEAN;
count INTEGER;
BEGIN
  test = (SELECT NOT EXISTS (SELECT 1 FROM Waitlist WHERE cno = NEW.cno));
  IF((SELECT COUNT(*) FROM ((SELECT tb3.prereq FROM Prerequisite tb3 WHERE tb3.cno = NEW.cno) EXCEPT (SELECT tb4.cno FROM HasTaken tb4 WHERE tb4.sid = NEW.sid)) AS foo) = 0) THEN
     IF((SELECT total + 1 FROM Course WHERE cno = NEW.cno) <= (SELECT max FROM Course WHERE cno = NEW.cno)) THEN
       UPDATE Course SET total = total + 1 WHERE cno = NEW.cno;
       INSERT INTO Enroll VALUES(NEW.sid, NEW.cno);
     ELSE
       IF(test) THEN
          INSERT INTO Waitlist VALUES (NEW.sid,NEW.cno,1);
       ELSE
          count = (SELECT MAX(position) FROM Waitlist WHERE cno = NEW.cno);
          INSERT INTO Waitlist VALUES (NEW.sid,NEW.cno,count + 1);
       END IF;
     END IF;
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE PLPGSQL;



CREATE OR REPLACE FUNCTION delete_enroll() RETURNS TRIGGER AS
$$
DECLARE
sid1 INTEGER;
cno1 INTEGER;
BEGIN
  IF((SELECT COUNT(*) FROM Waitlist WHERE cno = OLD.cno) = 0) THEN
     UPDATE Course SET total = total - 1 WHERE cno = OLD.cno;
  ELSE
     sid1 = (SELECT sid FROM Waitlist WHERE cno = OLD.cno AND position = (SELECT MIN(position) FROM Waitlist WHERE cno = OLD.cno));
     cno1 = (SELECT cno FROM Waitlist WHERE cno = OLD.cno AND position = (SELECT MIN(position) FROM Waitlist WHERE cno = OLD.cno));
     INSERT INTO Enroll VALUES(sid1, cno1);
     DELETE FROM Waitlist WHERE sid = sid1 AND cno = cno1;
     DELETE FROM Enroll WHERE sid = OLD.sid AND cno = OLD.cno;
     UPDATE Waitlist SET position = position - 1 WHERE cno = OLD.cno;
  END IF; 
  RETURN OLD;
END;
$$ LANGUAGE PLPGSQL;


CREATE TRIGGER insert_into_Enroll_student INSTEAD OF INSERT ON Enroll_view FOR EACH ROW EXECUTE PROCEDURE insert_enroll();

CREATE TRIGGER delete_from_Enroll_student INSTEAD OF DELETE ON Enroll_view FOR EACH ROW EXECUTE PROCEDURE delete_enroll();






