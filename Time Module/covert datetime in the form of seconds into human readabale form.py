import time
current_time=time.time()
print(current_time)
updated_current_time=time.ctime(current_time)
print(updated_current_time)
print(type(updated_current_time))