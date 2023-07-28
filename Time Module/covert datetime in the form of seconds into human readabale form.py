from datetime import datetime
import time
current_time=time.time()
print(current_time) #show date and time in seconds

#1st method using time module
updated_current_time1=time.ctime(current_time)
print(updated_current_time1)
print(type(updated_current_time1)) # type is string

#seconds method using datetime module
updated_current_time2=datetime.fromtimestamp(current_time)
print(updated_current_time2)
print(type(updated_current_time2)) #type is datetime object