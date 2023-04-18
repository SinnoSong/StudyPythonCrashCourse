import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.emp_2 = Employee('Test', 'Employee', 60000)

    def test_give_default_raise(self):
        self.emp_2.give_raise()
        self.assertEqual(self.emp_2.salary, 60000+5000)

    def test_give_current_raise(self):
        self.emp_2.give_raise(10000)
        self.assertEqual(self.emp_2.salary, 60000+10000)


if __name__ == '__main__':
    unittest.main()
