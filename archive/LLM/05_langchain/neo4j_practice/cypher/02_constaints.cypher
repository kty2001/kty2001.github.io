CREATE CONSTRAINT student_id_unique IF NOT EXISTS
FOr (student:Student)
REQUIRE student.student_id IS UNIQUE;

CREATE CONSTRAINT course_id_unique IF NOT EXISTS
FOr (course:Course)
REQUIRE course.course_id IS UNIQUE;

CREATE CONSTRAINT instructor_id_unique IF NOT EXISTS
FOr (instructor:Instructor)
REQUIRE instructor.instructor_id IS UNIQUE;

CREATE CONSTRAINT category_id_unique IF NOT EXISTS
FOr (category:Category)
REQUIRE category.category_id IS UNIQUE;

SHOW CONSTRAINTS;