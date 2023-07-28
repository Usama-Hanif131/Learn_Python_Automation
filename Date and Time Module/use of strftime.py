#converting our date-time object into custom date-time string
from datetime import datetime as dt
current_time=dt.now()
print("Time=", current_time.strftime("%I:%M:%S %p"))
print("Date=", current_time.strftime("%A %m,%Y"))