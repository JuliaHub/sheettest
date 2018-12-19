import run_hub

from apscheduler.schedulers.blocking import BlockingScheduler

def my_job():
    run_hub.step1()

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=120)
def timed_job():
    my_job()

sched.start()



    
    