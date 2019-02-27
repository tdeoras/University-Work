CREATE DATABASE tejas;
\connect tejas;

-- Solution 1

DROP TABLE superSetsOfSet;
DROP TABLE A;

CREATE table A(x int);
INSERT INTO A(x) values (1),(2),(3),(4);
SELECT * FROM A;

create or replace function get_combinations(source anyarray, size int) returns setof anyarray as $$
 with recursive combinations(combination, indices) as (
   select source[i:i], array[i] from generate_subscripts(source, 1) i
   union all
   select c.combination || source[j], c.indices || j
   from   combinations c, generate_subscripts(source, 1) j
   where  j > all(c.indices) and
          array_length(c.combination, 1) < size
 )
 select combination from combinations
 where  array_length(combination, 1) = size;
$$ language sql;

CREATE OR REPLACE FUNCTION supersetsofset1 (A int[]) RETURNS TABLE (c int[])
AS $$
   DECLARE
     b1 int[];
     length int;
   BEGIN
   SELECT COUNT(*) INTO length FROM A;
   CREATE TABLE IF NOT EXISTS superSetsOfSet(c int[]);
   INSERT INTO superSetsOfSet VALUES ('{}');
   SELECT ARRAY(SELECT * FROM A) INTO b1;
       FOR counter IN 1..length LOOP
           INSERT INTO superSetsOfSet(c) SELECT * FROM get_combinations(b1,counter);          
       END LOOP;
    RETURN QUERY SELECT DISTINCT ss.c FROM superSetsOfSet ss where A <@ ss.c;
   END
$$ LANGUAGE plpgsql;

SELECT supersetsofset1('{1,3}'); 


-- Solution 2

create table Graph (s int, t int);
insert into graph values(1,2), (2,3), (3,4), (4,5);
--insert into graph values(5,1);


CREATE OR REPLACE FUNCTION find_path_length (a1 int,a2 int) RETURNS INT
AS $$
   DECLARE
      end1 int = a1;
      len int := 0;
      x record;
   BEGIN
    WHILE end1 <> a2 LOOP
       for x in (SELECT * FROM Graph)
        LOOP
           IF x.s = end1
           THEN len := len + 1;
           end1 = x.t;
           EXIT;
           END IF; 
       END LOOP;
    IF len = 0 THEN 
        len := 999;
        EXIT;
    END IF;   
    END LOOP; 
    RETURN len;
   END
$$ LANGUAGE plpgsql;

SELECT find_path_length(1,2);

/*
CREATE OR REPLACE FUNCTION connectedByEvenLengthPath() RETURNS TABLE (p1 int,p2 int) 
AS $$

   DECLARE
     x int;
     y int;
     t1 int;
     t2 int;
   BEGIN
     CREATE TABLE IF NOT EXISTS nodes(c int);
     CREATE TABLE IF NOT EXISTS answer(p1 int,p2 int);
     INSERT INTO nodes(c) SELECT DISTINCT g.s from Graph g;
     INSERT INTO nodes(c) SELECT DISTINCT g.t from Graph g;
       FOR x in (SELECT DISTINCT n.c FROM nodes n)
         LOOP
            FOR y in (SELECT DISTINCT n.c FROM nodes n)
                LOOP
                t1 := find_path_length(x,y);
                t2 := find_path_length(y,x);
                IF t1 <> 999 THEN
                   IF t1%2 = 0 THEN
                      INSERT INTO answer VALUES (x,y);
                      EXIT;
                   END IF;
                END IF;
                IF t2 <> 999 THEN
                   IF t2%2 = 0 THEN
                      INSERT INTO answer VALUES (x,y);
                      EXIT;
                   END IF;
                END IF;
                IF x = y THEN
                   INSERT INTO answer VALUES (x,y);
                   EXIT;
                END IF;
            END LOOP;           
         END LOOP;
         RETURN QUERY SELECT * FROM answer;          
   END$$ LANGUAGE plpgsql;

 CREATE OR REPLACE FUNCTION connectedByOddLengthPath() RETURNS TABLE (p1 int,p2 int) 
AS $$

   DECLARE
     x int;
     y int;
     t1 int;
     t2 int;
   BEGIN
     CREATE TABLE IF NOT EXISTS nodes(c int);
     CREATE TABLE IF NOT EXISTS answer(p1 int,p2 int);
     INSERT INTO nodes(c) SELECT DISTINCT g.s from Graph g;
     INSERT INTO nodes(c) SELECT DISTINCT g.t from Graph g;
       FOR x in (SELECT DISTINCT n.c FROM nodes n)
         LOOP
            FOR y in (SELECT DISTINCT n.c FROM nodes n)
                LOOP
                t1 := find_path_length(x,y);
                t2 := find_path_length(y,x);
                IF t1 <> 999 THEN
                   IF t1%2 != 0 THEN
                      INSERT INTO answer VALUES (x,y);
                   END IF;
                END IF;
                IF t2 <> 999 THEN
                   IF t2%2 != 0 THEN
                      INSERT INTO answer VALUES (x,y);
                   END IF;
                END IF;
            END LOOP;           
         END LOOP;
         RETURN QUERY SELECT * FROM answer;          
   END$$ LANGUAGE plpgsql;

*/


--Solution 3

drop table graph;

CREATE TABLE graph (
    source int,
    target int
);

INSERT INTO graph VALUES 
(1, 3), 
(1, 2), 
(2, 3), 
(2, 4), 
(3, 7), 
(4, 5), 
(7, 4), 
(4, 6),
(7,6);


create table index(index serial);

create or replace function topologicalsort()
    returns table(  node integer) as
    $$
    --Begin
        WITH RECURSIVE traverse(id, path, cycle) AS (
                SELECT graph.source, ARRAY[graph.source], false FROM graph 
                LEFT OUTER JOIN graph AS e2
                ON graph.source = e2.target
                WHERE e2.target IS NULL
            UNION ALL
                SELECT DISTINCT graph.target, 
                       traverse.path || graph.target,
                       graph.target = ANY(traverse.path)
                FROM traverse
                INNER JOIN graph
                ON graph.source = traverse.id 
                WHERE NOT cycle 
        )


        SELECT traverse.id FROM traverse
        LEFT OUTER JOIN traverse AS any_cycles ON any_cycles.cycle = true
        WHERE any_cycles.cycle IS NULL
        GROUP BY traverse.id
        ORDER BY MAX(array_length(traverse.path, 1));
        --return next(index serial, node integer)
     --end;

    $$ language sql;


select * from topologicalsort();



-- Solution 6

DROP TABLE document;

CREATE TABLE document (doc text, words text[]);
INSERT INTO document VALUES ('d1', '{"A","B","C"}');
INSERT INTO document VALUES ('d2', '{"B","C","D"}');
INSERT INTO document VALUES ('d3', '{"A","E"}');
INSERT INTO document VALUES ('d4', '{"B","B","A","D"}');
INSERT INTO document VALUES ('d5', '{"E","F"}');
INSERT INTO document VALUES ('d6', '{"A","D","G"}');
INSERT INTO document VALUES ('d7', '{"C","B","A"}');
INSERT INTO document VALUES ('d8', '{"B","A"}');

SELECT DISTINCT UNNEST(d.words) AS word FROM document d;

create or replace function get_combinations(source anyarray, size int) returns setof anyarray as $$
 with recursive combinations(combination, indices) as (
   select source[i:i], array[i] from generate_subscripts(source, 1) i
   union all
   select c.combination || source[j], c.indices || j
   from   combinations c, generate_subscripts(source, 1) j
   where  j > all(c.indices) and
          array_length(c.combination, 1) < size
 )
 select combination from combinations
 where  array_length(combination, 1) = size;
$$ language sql;

CREATE OR REPLACE FUNCTION supersetsofset2 (A text[]) RETURNS TABLE (c text[])
AS $$
   DECLARE
     b1 text[];
     length int;
   BEGIN
   SELECT COUNT(*) INTO length FROM (SELECT DISTINCT UNNEST(d.words) AS word FROM document d) x;
   CREATE TABLE IF NOT EXISTS superSetsOfSet2(c text[]);
   INSERT INTO superSetsOfSet2 VALUES ('{}');
   SELECT ARRAY(SELECT DISTINCT UNNEST(d.words) AS word FROM document d) INTO b1;
       FOR counter IN 1..length LOOP
           INSERT INTO superSetsOfSet2(c) SELECT * FROM get_combinations(b1,counter);          
       END LOOP;
    RETURN QUERY SELECT DISTINCT ss.c FROM superSetsOfSet2 ss where A <@ ss.c;

   END
$$ LANGUAGE plpgsql;

--SELECT supersetsofset2('{}'::text[]);



CREATE OR REPLACE FUNCTION frequentSets (t int) RETURNS TABLE (c text[])
AS $$
   BEGIN 
     CREATE TABLE IF NOT EXISTS allcombi(c text[]);
     INSERT INTO allcombi(c) SELECT supersetsofset2('{}'::text[]);
     RETURN QUERY (SELECT DISTINCT ac.c FROM allcombi ac WHERE t <= (SELECT COUNT(*) FROM document WHERE ac.c <@ words));
   END
$$ LANGUAGE plpgsql;


SELECT * FROM frequentSets(1);
select * from frequentSets(2);
select * from frequentSets(3);
select * from frequentsets(4);
select * from frequentsets(5);



--Solution 7


create table points(pid int primary key, x float, y float);

create table centroids(cid int primary key, x float, y float);

create table clusters(pid int references points(pid), cid int);


insert into points values (1,1.0,1.0),(2,1.5,2.0),(3,3.0,4.0),(4,5.0,7.0),(5,3.5,5.0),(6,4.5,5.0),(7,3.5,4.5);


create or replace function init(k int)
returns void as $$
declare
	ctr int = 0;
	p points%rowtype;
begin
	truncate centroids;
	truncate clusters;
	loop
		insert into centroids values ((ctr+1),(select random()*(10-1)+1),(select random()*(10-1)+1));
		ctr = ctr+1;
		if ctr=k then
		exit;
		end if;
	end loop;
	truncate clusters;
	for p in select * from points loop
		insert into clusters values(p.pid,0);
	end loop;
end;
$$ language plpgsql;

create or replace function kmeans(k int)
returns table(p int, c int) as $$ 
declare 
	p points%rowtype;
	c centroids%rowtype;
	dist float;
	temp float;
	nearest int;
	ctr integer = 0; 
Begin
	perform init(k);
	loop
		for p in select * from points 
		loop 
			dist = 1000;
			for c in select * from centroids
			loop 
				temp = ((p.x-c.x)^2+(p.y-c.y)^2)^.5;
				if temp<dist then
					dist = temp;
					nearest = c.cid;
				end if; 
			end loop; 
			update clusters set cid=nearest where pid=p.pid;
		end loop;
		for c in select * from centroids
		loop
			if c.cid in (select clust.cid from clusters clust) then
				update centroids set x=(select avg(po.x) from clusters clust inner join points po on clust.pid=po.pid where clust.cid=c.cid group by clust.Cid), y=(select avg(po.y) from clusters clust inner join points po on clust.pid=po.pid where clust.cid=c.cid group by clust.Cid) where c.cid=cid;
			end if;
		end loop;
		ctr = ctr+1;
		if ctr=200 then
			exit;
		end if; 
	end loop; 
	return query
		select * from clusters;
end; 
$$language plpgsql;

SELECT * FROM kmeans(2);



--Solution 8


CREATE TABLE Parts_SubParts (pid integer, sid integer, quantity integer);
CREATE TABLE Parts (pid integer, weight integer);



insert into Parts_SubParts (pid, sid, quantity) values 
(1,2,4),
(1,3,1),
(3,4,1),
(3,5,2),
(3,6,3),
(6,7,2),
(6,8,3);

insert into parts (pid, weight) values
(2,5),
(4,50),
(5,3),
(7,6),
(8,10);




CREATE TABLE WeightTemp(id integer, q integer);

Create or replace function weight(part INTEGER)
returns INTEGER as
$$
DECLARE N INTEGER;
DECLARE total INTEGER;
DECLARE subPart INTEGER;
DECLARE quantity INTEGER;
Begin
	--Base case
	if (select not exists(select 1 from Parts_SubParts where pid = part)) then
		return (select p.weight from parts p where p.pid = part);
	end if; 


	
	insert into WeightTemp (select p.sid,p.quantity from Parts_SubParts p where p.pid = part);
	select count(*) into N from Parts_SubParts where pid = part;

	total := 0;
	while(N>0)
		loop
			begin
				
				select id into subPart from WeightTemp limit 1;
				select q into quantity from WeightTemp limit 1;
				delete from WeightTemp where id = subPart and q = quantity;
				total := total + (quantity * (select * from weight(subPart)));
				N := N-1; 
				
			end;
		end loop;
	return total;
End;
$$ LANGUAGE PLPGSQL;

select * from weight(1);

select * from weight(2);
select * from weight(3);
select * from weight(4);
select * from weight(5);

select q.pid , weight(q.pid) from (select pid from Parts_SubParts union select pid from parts) q order by 1;


--Solution 9

create table DGraph (s integer, t integer, w integer);
insert into DGraph values(0,1,2);
insert into DGraph values(1,0,2);
insert into DGraph values(0,4,10);
insert into DGraph values(4,0,10);
insert into DGraph values(1,3,3);
insert into DGraph values(3,1,3);
insert into DGraph values(1,4,7);
insert into DGraph values(4,1,7);
insert into DGraph values(2,3,4);
insert into DGraph values(3,2,4);
insert into DGraph values(3,4,5);
insert into DGraph values(4,3,5);
insert into DGraph values(4,2,6);
insert into DGraph values(2,4,6);



Create or replace function dijkstra(Source integer)
returns table (Target Integer, Distance Integer) as
$$
DECLARE SourceNode integer; 
DECLARE CurrentDistance integer;
DECLARE N integer;

Begin
	drop table if exists nodeList;
	CREATE TABLE nodeList (TargetNode integer NOT NULL, Distance integer NULL, Predecessor integer NULL, Done integer NOT NULL);



	INSERT INTO nodeList (TargetNode, Distance, Predecessor, Done) (select nodes.*, 2147483647, NULL, 0 FROM ((select DGraph.s from DGraph) union (select DGraph.t from DGraph)) nodes);

    UPDATE nodeList SET Distance = 0 WHERE TargetNode = Source;

    
    select 0 into N;
    
    while(1=1)
    loop
        
        
            select null into SourceNode;

            Select nodeList.TargetNode,  nodeList.Distance into SourceNode, CurrentDistance  
            FROM nodeList WHERE Done = 0 AND nodeList.distance < 2147483647
            ORDER BY nodeList.distance limit 1;
            
            
            if (SourceNode IS NULL) then
                exit;
            end if;
            UPDATE nodeList SET Done = 1 WHERE TargetNode = SourceNode;


            DECLARE r record;
            begin
            FOR r in (select * from DGraph where DGraph.s = SourceNode)
                loop
                    UPDATE nodeList SET distance = CurrentDistance + (select w from DGraph where r.t = DGraph.t and SourceNode = DGraph.s) 
                        WHERE nodeList.TargetNode = r.t and CurrentDistance + (select w from DGraph where r.t = DGraph.t and SourceNode = DGraph.s) < (select nodeList.distance from nodeList where nodeList.TargetNode = r.t);
                end loop;
            end;


    end loop;
    

	return query(select TargetNode, nodeList.distance from nodeList order by TargetNode);
End;
$$ LANGUAGE PLPGSQL;



select * from dijkstra(0);






--Solution 10

--Solution 10



-- Set Difference
drop table r;

drop table s;


drop function reduce();

drop function map();

create table if not exists r(a int);

create table if not exists s(a int);

insert into r values (1),(2),(3);

insert into s values (2),(3),(4);

select * from r;

select * from s;


create or replace function map(val int, relation text)
returns table(val int, relation text) as $$
	select val, relation;
$$ language sql;



create or replace function reduce(key int, bag_relations text[])
returns table(a int) as $$
begin
	if (select 'R' in (select * from unnest(bag_relations))) and (select 'S' not in (select * from unnest(bag_relations))) then
		return query
			select key;
	end if;
end;
$$ language plpgsql; 

--map phase 
drop table if exists key_value;

select distinct s.val as k, s.relation as v into key_value from
((select distinct l1.val, l1.relation from r r, lateral(select m1.val, m1.relation from map(r.a,'R') m1) l1)
union
(select distinct l2.val, l2.relation from s s, lateral(select m2.val, m2.relation from map(s.a,'S') m2) l2)) s;

--group phase
drop table if exists input_reduce;

select distinct k_v.k as k, 
(select array(select k_v1.v from key_value k_v1 where k_v.k=k_v1.k)) as v into input_reduce
from key_value k_v;

--reduce phase
select distinct l.a from input_reduce pair, lateral(select * from reduce(pair.k,pair.v)) l order by l.a;



-- Projection

drop table r;

create table if not exists r(a int, b int);

insert into r values (1,2),(3,4),(5,6);

select * from r;


drop function map();

create or replace function map(a int, b int)
returns table(a1 int, a2 int) as $$
	select a, a;
$$ language sql;


drop function reduce();

create or replace function reduce(key int, bag int[])
returns table(w int, value int) as $$
	select key, key;
$$ language sql;

--map phase
drop table if exists temp;
select l.a1 as a, l.a2 as b into temp from r r, lateral(select m.a1, m.a2 from Map(r.a,r.b) m) l; 

--group phase
drop table if exists input_reduce;
select distinct t1.a, (select array(select t2.b from temp t2 where t1.a=t2.a)) as ones into input_reduce from temp t1;

--reduce phase
select distinct l.w as a from input_reduce pair, lateral(select * from reduce(pair.a,pair.ones)) l order by l.w;



-- Join 

drop table r;

drop table s;

create table r(a int, b int);

create table s(b int, c int);

insert into r values (1,2),(3,4);

insert into s values (2,3),(5,6);

select * from r;

select * from s;

drop type if exists custom;

create type custom as (relation text, val int);

drop function map(int,text);


drop function map();

create or replace function map(val int, relation text)
returns table(key int, value custom) as $$
declare
	cust custom;
begin
	select relation into cust.relation;
	if relation='R' then
		select a into cust.val from r where b=val;
	else
		select c into cust.val from s where b=val;
	end if;
	return query
		select val, cust;
end;
$$ language plpgsql;



drop function reduce();

create or replace function reduce(key int, bag_relations custom[])
returns table(a int, b int, c int) as $$
declare
	rec1 record;
	i int = 0;
	a int;
	c int;
begin 
	for rec1 in select * from unnest(bag_relations)
	loop
		if rec1.relation='R' then
			a = rec1.val;
		else
   			c = rec1.val;
		end if;
		i = i+1;
	end loop;
	if i>1 then
		return query
			select a, key, c;
	end if;	
end;
$$ language plpgsql;

--map phase
drop table if exists key_value;

select distinct s.key as k, s.value as v into key_value from
((select distinct l1.key, l1.value from r r, lateral(select m1.key, m1.value from map(r.b,'R') m1) l1)
union
(select distinct l2.key, l2.value from s s, lateral(select m2.key, m2.value from map(s.b,'S') m2) l2)) s;

--group phase
drop table if exists input_reduce;

select distinct k_v.k as k, 
(select array(select k_v1.v from key_value k_v1 where k_v.k=k_v1.k)) as v into input_reduce
from key_value k_v;

--reduce phase
select l.a, l.b, l.c from input_reduce pair, lateral(select * from reduce(pair.k,pair.v)) l order by l.a;



