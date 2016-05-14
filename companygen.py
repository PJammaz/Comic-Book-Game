companies = []

class Company:

    def __init__(self, name):
        self.name = name


def create_player_company():
    player_name = input("Enter a name for your company.\n")
    player_company = Company(player_name)
    return player_company
