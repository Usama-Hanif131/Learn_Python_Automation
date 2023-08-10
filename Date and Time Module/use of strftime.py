#converting our date-time object into custom date-time string
from datetime import datetime as dt
# Get the current date and time
current_time = dt.now()

# Print the current time in a custom format
print("Time =", current_time.strftime("%I:%M:%S %p"))  # %I: Hour (12-hour clock), %M: Minute, %S: Second, %p: AM/PM indicator

# Print the current date in a custom format
print("Date =", current_time.strftime("%A %m, %Y"))  # %A: Full weekday name, %m: Month (numeric), %Y: Year (4 digits)
