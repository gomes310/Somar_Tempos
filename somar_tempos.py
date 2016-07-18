import datetime

timeList = ['9:30:56:500','0:00:01:500'] 
sum = datetime.timedelta()
for i in timeList:
    (h, m, s, ms) = i.split(':')
    d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s), milliseconds=int(ms))
    sum += d
print(str(sum))
