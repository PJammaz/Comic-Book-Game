from random import choice

def getsuffix():
    file = open('suffixes.txt', 'r')
    thing = file.read().split()
    suffix = choice(thing)
    file.close()
    return suffix


def getprefix():
    file = open('prefixes.txt', 'r')
    thing = file.read().split()
    prefix = choice(thing)
    file.close()
    return prefix



def createnames(amount):
    for i in range(amount):
        name = getprefix() + getsuffix()
        name = name.capitalize()
        print(name)
