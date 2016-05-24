'''
Allows an artist to draw a comic based on an existing script
'''

import employeegen
import scriptgen

class Comic:


    def __init__(self, script, artist, author, title, weeks):
        self.script = script
        self.artist = artist
        self.author = author
        self.title = title
        self.writing = writing
        self.art = art
        self.weeks = 3


def draw_comic():
    # allows player to draw a comic based on a script
    print("Available artists:")
    available_artists = []
    available_scripts = []

    for i in employeegen.employee_list:
        if i.job == 'artist':
            if not i.working:
                available_artists.append(i)
                print(i.name)
                pass
            else:
                print("All artists are busy!")
                return

    artist = input()

    for i in available_artists:
        if artist == i.name:
            pass
        else:
            print("That artist doesn't exist!")

    print("Available scripts:")

    if len(scriptgen.script_list) > 0:
        for i in scriptgen.script_list:
            available_scripts.append(i)
            print(i.title)
            pass
    else:
        print("No available scripts!")
        return

    script = input()

    for i in available_scripts:
        if script == i.title:
            script = i
            author = i.author
            title = i.title
            print(artist, "is now drawing", title)
            return Comic(script, artist, author, title, 3)

