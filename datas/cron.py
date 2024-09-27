import time
from apscheduler.schedulers.background import BackgroundScheduler

# Function to be scheduled
def a():
    print("Yoooo!")

# Create a scheduler
scheduler = BackgroundScheduler(timezone="Asia/Dhaka")
scheduler.start()

# Schedule the job with cron-style time specification (e.g., every day at 18:10)
scheduler.add_job(a, 'cron', hour=18, minute=10)

# Keep the main thread alive so the scheduler can run in the background
try:
    while True:
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
