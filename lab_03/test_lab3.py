from lab3 import StudentList, Student
import unittest

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.student_list = StudentList()

    def test_add_student(self):
        student = Student('John', '1234567890')
        self.student_list.add_student(student)
        self.assertEqual(self.student_list.students_list[0], student)

    def test_delete_student(self):
        student = Student('John', '1234567890')
        self.student_list.add_student(student)
        self.student_list.delete_student('John')
        self.assertEqual(len(self.student_list.students_list), 0)

    def test_update_student(self):
        student = Student('John', '1234567890')
        self.student_list.add_student(student)
        updated_student = Student('John', '0987654321')
        self.student_list.update_student(updated_student)
        self.assertEqual(self.student_list.students_list[0].phone, '0987654321')

if __name__ == '__main__':
    unittest.main(exit=False)

