
def second_convertissor(x):
    days=x//86400
    x-=(days*86400)
    hours=x//3600
    x-=(hours*3600)
    minutes=x//60
    seconds=x-(minutes*60)
    print("Time:",days,"days",hours,"hours",minutes,"minutes",seconds,"seconds")
    return days,hours,minutes,seconds

#test
second_convertissor(8946463)
