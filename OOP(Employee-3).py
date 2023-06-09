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

    def check_salary(self, days):
        workdays = self._get_workdays()
        salary = workdays * self.daily_salary
        return salary

    def _get_workdays(self):
        import datetime

        today = datetime.date.today()
        start_of_month = datetime.date(today.year, today.month, 1)

        workdays = 0
        current_day = start_of_month
        while current_day <= today:
            if current_day.weekday() < 5:  # з пн по пт (з 0 до 4)
                workdays += 1
            current_day += datetime.timedelta(days=1)

        return workdays


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start hiring."

    def __str__(self):
        return f"Position: Recruiter, Name: {self.name}"


class Developer(Employee):
    def __init__(self, name, daily_salary, tech_stack):
        super().__init__(name, daily_salary)
        self.tech_stack = tech_stack

    def work(self):
        return "I come to the office and start coding."

    def __str__(self):
        return f"Position: Developer, Name: {self.name}"

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __add__(self, other):
        name = self.name + " " + other.name
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        daily_salary = max(self.daily_salary, other.daily_salary)
        return Developer(name, daily_salary, tech_stack)


employee1 = Employee("Даша Петрова", 300)
employee2 = Employee("Маша Іванова", 350)

recruiter = Recruiter("Олексій Ковальов", 400)
developer1 = Developer("Марина Власенко", 450, ["Python", "JavaScript"])
developer2 = Developer("Іван Петренко", 500, ["JavaScript", "HTML", "CSS"])

print(employee1.work())
print(recruiter.work())
print(developer1.work())

print(employee1)
print(recruiter)
print(developer1)

print(employee1 == employee2)
print(developer1 == developer2)
print(recruiter == developer1)

print(employee1.check_salary(15))
print(developer1.check_salary(20))

developer3 = developer1 + developer2
print(developer3)

