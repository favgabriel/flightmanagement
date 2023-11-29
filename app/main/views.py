import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from flask import current_app

from . import main

#run this function every 1st day of every month
cron = BackgroundScheduler(daemon=True)
cron.add_job(current_app.config['back_func'], 'interval', months=0, hours=0, days=1)
cron.start()
#shutdown the function when server stops.
atexit.register(lambda :cron.shutdown(wait=False))

@main.route('/', methods=['GET'])
def index():
    return '''New Project Luco'''

@main.route('/notify/<url>',methods=['GET','POST'])
def notify(url):
    return '''notify {}'''.format(url)