import pytz 
from datetime import datetime  

region1 = "Asia/Karachi"  # Define the time zone region for Karachi
region2 = "Asia/Kolkata"  # Define the time zone region for Kolkata (India)

Pak_timezone = pytz.timezone(region1)  # Create a time zone object for Karachi
India_timezone = pytz.timezone(region2)  # Create a time zone object for Kolkata

pak_time = datetime.now(Pak_timezone).time()  # Get the current time in the Karachi time zone
india_time = datetime.now(India_timezone).time()  # Get the current time in the Kolkata time zone

print(f"pak_time = {pak_time}")  # Print the current time in the Karachi time zone
print(f"india_time = {india_time}")  # Print the current time in the Kolkata time zone
