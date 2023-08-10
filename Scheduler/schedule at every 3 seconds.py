import schedule
import time
from datetime import datetime
import pytz
pak_timezone="Asia/Karachi"
def intro():
    pak_time=pytz.timezone(pak_timezone)
    current_time=datetime.now(pak_time).time()
    print("Hello, this is osama",current_time.strftime("%I:%M:%S %p"))

schedule.every(3).seconds.do(intro)
while True:
    schedule.run_pending()
    time.sleep(1)