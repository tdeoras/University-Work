CREATE DATABASE tejas;
\connect tejas;

--Assignment Question 1
CREATE TABLE Sailor (Sid INTEGER, Sname VARCHAR(20), Rating INTEGER, Age INTEGER,PRIMARY KEY(Sid));
CREATE TABLE Boat (Bid INTEGER, Bname VARCHAR(15), Color VARCHAR(15),PRIMARY KEY(Bid));
CREATE TABLE Reserves (Sid INTEGER, Bid INTEGER, Day VARCHAR(10),PRIMARY KEY(Sid,Bid), CONSTRAINT FK_Sid FOREIGN KEY (Sid) REFERENCES Sailor(Sid) ON DELETE CASCADE, CONSTRAINT FK_Bid FOREIGN KEY (Bid) REFERENCES Boat (Bid) ON DELETE CASCADE);
--Assignment Question 2
--Primary Key should not contain null values
INSERT INTO  Boat VALUES (NULL , 'Interlake', 'blue');
--Primary key should not contain duplicate values
INSERT INTO  Boat VALUES (101,  'Interlake', 'blue');
INSERT INTO Boat VALUES (101, 'Sunset', 'red');
--Referential Integrity Insertion
INSERT INTO  Sailor VALUES (22,'Dustin',7,45);
INSERT INTO  Reserves VALUES (31,102,'Thursday');
INSERT INTO  Reserves VALUES (31,101,'Thursday');
INSERT INTO  Sailor VALUES (31,'Lubber',8,55);
INSERT INTO  Reserves VALUES (31,101,'Thursday');
--Referential Integrity Deletions
DELETE FROM Sailor;
DELETE FROM Boat;
DELETE FROM Reserves;
INSERT INTO  Boat VALUES (101,  'Interlake', 'blue');
INSERT INTO Boat VALUES (102, 'Sunset', 'red');
INSERT INTO  Boat VALUES (103,  'Clipper', 'green');
INSERT INTO  Sailor VALUES (22,'Dustin',7,45);
INSERT INTO  Sailor VALUES (29,'Brutus',1,33);
INSERT INTO  Sailor VALUES (31,'Lubber',8,55);
INSERT INTO  Sailor VALUES (32,'Andy',8,25);
INSERT INTO  Reserves VALUES (22,101,'Monday');
INSERT INTO  Reserves VALUES (22,102,'Tuesday');
INSERT INTO  Reserves VALUES (22,103,'Wednesday');
INSERT INTO  Reserves VALUES (31,102,'Thursday');
INSERT INTO  Reserves VALUES (31,103,'Friday');
DELETE FROM Boat WHERE Bid = 101;
SELECT * FROM Boat;
ALTER TABLE Reserves DROP CONSTRAINT FK_Bid;
ALTER TABLE Reserves ADD CONSTRAINT FK_Bid FOREIGN KEY (Bid) REFERENCES Boat (Bid) ON DELETE RESTRICT;
DELETE FROM Sailor;
DELETE FROM Boat;
DELETE FROM Reserves;
INSERT INTO  Boat VALUES (101,  'Interlake', 'blue');
INSERT INTO Boat VALUES (102, 'Sunset', 'red');
INSERT INTO  Boat VALUES (103,  'Clipper', 'green');
INSERT INTO  Sailor VALUES (22,'Dustin',7,45);
INSERT INTO  Sailor VALUES (29,'Brutus',1,33);
INSERT INTO  Sailor VALUES (31,'Lubber',8,55);
INSERT INTO  Sailor VALUES (32,'Andy',8,25);
INSERT INTO  Reserves VALUES (22,101,'Monday');
INSERT INTO  Reserves VALUES (22,102,'Tuesday');
INSERT INTO  Reserves VALUES (22,103,'Wednesday');
INSERT INTO  Reserves VALUES (31,102,'Thursday');
INSERT INTO  Reserves VALUES (31,103,'Friday');
DELETE FROM Boat WHERE Bid = 101;
SELECT * FROM Boat;
--Assignment Question 3
DELETE FROM Sailor;
DELETE FROM Boat;
DELETE FROM Reserves;
INSERT INTO  Boat VALUES (101,  'Interlake', 'blue');
INSERT INTO Boat VALUES (102, 'Sunset', 'red');
INSERT INTO  Boat VALUES (103,  'Clipper', 'green');
INSERT INTO  Boat VALUES (104,  'Marine',  'red');
INSERT INTO  Sailor VALUES (22,'Dustin',7,45);
INSERT INTO  Sailor VALUES (29,'Brutus',1,33);
INSERT INTO  Sailor VALUES (31,'Lubber',8,55);
INSERT INTO  Sailor VALUES (32,'Andy',8,25);
INSERT INTO  Sailor VALUES (58,'Rusty',10,35);
INSERT INTO  Sailor VALUES (64,'Horatio',7,35);
INSERT INTO  Sailor VALUES (71,'Zorba',10,16);
INSERT INTO  Sailor VALUES (74,'Horatio',9,35);
INSERT INTO  Sailor VALUES (85,'Art',3,25);
INSERT INTO  Sailor VALUES (95,'Bob',3,63);
INSERT INTO  Reserves VALUES (22,101,'Monday');
INSERT INTO  Reserves VALUES (22,102,'Tuesday');
INSERT INTO  Reserves VALUES (22,103,'Wednesday');
INSERT INTO  Reserves VALUES (31,102,'Thursday');
INSERT INTO  Reserves VALUES (31,103,'Friday');
INSERT INTO  Reserves VALUES (31,104,'Saturday');
INSERT INTO  Reserves VALUES (64,101,'Sunday');
INSERT INTO  Reserves VALUES (64,102,'Monday');
INSERT INTO  Reserves VALUES (74,102,'Saturday');

SELECT Rating,Sname FROM Sailor;

SELECT Bid,Color FROM Boat;

SELECT Sname FROM Sailor WHERE Age>15 AND Age<30;

SELECT B.Bname FROM Boat B,(SELECT M.Bid FROM Reserves M WHERE M.Day='Saturday' OR M.Day = 'Sunday') R WHERE B.Bid = R.Bid; 

SELECT B.Bname,S.Sid,B.Bid FROM Sailor S,Reserves R,Boat B WHERE B.Bid = R.Bid AND S.Sid = R.Sid AND B.Color ='blue' INTERSECT SELECT B.Bname,S.Sid,B.Bid FROM Sailor S,Reserves R,Boat B WHERE B.Bid = R.Bid AND S.Sid = R.Sid AND B.Color ='red';

SELECT B.Bname,S.Sid,B.Bid FROM Sailor S,Reserves R,Boat B WHERE B.Bid = R.Bid AND S.Sid = R.Sid AND B.Color ='red' EXCEPT SELECT B.Bname,S.Sid,B.Bid FROM Sailor S,Reserves R,Boat B WHERE B.Bid = R.Bid AND S.Sid = R.Sid AND (B.Color ='blue' OR B.Color = 'green');

SELECT COUNT(B.Bid),S.Sid,S.Sname FROM Sailor S,Reserves R,Boat B WHERE B.Bid = R.Bid AND S.Sid = R.Sid GROUP BY S.Sid HAVING COUNT(B.Bid) > 2;

SELECT S.Sid FROM Sailor S WHERE S.Sid NOT IN (SELECT S.Sid FROM Sailor S,Reserves R,Boat B WHERE S.Sid = R.Sid AND R.Bid = B.Bid);

SELECT S1.Sid,S2.Sid FROM Sailor S1,Sailor S2 WHERE S1.Sid <> S2.Sid AND EXISTS (SELECT S1.Sid FROM Reserves R WHERE R.Sid = S1.Sid AND R.Day='Saturday') AND EXISTS (SELECT S2.Sid FROM Reserves R WHERE R.Sid = S2.Sid AND R.Day='Saturday');

SELECT B.Bid FROM Sailor S,Reserves R,Boat B WHERE B.Bid = R.Bid AND S.Sid = R.Sid AND NOT EXISTS (SELECT B1.Bid FROM Sailor S1,Reserves R1,Boat B1 WHERE B1.Bid = R1.Bid AND S1.Sid = R1.Sid AND B1.Bid NOT IN (SELECT B2.Bid FROM Sailor S2,Reserves R2,Boat B2 WHERE B2.Bid = R2.Bid AND S2.Sid = R2.Sid AND B2.Bid != B.Bid));

\connect postgres;
DROP DATABASE tejas;

