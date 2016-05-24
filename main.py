"""Starts in the first week of 1938 and continues from there by week"""

import employeegen
import scriptgen
import timekeeping

EVENTS = {
    "write": scriptgen.write,
    "hire": employeegen.hire,
    "next week": timekeeping.next_week,
    "check employees": employeegen.check_employees}


def main():

    employeegen.new_game()

    while True:
        choice = input("Enter a command: ")
        if choice in EVENTS:
            EVENTS[choice]()

        else:
            print("That command doesn't exist!")


if __name__ == "__main__":
    main()

