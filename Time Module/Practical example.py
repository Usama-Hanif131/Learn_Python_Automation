"""this program design  to find all the files in the current working also in the 
sub directories and tells the time of creation of each file"""
import os
import time
path=os.getcwd()
for directories,sub_directories,files in list(os.walk(path)):
    for filename in files:
        files_path=os.path.join(directories,filename)
        current_time=os.path.getctime(files_path)
        print(f"{files_path}    {time.ctime(current_time)}")