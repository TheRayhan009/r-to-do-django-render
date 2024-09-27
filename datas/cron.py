from apscheduler.schedulers.background import BackgroundScheduler
import time

scheduler = BackgroundScheduler(timezone="Asia/Dhaka")
scheduler.start()

def a():
    print("Yoooo!")
    
# Schedule the job to run at 18:10 (6:10 PM)
job = scheduler.add_job(a, 'cron', hour="18", minute="10")

while True:
    time.sleep(2)  # Keeps the program running to allow the scheduler to work
