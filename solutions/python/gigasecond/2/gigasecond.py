"""Calculate the datetime that is 1,000,000,000 after the given moment."""

import datetime as dt

def add(moment):
    return moment + dt.timedelta(seconds=1_000_000_000)
