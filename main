'''Starts in the first week of 1938 and continues from there by week'''

current_week = 1
current_month = 1
current_year = 1938

MONTHS = {1 : 'January', 2 : 'February', 3 : 'March', 4 : 'April', 5 : 'May', 6 : 'June', 7 : 'July', 8 : 'August', 9 : 'September', 10 : 'October', 11 : 'November', 12 : 'December'}

def next_week():
    global current_week
    global current_month
    global current_year
    if current_week == 4:
        if current_month == 12:
            current_year += 1
            current_month = 1
            current_week = 1
        else:
            current_month += 1
    else:
        current_week += 1


def format_weeks():
    month = MONTHS[current_month]
    print(str(current_week), month, str(current_year))

