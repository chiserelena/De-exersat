import unittest

from student_grades import Catalog, Student


class TestStudentGrades(unittest.TestCase):
    def test_student_can_add_grade(self):
        elev = Student("Ana", "Popescu")

        elev.adauga_nota(9)

        self.assertEqual(elev.note, [9])

    def test_catalog_can_add_grade_to_student(self):
        catalog = Catalog()
        catalog.adauga_elev("Ana")

        catalog.adauga_nota("Ana", 10)

        self.assertEqual(catalog.elevi["Ana"].note, [10])


if __name__ == "__main__":
    unittest.main()
