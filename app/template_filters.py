from datetime import datetime
from pytz import UTC

def day_suffix(date_to_format):
    """
    format the date of the month with the appropriate suffix.
    eg:
        1 = 1st, 2 = 2nd, 3 = 3rd, 4 = 4th, 5 = 5th
    """
    day = date_to_format.day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return suffix


def register_jinja_filters(app):
    """
    """
    @app.template_filter('date_formatter')
    def date_formatter(date_to_parse):
        """
        """
        time_now = datetime.now()
        if time_now < date_to_parse:
            time_difference = (date_to_parse - time_now).seconds # time in seconds to sheduled date
            if (time_difference < 60):
                # time_statement = date_to_parse.strftime(f"%B %-m{ day_suffix } at %-I:%M %p")
                time_response = "Expecting client in about a minute."

            elif (time_difference/60) < 60:
                # time_statement = date_to_parse.strftime(f"%B %-m{ day_suffix } at %-I:%M %p")
                time_response = f"Service starting in  { int(time_difference/60) } minutes."
                
            elif (date_to_parse.day == time_now.day) and time_now.hour <= 18:
                time_statement = date_to_parse.strftime(f"%-I:%M %p")
                time_response = f"Today at {time_statement}."
            
            elif (time_difference/3600) < 24:
                # time_statement = date_to_parse.strftime(f"%B %-m{ day_suffix(date_to_parse) } at %-I:%M %p")
                time_response = f"In {int(time_difference/3600)} hours."

            elif (time_difference/(3600*24)) < 7:
                # time_statement = date_to_parse.strftime(f"%B %-m{ day_suffix(date_to_parse) } at %-I:%M %p")
                time_response = f"In { int(time_difference/(3600*24)) } days "
            else:
                time_statement = date_to_parse.strftime(f"%B %-m{ day_suffix(date_to_parse) } at %-I:%M %p")
                time_response = f"Sheduled for {time_statement}."

        else:
            time_difference = (time_now - date_to_parse).seconds
            if (time_difference < 60):
                time_response = "Sheduled for less than a minute ago."

            elif (time_now.day == date_to_parse.day) and (time_now.minute - date_to_parse.minute) < 60:
                time_response = f"Was sheduled for { time_now.minute - date_to_parse.minute } minutes ago."

            elif (time_now.day == date_to_parse.day) and (time_now.hour - date_to_parse.hour) < 18:
                time_statement = date_to_parse.strftime("%-I:%M %p")
                time_response = f"Was heduled for {time_now.hour - date_to_parse.hour} hours ago"

            elif (time_now.day == date_to_parse.day):
                time_statement = date_to_parse.strftime("%-I:%M %p")
                time_response = f"Was heduled for today at {time_statement}."

            elif (time_now.day - date_to_parse.day) == 1:
                time_statement = date_to_parse.strftime("%-I:%M %p")
                time_response = f"Was sheduled for yesterday at {time_statement}."

            else:
                time_statement = date_to_parse.strftime(f"%-m{ day_suffix(date_to_parse) } of %B %Y at %-I:%M %p")
                time_response = f"Was sheduled for {time_statement}."

        return time_response
