import unittest

class Employee:
    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary

    def work(self):
        return "I come to the office."

    def __str__(self):
        return f"Position: Employee, Name: {self.name}"

    def __eq__(self, other):
        return self.daily_salary == other.daily_salary

    def __lt__(self, other):
        return self.daily_salary < other.daily_salary

    def __gt__(self, other):
        return self.daily_salary > other.daily_salary

    def __le__(self, other):
        return self.daily_salary <= other.daily_salary

    def __ge__(self, other):
        return self.daily_salary >= other.daily_salary


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start hiring."

    def __str__(self):
        return f"Position: Recruiter, Name: {self.name}"


class Developer(Employee):
    def work(self):
        return "I come to the office and start coding."

    def __str__(self):
        return f"Position: Developer, Name: {self.name}"


class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.employee1 = Employee("Даша Петрова", 300)
        self.employee2 = Employee("Маша Іванова", 350)
        self.recruiter = Recruiter("Олексій Ковальов", 400)
        self.developer = Developer("Марина Власенко", 450)

    def test_work(self):
        self.assertEqual(self.employee1.work(), "I come to the office.")
        self.assertEqual(self.recruiter.work(), "I come to the office and start hiring.")
        self.assertEqual(self.developer.work(), "I come to the office and start coding.")

    def test_str(self):
        self.assertEqual(str(self.employee1), "Position: Employee, Name: Даша Петрова")
        self.assertEqual(str(self.recruiter), "Position: Recruiter, Name: Олексій Ковальов")
        self.assertEqual(str(self.developer), "Position: Developer, Name: Марина Власенко")

    def test_eq(self):
        self.assertEqual(self.employee1 == self.employee2, False)
        self.assertEqual(self.employee1 == self.developer, False)
        self.assertEqual(self.recruiter == self.developer, False)

    def test_comparison_operators(self):
        self.assertEqual(self.employee2 == Employee("Маша Іванова", 350), True)
        self.assertEqual(self.employee1 < self.employee2, True)
        self.assertEqual(self.recruiter >= self.developer, False)


if __name__ == '__main__':
    unittest.main()
