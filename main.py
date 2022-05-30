#simple exerise using the import datetime
import datetime

def date_time():
    time = datetime.datetime.now()
    return ("the current date is " ,
            time.month , time.day, time.year)

print(date_time())