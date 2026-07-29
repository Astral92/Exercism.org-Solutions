import datetime as dt

def add(moment):
    return moment + dt.timedelta(seconds=1_000_000_000)
