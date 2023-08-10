import schedule
import time
def intro():
    print("Hello , this is osama!")

# Schedule the 'intro' function to run every Thursday at 15:28 (3:28 PM)
schedule.every().thursday.at("15:28").do(intro)
while True:
    # Check if there are any scheduled tasks that need to run
    schedule.run_pending()
     # Pause the loop for 1 second to prevent excessive CPU usage
    time.sleep(1)