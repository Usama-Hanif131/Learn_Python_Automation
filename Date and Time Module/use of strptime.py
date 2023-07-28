#converting our custom date-time string into date-time object
from datetime import datetime
mydate="28 july,2023 5:23 PM"
mydate_object=datetime.strptime(mydate, "%d %B,%Y %I:%M %p")
print(mydate_object)