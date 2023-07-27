import pytz
from datetime import datetime
region1="Asia/Karachi"
region2="Asia/Kolkata"
Pak_timezone=pytz.timezone(region1)
India_timezone=pytz.timezone(region2)
pak_time=datetime.now(Pak_timezone).time()
india_time=datetime.now(India_timezone).time()
print(f"pak_time= {pak_time}")
print(f"india_time= {india_time}")
