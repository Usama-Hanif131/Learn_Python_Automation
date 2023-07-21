#Get the File Name From the File Path
import os
file_name = os.path.basename('/root/abd.csv')
print(os.path.splitext(file_name)[0])
