
CREATE TABLE student
(id INTEGER PRIMARY KEY, name TEXT, address TEXT);

CREATE TABLE application
(id INTEGER PRIMARY KEY, student_id INTEGER REFERENCES student (id), score INTEGER);

INSERT INTO student (id, name, address)
VALUES (20, "Eduardo Fajardo", "Raleigh NC");

INSERT INTO student (id, name, address)
VALUES (22, "Josh Turner", "Raleigh NC");

INSERT INTO student (id, name, address)
VALUES (12, "Chirs White", "Raleigh NC");

INSERT INTO application (student_id, score)
VALUES (12, 234);

INSERT INTO application (student_id, score)
VALUES (22, 0);

INSERT INTO application (student_id, score)
VALUES (20, 8);




#Answer:

SELECT student_id, name , IFNULL(score, 0) FROM student, application
WHERE application.student_id=student.id
ORDER by score ASC;

SELECT student_id , name, IFNULL(score, 0) FROM student, application
WHERE application.student_id=student.id
ORDER BY name ASC;
