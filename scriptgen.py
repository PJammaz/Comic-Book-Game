import employeegen
from random import choice, randrange

script_list = []

class Script:
    def __init__(self, title, issue_number, author, quality, weeks):
        self.title = title
        self.issue_number = issue_number
        self.author = author
        self.quality = quality
        self.weeks = 1


def getsuffix():
    file = open('lastpart.txt', 'r')
    thing = file.read().split()
    suffix = choice(thing)
    file.close()
    return suffix


def getprefix():
    file = open('firstpart.txt', 'r')
    thing = file.read().split()
    prefix = choice(thing)
    file.close()
    return prefix


def create_names():
        name = getprefix() + ' ' + getsuffix() + ' ' + 'Comics'
        return name


def write():  # player should be able to choose an author and title for script
    # issue_number should be determined based on how many from that series exist
    # quality is based on author chosen
    print("Available authors:")
    available_authors = []

    for i in employeegen.employee_list:
        if i.job == 'writer':
            if not i.working:
                available_authors.append(i)
                print(i.name)
                pass
            else:
                print("All writers are busy!")
                return


    writer = input()

    for i in available_authors:
        if writer == i.name:
            title = create_names()
            issue_number = 1
            quality = script_quality(i)
            new_script = Script(title, issue_number, writer, quality, 1)
            i.working = new_script
            print(writer, "has written a script called", new_script.title + '.')
            script_list.append(new_script)
            return writer, new_script
    else:
        print("That author does not exist!")
        write()


def script_quality(author):
    # determines random quality of script based on author skill
    quality = author.skill * randrange(5, 25)
    return quality
