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

employee1 = Employee("Даша Петрова", 300)
employee2 = Employee("Маша Іванова", 350)

recruiter = Recruiter("Олексій Ковальов", 400)
developer = Developer("Марина Власенко", 450)

print(employee1.work())
print(recruiter.work())
print(developer.work())

print(employee1)
print(recruiter)
print(developer)

print(employee1 == employee2)
print(employee1 == developer)
print(recruiter == developer)
print(employee2 == Employee("Маша Іванова", 350))
print(employee1 < employee2)
print(recruiter >= developer)
