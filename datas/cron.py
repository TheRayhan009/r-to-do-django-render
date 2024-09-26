from django_cron import CronJobBase, Schedule

class PrintSomethingCronJob(CronJobBase):
    RUN_EVERY_MINS = 15

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'datas.print_something'  # a unique code

    def do(self):
        print("Server is running!")  # This will be printed every 15 minutes
