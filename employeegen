import names
from random import choice
import companycreate

emp_dict = []


class Employee:
    def __init__(self, name, gender, salary, job, employer):
        self.gender = gender
        self.name = name
        self.salary = salary
        self.job = job
        self.employer = employer


def create_new():
    gender = choice(['male', 'female'])
    name = names.get_full_name(gender)
    salary = 0
    job = choice(['artist', 'writer'])
    employer = None
    return Employee(name, gender, salary, job, employer)


def hire(employee, new_employer):
    employee.employer = new_employer
    return employee


def new_game():
    two_employees = ['artist', 'writer']
    employed_by = companycreate.create_player_company()
    for i in two_employees:
        gender = choice(['male', 'female'])
        name = names.get_full_name(gender)
        salary = 100
        job = i
        employer = employed_by
        return Employee(name, gender, salary, job, employer)
