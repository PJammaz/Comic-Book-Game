import names
from random import choice, randrange
import companygen

employee_list = []


class Employee:


    def __init__(self, name, gender, skill, salary, job, employer, working):
        self.gender = gender
        self.name = name
        self.salary = salary
        self.skill = skill
        self.job = job
        self.employer = employer
        self.working = False


def create_new():
    gender = choice(['male', 'female'])
    name = names.get_full_name(gender)
    skill = 1
    salary = find_salary(skill)
    job = choice(['artist', 'writer'])
    employer = None
    employee_list.append(Employee(name, gender, skill, salary, job, employer, False))
    return Employee(name, gender, salary, job, employer, False)


def hire(employee, new_employer):
    employee.employer = new_employer
    return employee


def new_game():
    global employee_list
    two_employees = ['artist', 'writer']
    employed_by = companygen.create_player_company()
    for i in two_employees:
        gender = choice(['male', 'female'])
        name = names.get_full_name(gender)
        salary = 100
        job = i
        skill = 1
        employer = employed_by
        employee_list.append(Employee(name, gender, skill, salary, job, employer, False))
    return Employee(name, gender, skill, salary, job, employer, False)


def find_salary(skill):
    salary = skill * randrange(75, 125)
    return salary

def check_employees():
    for i in employee_list:
        print(i.name, "is a", i.job, "who works for", i.employer.name)