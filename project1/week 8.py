#Question 1
import datetime as dt
bday = dt.datetime(year=2000,month=11,day=10,hour=8,minute=20)
dt_now = dt.datetime.now()
alive = dt_now -bday
secs = (alive.days * 24 * 60 * 60) + alive.seconds
print (secs)

#Question 2:
days = dt.timedelta(days=1340)
future = dt.datetime.now()+days
alive = future -bday
age = alive.days/365.
res = f"In {days} days, I'll be {age: .2f} years old."
print (res)