SELECT * FROM dojos_and_ninjas_schema.dojos;


-- ALTER TABLE dojos
-- DROP COLUMN dojoscol;

-- Query: Create 3 new dojos
INSERT INTO dojos (name, created_at, updated_at) 
VALUES ('dojo_1', NOW(), NOW()),
('dojo_2', NOW(), NOW()),
('dojo_3', NOW(), NOW());

SELECT * FROM dojos_and_ninjas_schema.dojos;

-- Query: Delete the 3 dojos you just created
DELETE FROM dojos WHERE created_at>NOW();

-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at,dojo_id) 
VALUES ('ninja1_first', 'ninja1_last', 25, NOW(), NOW(), 1),
('ninja2_first', 'ninja2_last', 26, NOW(), NOW(), 1),
('ninja3_first', 'ninja3_last', 27, NOW(), NOW(), 1);

SELECT * FROM ninjas;

-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at,dojo_id) 
VALUES ('Tom', 'Smith', 25, NOW(), NOW(), 2),
('Tim', 'Mark', 26, NOW(), NOW(), 2),
('Kim', 'Caleb', 27, NOW(), NOW(), 2);

-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at,dojo_id) 
VALUES ('ninja1_first13', 'ninja1_last', 21, NOW(), NOW(), 3),
('ninja2_first23', 'ninja2_last', 226, NOW(), NOW(), 3),
('ninja3_first33', 'ninja3_last', 23, NOW(), NOW(), 3);

-- DELETE FROM ninjas
-- where age=37 and dojo_id=1;

-- Query: Retrieve all the ninjas from the first dojo
SELECT * 
FROM ninjas join dojos ON ninjas.dojo_id=dojos.id
WHERE dojo_id=1;

-- Query: Retrieve all the ninjas from the last dojo
SELECT * 
FROM ninjas join dojos ON ninjas.dojo_id=dojos.id
WHERE dojo_id=3;

-- Query: Retrieve the last ninja's dojo
SELECT * 
FROM ninjas
WHERE dojo_id=3 ;
