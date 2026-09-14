MATCH (node)
RETURN
    labels(node) as labels,
    count(node) as count
ORDER BY labels;

MATCH (student:Student)
WITH
    student.student_id as student_id,
    count(*) as count
WHERE count > 1
RETURN student_id, count;

MATCH (course:Course)
WITH
    course.course_id as course_id,
    count(*) as count
WHERE count > 1
RETURN course_id, count;

MATCH (instuctor:Instructor)
WITH
    instuctor.instructor_id as instructor_id,
    count(*) as count
WHERE count > 1
RETURN instructor_id, count;