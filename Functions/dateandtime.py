from datetime import date as d
from datetime import time as t
from datetime import datetime as dt

def date():
    today = d.today()
    cur = today.strftime("%a %m-%d-%Y")
    print("Current date is " + cur)

def time():
    now = dt.now()
    cur = now.strftime("%H:%M:%S%p")
    print("Current time is " + cur)
