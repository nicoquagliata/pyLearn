import datetime

now = datetime.datetime.now()
print(now)

central_time = datetime.timezone(datetime.timedelta(hours=-6))
print (central_time)

uy_time = datetime.timezone(datetime.timedelta(hours=-3))

print (uy_time)

now = datetime.datetime.now(uy_time)
print(now)
print(now.astimezone(central_time))
