import unittest
from CourseManager.course_manager import CourseManager

class TestCourseManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self._num_courses = 4
        self._manager = CourseManager(self._num_courses)

    def test_run_invalid_file_path(self):
        invalid_file_path = 'xxxxxx'
        with self.assertRaises(ValueError):
            self._manager._run(invalid_file_path)

    def test_run_valid_path

if __name__ == '__main__':
    unittest.main()