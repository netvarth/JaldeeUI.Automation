# import datetime
from datetime import datetime
from re import sub
from dateutil.relativedelta import relativedelta
from Framework.common_utils import *


def Generate_dob():
    fake = Faker()
    dob = fake.date_of_birth(minimum_age=35, maximum_age=45)
    year = dob.strftime("%Y")
    month = dob.strftime("%b")
    day = dob.strftime("%d")
    return [year, month, day]


def add_date(years):
    current_date = datetime.now()
    future_date = current_date + relativedelta(years=years)
    year = future_date.strftime("%Y")
    month = future_date.strftime("%b")
    day = future_date.strftime("%d")
    return [year, month, day]




def add_month(month):
    current_date = datetime.now()
    future_date = current_date + relativedelta(months=month)
    year = future_date.strftime("%Y")
    month = future_date.strftime("%b")
    day = future_date.strftime("%d")
    return [year, month, day]


def add_days(days):
    current_date = datetime.now()
    future_date = current_date + relativedelta(days=days)
    year = future_date.strftime("%Y")
    month = future_date.strftime("%b")
    day = int(future_date.strftime("%d"))
    return [year, month, day]

def sub_days(days):
    current_date = datetime.now()
    previous_date = current_date - relativedelta(days=days)
    year = previous_date.strftime("%Y")
    month = previous_date.strftime("%b")
    day = int(previous_date.strftime("%d"))
    return [year, month, day]
