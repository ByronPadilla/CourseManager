import os.path
import pathlib
from .course import Course

class CourseManager:
    """
    Internal program able to interact with stored courses and their respective "attributes" and Students.

    CourseManager has the following properties:

    Attributes:
        _courses: Dictionary of stored courses.
        _num_courses: Number of stored courses inside dictionary.

    """
    def __init__(self, num_of_courses: int):
        self._courses = {}
        self._num_courses = num_of_courses

    def run(self):
        filename = self.prompt("Please enter a valid CourseManager File",
                               "\nError: File was not found; Please try again\n",
                               lambda a: os.path.isfile(a))
        self._run(filename)
        print(self._courses)

    def prompt(self, message: str, err_message: str, is_valid: callable) -> str:
        """
        Function with the purpose of gathering valid information from the user.

        :param message: Directional message to be displayed to the user when asking for information.
        :param err_message: Error message to be displayed when user input is not valid
        :param is_valid: Function (Usually lambda) to validate user input
        :return: Returns valid (determined by isValid function) user input
        """
        response = None
        while True:
            response = input(message + ': ')
            if is_valid(response):
                break
            else:
                print(err_message)
        return response

    def generate_courses(self, line: str) -> {str: Course}:
        """
        Gathers the number of classes and the names of the classes from the first line of the read file.
        :param line: Str object representing the first line of the read file; Contains important information
        :return: None
        """
        classes = line.split(";")
        self._num_courses = int(classes[0])
        for course in classes[1:]:
            self._courses[course] = None
        return self._courses

    def _run(self, path_to_file: str) -> None:
        path = pathlib.Path(path_to_file)
        if not path.is_file():
            raise ValueError('"{0}" is not a valid file'.format(path_to_file))
        with path.open() as infile:
            for line in infile:
                self.generate_courses(line.strip())