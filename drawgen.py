'''
Allows an artist to draw a comic based on an existing script
'''

import employeegen
import writescript

class Comic:


    def __init__(self, script, artist, author, title, weeks):
        self.script = script
        self.artist = artist
        self.author = author
        self.title = title
        self.weeks = 3


def draw_comic():
    for i in writescript.script_list:
        print(i.title)

    for i in employeegen.emp_dict:
        print(i.name)

