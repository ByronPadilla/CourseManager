import os.path

class courseManager:
    """
    Internal program able to interact with stored courses and their respective "attributes" and Students.

    CourseManager has the following properties:

    Attributes:
        course_Dict: Dictionary of stored courses.
        num_of_Courses: Number of stored courses inside dictionary.

    """
    def __init__(self, num_of_courses):
        self.course_Dict = {}
        self.num_of_Courses = num_of_courses

    def run(self):
        filename = self.prompt("Please enter a valid CourseManager File",
                               "\nError: File was not found; Please try again\n",
                               lambda a: os.path.isfile(a))

        file = open(filename, 'r')
        self.generate_courses(file.readline().strip())

        print(self.course_Dict)

    def prompt(self, message, err_message, is_valid):
        """
        Function with the purpose of gathering valid information from the user.

        :param message: Directional message to be displayed to the user when asking for information.
        :param err_message: Error message to be displayed when user input is not valid
        :param is_valid: Function (Usually lambda) to validate user input
        :return: Returns valid (determined by isValid function) user input
        """
        response = None
        while response is None:
            response = input(str(message)+': ')
            if not is_valid(str(response)):
                print(str(err_message))
                response = None
        return response

    def generate_courses(self, line):
        """
        Gathers the number of classes and the names of the classes from the first line of the read file.
        :param line: Str object representing the first line of the read file; Contains important information
        :return: None
        """
        classes = line.split(";")
        self.num_of_Courses = int (classes[0])
        for course in range(len(classes)-1):
            self.course_Dict[classes[course+1]] = None








