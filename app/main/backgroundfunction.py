#@author favour gabriel
#@date may 10th 2023

from ..model import User, Flight
from datetime import datetime
from flask import redirect, url_for

def checkFlight():
    '''get all flight queries and calculate the months remaining from the time departure
    should take place. if a ticket is due get the appropriate user id and fetch email'''
    flight = Flight.query.all()
    curr = datetime.now()
    for li in flight:
        cal = calculate_time(curr, li.duration)
        if cal == 1:
            u = User.query.filter_by(id= li.user_id).first()
            return redirect(url_for('notify',email =u.email))
        elif cal == 2:
            u = User.query.filter_by(id= li.user_id).first()
            return redirect(url_for('notify',email =u.email))
        elif cal == 3:
            u = User.query.filter_by(id= li.user_id).first()
            return redirect(url_for('notify',email =u.email))
        pass

def calculate_time(date1,date2):
    return (date1.year - date2.year) * 12 + date1.month -date2.month