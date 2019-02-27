CREATE DATABASE tejas;
\connect tejas;

---	Insert and Table Creation

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

--q1 Logic - QUERY CHECKS IF SID OF PEOPLE HAVING MAJOR ARE IN SID OF PEOPLE WHO BOUGHT BOOKS WHOSE BOOKNO HAVING A PRICE < 20

SELECT Sid,Major FROM Major where Sid IN (SELECT Sid FROM Buys WHERE BookNo IN(SELECT BookNo FROM Book WHERE Price < 20));

--q2 Logic - FIRST CHECK THE PRICE THEN THEN SEE IF VALUES CORRESPOND TO CITED BOOK LIST 

SELECT BookNo , Title FROM Book WHERE Price > 20 AND Price < 40 AND BookNo IN (SELECT CitedBookNo FROM Cites);

--q3 CHECK IF SIDS OF CS AND USING RELATION HAS A LOWER COST CITED BOOK BY CHECKING THE BOOKNO IN CITEDLIST AND COMPARING PRICES

SELECT Sid, Sname FROM Student WHERE Sid IN (SELECT Sid From Major WHERE Major = 'CS' AND Sid IN (SELECT Sid from Buys WHERE BookNo IN ( SELECT BookNo FROM Book M WHERE BookNo IN (SELECT CitedBookNo FROM Cites WHERE CitedBookNo IN (SELECT BookNo FROM Book S WHERE M.Price > S.Price)))));

--q4 CHECK IF BOOK IS CITED AND THAT CITED BOOK IS CITED BY SOMEONE ELSE 

SELECT BookNo ,Title FROM Book WHERE BookNo IN (SELECT CitedBookNo FROM Cites WHERE CitedBookNo IN (SELECT BookNo FROM Cites));

--q5 REFERED SLIDES AND USED ALL <= AS LOWEST VALUE HAS TO BE EQUAL TO ITSELF

SELECT BookNo,Price FROM Book L WHERE L.Price <= ALL (SELECT Price FROM Book);

--q6 REFERED FROM : https://stackoverflow.com/questions/7171041/what-does-it-mean-by-select-1-from-table AS HAD PROBLEMS SELECTING 1 VALUE

SELECT BookNo,Title FROM Book L WHERE NOT EXISTS (SELECT 1 FROM Book M WHERE L.Price < M.Price);

--q7 FOUND THE 2nd MOST EXPENSIVE BY REMOVING MOST EXPEENSIVE AND AGAIN FINDING EXPENSINSIVE ON THE RESULT

SELECT BookNo,Title FROM Book S WHERE BookNo NOT IN (SELECT BookNo FROM Book T WHERE T.Price <= ALL(SELECT Price FROM Book) AND S.Price <= ALL(SELECT Price FROM Book);

--q8 CHECKED BOOKS THAT ARE NOT CITED THEN THE CITED BOOKS WITH PRICE >20

SELECT BookNo,Price FROM Book WHERE BookNo NOT IN (SELECT CitedBookNo FROM Cites) OR BookNo IN (SELECT CitedBookNo FROM Cites WHERE CitedBookNo IN (SELECT BookNo FROM Book WHERE Price > 20));

--q9 CHECKED BOOKS WHICH STUDENTS BOUGHT AND HAD GIVEN MAJORS

SELECT BookNo,Title FROM Book where BookNo IN (SELECT BookNo FROM Buys WHERE Sid IN (SELECT Sid FROM Student WHERE Sid IN (SELECT Sid FROM Major WHERE Major = 'Biology' OR Major = 'Psychology')));

--q10 SIMILAR LOGIC AS Q10 EXCEPT USED NOT IN

SELECT BookNo,Title FROM Book WHERE BookNo IN (SELECT BookNo FROM Buys where Sid NOT IN (SELECT Sid FROM Student WHERE Sid IN (SELECT Sid FROM Major WHERE Major = 'CS')));

--q11 SIMILAR LOGIC AS Q10

SELECT BookNo,Title FROM Book WHERE BookNo IN (SELECT BookNo FROM Buys where Sid NOT IN (SELECT Sid FROM Student WHERE Sid IN (SELECT Sid FROM Major WHERE Major = 'Biology')));

--q12 CHECKED BOOKS WHICH STUDENTS BOUGHT AND HAD GIVEN MAJORS

SELECT BookNo,Title FROM Book WHERE BookNo IN (SELECT BookNo FROM Buys where Sid NOT IN (SELECT Sid FROM Student WHERE Sid IN (SELECT Sid FROM Major WHERE Major = 'CS' AND Major = 'Math')));

--q13 CHECKED IF BOOKS BOUGHT BY TWO STUDENT HAD DIFFENT SIDS 

SELECT Sid,Sname FROM Student WHERE Sid IN (SELECT Sid FROM Buys WHERE BookNo NOT IN (SELECT BookNo FROM Buys M WHERE M.BookNo IN (SELECT BookNo FROM Buys K WHERE M.Sid != K.Sid)));

--q14 CHECK IF OTHER BOOK IS NOT THERE WHITH COST HIGHER THAN 20 

SELECT Sid,Sname FROM Student WHERE Sid NOT IN (SELECT Sid FROM Buys WHERE BookNo IN (SELECT BookNo FROM Book WHERE Price > 20));

--q15 CHECKED CHEAPEST PRICE BY ALL AND MATCHED IT WITH STUDENT SID

SELECT Sid,BookNo FROM Student S, Book B WHERE S.Sid IN (SELECT Sid FROM Buys WHERE BookNo IN (SELECT BookNo FROM Book WHERE Price <= ALL (SELECT Price FROM Book)));

--q16 FIRST COMAPRED MAJORS WITH EXISTS AND CHECKED IF THERE DOES NOT EXIST BOOK THAT THEY BOUGHT SAME

SELECT M.Sid,N.Sid FROM Student M,Student N WHERE EXISTS (SELECT Major FROM Major WHERE M.Sid = N.Sid) AND NOT EXISTS (SELECT BookNo FROM Book WHERE BookNo IN (SELECT BookNo FROM Buys WHERE N.Sid = M.Sid));

--q17 CHECK IF THERE DOES NOT EXIST A CASE WHERE BOOK BY S1 IS BOUGHT BY S2

SELECT M.Sid , N.Sid , B.BookNo FROM Student M,Student N,Buys B WHERE NOT EXISTS (SELECT L.Sid , K.Sid FROM Buys L,Buys K WHERE L.BookNo = K.BookNo AND L.BookNo IN (SELECT BookNo FROM Buys WHERE BookNo IN (SELECT BookNo FROM Buys K WHERE Sid != M.Sid) ) AND K.BookNo IN (SELECT BookNo FROM Buys WHERE BookNo IN (SELECT BookNo FROM Buys K WHERE Sid != N.Sid) ));

--q18 CHECK IF A BOK THEY BOUGHT IN COMMON EXISTS AND THEN CHECK IF THERE DOES NOT EXIST A BOOK COMMON TO BOTH OF THEM

SELECT M.Sid,N.Sid FROM Student M,Student N WHERE EXISTS (SELECT L.Sid , K.Sid FROM Buys L,Buys K WHERE L.BookNo = K.BookNo AND L.Sid = M.Sid AND K.Sid = N.Sid AND NOT EXISTS (SELECT P.Sid , Q.Sid FROM Buys P,Buys Q WHERE P.BookNo = L.BookNo AND Q.BookNo = K.BookNo AND L.Sid = M.Sid AND K.Sid = N.Sid));
--q19
SELECT DISTINCT Sid,BookNo FROM Student S, Book B WHERE S.Sid IN (SELECT Sid FROM Buys WHERE BookNo IN (SELECT BookNo FROM Book WHERE Price <= ALL (SELECT Price FROM Book WHERE BookNo IN (SELECT BookNo FROM Buys M WHERE M.Sid = S.Sid))));

\connect postgres;
DROP DATABASE tejas;


