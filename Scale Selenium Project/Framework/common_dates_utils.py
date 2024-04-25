import datetime
from Framework.common_utils import *


def Generate_dob():
    fake = Faker()
    dob = fake.date_of_birth(minimum_age=35, maximum_age=43)
    year = dob.strftime("%Y")
    month = dob.strftime("%b")
    day = dob.strftime("%d")
    return [year, month, day]



