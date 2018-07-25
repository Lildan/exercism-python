import datetime

def add_gigasecond(birth_date):
    gigasecond = 1000000000
    days = gigasecond / (3600*24)
    delta = datetime.timedelta(days=days)

    return birth_date + delta



