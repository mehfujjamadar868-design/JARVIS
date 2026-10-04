from datetime import datetime
# Used to get the current date and time


def get_time():
    # Gets the current time
    current_time = datetime.now().strftime("%I:%M %p")

    return current_time
    # Returns the current time


def get_date():
    # Gets today's date
    current_date = datetime.now().strftime("%d %B %Y")

    return current_date
    # Returns today's date
