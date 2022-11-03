import unittest
from builtins import str, ValueError, print, set

import self as self

from class_definitions import Student as Student



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.lname = 'Ord'
        self.fname = 'John'
        self.major = 'Computer Programming'
        self.gpa = 3.99
        self.student = Student(self.lname, self.fname, self.major, self.gpa)



    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        actual = Student(self.lname, self.fname, self.major)

        # evaluate
        self.assertEqual(actual.last_name, self.lname)
        self.assertEqual(actual.first_name, self.fname)
        self.assertEqual(actual.major, self.major)

    def test_object_created_all_attributes(self):
        student = Student('Ord', 'John', 'Computer Programming', 3.99)
        assert student.last_name == 'Ord'
        assert student.first_name == 'John'
        assert student.major == 'Computer Programming'
        assert student.gpa == 3.99

    def test_student_str(self):
        self.assertEqual(str(Student), 'Ord', 'John', 'Computer Programming', 3.99)

    def test_object_not_created_error_last_name(self):

            Student('123', 'John', 'History', 3.99)
            name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
            if self.lname and not (name_characters.issuperset(self.lname)):
                raise ValueError



    def test_object_not_created_error_first_name(self):

            Student('Ord', '123', 'History', 3.99)
            name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
            if self.fname and not (name_characters.issuperset(self.fname)):
                raise ValueError

    def test_object_not_created_error_major(self):

            Student('Ord', 'John', '123', 3.99)
            major_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
            if self.major and not (major_characters.issuperset(self.major)):
                raise ValueError

    def test_object_not_created_error_gpa(self):

            Student('Ord', '123', 'History', 0.0)
            gpa_characters = set("1234567890-")
            if self.gpa and not (gpa_characters.issuperset(self.gpa)):
                raise ValueError


def main():
    # Create 2 student objects and print them
    student1 = Student("Kent", "Clark", "Journalism", 4.0)
    student2 = Student("Wayne", "Bruce", "Criminology", 4.0)
    print("Student1 :",student1)
    print("Student2 :",student2)

# let's do the test :)
if __name__ == '__main__':
    main()
    unittest.main()




