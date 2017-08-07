class Course:
    """
    Python class designed to hold information on Students. Interacts with Students by creating Stats based on Student
    information.

    Course has the following properities:

    Attributes:
        student_set: Dictionary of Students in the Course.
        count_Student: The Number of Studnets in the Course.

    """
    def __init__(self, num_of_courses: int):
        self._courses = {}
        self._num_courses = num_of_courses



