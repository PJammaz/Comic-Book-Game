

class Script:

    def __init__(self, title, issue_number, author, quality, weeks):
        self.title = title
        self.issue_number = issue_number
        self.author = author
        self.quality = quality
        self.weeks = 1


def write():  # player should be able to choose an author and title for script
    # issue_number should be determined based on how many from that series exist
    # quality is based on author chosen

    for i in employeegen.emp_dict:
        print(i.name)

    author = input('''Who shall write the script?\n
    Available authors are:\n''')
    if author in employeegen.emp_dict:
        pass
    else:
        print("That author does not exist!")
    title = input("What is the name of the script?\n")
    issue_number = 1
    quality = 0
    script_list.append(Script(title, issue_number, author, quality))
