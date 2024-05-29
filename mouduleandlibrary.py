#Here we more discuss moudule and library. we can install every library from python website or using pip install and library name in command line
#many library and module build in so we can used and enhanced our program or project.

import random
import datetime

#calculate random number
x =random.randint(1,10)
print(x)

#calculate date time 
date = datetime.datetime.now()
print(date)

#calculate birthday...
dob = datetime.date(1997,3,23)
today = datetime.date.today()
age = today-dob
print(age)